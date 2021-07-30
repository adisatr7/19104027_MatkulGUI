# MathQuiz™
![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) 

## Welcome!
Selamat datang di page Github resmi MathQuiz™! Game ini dibuat
sebagai tugas besar mata kuliah GUI. Adapun orang-orang yang
terlibat dalam pengembangan game ini adalah:
```
- Mohammad Rifqi Zein     (19104006)
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

## Use Case Diagram dan Design Database MathQuiz

| Title | Description |
| ----- | ----------- |
| Use Case Diagram | ![useCaseMathQuiz](https://user-images.githubusercontent.com/58881125/127613895-d7b902e1-f027-4f63-a57a-1b7b0fefb38a.png) |
| Design Database | ![image](https://user-images.githubusercontent.com/34876769/127609877-5e800c2b-f3fb-4d89-9500-bdf863b119c7.png) |

## Panduan Penggunaan
- Tools : Pycharm / Vs Code untuk compiler python, xampp untuk database
- Pastikan XAMPP sudah dinyalakan
- Buka folder menggunakan text editor python (Vs Code atau Pycharm )
- Buka xampp, pergi ke phpmyadmin dan import database `Create.sql`
- Import `Create.sql` ke dalam database yang sudah dibuat
- Tambahkan akun player ke dalam database
- Jalankan program `main.py`

![image](https://user-images.githubusercontent.com/58881125/127616250-589b12b7-612f-4aab-ad4f-b2ef796f99be.png)

- Masukkan username dan password yang sudah dibuat

![login](https://user-images.githubusercontent.com/34876769/127620801-7f82473d-3f80-41a1-aa94-63d61313abe5.png)
- Setelah login, pilih tingkat kesulitan yang diinginkan dan waktu untuk menyelesaikan tiap soal diatur 60 detik. Jika sudah klik start.

![image](https://user-images.githubusercontent.com/58881125/127616070-58f2a1e7-9d00-4ec9-8e7a-4a78199ee0de.png)
- Selesaikan soal sesuai waktu yang disediakan
- Anda juga bisa menggunakan 3 `Power Ups` yang telah disediakan

![image](https://user-images.githubusercontent.com/58881125/127633172-21c9d73b-16a7-40d8-894c-19452f012452.png)


  > Freeze time : menghentikan waktu selama beberapa detik

  > Double Point : jika pemain menjawab 1 soal dengan benar, maka poin akan dilipat gandakan

  > Skip : Pemain dapat melanjutkan ke soal berikutnya tanpa kehilangan `life`

- Pada menu profile anda dapat melihat riwayat match yang telah anda selesaikan. Anda juga dapat mengganti avatar dan melihat statistik permainan anda.

![image](https://user-images.githubusercontent.com/58881125/127634114-5fcae8c9-79f9-4b6b-8024-2d7cc1f46d7f.png)

- Beralih ke menu shop, anda dapat membeli `power ups` dan `avatar` yang anda inginkan, untuk membelinya anda dapat menggunakan poin yang telah anda kumpulkan ketika menjawab soal.

![image](https://user-images.githubusercontent.com/58881125/127634595-db95c812-4ea7-429c-872e-d6ce77d3531b.png)
![image](https://user-images.githubusercontent.com/58881125/127634681-2b3e6622-7e51-44e4-b286-c4c461b3869e.png)

- Anda dapat melihat ranking atau urutan pemain pada menu `leaderboard`.
![image](https://user-images.githubusercontent.com/58881125/127634736-51054975-622f-437c-8551-53d53e44c276.png)


