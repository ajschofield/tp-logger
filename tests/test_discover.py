from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, patch
from discover import discover
from bleak.backends.device import BLEDevice

class TestDiscover(IsolatedAsyncioTestCase):
    @patch('src.discover.BleakScanner.discover', new_callable=AsyncMock)
    async def test_device_discovery_successful(self, mock_discover):
        device_1 = BLEDevice(address="AA:BB:CC:DD:EE:FF", name="TP350S", details={}, rssi=-40)

        mock_discover.return_value = [device_1]

        result = await discover()

        expected = [
            {"name": "TP350S", "address": "AA:BB:CC:DD:EE:FF"},
        ]

        self.assertEqual(result,expected)
    
    @patch('src.discover.BleakScanner.discover', new_callable=AsyncMock)
    async def test_device_discovery_successful_with_debug(self, mock_discover):
        device_1 = BLEDevice(address="AA:BB:CC:DD:EE:FF", name="TP350S", details={}, rssi=-40)
        device_2 = BLEDevice(address="GG:HH:II:JJ:KK:LL", name="Device 2", details={}, rssi=-64)

        mock_discover.return_value = [device_1, device_2]

        result = await discover()

        expected = [
            {"name": "TP350S", "address": "AA:BB:CC:DD:EE:FF"},
            {"name": "Device 2", "address": "GG:HH:II:JJ:KK:LL"}
        ]

        self.assertEqual(result,expected)
