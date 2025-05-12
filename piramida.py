tinggi, lebar = map(int,(input().split()))

for i in range(tinggi):
    for j in range(tinggi-i-1):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()


def piram(tinggi,lebar) :
    for a in range(tinggi):
        spasi = (lebar // 2) - a
        bintang = 2 * a - 1
        
        if bintang > lebar:
            bintang = lebar
            spasi = 0
            
        print(" " * spasi, end="")
        print("*" * bintang)
        
piram(tinggi,lebar)