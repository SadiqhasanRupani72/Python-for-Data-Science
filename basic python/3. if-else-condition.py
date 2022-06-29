# Dictionaries
dic = {35: ['Sadiqhasan Rupani', 'Su Mangal Vastu near jawahar society', 'age', 19],
       33: ['Soham Ganmote', 'xyz colony plot no.78', 'age', 19],
       37: ['Yasin Bhojani', 'Hussaini Plaza near khoja colony', 'age', 20],
       38: ['Zakir Kalwani','Khoja colony plot no.8', 'age', 20]}

print('\n Roll numbers in my database: 33, 35, 37, 38' )

data = int(input('\n What roll number data are you interested in?\n -> '))


if(data == 33 or data == 35 or data == 37 or data == 38):
  req_data = dic[data]
  print(f'\n What you were looking for is available here: \n -> {req_data} \n')
else:
  print(f'\n The Given number is not in our database, \n Sorry.... plz try again :) \n')