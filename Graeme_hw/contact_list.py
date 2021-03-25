
contacts = {
		"Henry Hunt": {
			"name": "Henry Hunt",
			"phone number": 2076508465,
			"address": "32 Osprey Lane, Yarmouth ME, 04096",
			"email": "henry.stewart.hunt@gmail.com",

		}
}

def create_contact(contacts, contact, name, phone, address="", email=""):
 """creates a new contact"""
 contacts[contact] = {
 "name":name.title(), 
 "phone":phone,
 "address":address, 
 "email":email
 }

def read_contact(contacts, contact, key=""):
    #give contact's information
    contact_info = []
    if key=="all":
        for info in contacts[contact].values():
            contact_info.append(info)
        print(contact_info)
    else:
        print(contacts[contact][key])

def delete_contact(contacts, contact):
	"""deletes the contact"""
	del contacts[contact]

def update_contact(contacts, contact, name, phone, address="", email=""):
	"""updates the information of the selected contact"""
	del contacts[contact]
	contacts[name] = {}
	contacts[name]["name"] = name
	contacts[name]["phone "] = phone
	contacts[name]["address"] = address
	contacts[name]["email"] = email

#create_contact(contacts, "hhh", "hhh", 213214214, "dfgfdgdfg", "324324324")

#read_contact(contacts, "Henry Hunt")

#delete_contact(contacts, "hhh")

#print(contacts)

read_contact(contacts, "Henry Hunt", "all")


#create_contact(contacts, "hhh", "hhh", 213214214, "dfgfdgdfg", "324324324")

#update_contact(contacts, "hhh", "Graeme F", 2079919919, "1059 Bergan Sreet", "GGFERG@gmail.com")

#print(contacts)

 

