import requests
import time
url = "https://127.0.0.1"
cant=int(input("How many requests?: "))
cont=0
cooldown=int(input("Cooldown (seconds): "))
while(cont<=cant):
    time.sleep(cooldown)
    r=requests.get(url)
    status = r.status_code
    cont+=1
    print("Request Nº",cont)