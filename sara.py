# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# user=str(input("unesite zeljeno voce:"))
# y.append(user)
# thistuple = tuple(y)
# print(thistuple)

thistuple=(5,4,3,24,5,43)
y=list(thistuple)
korisnik=int(input("unesite neki broj"))
if korisnik > 0:
    y.append(korisnik)
    thistuple=tuple(y)
    print(thistuple)
else:
    print("greska!")
