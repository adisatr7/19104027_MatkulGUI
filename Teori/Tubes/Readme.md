# MathQuiz™

## Welcome!
Selamat datang di page Github resmi MathQuiz™! Game ini dibuat
sebagai tugas besar mata kuliah GUI. Adapun orang-orang yang
terlibat dalam pengembangan game ini adalah:
```
- Muhammad Rifqi Zein     (19104006)
- Satria Adi Nugraha      (19104027)
- Rifqi Alfi Nur Charisma (19104031)
```

## What's this all about?

MathQuiz™ adalah game tebak-tebakan sederhana berbasis 
Matematika. Untuk soalnya sendiri, kami memanfaatkan
modul `random` bawaan Python untuk mendapatkan sembarang
angka. Dan untuk operasi Matematikanya sendiri masih sederhana,
yakni penjumlahan, pengurangan, perkalian, dan pembagian.

Game ini memiliki 3 tingkat kesulitan, dimana pada tingkat
paling mudah pemain sama sekali tidak akan disajikan soal
pembagian. Di sisi lain, pemain akan diberikan ekstra poin
jika bermain dengan tingkat kesulitan tinggi. Poin ini
nantinya akan disetorkan ke database. Game ini memiliki
leaderboard dimana pemain dapat membandingkan performa
bermain mereka dengan pemain lain.

Selain itu, poin juga dapat digunakan untuk membeli Power Up.
Ada total 3 Power Up di game ini, yakni Freeze Timer
(menghentikan timer permainan selama beberapa detik),
Double Point (pemain akan diberi poin dua kali lipat
jika pemain berhasil menjawab 1 soal dengan benar), dan
Skip Round (pemain dapat maju ke ronde/soal berikutnya
tanpa kehilangan 'Life').

Berbicara tentang Life, pemain akan diberikan 1-3 Life,
tergantung tingkat kesulitan yang dipilih. Life akan berkurang
jika pemain memilih jawaban yang salah. Selain itu, pemain
juga akan diberikan soal baru, agar pemain tidak asal pilih
saat mengerjakan soal.
