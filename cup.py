from dice import Dice, MockDice, RealDice
import abc

class Cup(classMeta = abc.ABCMeta):
  __num:int
  __dice1:Dice
  __dice2:Dice
  @classmethod
  def __subclasshook__(cls,  subclass):
    return (hasattr(subclass, 'shake') and callable(subclass.shake) and hasattr(subclass, 'getNum') and callable(subclass.getNum) or NotImplemented)
  
  @abc.abstractmethod
  @classmethod
  def shake(cls) -> None:
    firstNum = cls.__dice1.rollDice()
    secondNum = cls.__dice2.rollDice()
    cls.__num = int(str(firstNum) + str(secondNum))
    
  @abc.abstractmethod
  @classmethod
  def getNum(cls) -> int:
    return cls.__num
  
class RealCup(Cup):
  super().__dice1 = RealDice()
  super().__dice2 = RealDice()
  
  def shake(self) -> None:
    super().shake()
    
  def getNume(self) -> int:
    return super().getNum()
  
class MockCup(Cup):
  def __init__(self, dice1:MockDice, dice2:MockDice) -> None:
    super().__init__()
    super().__dice1 = dice1
    super().__dice2 = dice2
    
  def shake(self) -> None:
    super().shake()
    
  def getNume(self) -> int:
    return super().getNum()