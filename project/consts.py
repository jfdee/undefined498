from typing import (List, Dict, Any)

from config import settings
from localization.eng import ALL_CARDS_ENG
from localization.ru import ALL_CARDS_RU


ALL_CARDS: List[Dict[str, Any]] = ALL_CARDS_RU if settings.localization == 'ru' else ALL_CARDS_ENG

ALL_CARDS_COUNT: int = 52

GAME_UUID_LINE: int = 0
ALL_CARDS_ID_LINE: int = 1


__all__ = (
    'ALL_CARDS',
    'ALL_CARDS_COUNT',
    'GAME_UUID_LINE',
    'ALL_CARDS_ID_LINE',
)
