lst = []
ele = int(input('\n Enter how many element do you want in a list (integer): '))

for i in range(0, ele):
  element = int(input(f'\n Enter element no {i + 1}: '))
  lst.append(element)

out = []

for num in lst:
  out.append(num ** 2)

print(f' \n Square of the list {lst} is: {out} \n')
