def grep(file, word):
  file = open(file).readlines()
  lines01 = []
  result = []
  
  for i in file:
    lines01.append(i.strip('\n'))
  
  for i in lines01:
    if word in i:
      result.append(i)
  
  for i in result:
    print (i)
  return result
  

grep('cat-she.txt','sure')