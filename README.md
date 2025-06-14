# Honeypot Detector MCP

An MCP server that detects potential honeypot tokens on Ethereum, BNB Smart Chain (BSC), and Base.

> **Honeypot** is a type of fraudulent smart contract that allows users to buy tokens but prevents them from selling or makes selling extremely difficult.

![GitHub License](https://img.shields.io/github/license/kukapay/honeypot-detector-mcp) 
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## Features

- **Honeypot Analysis**: Check if a token address is a honeypot using the honeypot.is API.
- **Supported Chains**: Analyzes tokens on Ethereum, Binance Smart Chain and Base.
- **Markdown Output**: Returns detailed analysis in Markdown, including:
  - Token name
  - Address
  - Honeypot status
  - Risk level
  - Buy, sell, and transfer taxes
  - Contract code open-source status

## Installation

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kukapay/honeypot-detector-mcp.git
   cd honeypot-detector-mcp
   ```

2. **Install Dependencies**:
   ```bash
   uv sync
   ```

3. **Installing to Claude Desktop**:

    Install the server as a Claude Desktop application:
    ```bash
    uv run mcp install main.py --name "Honeypot Detector"
    ```

    Configuration file as a reference:

    ```json
    {
       "mcpServers": {
           "Honeypot Detector": {
               "command": "uv",
               "args": [ "--directory", "/path/to/honeypot-detector-mcp", "run", "main.py" ]
           }
       }
    }
    ```
    Replace `/path/to/honeypot-detector-mcp` with your actual installation path.
   ```

## Tool

The `check_honeypot` tool takes a token address as input parameter.

### Example Usage

**Input Prompt**:
```
Please check if the token at address 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48 is a honeypot.
```

**Output Markdown**:
```markdown
# Honeypot Analysis for USDC
- **Address**: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
- **Is Honeypot**: False
- **Risk Level**: Low
- **Buy Tax**: 0%
- **Sell Tax**: 0%
- **Transfer Tax**: 0%
- **Contract Code Open Source**: True
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

