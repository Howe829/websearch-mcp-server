# WebSearch MCP 服务器

一个简单的网络搜索服务器，支持自由搜索并将网页内容转换为Markdown格式。

## 功能特点

-   **网络搜索：** 使用不同的搜索提供商进行网络搜索。目前仅支持必应(Bing), 百度。
-   **Markdown转换：** 将URL内容转换为Markdown格式。
-   **微信公众号文章：** 搜索并获取微信公众号文章内容。
-   **GitHub 搜索功能：** 轻松搜索 GitHub 上的所有内容，包括仓库、用户、问题等。

## 快速开始

### 前提条件

-   Python 3.12 或更高版本
-   使用uv进行依赖管理（或pip）

### 安装

1.  克隆仓库：

    ```bash
    git clone https://github.com/Howe829/websearch-mcp-server.git
    cd websearch-mcp-server
    ```

2.  使用uv安装依赖（推荐）：

    ```bash
    uv venv && uv sync
    ```

    或者，如果您更喜欢使用pip：

    ```bash
    pip install -r requirements.txt
    ```

### 配置

1.  基于`.env.example`文件创建一个`.env`文件：

    ```bash
    cp .env.example .env
    ```

2.  根据您的需求修改`.env`文件：

    ```
    BING_SEARCH_BASE_URL="https://www.cn.bing.com"
    LANGUAGE="zh-Hans"
    CC="cn"
    IMPERSONATE="edge"
    HOST=127.0.0.1
    PORT=8002
    SERVER_MODE=streamable-http
    ```

### 使用方法

使用uv运行服务器：

```bash
uv run python server.py
```

或者使用python运行服务器：

```bash
source .venv/bin/activate
python server.py
```

## 贡献
欢迎贡献！

本项目使用pytest进行单元测试
```bash
uv pip install pytest
uv pip install pytest-asyncio
uv run pytest
```

并使用ruff进行代码风格格式化
```bash
uv pip install ruff
ruff format .
```

使用mcp inspector调试此服务器
```bash
uv run fastmcp dev server.py
```

