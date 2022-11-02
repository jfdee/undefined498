import uvicorn
from typing import (List, Any, Dict)

from fastapi import FastAPI

from logic.actions import (create_game, init_all_cards)
from logic.getters import get_card

app = FastAPI()

ALL_CARDS: List[Dict[str, Any]] = []
ALL_CARDS_ID: List[int] = []
PLAYERS_COUNT: int = 2


@app.get('/api/create-game')
def create_game_point():
    game_uuid = create_game()
    return {'uuid': game_uuid}


@app.get('/api/get-card')
def get_card_point(uuid: str):
    all_cards: List[Dict[str, Any]] = init_all_cards()
    selected_card = get_card(all_cards, game_uuid=uuid)
    return selected_card


if __name__ == '__main__':
    uvicorn.run(app=app, host='localhost', port=8000, log_level='info')