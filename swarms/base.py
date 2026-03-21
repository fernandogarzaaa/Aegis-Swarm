import abc

class BaseSwarm(abc.ABC):
    @abc.abstractmethod
    def run(self, data):
        pass

    def log(self, message):
        print(f"[Swarm][{self.__class__.__name__}] {message}")
