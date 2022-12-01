#DICTIONARIES
customer = { #you can declare "Variable: data"
    "name":"keanu",
    "age": 30,
    "boole":True
    #declare UNIQUE
}

print(customer["name"])
#prnt(customer["birthdate"]) //error because this doesnt exist
print(customer.get("birthdate")) #//it wont return error but it will return "none"

customer["name"]= "KEANU" #change "name:" to KEANU
customer["birthdate"] = "june 1 1980" #add variable birthdate


phone =input("Phone number: ")

number = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
1
output = ""
for ch in phone:
    output += number.get(ch,"!") + " "

print(output)