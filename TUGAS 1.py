def hitung_nilai(tugas, uts, uas):
    nilai_akhir = (0.25 * tugas) + (0.35 * uts) + (0.40 * uas)
    return nilai_akhir

def predikat (nilai_akhir):
    if nilai_akhir > 85:
        return 'A'
    elif nilai_akhir > 80:
        return 'A-'
    elif nilai_akhir > 75:
        return 'B+'
    elif nilai_akhir > 70:
        return 'B'
    elif nilai_akhir > 65:
        return 'B-'
    elif nilai_akhir > 60:
        return 'C+'
    elif nilai_akhir > 55:
        return 'C'
    elif nilai_akhir > 50:
        return 'C-'
    elif nilai_akhir > 30:
        return 'D'
    else:
        return 'E'

print("Selamat Datang di Aplikasi Perhitungan Nilai Mahasiswa")

tugas = float(input("Silahkan Masukan Nilai Tugas Anda: "))
uts = float(input("Silahkan Masukan Nilai UTS Anda: "))
uas = float(input("Silahkan Masukan Nilai UAS Anda: "))

nilai_akhir = hitung_nilai (tugas, uts, uas)
akreditas = predikat(nilai_akhir)

print(f"Nilai Akhir Anda: {nilai_akhir}")
print(f"Nilai dalam Huruf: {akreditas}")