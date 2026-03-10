import java.util.Scanner;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import javax.swing.JOptionPane;

public class HitungBangun {
    public static void main(String[] args) throws IOException {
        
        System.out.println("==============================================");
        System.out.println("PROGRAM PENGHITUNG BANGUN DATAR & RUANG");
        System.out.println("==============================================\n");

        // ---------------------------------------------------------
        // 1. MENGHITUNG KELILING LINGKARAN (Menggunakan Scanner)
        // ---------------------------------------------------------
        System.out.println("--- 1. Keliling Lingkaran (Input via Scanner) ---");
        Scanner scan = new Scanner(System.in);
        
        System.out.print("Masukkan jari-jari lingkaran (r): ");
        double jariJari = scan.nextDouble();
        
        // Rumus Keliling = 2 * PI * r
        double kelilingLingkaran = 2 * Math.PI * jariJari;
        
        System.out.printf("Hasil: Keliling Lingkaran adalah %.2f\n\n", kelilingLingkaran);


        // ---------------------------------------------------------
        // 2. MENGHITUNG LUAS TRAPESIUM (Menggunakan BufferedReader)
        // ---------------------------------------------------------
        System.out.println("--- 2. Luas Trapesium (Input via BufferedReader) ---");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        System.out.print("Masukkan panjang sisi sejajar atas (a): ");
        // BufferedReader membaca string, harus diubah ke double (parsing)
        double sisiA = Double.parseDouble(br.readLine());
        
        System.out.print("Masukkan panjang sisi sejajar bawah (b): ");
        double sisiB = Double.parseDouble(br.readLine());
        
        System.out.print("Masukkan tinggi trapesium (t): ");
        double tinggiTrap = Double.parseDouble(br.readLine());
        
        // Rumus Luas Trapesium = 1/2 * (a + b) * t
        double luasTrapesium = 0.5 * (sisiA + sisiB) * tinggiTrap;
        
        System.out.printf("Hasil: Luas Trapesium adalah %.2f\n\n", luasTrapesium);


        // ---------------------------------------------------------
        // 3. MENGHITUNG LUAS PRISMA SEGITIGA (Menggunakan JOptionPane)
        // ---------------------------------------------------------
        System.out.println("--- 3. Luas Permukaan Prisma Segitiga (Input via JOptionPane) ---");
        System.out.println("(Cek jendela pop-up yang muncul di layar Anda...)");
        
        // Rumus Luas Permukaan Prisma = (2 x Luas Alas) + (Keliling Alas x Tinggi Prisma)
        
        // Input Alas Segitiga
        String inputAlas = JOptionPane.showInputDialog("Menghitung Prisma Segitiga\nMasukkan Alas Segitiga (a):");
        double alasSegitiga = Double.parseDouble(inputAlas);
        
        // Input Tinggi Segitiga
        String inputTinggiSegitiga = JOptionPane.showInputDialog("Masukkan Tinggi Segitiga (t_alas):");
        double tinggiSegitiga = Double.parseDouble(inputTinggiSegitiga);
        
        // Input Keliling Segitiga (Total panjang sisi-sisi alas)
        // Kita minta langsung kelilingnya untuk menyederhanakan input
        String inputKeliling = JOptionPane.showInputDialog("Masukkan Keliling Alas Segitiga (jumlah semua sisi alas):");
        double kelilingAlas = Double.parseDouble(inputKeliling);
        
        // Input Tinggi Prisma
        String inputTinggiPrisma = JOptionPane.showInputDialog("Masukkan Tinggi Prisma (t_prisma):");
        double tinggiPrisma = Double.parseDouble(inputTinggiPrisma);
        
        // Perhitungan
        double luasAlas = 0.5 * alasSegitiga * tinggiSegitiga;
        double luasSelimut = kelilingAlas * tinggiPrisma;
        double luasPermukaanPrisma = (2 * luasAlas) + luasSelimut;
        
        // Menampilkan hasil via Message Dialog
        String hasilPesan = "Hasil Perhitungan Prisma Segitiga:\n" +
                            "Luas Alas: " + luasAlas + "\n" +
                            "Luas Selimut: " + luasSelimut + "\n" +
                            "Total Luas Permukaan: " + luasPermukaanPrisma;
                            
        JOptionPane.showMessageDialog(null, hasilPesan, "Hasil Prisma", JOptionPane.INFORMATION_MESSAGE);
        
        System.out.println("Selesai. Hasil Prisma telah ditampilkan di jendela pop-up.");
        System.out.println("==============================================");
    }
}