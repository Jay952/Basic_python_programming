#Dictionary
d1={"Jaydeep":"Burger","Rohan":"Pizza","Shubham":{"Break":"Bread","Lunch":"Paneer"}}
print(d1)
print(d1["Shubham"]["Break"])
d1["Aditya"]="Junk food"
d1["Mohan"]="Palak"
del d1["Rohan"]
print(d1)

d1.update({"Ankita":"Salad"})
print(d1)

print(d1.keys())
print(d1.items())
print('Now')
print(d1['Shubham'])
