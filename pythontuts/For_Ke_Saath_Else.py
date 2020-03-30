khana = ["Roti","Sabzi","Chaval"]

yr_item=input("Enter Your Item:")

for item in khana:
    if item==yr_item:
        print("Your item is Found")
        break
else:
    print("Your item is not found")

