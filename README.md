# MCP Server - Docs Search & Fetch Tool

This project implements an **MCP (Model Context Protocol) server** designed to provide documentation search and retrieval capabilities.  
It uses the [Serper API](https://google.serper.dev/) for Google search results and scrapes official documentation websites for detailed content.

---

## Features

- **Search the web** for documentation pages related to popular AI and developer libraries:  
  - LangChain  
  - LlamaIndex  
  - OpenAI  
- **Fetch and extract** textual content from official documentation URLs  
- **Expose tools** via MCP-compatible endpoints for easy integration with AI clients  

---

## Getting Started

### Prerequisites

- Python 3.10+  
- `requests`, `beautifulsoup4`, `fastmcp`, and `python-dotenv` libraries  
- Serper API key (set in `.env` file as `SERPER_API_KEY`)  

### Installation

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv .venv
# On Linux/macOS:
source .venv/bin/activate
# On Windows PowerShell:
.venv\Scripts\activate

pip install -r requirements.txt
```
Create a .env file with your Serper API key:

```bash
SERPER_API_KEY=your_serper_api_key_here
```
### Running the Server
Run the MCP server using:
```bash
python main.py
```

Alternatively, you can use uv python and package manager(suggested).
More about uv : https://docs.astral.sh/uv/
