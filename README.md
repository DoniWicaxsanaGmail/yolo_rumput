# Mencabut rumput dengan AI
setiap kali saya berjalan di rumput gajah mini yang saya pelihara saya merasa tidak ada masalah. namun jika diperhatikan ada beberapa rumput liar yang bentuk dan warnanya serupa. sehingga sering melakukan pemeliharaan dengan mencabut rumput-rumput liar tersebut. tapi keterbatasan mata manusia untuk rumput yang memiliki warna yang serupa cenderung susah kita lihat dan tiba-tiba rumput sudah besar dan menutupi rumput gajah mini yang kita pelihara. masalah terbesar adalah saat saya tinggal ke luar kota dan ketika pulang ke rumah hampir 20% rumput saya mati karena tertutup rumput liar. hedeeeh katanya rumput gajah masa kalah sama rumput liar.
## Belajar AI
Saya seorang QA Manager saya suka menghabiskan waktu luang saya untuk mempelajari hal-hal baru, kemunculan Chat GPT membuat saya penasaran untuk mempelajari AI, hingga saya membuat Private AI dengan Langchain, Ollama, NextJs, dan llama 3 dan Speech recognition. akhir nya saya bisa berbicara menggunakan suara dengan AI saya. selama berselancar di internet saya lihat banyak sekali model-model AI yang sebenarnya bisa kita gunakan (Tinggal Pake aja..!) salah satunya YOLO saya mencoba untuk mendeteksi beberapa object dengan YOLO.
## Berpikir LIAR melawan rumput LIAR
Oke kembali ke masalah rumput saya awalnya kesal karena saya harus mencabut rumput liar dan harus menanam kembali rumput gajah mini saya. saya giat melakukan inspeksi rumput liar, lumayan melelahkan dan banyak yang terlewat karena kemiripan warna. akhirnya saya terpikir untuk menggunakan YOLO 11 untuk membedakan mana rumput gajah mini dan mana yang rumput liar. Berkat rasa penasaran dan keisengan saya coba membuat AI dengan mengumpulkan foto-foto dari pekarangan untuk dikumpulkan menjadi dataset YOLO saya. PR yang paling melelahkan disini adalah **Annotate** atau memberi label ke setiap rumput liar agar YOLO bisa membedakan rumput liar dan rumput gajah mini. butuh waktu 4 hari untuk menandai rumput liar tersebut. ternyata membuat code nya nggak sampai 1 menit. training data saya lakukan 2 kali pertama menggunakan gambar ukuran 640 x 640 dan hasilnya kurang memuaskan, akhir nya saya coba dengan 1024x1024 dan hasilnya lebih baik tapi karena dataset yang saya miliki hanya 190 jadi akurasinya masih belum terbilang bagus. tetapi untuk mendeteksi rumput liar lumayan membantu. wkwkw.
## Pelajaran
1. Ide dan penemuan terkadang berawal dari kemalasan
1. Ilmu tidak hanya untuk dunia kerja tetapi bisa membantu kita dalam kehidupan sehari-hari.
1. Mengerjakan sesuatu meski tidak ada upah jika senang dan bermanfaat kenapa nggak.
## Langkah selanjutnya
1. membuat antar muka dengan Next Js
1. memperbaiki dataset karena YOLO menggunakan gambar dengan bentuk kotak bukan persegi panjang (kamera hp)
1. ngopi dan cari ide lagi.

## Installasi
Langkah-langkah
### Clone dari GitHub
https://github.com/DoniWicaxsanaGmail/yolo_rumput.git
### Membuat local environment
```powershell
python -m venv .venv
```
### Aktivasi virtual Environment (di Windows dengan ps1)
```powershell
.\.venv\Scripts\Activate.ps1
```
### Install Python Packages 
```powershell
pip install -r requirements.txt
```

## Menjalankan
### Aktivasi virtual Environment jika belum di aktifkan (di Windows dengan ps1)
```powershell
.\.venv\Scripts\Activate.ps1
```
### Menjalankan Object Detection 
```powershell
python .\main.py 
```