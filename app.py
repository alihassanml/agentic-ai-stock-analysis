from fastapi import FastAPI
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import playground, serve_playground_app

# Set Groq API key
groq_api = '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'

# Define Web Search Agent
web_Search_agent = Agent(
    name='Web Search Agent',
    role='Search the web for information',
    model=Groq(id='deepseek-r1-distill-llama-70b', api_key=groq_api),
    tools=[DuckDuckGo],
    instructions=["Always include source"],
    show_tool_calls=True,
    markdown=True,
)

# Define Finance Agent
finance_agent = Agent(
    name='Finance AI Agent',
    model=Groq(id='deepseek-r1-distill-llama-70b', api_key=groq_api),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use instructions to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Define Multi-Agent
multi_AI_Agent = Agent(
    team=[web_Search_agent, finance_agent],
    model=Groq(id='deepseek-r1-distill-llama-70b', api_key=groq_api),
    instructions=[
        "Provide well-structured and concise responses.",
        "Always include the original data source for transparency.",
        "Use a well-formatted table for numerical and financial data.",
        "Summarize key insights in bullet points for better readability.",
        "Highlight important trends, anomalies, and patterns.",
        "Ensure accuracy when presenting stock prices, financial reports, or news.",
        "For news updates, focus on the latest and most relevant information.",
    ],
    show_tool_calls=True,
    markdown=True,
)

multi_AI_Agent.print_response("Summarize analyst recommendation and share the latest news of Apple")

# Create FastAPI Playground App
from phi.playground import Playground, serve_playground_app

app = Playground(agents=[multi_AI_Agent]).get_app()


# Ensure correct module execution
if __name__ == "__main__":
    serve_playground_app("app:app", reload=True)
