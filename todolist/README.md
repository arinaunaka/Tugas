Nama: Arina Aunaka
NPM: 2106638690
Kelas: PBP - C
Link Heroku: [Tugas 4-5 - Arina Aunaka](https://tugas3arinaaunaka.herokuapp.com/todolist/)

# **Tugas 4**
### **Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?**
{% csrf_token % berguna sebagai perlindungan bawaan dari Django terhadap sebagian besar jenis serangan Cross Site Request Forgery (CSRF). CRSF termasuk dalam serangan yang bekerja dengan mengimplementasikan permintaan yang sifatnya tidak sah selama tindakan web berlangsung. Penyerang biasanya membajak session untuk dapat mengubah IP adress user. Perubahan tersebut menuntun user masuk ke dalam situs web baru yang telah disiapkan penyerang, biasanya berupa link untuk mengirimkan formulir yang serupa dengan permintaan server, namun telah dimodifikasi. Dengan demikian, dapat disimpulkan bahwa, jika tidak ada potongan kode tersebut, maka web yang sedang membuka formulir akan menjadi rentan terhadap serangan SCRF yang sangat merugikan itu, user kehilangan kredensial akses terhadap penyerang.

### **Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.**
Ya, kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }}. Membuat elemen secara manual dapat dilakukan dengan cara berikut:
```
<form action="[URL DESTINATION]" method="[METHOD]">
    {% csrf_token %}
    <input type="[INPUT TYPE]" other attribute>
    ...
    ...
    <input type="[INPUT TYPE]" other attribute>
</form>
```

### **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**
1. User meminta request dengan TyperAddress: http://host/path pada browser
2. Browser menghasilkan HTTP Request ke http://host/path
3. Server menerima HTTP Request dan mencari views.py yang sesuai untuk menangani permintaan
4. Views.py yang sesuai akan menghasilkan halaman FORM HTML
5. Halaman FORM yang dihasilkan views.py ditampilkan kepada user
6. User mengisi dan mengumpulkan Form
7. Browser menghasilkan HTTP Request, method, dan arguments ke URL tujuan berdasarkan HTML page FORM
8. Server menerima HTTP Request dan mencari views.py yang sesuai untuk menangani permintaan
9. Views.py yang sesuai akan melakukan sesuatu (data pada Form yang dikumpulkan akan disimpan dan dipetakan ke dalam Model sehingga dapat tersimpan pada database) dan menghasilkan output berupa render halaman HTML beserta data Form yang sudah disimpan dalam database
10. Browser menampilkan halaman HTML yang mengandung data dari submisi kepada user

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. ***Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.***
```
Membuat django-app bernama todolist dengan perintah `python manage.py startapp todolist`
```

2. ***Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.***
```
Membuat file urls.py untuk melakukan routing terhadap views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser. Kemudian mendaftarkan aplikasi todolist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode `path('todolist/', include('todolist.urls'))` pada variabel urlpatterns.
```

3. ***Membuat sebuah model Task yang memiliki atribut sebagai berikut: user, date, title, description***
```
Buka file models.py pada folder mywatchlist, kemudian buat class dengan parameter models.Model, isi dengan variabel nama atribut dan model fieldnya masing-masing: `user = models.ForeignKey(User, on_delete=models.CASCADE)`, `date = models.DateField()`, `title = models.CharField(max_length=255)`, `description = models.TextField()`
```

4. ***Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.***
```
- Form registrasi: Buat fungsi dengan nama register dengan parameter request pada views.py yang menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form dengan memanfaatkan class UserCreationForm, kemudian buat register.html, lalu tambahkan `path('register/', register, name='register'),` ke dalam urlpatterns dalam urls.py.
- Login: Buat fungsi dengan nama login_user dengan parameter request pada views.py yang mengautentikasi pengguna yang ingin login dengan menggunakan function authenticate, kemudian buat login.html, lalu tambahkan `path('login/', login_user, name='login'),` ke dalam urlpatterns dalam urls.py.
- Logout: Buat fungsi dengan nama logout_user dengan parameter request pada views.py melakukan mekanisme logout dengan menggunakan function logout(request) dan langsung diarahkan ke halaman login, kemudian tambahkan button logout pada todolist.html, lalu tambahkan `path('logout/', logout_user, name='logout'),` ke dalam urlpatterns dalam urls.py.
```
5. ***Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.***
```
Membuat todolist.html yang akan ditampilkan ketika path `/todolist` dibuka. Untuk memuat username pengguna, panggil `user.get_username` untuk mengembalikan username user. Untuk memuat tombol Tambah Task Baru, buat elemen button menggunakan tag `<button></button>` yang bertuliskan "Create New Task" dan ketika diklik akan redirect ke path `/todolist/create-task`. Untuk memuat tombol logout, buat elemen button menggunakan tag `<button></button>` yang bertuliskan "Logout" dan ketika diklik akan redirect ke path `/todolist/logout`. Untuk memuat tabel, buat elemen table menggunakan tag `<table></table>` kemudian set table headernya dengan Created time, Title, dan Description, setelah itu set table datanya dengan looping pada data Model.
``` 

6. ***Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.***
```
Buat file form.py yang memuat class ToDoForm dengan parameter class Form dari module forms Django. class berisikan title dan description dengan charField. Kemudian, buat function create_task yang menerima parameter request pada views.py, buat instance dari ToDoForm dengan parameter request.POST, jika form yang diisi valid (tidak ada error), maka title, description, dan user pada model akan dibuat dan disimpan, setelah itu mengembalikan message dan redirect kembali ke path `/todolist`. Form tersebut dimasukkan ke dalam context dan ikut dirender bersama file createtask.html, yang akan menambilkan form sebagai tabel dengan `{{ form.as_table }}`.
```

