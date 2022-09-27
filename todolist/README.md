Link Heroku: 

***Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?***

***Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.***

***Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.***

***Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.***
1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
> Membuat django-app bernama todolist dengan perintah `python manage.py startapp todolist`

2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
> Membuat file urls.py untuk melakukan routing terhadap views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser. Kemudian mendaftarkan aplikasi todolist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode `path('todolist/', include('todolist.urls'))` pada variabel urlpatterns.

3. Membuat sebuah model Task yang memiliki atribut sebagai berikut: user, date, title, description
> Buka file models.py pada folder mywatchlist, kemudian buat class dengan parameter models.Model, isi dengan variabel nama atribut dan model fieldnya masing-masing: `user = models.ForeignKey(User, on_delete=models.CASCADE)`, `date = models.DateField()`, `title = models.CharField(max_length=255)`, `description = models.TextField()`

4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
> - Form registrasi: Buat fungsi dengan nama register dengan parameter request pada views.py yang menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form dengan memanfaatkan class UserCreationForm, kemudian buat register.html, lalu tambahkan `path('register/', register, name='register'),` ke dalam urlpatterns dalam urls.py.
> - Login: Buat fungsi dengan nama login_user dengan parameter request pada views.py yang mengautentikasi pengguna yang ingin login dengan menggunakan function authenticate, kemudian buat login.html, lalu tambahkan `path('login/', login_user, name='login'),` ke dalam urlpatterns dalam urls.py.
> - Logout: Buat fungsi dengan nama logout_user dengan parameter request pada views.py melakukan mekanisme logout dengan menggunakan function logout(request) dan langsung diarahkan ke halaman login, kemudian tambahkan button logout pada todolist.html, lalu tambahkan `path('logout/', logout_user, name='logout'),` ke dalam urlpatterns dalam urls.py.

5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
> 

6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
> 

7. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut
> Tambahkan path url: `path('', show_todolist, name='show_todolist'),`, `path('register/', register, name='register'),`, `path('login/', login_user, name='login'),`, `path('logout/', logout_user, name='logout'),`, ` path('create-task/', create_task, name='create_task'),` ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor pada urls.py.

8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
> Pastikan file Procfile, dpl.yml, dan .gitignore sudah ada dan telah melakukan add, commit, push ke GitHub untuk menyimpan perubahan. Setelah aplikasi siap untuk di-deploy, pastikan API key Heroku telah disimpan pada Secrets GitHub. Setelah disimpan, buka tab GitHub Actions dan jalankan kembali workflow yang gagal.

9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
>