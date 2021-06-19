class Stack:
  lista = []
  index = 0
  def __init__(self, size):
    if(size <= 0):
      raise Exception()
    self.size = size
  def push(self, item):
    if(len(self.lista) >= self.size):
      raise Exception();
    self.lista.append(item)
    self.index = self.index + 1
  def pop(self):
    if(len(self.lista) <= 0):
      raise Exception();
    item = self.lista[self.index - 1]
    self.lista.remove(item)
    self.index = self.index - 1
    return item;
  def hasItems(self):
    return self.index != 0;

newLista = list(range(0,50))
print('newLista: {newLista}'.format(newLista=newLista))

pilha = Stack(50)
for item in newLista:
  pilha.push(item)

while pilha.hasItems():
  print(pilha.pop())