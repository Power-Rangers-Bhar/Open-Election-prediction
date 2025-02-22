import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon if not already present
nltk.download("vader_lexicon")

# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(title, content):
    """
    Analyze sentiment using VADER for both title and content.
    Title is weighted slightly more.
    """
    title_score = sia.polarity_scores(title)["compound"]
    content_score = sia.polarity_scores(content)["compound"]
    overall_score = (0.6 * title_score) + (0.4 * content_score)
    sentiment = ("positive" if overall_score > 0.05 
                 else "negative" if overall_score < -0.05 
                 else "neutral")
    return {
        "title_score": title_score,
        "content_score": content_score,
        "overall_score": overall_score,
        "sentiment": sentiment
    }

def fetch_news(query, language="en", sort_by="relevancy"):
    """
    Fetch news articles from NewsAPI based on a dynamic query.
    Saves the articles (with title and content) to 'news_data.json'
    and returns the list of articles.
    """
    from newsapi import NewsApiClient
    newsapi = NewsApiClient(api_key='3be190842de64ec492113f90af6ae055')
    
    # Get news articles based on query
    everything = newsapi.get_everything(q=query, language=language, sort_by=sort_by)
    
    # Extract title and content; fallback to description if content is missing
    articles_data = [
        {
            "title": article["title"],
            "content": article.get("content") or article.get("description") or ""
        }
        for article in everything.get("articles", [])
    ]
    
    with open("news_data.json", "w", encoding="utf-8") as json_file:
        json.dump(articles_data, json_file, indent=4, ensure_ascii=False)
    
    print("✅ News data saved as 'news_data.json'")
    return articles_data

def calculate_party_polarity(articles, party_keywords):
    """
    Calculate the average sentiment polarity for each party based on the articles.
    
    Args:
        articles (list): List of article dictionaries containing 'title', 'content', and 'sentiment_analysis'.
        party_keywords (dict): Dictionary mapping party names to lists of keywords.
        
    Returns:
        dict: A mapping of party names to their average polarity (or None if no mentions).
    """
    # Initialize cumulative sentiment and mention count per party
    party_scores = {party: {"total_sentiment": 0.0, "count": 0} for party in party_keywords}
    
    for article in articles:
        # Combine title and content for keyword matching
        text = (article.get("title", "") + " " + article.get("content", "")).lower()
        overall_score = article.get("sentiment_analysis", {}).get("overall_score", 0)
        # Check for each party's keywords in the text
        for party, keywords in party_keywords.items():
            if any(keyword.lower() in text for keyword in keywords):
                party_scores[party]["total_sentiment"] += overall_score
                party_scores[party]["count"] += 1
    
    # Compute average sentiment per party
    party_polarity = {}
    for party, data in party_scores.items():
        if data["count"] > 0:
            party_polarity[party] = data["total_sentiment"] / data["count"]
        else:
            party_polarity[party] = None  # No mentions found
    
    return party_polarity

# --- Main Execution ---

# Step 1: Fetch news based on a query (this can be called from your UI)
articles = fetch_news("usa")

# Step 2: For each article, perform sentiment analysis (adding a new key)
for article in articles:
    article["sentiment_analysis"] = analyze_sentiment(article["title"], article["content"])

# Optionally, save the updated articles with sentiment analysis back to file
with open("news_data_with_sentiment.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=4, ensure_ascii=False)
print("✅ Sentiment analysis added and saved as 'news_data_with_sentiment.json'")

# Step 3: Define your party keywords.
# For example, for an Indian context:
'''
party_keywords = {
    "BJP": ["bjp", "ind"],
    "Congress": ["congress", "inc", "indian national congress"]
}
'''

# For a U.S. context, you might use:
party_keywords = {
    "Democratic": ["democrat", "democratic"],
    "Republican": ["republican", "gop","usa"]
}

# Step 4: Calculate polarity distribution for the defined parties.
party_polarity = calculate_party_polarity(articles, party_keywords)
print("Party polarity distribution:")
print(json.dumps(party_polarity, indent=4))
