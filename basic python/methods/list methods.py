
# creating a empty list.
lst = []
n = int(input('\n Enter how many element you wanna put into the list: '))
print('\n')
for i in range(0,n):
  ele = int(input(f' Enter number {i+1}: '))
  lst.append(ele) # appends is also a method!

print(f"\n Your List is given below. \n -> {lst} ")

pop_ele= int(input('\n Which element you wanna delete form the list (in index format)? \n -> '))

# pop method: It allows you to delete an element from the list, if you type on pop then it will pop the last element
# by default but if you want to delete first or in the middle then you can just write the index of that element inside
# the parenthesis
pop = lst.pop(pop_ele)

print(f"\n Popped element is: '{pop}', and you list have now\n -> {lst} elements. \n")

insert_ele = int(input("\n What element do you wanna insert in your list? -> "))

# where = int(input(' Where do you wanna insert you element in your list, (index formate): '))

# result = lst.append(insert_ele)[where]

result = lst.append(insert_ele)

print(f"\n Inserted element is: {insert_ele}.")
print(f" Your list have now {lst} elements. \n")