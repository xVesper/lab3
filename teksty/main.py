#za pomoca petli
# lista = []
# for element in zakres:
#     if warunek_na_element:
#         lista.append("cos sie dzieje z elementem " element)
#
# lista2 =["cos sie dzieje z "element for in zakres if pewien_warunek_na_element]
#
# lista_a= []
# for x in range(10):
#     lista_a.append(x**2)
#
# print(lista_a)
#
# a= [x**2 for x in range(10)]
# print(a)
#
# lista_b = []
# for y in range(6):
#     lista_b.append(3**y)
#
# print(lista_b)
#
# b = [3**y for y in range(6)]
# print(b)
#
# lista_c = []
# for z in lista_a:
#     if z% 2 == 1:
#         lista_c.append(z)
#
# print(lista_c)
#
# c = [z for z in a if z % 2 == 1]
# print(c)
#
# lista = [1,2,3,4,5,6,7,8,9,10]
# liczba_parzysta = []
# for x in lista:
#     if x % 2 == 0:
#         liczba_parzysta.append(x)
#
# print(liczba_parzysta)
#
# d = [liczba for liczba in lista if liczba % 2 == 0]
# print(d)
#
# lista = []
# for a in [1,2,3]:
#     for b in [4,5,6]:
#         lista.append((a,b))
#
# print(lista)
#
# c = [(i,j) for i in [1,2,3] for j in [4,5,6]]
# print(c)
#
# skroty = {"PZU": "Panstwowy zaklad ubezpieczen","ZUS": "Zaklad ubezpieczen spolecznych","PKO": "Panstwowa kasa oszczednosciowa"}
#
# odwrocone_skroty = {}
# print(skroty)
#
# for key,value in skroty.items():
#     odwrocone_skroty[value] = key
#
# print(odwrocone_skroty)
#
# odwrocone = {value: key for key, value in skroty.items()}
#
# print(odwrocone)

# def nazwa(arg_pozycyjne, arg_domyslna = wartosc, *arg, **arg):
#     instrukcje
#     return
#
# nazwa()
# def rownanie_kwadratowe(a, b, c):
#     delty = b**2 - 4 * a * c
#     if delty < 0:
#         print("brak pierwiastkow")
#         return -1
#     elif delty == 0:
#         print("jeden pierwiastek")
#         x = (-b)/(2*a)
#         return x
#     else:
#         print("dwa pierwiastki")
#         x1 = (-b - sqrt(delty))/(2*a)
#         x2 = (-b + sqrt(delty))/(2*a)
#         return x1,x2
#
# print(rownanie_kwadratowe(6,1,3))
# print(rownanie_kwadratowe(1,2,1))
# print(rownanie_kwadratowe(1,4,1))

# def dlugosc_odcinka(x1=0, y1=0, x2=0, y2=0):
#     return sqrt((x2-x1)**2 + (y2-y1)**2)
#
# #dla argumentow domyslnych
# print(dlugosc_odcinka())
# #dla naszych wartoscim, argumenty pozycyjne
# print(dlugosc_odcinka(1,2,3,4))
# #dla mieszanych wartosci, dwie pierwsze wartosci w polejnosci, dwie we wlasnej kolejnosci
# print(dlugosc_odcinka(2,2,y2=2,x2=1))
# #wartosci nie w kolejnosci
# print(dlugosc_odcinka(x2=5,x1=2,y2=6,y1=2))
# #dwa argument domyslne, dwa argumenty podane
# print(dlugosc_odcinka(x2=5,y2=5))

# def ciag(* liczba):
#     if len(liczba) == 0:
#         return 0
#     else:
#         suma = 0
#         for i in liczba:
#             suma += i
#         return suma
#
# print(ciag())
# print(ciag(1,2,3,4,5,6,7))

# def to_lubie(** rzeczy):
#     for cos in rzeczy:
#         print("to jest")
#         print(cos)
#         print("co lubie")
#         print(rzeczy[cos])
#
# to_lubie(slodycze = "czekolada", rozrywka = ["gry","filmy"])

from teksty import litery

a = "Ala ma kota"

litery.wyswietl(a)
print(litery.dlugosc(a))
