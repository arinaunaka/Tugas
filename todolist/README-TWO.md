Nama: Arina Aunaka
NPM: 2106638690
Kelas: PBP - C
Link Heroku: [To Do List](https://tugas6arinaaunaka.herokuapp.com/todolist/)

# **Tugas 6**
### **Jelaskan perbedaan antara ***asynchronous programming*** dengan ***synchronous programming.*****
- Asynchronous programming: perintah-perintah dapat dijalankan secara bersamaan dengan perintah yang sedang dieksekusi tanpa harus menunggu proses antrian.
- Synchronous programming: proses jalannya program secara sekuensial di mana setiap perintah akan memblok eksekusi perintah selanjutnya hingga perintah yang sedang dieksekusi selesai.

### **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma ***Event-Driven Programming***. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Event-driven programming adalah paradigma pemrograman di mana aliran program didasarkan atas peristiwa atau perilaku yang dilakukan antar user dan client. Sehingga ketika user menyebabkan suatu peristiwa, maka terjadi pengiriman event yang ingin diproses dan program akan memanggil perintah-perintah berdasarkan event yang didapat.
Pada tugas ini, penerapan event-driven programming terdapat pada bagian `$(document).ready()` yang memungkinkan untuk menjalankan fungsi saat dokumen dimuat penuh.

### **Jelaskan penerapan ***asynchronous programming*** pada AJAX.**
AJAX membuat halaman web memperbarui data secara asinkronus dengan mengirimkan data ke server di balik layar sementara browser akan terus berjalan seperti biasa, sehingga AJAX dapat memperbarui sebagian elemen data pada halaman tanpa harus me-reload keseluruhan halaman.

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
- AJAX GET
  1. Buat view `show_json` yang mengembalikan seluruh data task dalam bentuk JSON.
  2. Membuat routing `/todolist/json` untuk mengakses view tersebut pada urls.py.
  3. Pada todolist.html, buat script JQuery yang melakukan request get pada `/todolist/json`. Gunakan for loop untuk melakukan iterasi setiap elemen dan setiap elemennya ditambahkan pada card yang akan muncul (di-append) pada halaman todolist. 
- AJAX POST
  1. Buat elemen button `Add Task` yang membuka modal sebagai form input title dan description dari task. Modal yang saya gunakan dari Bootstrap.
  2. Buat view `add_task` yang membuat object task baru dan menambahkannya ke dalam database.
  3. Membuat routing `/todolist/add` untuk mengakses view tersebut pada urls.py.
  4. Pada todolist.html, buat script JQuery yang melakukan fungsi post yang dipanggil ketika button Add pada modal di-click. Untuk menghubungkan form pada modal dengan path `/todolist/add`, tambahkan url tersebut pada JQueryAjaxSettings. Sehingga ketika post berhasil, maka fungsi pada views yang membuat object task baru dan mengembalikan datanya dalam bentuk JSON, datanya akan ditambahkan pada card yang akan muncul (di-append) pada halaman todolist. Tidak perlu melakukan refresh untuk menampilkan data yang baru dibuat, menandakan Ajax sudah terimplementasi. 