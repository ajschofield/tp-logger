from bleak import BleakScanner
from logger import get_logger

logger = get_logger("Discovery")

async def discover(debug=False):
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
        return filtered_devices
    except Exception as e:
        logger.error(f"There was an issue during Bluetooth discovery: \n {e}")
        raise
