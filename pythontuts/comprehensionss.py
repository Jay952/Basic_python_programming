# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)


# ls=[2*i for i in range(100) if i%11==0 ]
# print(ls)


# dict1={
#     i:f"Student{i}" for i in range(50) if i%5==0
#
# }
# dict1={value:key for key,value in dict1.items()}
#
# print(dict1)


# dresses={dress for dress in ["dress1","dress2","dress3","dress1","dress2","dress3","dress1","dress2","dress3"]}
#
# print(type(dresses))

# evens=(i for i in range(100) if i%3==0)
# # print(evens)
# # print(evens.__next__())
# # print(evens.__next__())
# # print(evens.__next__())
# # print(evens.__next__())
# # print(evens.__next__())
# #
# #
# # for item in evens:
# #     print(item)


n=int(input("Enter the number of items you want to enter in list:"))



print("Which type Comprehension you want:1 for List,2 for set.3 for dictionary")
k=int(input())
if k==1:
    print("Enter the items:")
    lst = [input() for i in range(n)]
    print(f"Your list is:{lst}")
elif k==3:
    print("Enter the items:")
    dict={i:input() for i in range(n)}
    print(f"Your dictionary is:{dict}")
elif k==2:
    print("Enter the items:")
    set={item for item in [input() for i in range(n)]}
    print(f"Your set is:{set}")















