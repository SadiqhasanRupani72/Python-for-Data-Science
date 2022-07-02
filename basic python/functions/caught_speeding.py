# *You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible
# results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If
# speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big
# Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your
# birthday, your speed can be 5 higher in all cases. *

def caught_speed(speed, is_birthday):
  if is_birthday:
    speeding = speed - 5
  else:
    speeding = speed

  if speeding >= 80:
    print('\n BIG Ticket. \n')
  elif speeding >= 60:
    print('\n SMALL Ticket. \n')
  else:
    print('\n NO Ticket. \n')

speed = int(input('\n What is your speed: '))

is_birthday = str(input('\n Is today is your birthday? (Yes OR No)\n -> '))

birthday = is_birthday.lower

if birthday == 'yes':
  birthday = True
elif birthday == 'no':
  birthday = False

caught_speed(speed, birthday)