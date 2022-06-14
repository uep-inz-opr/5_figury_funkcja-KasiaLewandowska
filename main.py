import math

liczbaFigur =int(input())

figury=[]

for i in range(liczbaFigur):
  figura=input().split()
  figury.append([float(x) for x in figura])
[x for x in figura if x==0]

def poleKola(lista):
  return lista[0]**2*math.pi

def poleProstokata(lista):
  return lista[0]*lista[1]

def poleTrojkata(lista):
  p=(lista[0]+lista[1]+lista[2])/2
  return math.sqrt(p*(p-lista[0])*(p-lista[1])*(p-lista[2]))

def zaokr(suma, decimals):
  multiplier = 10**decimals
  return math.ceil(suma*multiplier)/multiplier

suma=0
for lista in figury:
  if len(lista)==1:
    wynik=(poleKola(lista))  
  elif len(lista)==2:
    wynik=(poleProstokata(lista))
  elif len(lista)==3:
    wynik=(poleTrojkata(lista))

  suma=suma+wynik
print(zaokr(suma,2)) 
for lista in figury:  
  if len(lista)>3:
    print("Błąd: można podać maksymalnie trzy liczby")