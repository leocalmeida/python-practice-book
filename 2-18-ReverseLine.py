lines = open('cat-she.txt').readlines()

lines01 = []
for i in lines:
  lines01.append(i.strip('\n'))
lines02 =[]


for i in lines01:
  aux=''
  for j in range(len(i)-1,-1,-1):
    aux += i[j]
  lines02.append(aux.lower())
  

print(lines02)



