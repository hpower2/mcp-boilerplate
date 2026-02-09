# MCP Boilerplate

A simple Model Context Protocol (MCP) server boilerplate that returns "hello world".

## Features

- Simple MCP server implementation using FastMCP
- Returns "hello world" message
- Easy to extend and customize

## Prerequisites

- Python 3.10 or higher
- pip or uv for package management

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mcp-boilerplate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or using uv:
```bash
uv pip install -r requirements.txt
```

## Usage

Run the server:
```bash
python server.py
```

The server will start and be ready to handle MCP requests.

## Configuration

This is a boilerplate project. Customize it according to your needs by:
- Adding new tools to `server.py`
- Modifying the `hello_world` function
- Adding dependencies to `requirements.txt`

## License

MIT
