def unique(x):
  new_set=set()
  
  for i in x:
    new_set.add(i)
  return new_set
x = {1, 2, 1, 3, 2, 5}

print(x)

print(unique(x))

# O SET é composto apenas por elementos unicos, logo, quando incluido elementos repetidos ele 
# ignora os elementos duplicados.