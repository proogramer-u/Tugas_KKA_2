# Tugas Python Uninformed Search

## Deskripsi Tugas

Tugas ini mengimplementasikan pencarian rute menggunakan Python pada peta
kota-kota di Romania. Tujuannya adalah mencari rute dari **Arad** menuju
**Bucharest** menggunakan tiga strategi uninformed search:

1. **DFS (Depth-First Search)**: menelusuri cabang sedalam mungkin sebelum
   kembali dan mencoba cabang lain.
2. **BFS (Breadth-First Search)**: menelusuri semua kota berdasarkan tingkat
   kedalaman. BFS mencari rute dengan jumlah edge paling sedikit, tetapi belum
   tentu jaraknya paling pendek.
3. **UCS (Uniform-Cost Search)**: selalu memilih rute dengan total jarak
   terkecil yang sudah ditemukan. Dengan bobot jalan positif, UCS mencari
   rute dengan jarak minimum.

Peta pada soal direpresentasikan sebagai graph tidak berarah. Setiap jalan
memiliki jarak dalam kilometer, sehingga hubungan jalan berlaku dua arah.

## Struktur File

```text
.
├── README.md
└── Uninformed Search/
    ├── romania_search.py
    └── test_romania_search.py
```

## Hasil Pencarian

Program menjalankan pencarian dari `Arad` ke `Bucharest`.

| Strategi | Keterangan |
| --- | --- |
| DFS | Menemukan rute berdasarkan urutan penelusuran depth-first. Hasilnya tidak dijamin paling pendek. |
| BFS | Menemukan rute dengan jumlah jalan paling sedikit. Hasilnya tidak dijamin memiliki jarak minimum. |
| UCS | Menemukan rute terpendek berdasarkan total jarak. |

Rute minimum yang ditemukan oleh UCS adalah:

```text
Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
```

Total jaraknya adalah **418 km**:

```text
140 + 80 + 97 + 101 = 418 km
```

## Cara Menjalankan Program

Dari folder utama repository, jalankan:

```bash
python3 "Uninformed Search/romania_search.py"
```

Program akan menampilkan rute dan jarak yang ditemukan oleh DFS, BFS, dan
UCS.

## Menjalankan Pengujian

```bash
python3 -m unittest discover -s "Uninformed Search" -p 'test_*.py'
```

