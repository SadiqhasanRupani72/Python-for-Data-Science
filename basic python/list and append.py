# This program can generate a file by user and the user also can append the list!

lst = []  # First creating a empty list.

n = int(input('\n Enter number of elements: '))  # taking a user-provided element count.

print('\n')
for i in range(0, n):  # until the desired range is reached
  element = input(f' Enter element no {i + 1}: ')
  lst.append(element)

print(f'\nThe element lists are: {lst} \n')
