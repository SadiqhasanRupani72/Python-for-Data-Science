def my_func(st):
  result = []
  # Iterate over the character
  for index in range(len(st)):
    if index % 2 == 0:
      # Refer to each character via index and append modified character to list
      result.append(st[index].upper())
    else:
      result.append(st[index].lower())

  # Join the list into a string and return
  return ''.join(result)


result = my_func('Sadiqhasan Rupani')

print(f'\n The result is given below\n -> {result}')