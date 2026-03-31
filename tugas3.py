# ==============================
# Deklarasi Variabel & Tipe Data
# ==============================
nama = "Sweety"          # string
umur = 21                 # integer
tinggi = 160           # float
is_mahasiswa = True       # boolean
hobi = ["Traveling", "Hiking", "Music"]  # list

# ==============================
# Manipulasi String
# ==============================
print("=== Manipulasi String ===")
kalimat = "Halo, saya " + nama
print(kalimat)

print("Panjang string:", len(kalimat))
print("Huruf besar:", kalimat.upper())
print("Huruf kecil:", kalimat.lower())

# ==============================
# Operasi Matematika Sederhana
# ==============================
print("\n=== Operasi Matematika ===")
a = 10
b = 3

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Modulus:", a % b)

# ==============================
# List dan Akses Elemen
# ==============================
print("\n=== List ===")
print("List awal:", hobi)

print("Elemen pertama:", hobi[0])
print("Elemen terakhir:", hobi[-1])

# Tambah item
hobi.append("Sing")
print("Setelah ditambah:", hobi)

# Hapus item
hobi.remove("Music")
print("Setelah dihapus:", hobi)

# ==============================
# Input dari User
# ==============================
print("\n=== Input User ===")
nama_user = input("Masukkan nama kamu: ")
umur_user = input("Masukkan umur kamu: ")

print("Halo, nama saya", nama_user, "dan umur saya", umur_user, "tahun.")