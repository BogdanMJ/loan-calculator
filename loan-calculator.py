cena = float(input("Cena Towaru: "))


if cena <100:
    print("Minimalna wysokość kredytu 100 PLN")
    cena = float(input("Cena Towaru: "))
elif cena >=10000:
    print("Maksymalna wysokość kredytu 10 000 PLN")
    cena = float(input("Cena Towaru: "))

raty = int(input("Liczba Rat: "))

if raty <6:
    print("Minimalny okres kredytowania wynosi 6 rat")
    raty = int(input("Liczba Rat: "))
if raty >48:
   print("Maksymalny okres kredytowania wynosi 48 rat")
   raty = int(input("Liczba Rat: ")) 
if raty in range(6,12):
    opr = 0.025
if raty in range(13,24):
    opr = 0.05
if raty in range(25,48+1):
    opr = 0.1
odsetki=(cena/raty)*opr
rata_miesięczna = odsetki + (cena/raty)

print(f"Dla towaru o wartości {cena} PLN i okresie kredytowania {raty} mieisięcy, miesięczna rata wyniesie {rata_miesięczna:.2f} PLN. Oprocentowanie wyniesie {opr*100}%.")