def sqr(x):
	return x **2

sqrlist = []

n = int(input('\nEnter how many integer items you wanna add in you list: '))

for i in range(0, n):
	ele = int(input(f'Enter the integer item no {i+1}: '))
	sqrlist.append(ele)

sqr_map_list= list(map(sqr,sqrlist));

print(f'\nThe square of the list {sqrlist} is \n-> {sqr_map_list} \n')
