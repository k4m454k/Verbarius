from random import choice
from string import Template
from verbarius.languages import BaseLanguage, russian


class Verbarius:
    """
        A class Verbarius

        ...

        Attributes
        ----------
        language : BaseLanguage, optional
            language template, Default russian

        Methods
        -------
        get_time_string(hour: str, minute: str):
            Prints the person's name and age.
        """
    def __init__(self, language: BaseLanguage = russian):
        self.language = language

    def get_time_string(self, hour: int, minute: int) -> str:
        """
        Prints random verbarius time string.

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
        base_template = Template(choice(self.language.minutes.get(minute)))
        return base_template.safe_substitute(self.language.hours.get(hour))
