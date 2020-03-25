# def function_print_name(a,b,c,d):
#     print(a,b,c,d)
#
# function_print_name("Jay","Vijay","sujait","Alpha")
def funtionarg(normal,*args,**kwargs):
    print(normal)
    print(args[0:5])
    for key,value in kwargs.items():
        print(key,value)


normal="I am the normal:"
har=["Ajay","Vijay","Jay","pratap"]
kw={"Rohan":"Monitor","Harry":"Fitness instructor","The great khali":"Coder"}
funtionarg(normal,*har,**kw)