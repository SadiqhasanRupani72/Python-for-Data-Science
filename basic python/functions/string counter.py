# creating a function.
def count_string(str_name, word):
  count = 0
  for str_word in str_name.lower().split():
    if str_word == word:
      count += 1
  return count

print("\n ########## Dynamic String Counter ########## \n")

sent = str(input(" Type a sentence here: "))

word = str(input(f'\n {sent}\n -> which word you wanna count from the above sentence: '))

n_count = count_string(sent, word)

print(f"\n The following counts for the word '{word}' have: '{n_count} counts'. \n")

print("\n ########## Dynamic String Counter ########## \n")

input(' \n \n Input a enter key for exit.......')