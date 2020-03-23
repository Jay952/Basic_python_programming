# a=int(input("Enter number rows you want in * pattern"))
# i=0
# j=0
# b=int(input("1-for ascending order and 2-for descending order"))
# if b==1:
#     while i<a:
#         while j<=i:
#             print(j)
#             j=j+1
#         j=0
#         print("\n")
#         i=i+1
# elif b==2:
#     for i in range(a):
#         for j in range(i):
#             print("*")
#         print("\n")

n=int(input("Enter number of rows you want to print"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()