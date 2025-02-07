import asyncio
from bleak import BleakScanner
import os
from logger import get_logger

logger = get_logger("Discovery")

async def discover(debug=False):
    try:
        logger.info("Starting Bluetooth discovery...")
        devices = await BleakScanner.discover()
        logger.info("Conpleted Bluetooth discovery!")
        if debug:
            filtered_devices = [{"name": device.name, "address": device.address} for device in devices]
            if not filtered_devices:
                logger.error("No Bluetooth devices found!")
        else:
            filtered_devices = [
                {"name": device.name, "address": device.address}
                for device in devices
                if device.name and "TP350S" in device.name
            ]
    except Exception as e:
        logger.error(f"There was an issue during Bluetooth discovery: \n {e}")
        raise

async def main(debug_flag=None):
    check_debug = debug_flag if debug_flag is not None else os.getenv("DEBUG", "FALSE").upper() == "TRUE"
    if check_debug:
        print("DEBUG MODE ENABLED")
    devices = await discover(debug=check_debug)

if __name__ == "__main__":
    asyncio.run(main())
