from graphviz import Digraph

# Membuat objek diagram
dot = Digraph(comment='DFD Level 0 - Sistem Informasi Akademik')
dot.attr(rankdir='TB', size='10')

# --- ENTITAS LUAR (Kotak Persegi) ---
dot.attr('node', shape='box', style='filled', color='lightgrey')
dot.node('MHS', 'Mahasiswa')
dot.node('DSN', 'Dosen')
dot.node('ADM', 'Admin')

# --- PROSES (Lingkaran/Rounded) ---
dot.attr('node', shape='circle', style='bold', fixedsize='false', width='1.5', color='black', fillcolor='white')
dot.node('P1', '1.0\nManajemen\nData Master')
dot.node('P2', '2.0\nRegistrasi\n(KRS)')
dot.node('P3', '3.0\nPenilaian\n(Input Nilai)')
dot.node('P4', '4.0\nLaporan &\nTranskrip')

# --- DATA STORE (Dua garis horizontal - direpresentasikan kotak terbuka di graphviz standar) ---
dot.attr('node', shape='box', style='rounded', color='black', penwidth='1')
dot.node('D1', 'D1 Data Mahasiswa')
dot.node('D2', 'D2 Data Dosen')
dot.node('D3', 'D3 Data Matkul')
dot.node('D4', 'D4 Data KRS')
dot.node('D5', 'D5 Data Nilai')

# --- ALUR DATA (Edges) ---

# Alur 1.0 Manajemen Data
dot.edge('ADM', 'P1', label='Input Data Master')
dot.edge('P1', 'D1', label='Simpan Mhs')
dot.edge('P1', 'D2', label='Simpan Dosen')
dot.edge('P1', 'D3', label='Simpan Matkul')

# Alur 2.0 KRS
dot.edge('MHS', 'P2', label='Input KRS')
dot.edge('D1', 'P2', label='Validasi Mhs')
dot.edge('D3', 'P2', label='Cek Jadwal')
dot.edge('P2', 'D4', label='Simpan KRS')
dot.edge('P2', 'MHS', label='Cetak KRS')

# Alur 3.0 Penilaian
dot.edge('DSN', 'P3', label='Input Nilai')
dot.edge('D4', 'P3', label='Data Peserta')
dot.edge('P3', 'D5', label='Simpan Nilai')
dot.edge('P3', 'MHS', label='Lihat KHS')

# Alur 4.0 Laporan
dot.edge('ADM', 'P4', label='Req Laporan')
dot.edge('D5', 'P4', label='Ambil Nilai')
dot.edge('D1', 'P4', label='Data Mhs')
dot.edge('P4', 'MHS', label='Cetak Transkrip')
dot.edge('P4', 'ADM', label='Laporan Statistik')

# Render hasil
# dot.render('dfd_level_0_siakad', view=True, format='png')
print(dot.source)