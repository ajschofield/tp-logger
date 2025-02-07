from bleak import BleakClient, BleakScanner
from logger import get_logger

logger = get_logger("Connection")

async def connect(address):
    try:
        async with BleakClient(address) as client:
            if client.is_connected:
                logger.info("Connection successful!")

                services = await client.get_services()
                for service in services:
                    logger.debug(f"Service: {service.uuid}")
                    for char in service.characteristics:
                        logger.debug(f"  └── Characteristic: {char.uuid}, Properties: {char.properties}")
                return client
            else:
                logger.error("Failed to connect!")
    except Exception as e:
        logger.error(f"Connection error: {e}")
        raise