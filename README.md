# AI Customer Support Agent with LangFlow

A sophisticated customer support AI system built using LangFlow that combines RAG (Retrieval Augmented Generation) with order and product database lookups. This agent can answer FAQs, check order statuses, and provide product information through a simple Streamlit interface.

I am using the Python API not the actual python code from langflow, So I am attaching the langflow json which includes the agents and model details.

## 🌟 Features

- **FAQ Handling**: Uses RAG to retrieve and answer common customer questions from company documentation
- **Order Lookup**: Checks order status and details using order ID
- **Product Information**: Retrieves detailed product information from the database
- **Multi-Agent Architecture**: Uses a manager agent to route queries to specialized sub-agents
- **Simple UI**: Clean Streamlit interface for easy interaction

## 🛠️ Technologies Used

- LangFlow for AI agent orchestration
- AstraDB for vector and traditional database storage
- OpenAI API for language model capabilities
- Streamlit for the user interface
- Python for backend implementation

## 📋 Prerequisites

- Python 3.8+
- LangFlow account
- AstraDB account
- OpenAI API key

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/customer-support-ai.git
cd customer-support-ai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
APP_TOKEN=your_langflow_token
```

4. Import the LangFlow configuration:
- Go to LangFlow
- Use the Import button
- Select the `flow.json` file from this repository

5. Set up the databases:
- Create an AstraDB database named "customer"
- Import the sample data:
  - `sample_orders.csv` into the orders collection
  - `sample_products.csv` into the products collection
  - Upload the FAQ PDF to the FAQ collection

6. Run the application:
```bash
streamlit run main.py
```

## 📁 Project Structure

```
customer-support-ai/
├── main.py              # Streamlit application
├── requirements.txt     # Python dependencies
├── flow.json           # LangFlow configuration
├── data/
│   ├── sample_orders.csv
│   ├── sample_products.csv
│   └── faq.pdf
└── .env                # Environment variables , In here you should add the APP_TOKEN from langflow
```

# This is the simple practise project, working on small dataset, just to learn things. Happy Coding!!
