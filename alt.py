import json
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from newspaper import Article
from newsapi import NewsApiClient
from concurrent.futures import ThreadPoolExecutor
import time
import os
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NewsArticleExtractor:
    def __init__(self, api_key: Optional[str] = '3be190842de64ec492113f90af6ae055'):
        """Initialize the NewsArticleExtractor with API key."""
        load_dotenv()  # Load environment variables from .env file
        self.api_key = api_key or os.getenv('NEWS_API_KEY')
        if not self.api_key:
            raise ValueError("API key is required")
        self.newsapi = NewsApiClient(api_key=self.api_key)
        
    def fetch_articles(self, query: str, language: str = "en", 
                      days: int = 7, max_articles: int = 100) -> List[Dict]:
        """Fetch articles from NewsAPI with parameters."""
        try:
            response = self.newsapi.get_everything(
                q=query,
                language=language,
                sort_by="relevancy",
                from_param=(datetime.now() - timedelta(days=days)).date().isoformat(),
                page_size=min(max_articles, 100)  # NewsAPI limit is 100 per request
            )
            return response.get("articles", [])
        except Exception as e:
            logger.error(f"Error fetching articles: {str(e)}")
            return []

    def get_full_article_content(self, url: str) -> Dict[str, str]:
        """Extract full article content using newspaper3k."""
        try:
            article = Article(url)
            article.download()
            article.parse()
            return {
                "full_text": article.text,
                "authors": article.authors,
                "publish_date": article.publish_date.isoformat() if article.publish_date else None,
                "top_image": article.top_image,
                "summary": article.summary
            }
        except Exception as e:
            logger.error(f"Error extracting content from {url}: {str(e)}")
            return {"full_text": None, "authors": [], "publish_date": None, "top_image": None, "summary": None}

    def process_article(self, article: Dict) -> Dict:
        """Process a single article with full content extraction."""
        url = article.get("url")
        if not url:
            return article

        # Add rate limiting
        time.sleep(1)  # Be nice to servers
        
        full_content = self.get_full_article_content(url)
        return {
            "title": article.get("title"),
            "url": url,
            "source": article.get("source", {}).get("name"),
            "published_at": article.get("publishedAt"),
            "original_content": article.get("content"),
            **full_content
        }

    def save_articles(self, articles: List[Dict], filename: str):
        """Save articles to JSON file with timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename}_{timestamp}.json"
        
        try:
            with open(filename, "w", encoding="utf-8") as json_file:
                json.dump(articles, json_file, indent=4, ensure_ascii=False)
            logger.info(f"Successfully saved articles to {filename}")
        except Exception as e:
            logger.error(f"Error saving articles: {str(e)}")

    def extract_and_save(self, query: str, output_file: str = "news_data", 
                        max_articles: int = 100):
        """Main method to extract and save articles."""
        logger.info(f"Starting article extraction for query: {query}")
        
        # Fetch initial articles from NewsAPI
        articles = self.fetch_articles(query, max_articles=max_articles)
        logger.info(f"Found {len(articles)} articles")

        # Process articles in parallel with full content extraction
        with ThreadPoolExecutor(max_workers=5) as executor:
            processed_articles = list(executor.map(self.process_article, articles))

        # Filter out articles with failed content extraction
        valid_articles = [
            article for article in processed_articles 
            if article.get("full_text")
        ]
        
        self.save_articles(valid_articles, output_file)
        return valid_articles

def main():
    """Main execution function."""
    try:
        extractor = NewsArticleExtractor()
        articles = extractor.extract_and_save(
            query="usa elections",
            output_file="election_news",
            max_articles=50
        )
        logger.info(f"Successfully processed {len(articles)} articles")
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()