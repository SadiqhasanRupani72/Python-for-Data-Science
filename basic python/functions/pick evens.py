# def myfunc(x):
#   if (x % 2 == 0):
#     return x
#   else:
#     return 0;
#
# mylist = (5, 6, 7, 8)
#
# result = list(filter(myfunc,mylist))
#
# print(result)

def myfunc(*args):
  lst = []
  for n in args:
    if n % 2 == 0:
      lst.append(n)
  return lst


result = myfunc(5, 4, 5, 6, 3, 2)
print(result)
