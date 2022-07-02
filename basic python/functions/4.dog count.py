# Creating a function to count how many times dog word came in the sentence

def countDog(d_name):
  count = 0 #declared a count variable and it set to null.
  for d_word in d_name.lower().split():
    if d_word == 'dog' or d_word == 'dogs':
      # count = count + 1 # OR
      count += 1
  return count

sent = str(input('\n Enter a sentence: '))

n_count = countDog(sent)

print(f'\n {sent}\n-> In this sentence no of count for the dog is: {n_count} \n')