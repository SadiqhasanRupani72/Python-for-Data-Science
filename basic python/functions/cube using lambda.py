# Program to accept list from user and make a cube lambda and implement on the accepted list.

lst = []
n = int(input('\n Enter a number: '))
print("\n")
for i in range (0,n):
  ele = int(input(f' Enter number {i + 1}: '))
  lst.append(ele)

cube_map = tuple(map(lambda c: c ** 3, lst))

print(f"\n The Cube of this list {lst} is\n-> {cube_map}. \n")