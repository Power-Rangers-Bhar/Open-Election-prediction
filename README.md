# 🗳️ Election Sentiment Analyzer 📊

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

An advanced open-source election sentiment analysis platform that goes beyond traditional exit polls by leveraging multi-dimensional data analysis, machine learning, and real-time sentiment tracking.

## 🌟 What Sets Us Apart

Unlike other open-source exit poll solutions, we offer:
- Multi-source data integration (social media, news, YouTube, manifestos)
- Real-time voter sentiment analysis.
- Economic and demographic factor correlation
- Cross-platform sentiment aggregation
- Transparent methodology and reproducible results
- Community-driven development approach

## 🚀 Tech Stack

### Frontend
- Next.js 13+ (App Router)
- Tailwind CSS
- TypeScript
- React Query
- Chart.js/D3.js for visualizations

### Backend
- Node.js
- Express.js
- MongoDB
- Redis for caching
- JWT authentication

### ML Pipeline
- Python 3.9+
- PyTorch
- Hugging Face Transformers
- NLTK/spaCy
- Pandas/NumPy
- Scikit-learn

### Data Collection
- Beautiful Soup/Scrapy
- Twitter API v2
- YouTube Data API
- News API
- Custom web scrapers

### DevOps
- Docker
- GitHub Actions
- Kubernetes
- Prometheus/Grafana

## 📋 Prerequisites

```

```

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/Power-Rangers-Bihar/Open-Election-prediction.git
cd election-sentiment-analyzer
```

2. Install frontend dependencies
```bash
cd frontend
npm install
```

3. Install backend dependencies
```bash
cd backend
npm install
```

4. Set up Python environment
```bash
cd ml_pipeline
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

5. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

6. Run using Docker Compose
```bash
docker-compose up
```

## 📁 Project Structure

```
election-sentiment-analyzer/
├── README.md
├── LICENSE
├── .gitignore
├── docker-compose.yml
├── requirements.txt
├── package.json
│
├── frontend/                      # Next.js Frontend
│   ├── src/
│   │   ├── app/                  # Next.js 13+ App Router
│   │   ├── components/           # Reusable UI components
│   │   ├── styles/               # Tailwind and custom styles
│   │   ├── lib/                  # Frontend utilities
│   │   └── types/                # TypeScript type definitions
│   ├── public/                   # Static assets
│   └── tests/                    # Frontend tests
│
├── backend/                     # Node.js Backend
│   ├── src/
│   │   ├── controllers/         # Route controllers
│   │   ├── models/              # Database models
│   │   ├── routes/              # API routes
│   │   ├── middleware/          # Custom middleware
│   │   ├── services/            # Business logic
│   │   └── utils/               # Helper functions
│   ├── config/                  # Configuration files
│   └── tests/                   # Backend tests
│
├── ml_pipeline/                 # Python ML Components
│   ├── src/
│   │   ├── data_collection/     # Data gathering modules
│   │   │   ├── social_media/    # Social media API integrations
│   │   │   ├── news_scraper/    # News website scrapers
│   │   │   ├── youtube_api/     # YouTube data collection
│   │   │   └── manifesto_parser/ # Political manifesto analysis
│   │   │
│   │   ├── data_pipeline/       # Data Integration Pipeline (moved inside ML pipeline)
│   │   │   ├── collectors/      # Data collection jobs
│   │   │   ├── transformers/    # Data transformation logic
│   │   │   ├── loaders/         # Database loading scripts
│   │   │   └── schedulers/      # Pipeline scheduling
│   │   │
│   │   ├── preprocessing/       # Data preprocessing
│   │   │   ├── text_cleaning/
│   │   │   ├── feature_engineering/
│   │   │   └── data_integration/
│   │   │
│   │   ├── models/              # ML models
│   │   │   ├── sentiment_analysis/
│   │   │   ├── topic_modeling/
│   │   │   └── prediction/
│   │   │
│   │   ├── rag_engine/          # RAG Implementation
│   │   │   ├── document_store/
│   │   │   ├── embeddings/
│   │   │   └── retrieval/
│   │   │
│   │   └── evaluation/          # Model evaluation
│   │
│   ├── notebooks/               # Jupyter notebooks for analysis
│   ├── data/                    # Data directory
│   │   ├── raw/                # Raw collected data
│   │   ├── processed/          # Processed datasets
│   │   └── external/           # External data sources
│   │
│   └── tests/                   # ML pipeline tests
│
└── docs/                        # Documentation
    ├── api/                   # API documentation
    ├── ml/                    # ML pipeline documentation
    ├── deployment/            # Deployment guides
    └── development/           # Development setup guides
```

## 🔧 Usage

### Development Mode

1. Start the frontend
```bash
cd frontend
npm run dev
```

2. Start the backend
```bash
cd backend
npm run dev
```

3. Run ML pipeline
```bash
cd ml_pipeline
python src/main.py
```

### Production Mode
```bash
docker-compose -f docker-compose.prod.yml up
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📊 Features

### Data Collection 
- 🌐 Multi-platform social media analysis
- 📰 News source aggregation
- 🎥 YouTube comment sentiment analysis
- 📄 Political manifesto parsing
- 📊 Demographic data integration

### Analysis
- 🤖 Machine learning-based sentiment analysis
- 📈 Trend prediction
- 🗺️ Geographic sentiment mapping
- 💹 Economic indicator correlation
- 👥 Demographic impact analysis

### Visualization
- 📊 Interactive dashboards
- 🗺️ Geographic heat maps
- 📈 Real-time trend graphs
- 📱 Responsive design
- 🔄 Live updates

## 📖 Documentation

Detailed documentation is available in the `/docs` directory:
- [API Documentation](docs/api/README.md)
- [ML Pipeline Guide](docs/ml/README.md)
- [Deployment Guide](docs/deployment/README.md)
- [Development Guide](docs/development/README.md)

## 🔍 Testing

```bash
# Run frontend tests
cd frontend
npm test

# Run backend tests
cd backend
npm test

# Run ML pipeline tests
cd ml_pipeline
pytest
```

## 📈 Performance

- To be added

## 🔐 Security

- Data encryption
- GDPR compliance
- Regular security audits

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors
- Built with support from the open-source community
- Special thanks to ML/NLP research papers that influenced this project

## 📞 Contact

- Github: [Kaushlendu Narayan Prashar](https://github.com/Kaushlendu-Narayan-Parashar)
          [Aditya Pandey](https://github.com/pandeyOnGit)
- LinkedIn: [Kaushlendu Narayan Prashar](https://www.linkedin.com/in/kaushlendu-parashar-790447230?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
            [Aditya Pandey](https://www.linkedin.com/in/pandeyonsocial?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
- Twitter: [@Kaushlendu](https://x.com/_Kaush)

---
