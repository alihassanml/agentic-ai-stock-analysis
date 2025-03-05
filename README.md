# Agentic AI Stock Analysis

![Agentic AI Stock Analysis](https://your-image-url.com/banner.png)

## 🚀 Overview
Agentic AI Stock Analysis is an AI-powered multi-agent system that analyzes stock market trends, provides analyst recommendations, and fetches the latest news using Groq AI models. It integrates financial and web search agents to deliver real-time insights.

## 🔥 Features
- **Multi-Agent System:** Uses multiple AI agents for finance and web search.
- **Stock Analysis:** Retrieves stock prices, analyst recommendations, and financial fundamentals.
- **Web Search Integration:** Fetches the latest news and updates.
- **FastAPI-based Playground:** Interactive UI for seamless exploration.
- **Groq AI Model:** Leverages `deepseek-r1-distill-llama-70b` for processing.

## 🛠 Tech Stack
- **Backend:** FastAPI
- **AI Model:** Groq (`deepseek-r1-distill-llama-70b`)
- **Finance Data:** `YFinanceTools`
- **Web Search:** `DuckDuckGo`
- **Deployment:** FastAPI Playground

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/alihassanml/agentic-ai-stock-analysis.git
cd agentic-ai-stock-analysis

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## 🔑 Environment Variables
Create a `.env` file and add your API keys:
```env
GROQ_API_KEY=your_groq_api_key
PHI_API_KEY=your_phi_api_key
```

## 🚀 Usage
```bash
python app.py
```
The application will run and provide stock insights based on AI-powered analysis.

## 🖥️ API Endpoints
- **`/playground`** - Interactive AI playground
- **`/analyze?query=<stock_query>`** - Fetch stock recommendations and news

## 📝 Example Output
```
Analyst Recommendations for AAPL:
Strong Buy: 8 | Buy: 24 | Hold: 12 | Sell: 1 | Strong Sell: 2

Latest News:
1. Apple Unveils Most Powerful Mac Ever - Yahoo Finance
2. Apple Updates MacBook Air with M4 Chip - TechCrunch
```

## 🤖 Contributing
Contributions are welcome! Feel free to submit a pull request.

## 📜 License
This project is licensed under the MIT License.

## 📧 Contact
Ali Hassan - [GitHub](https://github.com/alihassanml)

---
✅ **Star this repo** if you find it helpful! ⭐

