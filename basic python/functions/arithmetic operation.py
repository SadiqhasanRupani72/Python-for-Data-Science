def addition(x, y):
  c = x + y
  print(f"\n The addition of {x} and {y} is: {c}")


def multiplication(x, y):
  m = x * y
  print(f'\n The multiplication of {x} and {y} is: {m}')


def substraction(x, y):
  s = x - y
  print(f'\n The substraction of {x} and {y} is: {s}')


def division(x, y):
  d = x / y
  print(f'\n The divsion of {x} and {y} is: {d} \n'.format(d=d))


print('\n ##### Arithmetic Operation #####')

num1 = int(input('\n Enter value 1: '))
num2 = int(input(' Enter value 2: '))

addition(num1, num2)
substraction(num1, num2)
multiplication(num1, num2)
division(num1, num2)
