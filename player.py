import abc

class Player(classMeta = abc.ABCMeta):
  @classmethod
  def __subclasshook__(cls,  subclass):
    return (hasattr(subclass, 'shake') and callable(subclass.shake) and hasattr(subclass, 'getNum') and callable(subclass.getNum) or NotImplemented)

class HumanPlayer():
  pass

class ComputerPlayer():
  pass