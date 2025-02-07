from bleak import BleakScanner
from logger import get_logger
import asyncio

logger = get_logger("Discovery")

async def discover(debug=False):
    while True:
        try:
            logger.info("Starting Bluetooth discovery...")
            scan = await BleakScanner.discover()
            logger.info("Completed Bluetooth discovery!")
            logger.debug(scan)
            devices = [{"name": device.name, "address": device.address} for device in scan]
            filtered_devices = [
                device
                for device in devices
                if device["name"] and "TP350S" in device["name"]
            ]
            if filtered_devices:
                return filtered_devices
            else:
                logger.info("No device was found. Trying again in 5 seconds...")
                await asyncio.sleep(5)
        except Exception as e:
            logger.error(f"There was an issue during Bluetooth discovery: \n {e}")
            raise
