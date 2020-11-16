from typing import Dict, List
from verbarius import string_temps_ru


class BaseLanguage:
    def __init__(self, minutes_temp_dict: Dict[int, List[str]], hours_temp_dict: Dict[int, Dict[str, str]]):
        self.minutes_temp_dict = minutes_temp_dict
        self.hours_temp_dict = hours_temp_dict

    @property
    def hours(self) -> Dict[int, Dict[str, str]]:
        return self.hours_temp_dict

    @property
    def minutes(self) -> Dict[int, List[str]]:
        return self.minutes_temp_dict


russian = BaseLanguage(string_temps_ru.minutes_temps, string_temps_ru.hours_temps)
