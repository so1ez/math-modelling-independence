"""Project settings, path - to the file storing the data"""


class Config:
    """project config"""

    @property
    def path(self) -> str:
        """path getter"""
        return self.__path


    @path.setter
    def path(self, v) -> None:
        """path setter"""
        self.__path = v


SETTINGS = Config()
