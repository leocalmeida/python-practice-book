lines = open('cat-she.txt').readlines()
lines.reverse()

new_lines = []
for i in lines:
  new_lines.append(i.strip('\n'))

for i in new_lines:
  print(i)