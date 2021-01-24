def headsTails(file):
  firt_lines = open(file).readlines()

  lines01 = []
  for i in firt_lines:
    lines01.append(i.strip('\n'))
  
  lines02 = lines01.copy()
  lines02.reverse()
    
  for i in range(len(lines01)):
    if i <= 9:
      print (lines01[i])
  
  for i in range(len(lines02)):
     if i <= 9:
      print (lines02[i])
  return None

headsTails('natureza-homem-bom.txt')