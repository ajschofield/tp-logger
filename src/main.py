from discover import discover
import os
from logger import get_logger
import asyncio

logger = get_logger("Main")

async def main(debug_flag=None):
    check_debug = debug_flag if debug_flag is not None else os.getenv("DEBUG", "FALSE").upper() == "TRUE"
    if check_debug:
        logger.info("Debug mode is enabled")
    devices = await discover(debug=check_debug)
    print(devices)

if __name__ == "__main__":
    asyncio.run(main())
