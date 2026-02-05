"""Support for SmartThings Cloud."""

import logging
from dataclasses import dataclass

from homeassistant.config_entries import ConfigEntry
from pysmartthings import ComponentStatus, Device, Scene, SmartThings

_LOGGER = logging.getLogger(__name__)


@dataclass
class SmartThingsData:
    """Define an object to hold SmartThings data."""

    devices: dict[str, FullDevice]
    scenes: dict[str, Scene]
    rooms: dict[str, str]
    client: SmartThings


@dataclass
class FullDevice:
    """Define an object to hold device data."""

    device: Device
    status: dict[str, ComponentStatus]
    online: bool


type SmartThingsConfigEntry = ConfigEntry[SmartThingsData]
