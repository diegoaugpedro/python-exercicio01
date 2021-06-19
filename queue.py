class Queue:
  lista = []
  index = 0
  def __init__(self, size):
    if(size <= 0):
      raise Exception()
    self.size = size
  def add(self, item):
    if(len(self.lista) >= self.size):
      raise Exception();
    self.lista.append(item)
    self.index = self.index + 1
  def remove(self):
    if(len(self.lista) <= 0):
      raise Exception();
    item = self.lista[0]
    self.lista.remove(item)
    self.index = self.index - 1
    return item;
  def hasItems(self):
    return self.index != 0;

newLista = list(range(0,50))
print('newLista: {newLista}'.format(newLista=newLista))

fila = Queue(50)
for item in newLista:
  fila.add(item)

while fila.hasItems():
  print(fila.remove())