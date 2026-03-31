# =========================
# LIST – akses & manipulasi
# =========================
data_list = ["apel", 10, "jeruk", 25, "mangga", 50]

print("List awal:", data_list)
print("Elemen pertama:", data_list[0])
print("Elemen terakhir:", data_list[-1])
print("Slicing [1:5:2]:", data_list[1:5:2])

# Manipulasi
print("\nSebelum manipulasi:", data_list)

data_list.append("pisang")
data_list.insert(2, "anggur")
data_list.extend([100, "melon"])
data_list.pop()
data_list.remove("apel")

print("Sesudah manipulasi:", data_list)


# =========================
# TUPLE – immutability & unpacking
# =========================
data_tuple = ("A", "B", "C", "D", "E")

print("\nTuple:", data_tuple)
print("Panjang tuple:", len(data_tuple))
print("Akses indeks ke-2:", data_tuple[2])

a, b, c, *rest = data_tuple
print("Unpacking:")
print("a:", a)
print("b:", b)
print("c:", c)
print("rest:", rest)


# =========================
# SET – operasi himpunan
# =========================
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# Duplikat hilang
set_duplikat = {1, 2, 2, 3, 3, 4}
print("Set dengan duplikat:", set_duplikat)


# =========================
# DICTIONARY – key/value
# =========================
mahasiswa = {
    "nama": "Sweety",
    "nim": "123456",
    "angkatan": 2023,
    "kota": "Sorong"
}

print("\nDictionary awal:", mahasiswa)

# Tambah key
mahasiswa["jurusan"] = "Informatika"

# Ubah nilai
mahasiswa["kota"] = "Manokwari"

# Hapus key
del mahasiswa["angkatan"]

print("Dictionary setelah perubahan:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("\nIterasi:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")


# =========================
# NESTED STRUCTURES
# =========================
buku = [
    {"judul": "Python Dasar", "penulis": "Andi", "tahun": 2020},
    {"judul": "AI Modern", "penulis": "Budi", "tahun": 2023},
    {"judul": "Data Science", "penulis": "Citra", "tahun": 2021},
    {"judul": "Machine Learning", "penulis": "Dedi", "tahun": 2024}
]

print("\nDaftar Judul Buku:")
for b in buku:
    print(b["judul"])

# Filter buku >= tahun tertentu
tahun_filter = 2022
buku_baru = [b for b in buku if b["tahun"] >= tahun_filter]

print("\nBuku terbit >= 2022:")
for b in buku_baru:
    print(b)


# =========================
# COMPREHENSION & UTILITAS
# =========================
angka = list(range(1, 21))

genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("\nAngka genap:", genap)
print("Kuadrat:", kuadrat)

# Dict comprehension
mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("\nMapping angka:", mapping)

# Set comprehension
kalimat = "Belajar Python Itu Menyenangkan"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf_unik)


# =========================
# KEANGGOTAAN & PENCARIAN
# =========================
print("\nCek keanggotaan:")

if 10 in data_list:
    print("10 ada di list")

if 3 in set1:
    print("3 ada di set1")

# Pencarian posisi
if "jeruk" in data_list:
    print("Posisi 'jeruk':", data_list.index("jeruk"))
else:
    print("'jeruk' tidak ditemukan")