"""https://www.codewars.com/kata/51fda2d95d6efda45e00004e/
"""
class User(object):
    RANKS = (*range(-8, 0), *range(1, 9))

    def __init__(self):
        self.__rank     = 0
        self.__progress = 0

    @property
    def rank(self) -> int:
        return User.RANKS[self.__rank]

    @property
    def progress(self) -> int:
        return self.__progress

    @rank.setter
    def rank(self, __val: int) -> None:
        try:
            self.__rank = User.RANKS.index(__val)
        except:
            ...


    @progress.setter
    def progress(self, __val: int) -> None:
        if self.rank == 8:
            return None

        self.__progress = __val

        if (n := self.__progress // 100):
            self.rank += n
            self.__progress -= 100 * n

    def inc_progress(self, activity_rank: int) -> None:
        if activity_rank not in User.RANKS:
            raise Exception
        elif activity_rank == self.rank:
            self.progress += 3
        elif activity_rank + 1 == self.rank:
            self.progress += 1
        elif activity_rank == 1 and self.rank == -1:
            self.progress += 10
        elif activity_rank > self.rank:
            self.progress += 10 * (self.rank - activity_rank) * (self.rank - activity_rank)