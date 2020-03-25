import time
initial=time.time()
print(initial)
localtime=time.asctime(time.localtime(time.time()))
print(localtime)
for i in range(45):
    print("I am lala")
    time.sleep(2)
initial2=time.time()
print(initial2-initial)
k=0
while(k<45):
    print("I am jaydeep")
    time.sleep(3)
    k=k+1

initial3=time.time()
print(initial3-initial2)