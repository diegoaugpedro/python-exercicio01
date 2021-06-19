class Set:
  lista = []
  def __init__(self):
    self.lista = []
  def add(self,item):
    if(item not in self.lista):
      self.lista.append(item)
  def getList(self):
    return self.lista;

newSet = Set();

for n in range(1,50):
    for x in range(5,n):
        if n % x == 0:
            newSet.add((n//x))

for i in newSet.getList():
  print(i)