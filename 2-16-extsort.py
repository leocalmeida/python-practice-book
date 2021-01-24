def extsort(data):
  list01 =  []
  list02 = []

  # Separa pelo '.' os elementos da lista
  for i in data:
    list01.append(i.split('.'))
  
  # Realiza a ordenação os elementos baseando na extensão do arquivo
  list01.sort(key=lambda ext: ext[1])
  
  # Junta os elementos novamente
  for i in list01:
    list02.append('.'.join(i))
  return list02

data = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']

print(extsort(data))