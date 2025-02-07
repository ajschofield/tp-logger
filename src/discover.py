import asyncio
from bleak import BleakScanner

async def discover():
    try:
        devices = await BleakScanner.discover()
        return [{"name": device.name, "address": device.address} for device in devices]
    except Exception:
        return []