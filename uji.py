def analisis_nilai_mahasiswa():
    print("=== Program Analisis Data Nilai Mahasiswa ===")
    
    # 1. Inisialisasi Data (Array/List Nilai)
    # Anda bisa mengubah angka-angka di dalam kurung siku ini sesuai soal nanti
    nilai_mahasiswa = [55, 80, 65, 90, 45, 70, 85, 60, 40, 95, 78, 50]
    
    # Menampilkan data mentah
    print(f"Data Nilai: {nilai_mahasiswa}")
    print("-" * 40)

    # Pastikan data tidak kosong untuk menghindari error
    if not nilai_mahasiswa:
        print("Data nilai kosong.")
        return

    # a. Menghitung Nilai Maksimum
    # Menggunakan fungsi bawaan max()
    nilai_maksimum = max(nilai_mahasiswa)

    # b. Menghitung Nilai Minimum
    # Menggunakan fungsi bawaan min()
    nilai_minimum = min(nilai_mahasiswa)

    # c. Menghitung Rata-rata Nilai
    # Rumus: Total semua nilai dibagi jumlah data
    total_nilai = sum(nilai_mahasiswa)
    jumlah_data = len(nilai_mahasiswa)
    rata_rata = total_nilai / jumlah_data

    # d. Menghitung Jumlah Mahasiswa yang Lulus (Nilai >= 60)
    # Menggunakan perulangan (looping) untuk mengecek satu per satu
    jumlah_lulus = 0
    mahasiswa_lulus = [] # Opsional: menyimpan nilai yang lulus
    
    for nilai in nilai_mahasiswa:
        if nilai >= 60:
            jumlah_lulus += 1
            mahasiswa_lulus.append(nilai)

    # --- MENAMPILKAN HASIL ---
    print("Hasil Analisis:")
    print(f"a. Nilai Tertinggi (Maksimum) : {nilai_maksimum}")
    print(f"b. Nilai Terendah (Minimum)   : {nilai_minimum}")
    print(f"c. Rata-rata Nilai            : {rata_rata:.2f}") # .2f artinya 2 angka di belakang koma
    print(f"d. Jumlah Mahasiswa Lulus     : {jumlah_lulus} orang")
    print(f"   (Nilai >= 60)              : {mahasiswa_lulus}")

if __name__ == "__main__":
    analisis_nilai_mahasiswa()