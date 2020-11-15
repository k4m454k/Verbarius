from random import choice
from string import Template
from verbarius.string_temps import base_temps, hours_temps


class Verbarius:
    """
        A class Verbarius

        ...

        Attributes
        ----------
        base_temps : dict, optional
            minutes template dict
        hours_temps : dict, optional
            hours template dict

        Methods
        -------
        get_time_string(hour: str, minute: str):
            Prints the person's name and age.
        """
    def __init__(self, base_temps=base_temps, hours_temps=hours_temps):
        self.base_temps = base_temps
        self.hours_temps = hours_temps

    def get_time_string(self, hour: int, minute: int) -> str:
        """
        Prints verbarius time string.

        Parameters
        ----------
        hour: int
            hour (0-23)
        minute: int
            minute (0-59)

        Returns
        -------
        str
        """
        if not all([hour in range(24), minute in range(60)]):
            raise ValueError
        base_template = Template(choice(self.base_temps.get(minute)))
        return base_template.safe_substitute(self.hours_temps.get(hour))
