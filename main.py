import socket
import time

adres=input("Podaj adres IPv4 ktory chcesz sprwadzic: ")
print("Wybierz zakres portow do przeskanowania")
pierwszy=int(input("Podaj pierwszy port: "))
ostatni=int(input("Podaj ostatni port: "))
start=time.time()
for nr in range(pierwszy,ostatni+1):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        try:
            s.connect((adres,nr))
            print(f"Port {nr} jest OTWARTY!")
        except:
            print(f"Port {nr} jest ZAMKNIETY!")
koniec=time.time()
czas=round(koniec-start,2)
print(f"Skanowanie wszystkich portow trwalo {czas}s")