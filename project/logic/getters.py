from typing import (List, Dict, Any)

from consts import ALL_CARDS_ID_LINE
from logic.actions import rewrite_all_cards_id
from logic.utils import (convert_str_into_list, get_line_from_file)


def _get_all_cards_id_from_file(file_name: str) -> List[str]:
    all_cards_id_str: str = get_line_from_file(file_name, ALL_CARDS_ID_LINE)
    return convert_str_into_list(all_cards_id_str)


def _get_card_by_id(cards: List[Dict[str, Any]], card_id: str) -> Dict[str, Any]:
    for card in cards:
        if card['id'] == int(card_id):
            return card


def get_card(all_cards: List[Dict[str, Any]], game_uuid: str) -> Dict[str, Any]:
    all_cards_id: List[str] = _get_all_cards_id_from_file(file_name=game_uuid)
    last_card_id: str = all_cards_id[-1]
    # remove selected card
    all_cards_id.remove(last_card_id)
    # need rewrite all cards without selected
    rewrite_all_cards_id(file_name=game_uuid, all_cards_id=all_cards_id)
    return _get_card_by_id(cards=all_cards, card_id=last_card_id)


__all__ = (
    'get_card',
)
