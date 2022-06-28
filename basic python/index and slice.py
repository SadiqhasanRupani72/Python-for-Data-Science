word = input('\n Enter a sentence: ')

index = int(input(' Put an index number to indicate where you want to start: '))

slice = word[index:]

print(f'\n The result: {slice}')