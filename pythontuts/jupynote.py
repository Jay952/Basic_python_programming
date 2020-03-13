X=[1,2,3,4,5]
Y=[1,5,7,8,9]
theta0=0
theta1=1


i=0
while i<1000:
    dJ0= []
    dJ1= []
    for (x, y) in zip(X, Y):
        dJ0.append((theta0+theta1*x+y)/11)
        dJ1.append((theta0+theta1*x-y)*x)
        k=sum(dJ0)
        theta0=theta0-.01*k
    i=i+1


print(theta0)

