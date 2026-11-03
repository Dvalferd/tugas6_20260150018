import modul_evaluasi


def input_angka_valid(prompt, min_val, max_val):
    """Meminta input angka (float) sampai valid dan berada di rentang min_val - max_val."""
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("Error: Input harus berupa angka, bukan huruf/teks. Silakan ulangi.")
            continue

        if nilai < min_val or nilai > max_val:
            print(f"Warning: Angka harus di antara {min_val:g} dan {max_val:g}. Silakan ulangi.")
            continue

        return nilai


def input_teks_tidak_kosong(prompt):
    """Meminta input teks yang tidak boleh kosong."""
    while True:
        teks = input(prompt).strip()
        if teks:
            return teks
        print("Error: Input tidak boleh kosong. Silakan ulangi.")


def proses_kelayakan():
    """Mengelola input data aslab, memanggil fungsi modul, dan menampilkan hasil."""
    print("\n--- Input Data Calon Asisten Laboratorium ---")
    nama = input_teks_tidak_kosong("Nama                     : ")
    nim = input_teks_tidak_kosong("NIM                      : ")
    hadir = input_angka_valid("Jumlah kehadiran (0-14)  : ", 0, 14)
    tugas = input_angka_valid("Nilai Tugas (0-100)      : ", 0, 100)
    ucp1 = input_angka_valid("Nilai UCP 1 (0-100)      : ", 0, 100)
    ucp2 = input_angka_valid("Nilai UCP 2 (0-100)      : ", 0, 100)

    persentase = modul_evaluasi.hitung_persentase_presensi(hadir)
    nilai_akhir = modul_evaluasi.hitung_nilai_akhir(tugas, ucp1, ucp2)
    status = modul_evaluasi.cek_kelayakan_aslab(persentase, nilai_akhir)

    print("\n" + "=" * 45)
    print("        HASIL EVALUASI KELAYAKAN ASLAB")
    print("=" * 45)
    print(f"Nama                : {nama}")
    print(f"NIM                 : {nim}")
    print(f"Kehadiran           : {hadir:g} dari 14 pertemuan")
    print(f"Persentase Presensi : {persentase:.2f}%")
    print(f"Nilai Akhir         : {nilai_akhir:.2f}")
    print(f"Status              : {status}")
    print("=" * 45)


def main():
    while True:
        print("\n===== SISTEM EVALUASI KELAYAKAN ASLAB AI =====")
        print("1. Hitung Kelayakan")
        print("2. Keluar")

        try:
            pilihan = int(input("Pilih menu (1/2): "))
        except ValueError:
            print("Error: Pilihan menu harus berupa angka 1 atau 2.")
            continue

        if pilihan == 1:
            proses_kelayakan()
        elif pilihan == 2:
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Warning: Pilihan tidak tersedia. Pilih 1 atau 2.")


if __name__ == "__main__":
    main()