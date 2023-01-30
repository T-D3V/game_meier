import typer
import random

class Dice:
  MAX_NUMBER:int = 6
  
  def rollDice(self) -> int:
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

class Cup:
  __nums:list[int]
  __dice1:Dice
  __dice2:Dice
  
  def __init__(self, dice1:Dice = RealDice(), dice2:Dice = RealDice()) -> None:
    self.__dice1 = dice1
    self.__dice2 = dice2
    
  def shake(self) -> None:
    self.__nums.clear()
    self.__nums.append(self.__dice1.rollDice())
    self.__nums.append(self.__dice2.rollDice())
    
  def getNum(self) -> int:
    self.__nums.sort(reverse=True) 
    return int(''.join(map(str,self.__nums)))
  
class Numbers:
  __nums:list[int] = [31,32,41,42,43,51,52,53,54,61,62,63,64,65,11,22,33,44,55,66,21]
  
  def isBigger(self, a:int, b:int) -> bool:
    return self.__nums.index(a) > self.__nums.index(b)
  
  def isBiggerEqual(self, a:int, b:int) -> bool:
    return self.__nums.index(a) >= self.__nums.index(b)
  
  def nextNum(self, num:int) -> int:
    return self.__nums[self.__nums.index(num)+1]
  
class Player:
  __negativePoints:int = 0
  __name:str
  
  def __init__(self, name:str) -> None:
    self.__name = name
    
  def recieveNegativePoint(self) -> None:
    self.__negativePoints += 1
    
  @property
  def negativePoints(self) -> int:
    return self.__negativePoints
    
  @property
  def name(self) -> str:
    return self.__name
  
  def askChoice(self, toldNumber:int) -> int:
    raise NotImplementedError
  
  def playTurn(self, rolledNumber:int, toldNumber:int) -> int:
    raise NotImplementedError
  
class Human(Player):
  def __init__(self, name: str) -> None:
    super().__init__(name)
    
  def askChoice(self, toldNumber: int) -> int:
    return super().askChoice(toldNumber)
  
  def playTurn(self, rolledNumber: int, toldNumber: int) -> int:
    return super().playTurn(rolledNumber, toldNumber)
    
class Computer(Player):
  def __init__(self, name: str) -> None:
    super().__init__(name)
    
  def askChoice(self, toldNumber: int) -> int:
    return super().askChoice(toldNumber)
  
  def playTurn(self, rolledNumber: int, toldNumber: int) -> int:
    return super().playTurn(rolledNumber, toldNumber)
  
class GUI:
  
  def askPlayers(self) -> list[str]:
    return []
  
  def __askAnotherPlayer(self) -> bool:
    return True
  
  def printRanks(self, competetors:list[Player]) -> None:
    pass
  
  def cupUncovered(self, player:Player, loser:Player, rolledNum:int) -> None:
    pass

class Meier:
  __MEIER:int = 21
  __toldNumber:int
  __cup:Cup
  def __init__(self, cup:Cup = Cup()) -> None:
    self.__cup = cup
    
  def shakeCup(self) -> None:
    return self.__cup.shake()

class GamePlay(typer.Typer):
  __currentPlayer:Player
  __previousPlayer:Player
  __meierClass:Meier
  __players:list[Player]
  def __init__(self, players:list[str], meier: Meier) -> None:
    for player in players:
      self.__players.append(Player(player))
    self.__meierClass = meier
  
  def play(self) -> None:
    pass
  
  def __currentPlayerTurn(self) -> None:
    pass
  
  def __nextPlayer(self) -> None:
    __nextIndex:int = self.__players.index(self.__currentPlayer) + 1
    if __nextIndex == len(self.__players):
      __nextIndex = 0
    self.__previousPlayer = self.__currentPlayer
    self.__currentPlayer = self.__players[__nextIndex]
  
  def __setStarter(self) -> None:
    self.__currentPlayer = self.__players[random.randint(0, len(self.__players)-1)]
    
  def __meier(self) -> None:
    pass

def main():
  players:list[str] = []
  GamePlay(players, Meier()).play()
  

if __name__ == "__main__":
  main()