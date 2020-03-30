import json
# data={"var1":"harry","var2":56}
# parsed=json.load(data)
# print(parsed)

# with open('person.json.py') as f:
#   data = json.load(f)
#   print(data)

# person_dict = {"name": "Bob",
# "languages": ["English", "Fench"],
# "married": True,
# "age": 32
# }
#
# with open('person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file)

data2={"channel_name":"codeWithHaryy","cars":['bmw','audi','ferari'],"fridge":('roti',540) }
jscomb=json.dumps(data2)
print(jscomb)