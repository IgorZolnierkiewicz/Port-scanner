import socket


for nr in range(20,30):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        try:
            s.connect(("127.0.0.1",nr))
            print(f"Port {nr} jest OTWARTY!")
        except:
            print(f"Port {nr} jest ZAMKNIETY!")