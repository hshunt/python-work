

contacts = {
		"Henry Hunt": {
			"name": "Henry Hunt",
			"phone number": 2076508465,
			"address": "32 Osprey Lane, Yarmouth ME, 04096",
			"email": "henry.stewart.hunt@gmail.com",

		}
}




#read_contact(contacts, "Henry Hunt", "phone number")

def read_contact(contacts, contact, key=""):
    #give contact's information
    contact_info = []
    if key=="all":
        for info in contacts[contact].values():
            contact_info.append(info)
        print(contact_info)
    else:
        print(contacts[contact][key])

read_contact(contacts, "Henry Hunt", "all")
