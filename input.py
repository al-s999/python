# Membaca input
p, k = map(int, input().split())
x = input()

# Mengganti semua kemunculan 'x' dalam string dengan nilai p
# Menggunakan eval untuk menghitung nilai dari ekspresi
result = eval(x.replace('x', str(p)))

# Membandingkan hasil dengan k
if result == k:
    print(True)
else:
    print(False)