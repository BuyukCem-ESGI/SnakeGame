class Player:
    def __init__(self):
        self._name = ""
        self._score = 0
        self.is_GameOver = False

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def __str__(self):
        if (self.is_GameOver):
            return "Name: " + self._name + " Score: " + str(self._score) + " is Game Over"
        if (self.is_GameOver == False):
            return "Name: " + self._name + " Score: " + str(self._score) + " is a Winner"

    score = property(get_score, set_score)
    name = property(get_name, set_name)
