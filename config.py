from pathlib import Path
from typing import List, Set, Union

from pydantic import BaseModel, Extra, validator


class Config(BaseModel, extra=Extra.ignore):
    today_waifu_ban_id_list: Set[int] = set()
    today_waifu_default_change_waifu: bool = True
    today_waifu_default_limit_times: int = 2
    today_waifu_aliases: List[str] = ['每日老婆', ]
    today_waifu_record_dir: Path = Path(__file__).parent / 'record'
    today_waifu_superuser_opt: bool = False