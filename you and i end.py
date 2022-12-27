while True :
	i = int(input("angka : "))
	
	if  i %2 == 0 :
		for j in range (2,i+2,2):
			print(j)
	elif i %2 != 0 :
		print ("you and i, end")
		break
