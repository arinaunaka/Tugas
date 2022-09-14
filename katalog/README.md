Link Heroku: [Tugas 2 - Arina Aunaka](https://tugas2arinaaunaka.herokuapp.com/katalog/).

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
![This is an image](/katalog/assets/Tugas%202%20-%20PBP.png)
HTTP request yang diberikan dari klien pada Django akan diterima oleh URLS (urls.py), kemudian urls.py akan menyalurkan request tersebut kepada View (views.py) yang sesuai. Jika request yang diberikan membutuhkan pembacaan dan penulisan data pada database, maka views.py akan mengirim atau menerima data dari Model (models.py) yang berperan sebagai manajer data. Data yang didapat akan ditampilkan pada klien, namun untuk melakukannya membutuhkan template. views.py akan mengambil template halaman yang sesuai dari html. Setelah views.py mendapatkan data dari models.py dan template dari html, views.py akan menyalurkan data tersebut pada template sehingga menjadi halaman yang utuh. Halaman html yang utuh tersebut akan menjadi response yang dikirim kepada klien. 

### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment (lingkungan virtual) digunakan untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun sebaiknya setiap proyek Django memiliki virtual environment-nya sendiri. 

### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
- Mengimpor data dari model dan mendefinisikan fungsi dengan parameter request yang memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel. Fungsi ini kemudian akan mengembalikan HttpResponse yang isinya diisi dengan hasil pemanggilan django.template.loader.render_to_string() yang akan melakukan render oleh Django sehingga nantinya dapat memunculkan data tersebut pada halaman HTML.
- Kode:
    > def show_catalog(request):
        data_katalog = CatalogItem.objects.all()
        context = {
        'list_katalog': data_katalog,
        'nama': 'Arina Aunaka',
        'npm': '2106638690',
    }
        return render(request, "katalog.html", context)

2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
- Mengimpor fungsi path dari module django.urls dan mengimpor fungsi yang telah dibuat dari views.py. Kemudian memanggil fungsi path dengan argumen fungsi tersebut untuk melakukan routing URL ke fungsi tampilan yang sesuai dalam aplikasi Django menggunakan operator URL.
- Kode:
    > from django.urls import path
    from katalog.views import show_catalog
    app_name = 'katalog'
    urlpatterns = [
        path('', show_catalog, name='show_catalog'),
    ]

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
- Mengisi data yang ingin dipetakan dengan menggunakan sintaks khusus template yang ada pada Django, yakni {{data}}. Pada kasus ini, untuk menampilkan daftar katalog, perlu melakukan iterasi terhadap variabel list_katalog yang telah ikut dirender ke dalam HTML. Kita tidak dapat memanggil daftar katalog tersebut secara langsung sebab variabel tersebut sebuah kontainer yang berisikan objek sehingga kita perlu memanggil nama 'katalog' dari objek yang ada dalam kontainer tersebut untuk memanggil data dari objek tersebut.
- Kode:
> {% for katalog in list_katalog %}
    <tr>
        <th>{{katalog.item_name}}</th>
        <th>{{katalog.item_price}}</th>
        <th>{{katalog.item_stock}}</th>
        <th>{{katalog.rating}}</th>
        <th>{{katalog.description}}</th>
        <th>{{katalog.item_url}}</th>
    </tr>
    {% endfor %}

4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Memastikan berkas bernama Procfile, dpl.yml, .gitignore sudah tersedia. Selain itu, memastikan konfigurasi pada settings.py sudah siap untuk di-deploy ke Heroku dan melakukan push seluruh file ke repositori GitHub. Kemudian buka Heroku dan membuat aplikasi baru dengan nama aplikasi yang diinginkan, lalu memilih deployment method GitHub yang selanjutnya akan menghubungkannya dengan repositori yang sudah dibuat untuk tugas 2 ini. Setelah terhubung, maka kita dapat langsung melakukan manual deploy dengan menekan button 'Deploy Branch', setelah deployment selesai, aplikasi langsung dapat diakses melalui internet. 