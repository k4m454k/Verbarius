from random import choice
from string import Template
from string_temps import base_temps, hours_temps


def get_time_string(hour: int, minute: int):
    if not all([hour in range(24), minute in range(60)]):
        raise ValueError
    base_template = Template(choice(base_temps.get(minute)))
    return base_template.safe_substitute(hours_temps.get(hour))
