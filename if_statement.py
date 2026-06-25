from datetime import datetime

print("=== Aplikasi Manajemen Aktivitas ===")

aktivitas = input("Masukkan kegiatan yang akan dilakukan (sarapan / berangkat kerja): ").lower()

if aktivitas == "sarapan":
    menu = input("Masukkan menu sarapan yang diinginkan: ").lower()

    if menu == "telur" or menu == "ikan" or menu == "nugget":
        print(f"Anda memilih {menu}.")
        print("Bahan tersedia di rumah, silakan dimasak terlebih dahulu.")
    else:
        print(f"Anda memilih {menu}.")
        print("Bahan tidak tersedia, silakan membeli bahan terlebih dahulu.")

elif aktivitas == "berangkat kerja":
    sekarang = datetime.now()
    jam_masuk = sekarang.replace(hour=8, minute=0, second=0, microsecond=0)

    print("Waktu saat ini:", sekarang.strftime("%H:%M"))

    if sekarang > jam_masuk:
        print("Peringatan: Anda sudah terlambat masuk kerja!")
    else:
        print("Anda belum terlambat. Segera bersiap berangkat kerja.")

else:
    print("Aktivitas tidak dikenali.")