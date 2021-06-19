class Tuple:
  def __init__ (self, item01, item02):
    self.item01 = item01
    self.item02 = item02
  def toString(self):
    return '({item01},{item02})'.format(item01 = self.item01, item02 = self.item02)

newTuple = Tuple('Hello Darkness', ' my old friend!')
print(newTuple.toString())