class Config:
    n: int = 1

    @property
    def repeats(self):
        return self.n
    
    @repeats.setter
    def repeats(self, n: int):
        self.n = n


SETTINGS = Config()
