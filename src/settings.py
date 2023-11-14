"""Project settings, path - to the file storing the data"""


class Config:
    """Project config"""

    @property
    def path(self) -> str:
        """Path getter"""

        return self.__path


    @path.setter
    def path(self, v) -> None:
        """Path setter"""

        self.__path = v


SETTINGS = Config()
