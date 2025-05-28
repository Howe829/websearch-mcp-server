# WebSearch MCP Server

A simple web search server that supports free search and converts URL content to Markdown. [中文](README-zh.md)

## Features

-   **Web Search:** Perform web searches using different providers. Currently, only Bing is supported.
-   **Markdown Conversion:** Convert the content of a URL into Markdown format.
-   **Wechat Official Account Articles:** Search and retrive wechat official account articles content.

## Getting Started

### Prerequisites

-   Python 3.12 or higher
-   uv for dependency management (or pip)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Howe829/websearch-mcp-server.git
    cd websearch-mcp-server
    ```

2.  Install the dependencies using uv (Recomend):

    ```bash
    uv venv && uv sync
    ```

    Or, if you prefer using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1.  Create a `.env` file based on the `.env.example` file:

    ```bash
    cp .env.example .env
    ```

2.  Modify the `.env` file with your desired settings:

    ```
    BING_SEARCH_BASE_URL="https://www.bing.com"
    LANGUAGE="en"
    CC="us"
    IMPERSONATE="edge"
    HOST=127.0.0.1
    PORT=8002
    SERVER_MODE=streamable-http
    ```

### Usage

Run the server using uv:

```bash
uv run python server.py
```

Or run the server using python:

```bash
source .venv/bin/activate
python server.py
```

## Contribution
Contributions are welcome!

This project uses pytest for unit tests
```bash
uv pip install pytest
uv pip install pytest-asyncio
uv run pytest
```

And use the ruff for code sytle formatting
```bash
uv pip install ruff
ruff format .
```

use mcp inpector to debug this server
```bash
uv run fastmcp dev server.py
```