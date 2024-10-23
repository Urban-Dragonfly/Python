import sys
sys.stdout.reconfigure(encoding='utf-8')

podzielne = []
for x in range (1, 101):
    if x % 5 == 0:
        podzielne.append(x)

print()
print ("Liczby podzielne przez 5 to:")
print(", ".join(map(str, podzielne)))
print()
print("A ich trzecie potęgi to:")
print(", ".join(map(str, [x**3 for x in podzielne])))