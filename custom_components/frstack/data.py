"""Custom types for frstack."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import FRStackApiClient
    from .coordinator import FRStackDataUpdateCoordinator


type FRStackConfigEntry = ConfigEntry[FRStackData]


@dataclass
class FRStackData:
    """Data for the FRStack integration."""

    client: FRStackApiClient
    coordinator: FRStackDataUpdateCoordinator
    integration: Integration
