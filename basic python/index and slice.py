word = input('\n Enter a sentence: ')

print(f'\n Your sentence: {word}')

index = int(input(' \n Enter the index number that you want to use to extract from the preceding sentence: '))

ind = word[index]

print(f' The result: {ind}')

sl = int(input(' \n Enter the index number you wish to slice from: '))

slice = word[sl:]

print(f' The index number that you want to slice is as follows: {slice}')

start = int(input(f"\n Where to start? \n -> "))

end = int(input(f' Where to end? \n -> '))

slice = word[start:end]

print(f" The result is: {slice}")
