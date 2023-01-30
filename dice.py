import abc
import random

class Dice(metaclass= abc.ABCMeta):
  MAX_NUMBER:int = 6
  
  @classmethod
  def __subclasshook__(cls,  subclass):
    return (hasattr(subclass, 'rollDice') and callable(subclass.rollDice) or NotImplemented)
  
  @abc.abstractmethod
  @classmethod
  def rollDice(cls) -> int:
    raise NotImplementedError

class RealDice(Dice):
  __random:random.Random = random.Random()
  
  def rollDice(self) -> int:
    return self.__random.randint(1, super().MAX_NUMBER)

class MockDice(Dice):
  __num:int
  
  def __init__(self, num:int) -> None:
    super().__init__()
    self.__num = num
    
  def rollDice(self) -> int:
    return self.__num