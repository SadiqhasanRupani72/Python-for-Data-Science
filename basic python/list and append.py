# This program can generate a file by user and the user also can append the list!

lst = []  # First creating a empty list.

print('\n ###### Normal List Generator #####')
n = int(input('\n Enter number of elements: '))  # taking a user-provided element count.

print('\n')
for i in range(0, n):  # until the desired range is reached
  element = str(input(f' Enter element no {i + 1}: '))
  lst.append(element)

print(f'\nThe normal element lists are: {lst} \n')

print('\n ##### Nested List Generator #####')
lst2 = []

n = int(input('\n Enter number of elements: '))
print('\n')

j = 0
for i in range(0, n):
   element = [int(input(f' Enter integer element no {i + 1}: ')), str(input(f' Enter element no {i + 1}: '))]
   lst2.append(element)

print(f'\n The nested elements are: {lst2} \n')
