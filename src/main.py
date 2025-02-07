from discover import discover
import os
from logger import get_logger
import asyncio

logger = get_logger("Main")

# TODO - This is not tested yet as I only have one device.
# Needs mocking and testing in test_main.py

async def device_selection(devices):
    print("\nPlease choose which device to use:")
    for index, device in enumerate(devices, start=1):
        print(f"{index}. {device['name']} - {device['address']}")

    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(devices):
                return devices[choice - 1]
            else:
                logger.warning("Invalid selection.")
        except ValueError:
            logger.warning("Invalid selection.")

async def main(debug_flag=None):

    # Discover

    check_debug = debug_flag if debug_flag is not None else os.getenv("DEBUG", "FALSE").upper() == "TRUE"
    if check_debug:
        logger.info("Debug mode is enabled")
    devices = await discover(debug=check_debug)

    if not devices:
        logger.error("No supported devices were found during discovery")
        return
    
    if len(devices) >= 2:
        logger.info("There are multiple TP350S devices!")
        device = await device_selection(devices)
    else:
        device = devices[0]
        logger.info(f"Single device selected: {device['name']} - {device['address']}")

if __name__ == "__main__":
    asyncio.run(main())
