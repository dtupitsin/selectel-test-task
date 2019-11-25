from abc import ABC, abstractmethod


class Storage(ABC):
    """ Just as Interface """
    def __init__(self):
        pass

    @abstractmethod
    def upload(self, user_id: str, filename: str, data: str):
        """This method must upload `data` as `filename` to user_id container """

    @abstractmethod
    def list(self, user_id: str):
        pass

    @abstractmethod
    def delete(self, user_id: str, filename: str):
        pass
