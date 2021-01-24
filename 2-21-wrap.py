def wrap(file, width):
  editable_file = open(file).readlines()

  lines01 = []
  for i in editable_file:
    lines01.append(i.strip('\n'))
  
  for i in lines01:
    print(i.split(30))
  
  return None

wrap('cat-she.txt', 30)