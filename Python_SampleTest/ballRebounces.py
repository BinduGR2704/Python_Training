H = int(input("Initial height:"))
V = int(input("Initial velocity:"))
Vn = int(input("Final velocity:"))

en = V / Vn

H1 = H * (en ** 2)

print(H1)