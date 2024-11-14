import sys
sys.stdout.reconfigure(encoding='utf-8')

zakupy = {"putka" : ["chleb", "pączek", "bułki"],
          "warzywniak" : ["marchew", "seler", "rukola"],}

print("Lista zakupów: ")
print()
for k, v in zakupy.items():
    print(f"{k.capitalize()} to sklep gdzie znajdę nastepujące produkty: {', '.join(v.capitalize() for v in v)}")
print()
x = sum(map(len, zakupy.values()))
print(f"Lista zakupów zawiera {x} produktów.")
