#Library,display,lend,add,return Book
class Library:
    type1 = ["Geeta", "Ramayan", "Mahabharata", "Bible", "Quran"]
    type2 = ["Spiderman", "Batman", "Superman", "Shaktiman", "Perman"]

    def __init__(self):
        pass


    def Display(self,type):
        return self.type




while(True):
    print("Enter the number for your purpose: 1 for Display,2 for Lend,3 for Add,4 for Return\n ")
    k = int(input())
    if k == 1:
        print("Enter the Type you Want: A for Type1(Dharmik book), B for Type2(Super Heroes)")
        l = input()
        if l == "A":
            print(Library.type1)
        elif l == "B":
            print(Library.type2)
    elif k == 3:
        print("Enter the Type you Want: A for Type1(Dharmik book), B for Type2(Super Heroes)")
        l = input()
        if l == "A":
            print(Library.type1)
            Library.type1 = Library.type1.insert(1,"Shiva")
            print(Library.type1)

        elif l == "B":
            pass