7. ***Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut***
```
Tambahkan path url: `path('', show_todolist, name='show_todolist'),`, `path('register/', register, name='register'),`, `path('login/', login_user, name='login'),`, `path('logout/', logout_user, name='logout'),`, ` path('create-task/', create_task, name='create_task'),` ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor pada urls.py.
```

8. ***Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.***
```
Pastikan file Procfile, dpl.yml, dan .gitignore sudah ada dan telah melakukan add, commit, push ke GitHub untuk menyimpan perubahan. Setelah aplikasi siap untuk di-deploy, pastikan API key Heroku telah disimpan pada Secrets GitHub. Setelah disimpan, buka tab GitHub Actions dan jalankan kembali workflow yang gagal.
```

# **Tugas 5**
### **Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**
- Inline style: Properti CSS berada di dalam baris tag HTML atribut elemen. Kelebihannya adalah memiliki priority tertinggi dibanding style lainnya dan berguna untuk memperbaiki kode dengan cepat. Kekurangannya adalah tidak efisien karena hanya bisa diterapkan pada satu elemen HTML.
- Internal Style Sheet: Kumpulan properti CSS berada di dalam file HTML yang sama, tepatnya pada bagian head dengan tag `<style>`. Kelebihannya adalah dapat mengubah tampilan dalam satu halaman tanpa perlu melakukan upload beberapa file. Kekurangannya adalah tidak efisien jika ingin menggunakan CSS yang sama dalam beberapa file.
- External Style Sheet: Properti CSS berada pada file terpisah dengan HTML yang harus ditautkan menggunakan tag `<link>`. Kelebihannya adalah file CSS dapat digunakan di beberapa halaman website sekaligus sehingga mudah untuk melakukan maintenance. Kekurangannya adalah memiliki priority terendah dibanding style lainnya dan halaman akan menjadi berantakan jika file CSS gagal dipanggil oleh file HTML.

### **Jelaskan tag HTML5 yang kamu ketahui.**
- `<a>` untuk mendefinisikan hyperlink.
- `<audio>` untuk menyematkan audio dalam halaman HTML.
- `<br>` untuk menghasilkan jeda single-line.
- `<button>` untuk membuat tombol yang dapat diklik.
- `<div>` untuk menentukan divisi atau bagian dalam dokumen.
- `<form>` untuk mendefinisikan form HTML untuk input pengguna.
- `<img>` untuk merepresentasikan gambar.
- `<input>` untuk mendefinisikan kontrol input.
- `<label>` untuk mendefinisikan label untuk kontrol `<input>`.
- `<link>` untuk mendefinisikan hubungan antara dokumen saat ini dan sumber daya eksternal.
- `<nav>` untuk mendefinisikan bagian dari navigasi.
- `<p>` untuk mendefinisikan paragraf.
- `<style>` untuk menyisipkan informasi style (CSS) ke dalam head HTML.
- `<title>` untuk mendefinisikan judul untuk dokumen.
- `<table>` untuk mendefinisikan tabel data.

### **Jelaskan tipe-tipe CSS selector yang kamu ketahui.**
- Element Selector: menggunakan tag HTML sebagai selector untuk mengubah properti yang terdapat dalam tag tersebut.
- ID Selector: menggunakan ID pada tag sebagai selector-nya dengan format yang diawali "#".
- Class Selector: menggunakan Class pada tag sebagai selector-nya dengan format yang diawali ".".

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
1. ***Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin.***
```
Pada halaman login, register, dan create-task, saya mengubah background menjadi animation-gradient yang codenya saya dapatkan dari source `https://codepen.io/P1N2O/pen/pyBNzX`. Kemudian, untuk tampilan form login dan register saya kustom dari example yang sudah disediakan oleh Bootstrap dengan tampilan yang clean dan menarik. Pada halaman create-task, saya menambahkan navigation bar dan button "Back" untuk kembali ke halaman To Do List tanpa mengeklik tombol pada browser.
```
2. ***Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).***
```
Pada halaman todolist, saya juga menjadikan backgroundnya dengan animation-gradient yang sama. Kemudian saya menambahkan navigation bar dengan judul To Do List dan button untuk Logout. Kemudian saya juga mengubah tiap task menjadi bentuk card yang tersusun menjadi grid, yang tiap cardnya mengandung satu task dengan button untuk menghapus task pada bagian kanan atas card. Jika perbandingan jumlah task dengan status Finished lebih banyak atau sama dengan jumlah status Not Finished, maka kata-kata yang ditampilkan pada bagian atas todolist akan berbeda dengan jika perbandingan jumlah task dengan status Not Finished yang lebih banyak. 
```
3. ***Membuat keempat halaman yang dikustomisasi menjadi responsive.***
```
Pada tugas ini, saya menggunakan CSS framwork, Bootstrap, yang pada dasarnya menyediakan layout dengan responsif. Mereka telah memiliki media queries dengan breakpoint yang telah ditentukan dengan ukuran xs, sm, md, dan lg. Namun, untuk lebih menyesuaikan dengan halaman yang saya miliki, saya juga membuat media queries sendiri dengan breakpoint yang saya sesuaikan dengan ukuran elemen yang digunakan.
```