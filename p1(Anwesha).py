# Anwesha project.
# Country currencies.
print("1 = usd")
print("2 = Dinar")
print("3 = Dhiram")

usd = 90.79
Dinar = 296.20
Dhiram = 24.71

choose = int(input("1,2,3:- "))
Amount = int(input("Entre amount:- "))
if choose == 1:
    print(Amount * usd)
elif choose == 2:
    print(Amount * Dinar)
elif choose == 3:
    print(Amount * Dhiram)