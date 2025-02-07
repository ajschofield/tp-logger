import asyncio
from bleak import BleakScanner
import os

async def discover(debug=False):
    try:
        devices = await BleakScanner.discover()
        if debug:
            return [{"name": device.name, "address": device.address} for device in devices]
        else:
            return [
                {"name": device.name, "address": device.address}
                for device in devices
                if device.name and "TP350S" in device.name
            ]
    except Exception:
        return []

async def main():
    check_debug = os.getenv("DEBUG", "FALSE").upper() == "TRUE"
    if check_debug:
        print("DEBUG MODE ENABLED")
    devices = await discover(debug=check_debug)

    print(devices)

if __name__ == "__main__":
    asyncio.run(main())