"""
modul_evaluasi.py
Pustaka logika untuk Sistem Evaluasi Kelayakan Asisten Laboratorium AI.
Catatan: file ini tidak berisi input() maupun print() utama.
"""


def hitung_persentase_presensi(hadir, total_pertemuan=14):
    """Menghitung persentase kehadiran berdasarkan jumlah hadir."""
    return (hadir / total_pertemuan) * 100


def hitung_nilai_akhir(tugas, ucp1, ucp2):
    """Menghitung nilai akhir: Tugas 20%, UCP 1 40%, UCP 2 40%."""
    return (0.20 * tugas) + (0.40 * ucp1) + (0.40 * ucp2)


def cek_kelayakan_aslab(persentase_presensi, nilai_akhir):
    """Menentukan status kelayakan asisten laboratorium."""
    if persentase_presensi < 75.0:
        return "DITOLAK (Kehadiran di bawah 75%)"
    elif nilai_akhir >= 75.0:
        return "DITERIMA (Memenuhi Syarat)"
    else:
        return "DITOLAK (Nilai Akhir Kurang)"