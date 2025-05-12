l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

# Membalikkan kedua list untuk memudahkan penjumlahan dari digit terkecil
l1.reverse()
l2.reverse()

result = []
carry = 0

# Menggunakan panjang maksimum dari kedua list
max_length = max(len(l1), len(l2))

for i in range(max_length):
    # Ambil digit dari l1 dan l2, jika tidak ada gunakan 0
    digit1 = l1[i] if i < len(l1) else 0
    digit2 = l2[i] if i < len(l2) else 0
    
    # Hitung jumlah dan carry
    total = digit1 + digit2 + carry
    carry = total // 10  # Dapatkan carry
    result.append(total % 10)  # Ambil digit terakhir

# Jika masih ada carry setelah loop
if carry:
    result.append(carry)

print(result)  # Output: [7, 0, 8]