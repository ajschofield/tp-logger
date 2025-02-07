from bleak import BleakScanner
from logger import get_logger

logger = get_logger("Discovery")

async def discover(debug=False):
    try:
        logger.info("Starting Bluetooth discovery...")
        devices = await BleakScanner.discover()
        logger.info("Completed Bluetooth discovery!")
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
