import asyncio
import httpx
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP, Context
from mcp.server.fastmcp.prompts import base

# Configuration
API_KEY = None  # Optional: Replace with your honeypot.is API key if available
HONEYPOT_API_URL = "https://api.honeypot.is/v2/IsHoneypot"

# Initialize FastMCP server
mcp = FastMCP(
    name="Honeypot Detector",
    dependencies=["httpx"]
)

async def fetch_honeypot_data(address: str, ctx: Context) -> Dict[str, Any]:
    """Fetch data from honeypot.is API"""
    async with httpx.AsyncClient() as client:
        headers = {"X-API-KEY": API_KEY} if API_KEY else {}
        params = {"address": address}
        try:
            response = await client.get(HONEYPOT_API_URL, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise ValueError(f"API request failed: {str(e)}")

@mcp.tool()
async def check_honeypot(address: str, ctx: Context) -> str:
    """Check if a token address is a honeypot using honeypot.is API

    Supports tokens on Ethereum, Binance Smart Chain (BSC) and Base.

    Args:
        address: Token address to check (e.g., 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48)

    Returns:
        Markdown string containing honeypot analysis results
    """
    ctx.info(f"Checking honeypot status for address {address}")

    # Validate address format (basic check)
    if not address.startswith("0x") or len(address) != 42:
        raise ValueError("Invalid address format")

    data = await fetch_honeypot_data(address, ctx)
    
    # Extract relevant fields
    is_honeypot = data.get("honeypotResult", {}).get("isHoneypot", False)
    risk = data.get("summary", {}).get("risk", "unknown")
    token_name = data.get("token", {}).get("name", "Unknown")
    buy_tax = data.get("simulationResult", {}).get("buyTax", "N/A")
    sell_tax = data.get("simulationResult", {}).get("sellTax", "N/A")
    transfer_tax = data.get("simulationResult", {}).get("transferTax", "N/A")
    is_open_source = data.get("contractCode", {}).get("openSource", "Unknown")

    # Format as Markdown
    result = f"""# Honeypot Analysis for {token_name}
- **Address**: {address}
- **Is Honeypot**: {is_honeypot}
- **Risk Level**: {risk}
- **Buy Tax**: {buy_tax}
- **Sell Tax**: {sell_tax}
- **Transfer Tax**: {transfer_tax}
- **Contract Code Open Source**: {is_open_source}
"""
    return result

@mcp.prompt()
def analyze_honeypot(address: str) -> list[base.Message]:
    """Prompt to analyze a token address for honeypot status

    Args:
        address: Token address to analyze
    """
    return [
        base.UserMessage("Please analyze this token address for potential honeypot risks:"),
        base.UserMessage(f"Address: {address}"),
        base.AssistantMessage("I'll check the honeypot status using the honeypot.is API.")
    ]

if __name__ == "__main__":
    mcp.run()
