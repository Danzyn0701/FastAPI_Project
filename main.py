from fastapi import FastAPI

app = FastAPI(
    title= "DiaryAPP",
    description = "website app tentang diary yang bisa kamu tambahkan"
)

@app.get("/")
def read_root():
    return {"halo dunia"}

@app.get("/penjumlahan")
def penjumlahan(a:int=0,b:int=1):
    return a+b

@app.get("/perkalian")
def perkalian(a:int=0,b:int=0):
    if a==0:
        notifa="a harus diisi"
        return notifa
    elif b==0:
        notifb="b harus diisi"
        return notifb
    else:
        return a+b

@app.get("kalkulator")

def tambah(a,b):
    return a + b

def kurang (a,b):
    return a - b

def kali(a,b):
    return a * b

def bagi(a,b):
    return a / b




    

    













