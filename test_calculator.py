import pytest
import calculator


def test_tambah():
    assert calculator.tambah (1, 1) == 2
    assert calculator.tambah (-1, 1) == 0
    assert calculator.tambah (0, 0) == 0
    assert calculator.tambah (2.5, "asdada") == "Error: Masukkan angka yang valid!"
    assert calculator.tambah (2.5, 3.5) == 6.0

def test_kurang():
    assert calculator.kurang (5, 5) == 0
    assert calculator.kurang (0.5, "yausgdyuagsdu") == "Error: Masukkan angka yang valid!"

def test_kali():
    assert calculator.kali (1, 1) == 1
    assert calculator.kali (6, "hasdhy") == "Error: Masukkan angka yang valid!"

def test_bagi():
    assert calculator.bagi (1, 1) == 1
    assert calculator. bagi (9, "hsdahsdfh") == "Error: Masukkan angka yang valid!"
    assert calculator.bagi (1, 0) == "Error: Tidak bisa dibagi dengan 0"


a = int(input("Masukkan angka pertama: "))

b = int(input("Masukkan angka ke 2"))
 


    















