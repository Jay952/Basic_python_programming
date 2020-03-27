class Dad:
    basketball=1

class Son(Dad):
    dance=1
    def isdance(self):
        return f"yes I dance {self.dance} number times"


class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"yes I dance Very Awesome {self.dance} number times"


darry=Dad()
larry=Son()
harry=Grandson()
print(harry.isdance())
print(harry.basketball)

