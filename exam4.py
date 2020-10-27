def guest_list(guests):
	for elem in guests:
		#print(elem)
		print("{} is {} years old and works as {}".format(elem[0],elem[1],elem[2]))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
