
contacts = {
		"Henry Hunt": {
			"name": "Henry Hunt",
			"phone number": 2076508465,
			"address": "32 Osprey Lane, Yarmouth ME, 04096",
			"email": "henry.stewart.hunt@gmail.com",

		}
}



def create_contact(contacts, contact, name, phone, address, email):
 """creates a new contact"""
 contacts[contact] = {
 "name":name, 
 "phone":phone,
 "address":address, 
 "email":email}


create_contact(contacts, "hhh", "hhh", 213214214, "dfgfdgdfg", "324324324")

print(contacts)

def read_contact(contacts, contact):
	"""give the contact's information"""
	contact_info = []

	for info in contacts[contact].values():
		contact_info.append(info)

	print(contact_info)

read_contact(contacts, "Henry Hunt")

def delete_contact(contacts, contact):
	"""deletes the contact"""
	del contacts[contact]

delete_contact(contacts, "hhh")

print(contacts)



def update_contact(contacts, contact, name, phone, address, email):
	"""updates the information of the selected contact"""
	del contacts[contact]
	contacts[name] = {}
	contacts[name]["name"] = name
	contacts[name]["phone "] = phone
	contacts[name]["address"] = address
	contacts[name]["email"] = email

create_contact(contacts, "hhh", "hhh", 213214214, "dfgfdgdfg", "324324324")

update_contact(contacts, "hhh", "Graeme F", 2079919919, "1059 Bergan Sreet", "GGFERG@gmail.com")

print(contacts)

'''x = {
	"1": {
		"2": "value11",
		"3": "value21",
		"4": 31
	},
	"2": {
		"2": "value12",
		"3": "value22",
		"4": 32
	},
	"3": [0,"a",2,"c",4,"d"]
}



print(x["3"][4])'''


