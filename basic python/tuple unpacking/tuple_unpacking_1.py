
# making a empty list.
lst = []
n = int(input('\n Enter how many element do you want to in a list: '))
print("\n")
for i in range(0,n):
  tup_ele = (int(input(f'Enter tuple number {i + 1}: ')), int(input(f'Enter next tuple number {i + 1}: ')))
  lst.append(tup_ele)

print(f"\n Your list is given below. \n -> {lst}.")

# Tuple unpacking 👇🏻
print("\n Displaying tuple left part from the list. ")
print(f" The outcomes are provided below.")
for(a,b) in lst:
  print(f' {a}')

print("\n Displaying tuple right part from the list. ")
print(f" The outcomes are provided below.")
for(a,b) in lst:
  print(f' {b}')
  
print('\n')