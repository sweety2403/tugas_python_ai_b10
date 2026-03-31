# =========================
# IMPORT & SETUP
# =========================
import numpy as np
import pandas as pd
import os  # opsional

np.random.seed(42)


# =========================
# NUMPY – DATA & STATISTIK
# =========================
# Membuat array nilai ujian (minimal 10 data)
nilai_array = np.random.randint(50, 101, size=12)

# Statistik
rata_np = np.mean(nilai_array)
median_np = np.median(nilai_array)
std_np = np.std(nilai_array)
min_np = np.min(nilai_array)
max_np = np.max(nilai_array)


# =========================
# PANDAS – DATAFRAME
# =========================
data = {
    "nama": ["sweety", "jekson", "indriany", "bunga", "arga"],
    "nim": ["202365040", "202365012", "202365043", "202365065", "202365020ge"],
    "nilai": nilai_array[:5]  # ambil 5 data dari numpy
}

df = pd.DataFrame(data)

# Tambah kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")


# =========================
# FILE I/O – TULIS KE TXT
# =========================
file_path = "ringkasan_tugas6.txt"

def tulis_ringkasan_awal():
    with open(file_path, "w") as f:
        f.write("=== RINGKASAN NUMPY ===\n")
        f.write(f"Rata-rata: {rata_np:.2f}\n")
        f.write(f"Median: {median_np:.2f}\n")
        f.write(f"Std Dev: {std_np:.2f}\n")
        f.write(f"Min: {min_np}\n")
        f.write(f"Max: {max_np}\n\n")

        f.write("=== RINGKASAN DATAFRAME ===\n")
        f.write(f"Jumlah data: {len(df)}\n")
        f.write(f"LULUS: {len(df[df['status']=='LULUS'])}\n")
        f.write(f"TIDAK LULUS: {len(df[df['status']=='TIDAK LULUS'])}\n\n")


# =========================
# OOP – GRADEBOOK
# =========================
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        lulus = len(self.df[self.df["nilai"] >= threshold])
        return (lulus / total) * 100 if total > 0 else 0.0

    def save_summary(self, path: str):
        with open(path, "a") as f:
            f.write("=== RINGKASAN GRADEBOOK ===\n")
            f.write(f"Rata-rata nilai: {self.average():.2f}\n")
            f.write(f"Persentase lulus: {self.pass_rate():.2f}%\n\n")

    def __str__(self):
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average():.2f})"


# =========================
# DEMO
# =========================
if __name__ == "__main__":
    print("=== NUMPY ===")
    print("Data:", nilai_array)
    print("Rata-rata:", round(rata_np, 2))
    print("Median:", median_np)
    print("Std Dev:", round(std_np, 2))
    print("Min:", min_np)
    print("Max:", max_np)

    print("\n=== PANDAS ===")
    print(df.head())

    # Tulis ringkasan awal ke file
    tulis_ringkasan_awal()

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)

    print(gb)
    print("Average:", round(gb.average(), 2))
    print("Pass Rate:", round(gb.pass_rate(), 2), "%")

    # Simpan tambahan ringkasan
    gb.save_summary(file_path)

    print(f"\nRingkasan disimpan di: {os.path.abspath(file_path)}")