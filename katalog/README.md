Link Heroku: https://tugas2arinaaunaka.herokuapp.com/katalog/

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment (lingkungan virtual) digunakan untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun sebaiknya setiap proyek Django memiliki virtual environment-nya sendiri. 

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
- Mengimpor data dari model dan mendefinisikan fungsi dengan parameter request yang memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel. Fungsi ini kemudian akan mengembalikan HttpResponse yang isinya diisi dengan hasil pemanggilan django.template.loader.render_to_string() yang akan melakukan render oleh Django sehingga nantinya dapat memunculkan data tersebut pada halaman HTML.
- Kode:
def show_catalog(request):
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
from django.urls import path
from katalog.views import show_catalog

app_name = 'katalog'

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
- 