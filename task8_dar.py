#square each odd number in the list

list = input("Enter the numbers seperated by a comma: ")

#print(list)

i_list= [int(i) for i in list.split(',')]
	
#print(i_list)

odd_squared_list= [(num*num) for num in i_list if num%2 !=0]
print(odd_squared_list)

