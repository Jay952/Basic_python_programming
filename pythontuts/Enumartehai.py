L1=["Bhindi","Aloo","Gobi","Chinese","Maithi","Loki"]

# i=1
# for item in L1:
#     if i%2!=0:
#         print(f"please buy  {item}")
#     i=i+1


for index,item in enumerate(L1):
    if index%2==0:
        print(f"please buy {item}")



