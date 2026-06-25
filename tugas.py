# ==========================
# SOAL 1: LAYOUT PAPAN CATUR
# ==========================

print("=== Layout Papan Catur ===")

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")
    print()

# ==========================
# SOAL 2: DAFTAR AKTIVITAS
# ==========================

print("\n=== Input Aktivitas ===")

daftar_aktivitas = []

jumlah = int(input("Berapa aktivitas yang ingin dimasukkan? "))

for i in range(jumlah):
    print(f"\nAktivitas ke-{i+1}")

    aktivitas = input("Nama aktivitas: ")
    waktu = input("Waktu aktivitas: ")
    prioritas = input("Prioritas (Tinggi/Sedang/Rendah): ")

    data = {
        "aktivitas": aktivitas,
        "waktu": waktu,
        "prioritas": prioritas
    }

    daftar_aktivitas.append(data)

print("\n===== DAFTAR AKTIVITAS =====")

for i, item in enumerate(daftar_aktivitas, start=1):
    print(f"{i}. Aktivitas : {item['aktivitas']}")
    print(f"   Waktu     : {item['waktu']}")