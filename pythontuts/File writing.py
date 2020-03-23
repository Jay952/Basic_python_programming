f=open("jaydeep")

print(f.readlines())
#print(f.readline())
#print(f.readline())
#for line in f:
  #  print(line)

content=f.read()
print("1",content)
content=f.read(4566)
print("2",content)

f.close()