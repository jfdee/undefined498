from typing import (List, NoReturn)

from config import settings


def convert_list_into_str(v: List[str]) -> str:
    return ' '.join(v)


def convert_str_into_list(v: str) -> List[str]:
    return v.strip('\n').split(' ')


def get_line_from_file(file_name: str, line_number: int) -> str:
    file = open(f'{settings.GAMES_DIR}{file_name}.txt', 'r')
    lines = file.readlines()
    return lines[line_number]


def add_data_inside_file(file_name: str, data) -> NoReturn:
    file = open(f'{settings.GAMES_DIR}{file_name}.txt', 'a')
    saving_data = data
    if isinstance(data, list):
        saving_data = convert_list_into_str(data)
    file.write(f'{saving_data}\n')
    file.close()
