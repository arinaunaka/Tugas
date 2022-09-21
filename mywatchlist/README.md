Link Heroku: [Tugas 3 - Arina Aunaka](https://tugas3arinaaunaka.herokuapp.com/mywatchlist/).

***Jelaskan perbedaan antara JSON, XML, dan HTML!***
> - JSON: JSON adalah singkatan dari JavaScript Object Notation. JSON bersifat self-describing, sehingga JSON sangat mudah untuk dimengerti dibandingkan XML. Data pada JSON disimpan dalam bentuk key dan value. Value dapat berupa tipe data primitif (string, number, boolean) ataupun berupa objek. 
> - XML: XML adalah singkatan dari eXtensible Markup Language. XML bersifat self-descriptive, sehingga dengan membaca XML tersebut kita bisa mengerti informasi apa yang ingin disampaikan dari data yang tertulis walaupun relatif sulit untuk dibaca dan ditafsirkan. Dokumen XML membentuk struktur seperti tree yang dimulai dari root, lalu branch, hingga berakhir pada leaves. Dokumen XML harus mengandung sebuah root element yang merupakan parent dari elemen lainnya.
> - HTML: HTML adalah singkatan dari Hyper Text Markup Language. HTML merupakan bahasa markup dan digunakan untuk menampilkan data. HTML tidak membawa data melainkan hanya menampilkannya. HTML menggambarkan struktur halaman web secara semantik dan memiliki elemen HTML berupa blok bangunan halaman HTML.

***Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?***
> Karena dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan ini bisa bermacam-macam bentuknya. 

***Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas***
1. Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
> Membuat django-app bernama mywatchlist dengan perintah `python manage.py startapp mywatchlist`

2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
> Membuat file urls.py untuk melakukan routing terhadap views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser. Kemudian mendaftarkan aplikasi mywatchlist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode `path('mywatchlist/', include('mywatchlist.urls'))` pada variabel urlpatterns.

3.  Membuat sebuah model MyWatchList yang memiliki atribut sebagai berikut: watched, title, rating, release_date, review
> Buka file models.py pada folder mywatchlist, kemudian buat class dengan parameter models.Model, isi dengan variabel nama atribut dan model fieldnya masing-masing: `watched = models.BooleanField()`, `title = models.CharField(max_length=255)`, `rating = models.IntegerField()`, `release_date = models.DateField()`, `review = models.TextField()`

4. Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat di atas
> Buat 10 data berisi model, nomor pk, dan fields masing-masing objek pada file json yang dinamai `initial_mywatchlist_data.json`

5. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format:
> - HTML: Buat fungsi bernama `show_html` pada views.py yang menerima parameter request, yang menyimpan hasil query dari seluruh data yang ada. Fungsi ini kemudian akan mengembalikan HttpResponse yang isinya diisi dengan hasil pemanggilan django.template.loader.render_to_string() yang akan melakukan render oleh Django sehingga nantinya dapat memunculkan data tersebut pada halaman HTML.
> - JSON: Buat fungsi bernama `show_json` pada views.py yang menerima parameter request, yang menyimpan hasil query dari seluruh data yang ada ke dalam sebuah variabel. Tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json".
> - XML: Buat fungsi bernama `show_xml` pada views.py yang menerima parameter request, yang menyimpan hasil query dari seluruh data yang ada ke dalam sebuah variabel. Tambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml".

6. Membuat routing sehingga data di atas dapat diakses melalui URL: /html, /json, /xml
> Tambahkan path url: `path('html/', show_html, name='show_html')`, `path('xml/', show_xml, name='show_xml')`, `path('json/', show_json, name='show_json')` ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor pada urls.py.

7. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
> Pastikan file Procfile, dpl.yml, dan .gitignore sudah ada dan telah melakukan add, commit, push ke GitHub untuk menyimpan perubahan. Setelah aplikasi siap untuk di-deploy, pastikan API key Heroku telah disimpan pada Secrets GitHub. Setelah disimpan, buka tab GitHub Actions dan jalankan kembali workflow yang gagal.

***Screenshot Postman:***
> JSON
![This is an image](/mywatchlist/assets/Postman_JSON.jpg)

> XML
![This is an image](/mywatchlist/assets/Postman_XML.jpg)

> HTML
![This is an image](/mywatchlist/assets/Postman_HTML.jpg)