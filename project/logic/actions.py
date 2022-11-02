from random import shuffle
from typing import (List, Dict, Any)
from uuid import uuid4

from config import settings
from consts import (ALL_CARDS, ALL_CARDS_COUNT)
from logic.utils import (add_data_inside_file, convert_list_into_str)


def _create_game_file() -> str:
    game_uuid: str = str(uuid4())
    add_data_inside_file(file_name=game_uuid, data=game_uuid)
    return game_uuid


def init_all_cards() -> List[Dict[str, Any]]:
    identified: int = 0
    # set identifier to all cards
    for card in ALL_CARDS:
        card['id'] = identified
        identified += 1
    return ALL_CARDS


def _init_all_cards_id() -> List[str]:
    return [str(i) for i in range(0, ALL_CARDS_COUNT)]


def _shuffle_cards_id(cards_id: List[str]) -> List[str]:
    shuffle(cards_id)
    return cards_id


def _add_all_cards_id_inside_game_file(uuid: str):
    all_cards_id = _init_all_cards_id()
    # shuffle cards id for randomize
    all_cards_id = _shuffle_cards_id(cards_id=all_cards_id)
    add_data_inside_file(file_name=uuid, data=all_cards_id)


def rewrite_all_cards_id(file_name: str, all_cards_id: List[str]):
    # rewrite uuid and cards id data
    file = open(f'{settings.GAMES_DIR}/{file_name}.txt', 'w')
    file.write(f'{file_name}\n')
    file.write(f'{convert_list_into_str(all_cards_id)}\n')
    file.close()


def create_game():
    current_game_uuid: str = _create_game_file()
    _add_all_cards_id_inside_game_file(uuid=current_game_uuid)
    return current_game_uuid


__all__ = (
    'init_all_cards',
    'rewrite_all_cards_id',
    'create_game',
)
