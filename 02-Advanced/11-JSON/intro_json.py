# analogy

# python                # json
# dict                  # object
# list, tuple           # array
# str                   # string
# int, float, complex   # number
# True                  # true
# False                 # false
# None                  # null

import json

json_data = None

with open("/Users/prabhatmishra/personal-workspace/python-complete-guide/02-Advanced/11-JSON/example.json", "r") as f:
    data = f.read()
    json_data = json.loads(data)

# remember
# 1. json.loads()  # string -> python object(dict)
# 2. json.dumps()  # python object(dict) -> string

print(json_data, type(json_data))  # <class 'dict'>
person = json.dumps(json_data)
print(person, type(person))  # <class 'str'> 

print(json.dumps(json_data, indent=4))  # pretty print with indentation


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Alice", 30)
user_json = json.dumps(user.__dict__)
print(user_json) 



from json import JSONEncoder

class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city

class AddressEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Address):
            return {"street": obj.street, "city": obj.city}
        return super().default(obj)

address = Address("123 Main St", "New York")
print(json.dumps(address, cls=AddressEncoder))

addressJSON = AddressEncoder().encode(address)
print(addressJSON)

# simple decode 
address_dict = json.loads(addressJSON)
print(address_dict, type(address_dict))  # {'street': '123 Main St', 'city': 'New York'} <class 'dict'>