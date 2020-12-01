import json
ct=1
while ct:

	def create():
		data={}
		x=input("Enter the Path of the JSON File,if not specified, data.json under the current dir will be considered\n")
		if x=="":
			x="data.json"
		with open(x, 'w') as fp:
			json.dump(data, fp)
		n=input("no of input:")  #no.of data entry
		print("Enter the data in the following format\nKey<space>Value\n")
		for j in range(int(n)):
			k=input()
			y=k.split(' ')
			if len(y[0])<32:
				if y[0] in data.keys():
					print("\nKey already exists,try a new key")
					continue
				data[y[0]] = y[1:]
		
		print("\nThe data you entered is\n")
		print(data)
		with open(x, 'w') as fp:
			json.dump(data, fp)

	def rd():
		x=input("Enter the Path of the JSON File,if not specified, data.json under the current dir will be considered\n")
		if x=="":
			x="data.json"
		f=open(x,"r")       #opening a json file in read mode 
		data=json.load(f)   #parsing a json file
		f.close()
		y=input("\nEnter the Key to be read: ")
		print(data[y])

	def delete():
		x=input("Enter the Path of the JSON File,if not specified, data.json under the current dir will be considered\n")
		if x=="":
			x="data.json"
		f=open(x,"r")       #opening a json file in read mode 
		data=json.load(f)
		print(data)
		y=input("Enter the Key of the element to be deleted")
		del data[y]
		print(data)
		f.close()

	i=input("Enter the operation to be performed :\n1.Create\n2.Read\n3.Delete\n4.exit\n")
	if i=="1":
		create()
	elif i=="2":
		rd()
	elif i=="3":
		delete()
	elif i=="4":
		break

