#lambda function or Anonymous Function
def add(a,b):
    return print(a+b)
add(5,9)

addition=lambda x,y:x+y
print(addition(5,8))

# def a_first(a):
#     return a[0]
a_first=lambda a:a[0]

a=[[1,25],[5,9],[0,1]]
a.sort(key=a_first)
print(a)