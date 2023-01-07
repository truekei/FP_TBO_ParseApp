from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit,
    QGridLayout, QScrollArea, QGroupBox, QMessageBox
)
from PyQt6.QtCore import Qt

import sys
import fungsiCFG as cfg
 
class ListLexicon(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamus")
        self.resize(400, 600)
        
        self.scroll = QScrollArea()
        groupBox = QGroupBox()
        kamusLayout = QGridLayout()
        groupBox.setLayout(kamusLayout)
        
        # membuat scroll area untuk layout-nya
        self.scroll.setWidget(groupBox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        outerLayout = QVBoxLayout()
        outerLayout.addWidget(self.scroll)
        self.setLayout(outerLayout)
        
        # membuat komponen label tiap jenis lexicon
        pronLabel = QLabel("Kata Ganti:")
        nounLabel = QLabel("Kata Benda:")
        propLabel = QLabel("Kata Benda Khusus:")
        verbLabel = QLabel("Kata Kerja:")
        adjLabel = QLabel("Kata Sifat:")
        advLabel = QLabel("Kata Keterangan:")
        prepLabel = QLabel("Preposisi:")
        numLabel = QLabel("Numeralia:")
        
        # menaruh semua lexicon ke dalam variabel
        pron = "saya | aku | hamba | kami | kita | kamu | anda | engkau | kalian | dia | ia | beliau | mereka | ini | itu"
        noun = "perahu | kapal | kereta | tungku | paru-paru | hati | adik | buaya | orang | desa | badan | badanku | wajan | panci | spatula | polisi | harta | suami | istri | kamar | tangga | toilet | tangannya | kakinya | kakimu | gedung | drum | potongan | kayu | kotaknya | bolanya | rumahnya | permen | kain | bukunya | rambutnya | mulutnya | pantai | pasir | perumahan | tubuhnya | sendok | garpu | piring | mangkok | plastik | kolam | kesayangan | warna | bajunya | gorden | laptop | keranjang | pria | kemeja | sensor | sarung | bantal | guling | selimut | jendela | cermin | bibirnya | pintu | dapur | mata | langit | angkasa | waktu | fajar | bagian | bawah | kue | tangkai | sapu | pengantin | boneka | anak | jaket | kulihat | hidupnya | dadu | koin | tanah | topi | tomat | pesta | buah | wortel | terung | wajah | lensa | kamera | persegi | Kura-kura | pidato | seminar | bocah | rumahku | usianya | guci | ketua | periode | barang | cincin | lapangan | temanku | pohon | mangga | rumah-rumah | jeda | daki | celana | TV | amplop | uang | sembako | kop | surat | ular | rongga | mulut | sakura | kemenangan | kemarin | rumah | petir | hukuman | gitar | malam | siang | sore | pagi | kucingnya | keputusan | rusa | harimau | prestasinya | sifat | keberhasilan | hal | kisah | perjuangan | suara | apel | anggur | bunyi | parfum | bunga | nanas | lukisan | pisau | tembok | lantai | kulit | buku | obat | teh | tulisan | layar | ingin | antara | dahulu | zaman | saat | matematika | sepupu | dia | kakek | nenek | ayah | gaun | orangtua | sepatu | baju | presiden | gubernur | bupati | wali | kota | camat | hunian | lurah | pencuri | paman | tante | bibi | kerabat | saudara | keturunan | keripik | pasar | pekerjaan | sekolah | putri | payung | hujan | atap | menara | kakak | karyawan | sabit | sepeda | jantung | otak | kematian | fasilitas | umum | garam | roti | lampu | sikap | juara | kabar | mereka | tahun | usul | mungkin | kenyataan | mahasiswa | kertas | radio | ponsel | korban | bencana | alam | tugas | beban | kelas | gereja | komputer | makanan | hak | kewajiban | manusia | uud | 1945 | kultur | jaringan | wadah | masalah | presentasi | mobil | taman | bermain | apartemen | kandang | restoran | toko | kampus | kantor | acara | itu | saya | motor | pekarangan | sayur-sayuran | kursi | bengkel | atas | meja | harga | martabak | manis | pertigaan | perempatan | persimpangan | trotoar | kantin | jalan | kucing | anjing | burung | sapi | bebek | ayam | kampung | kami | anaknya | bapak | ibu | guru | diri | pak | keliling | jati | tubuh | mawar | rasa | air | terminal | pelabuhan | bandara | sungai | danau | selat | tanjung | laut | sekolahku | sekolahmu | hatinya | permainan | siswa | keluarga | asap | rokok | pipi | kainnya | matahari | gadis | meteor | bintang | bulan | bumi | berita | senja | kaki | kebun | bis | tangisan | bayi | kopinya | gadis-gadis | pertanyaan | murid | tangguh | kuasa | paham | marah | tenggara | timur | barat | utara | selatan | tengah | kiri | kanan | sebelah | samping | depan | belakang | hiu | senin | selasa | rabu | kamis | jumat | sabtu | minggu | januari | februari | maret | april | mei | juni | juli | agustus | september | oktober | november | desember | ujian | bola | dinding | peraturan | kuliah | penyakit | bantuan | kepanitiaan | sedih | vaksin | pramuka | pancasila | lemari | audisi | puncak | lawan | ikan | ketenarannya | setahun | pertandingan | hari | nanti | neneknya | akhir | cupang | usia | tv | masakan | saturnus | uranus"
        prop = "budi | steven | matthew | wahyu | roni | dito | jakarta | andi | indra | upin | saputra | susi | adi | banu | intan | dara | syifa | kadek | indah | abi | putri | wati | amanda | dian | arya | diah | citra | bali"
        verb = "masuk | keluar | datang | menggigit | meracuni | banting | membanting | terbenam | menusuk | dipotong | makan | minum | memakan | dimakan | meminum | diminum | memalak | dipalak | melintas | menjelajahi | berlayar | merokok | berseru | menyerukan | menyembah | bangkit | membangkitkan | menunduk | meniup | menjalani | menempuh | mengikat | membunuh | menyerahkan | merayakan | disebutkan | dilakukan | dijelaskan | menjilat | melaju | menyukai | percaya | mengajak | pergi | tersebut | berhenti | mengendus | mencium | menukik | menendang | ditendang | menunggangi | mencuci | membeli | menggunakan | menduduki | diperbaiki | ditaruh | berkeliaran | menyuruh | disuruh | memuridkan | memperkenalkan | membimbing | menghukum | lari | berlari | mengemudi | memiliki | turun | menuruni | mendaki | menyanyi | menari | berdansa | terkena | menjadi | memodifikasi | menyimpan | menuduh | menduplikat | membuat | menyeberang | ada | menggembirakan | melangkahkan | menyakiti | menyayat | menyayangi | melangkah | menekuni | menemui | menemukan | ditemukan | menghampiri | berjalan | terdengar | mengerjakan | menjawab | berharga | naik | bergerak | membawa | menjual | memberikan | dikenal | mendapatkan | memanjat | berenang | membangun | melihat | mendengar | berperilaku | mewarnai | menolak | membatasi | dibatasi | menambahkan | mengurangi | mengalikan | membagi | memotong | menyatakan | dibuat | menerima | dihukum | lulus | mengungsi | merawat | mencuri | tidur | meminjam | mengangkat | mengantuk | membuang | membantu | memakai | berwarna | menyusui | suka | mengecat | berubah | merupakan | melempar | menangkap | menebak | menembak | memancing | melompat | menghitung | pulang | tinggal | berlangsung | dimulai | berdebat | berpamitan | menginjak | adalah | mengoleksi | dibangun | memberi | melekat | menempel | berada | bertanya | menjelaskan | melawan | melakukan | berteriak | merasa | membenci | mengajar | menegarkan | berkuasa | mengendarai | kabur | jatuh | menjatuhkan | dijatuhkan | menjahit | atur | mengatur | diatur | paham | bingung | jujur | bohong | berolahraga | berkebun | bertanding | lalu | menang | berhasil | belajar | membuka | mengetuk | duduk | dilewati | sayang"
        adj = "pedas | lihai | selambat | secepat | terenak | ketus | gugup | panik | semanis | tegar | setegar | sesak | mampu | semampu | enak | asasi | jelas | steril | singkat | merdu | murah | baru | kecil | baik | tua | kotor | suka | segar | rusak | bulat | mewah | mahal | liar | nakal | kokoh | resah | gundah | kepanjangan | menyenangkan | basah | elok | bahagia | patah | pintar | harmonis | kemerahan | menyeramkan | kering | terik | langsing | kebesaran | kemerah-merahan | megah | yakin | ragu-ragu | secepatnya | sebaik-baiknya | sungguh-sungguh | takut | cepat | panas | hati-hati | rajin | benar | larut | lambat | lama | perlahan | mendadak | kuno | antik | primitif | lawas | lelet | dekat | jauh | akrab | lebat | rapat | besar | sempit | luas | bangga | bosan | ngeri | kesal | sedih | segan | ragu | kagum | benci | berani | lembut | gembira | serius | iba | lezat | busuk | harum | semerbak | manis | pahit | asin | asam | tampan | cantik | serak | bising | nyaring | indah | kasar | licin | halus | tebal | dingin | rapi | kusut | kacau | lebar | hebat | jelek | muda | boros | ganas | kaya | kikir | miskin | ramah | sehat | gila | sakit | jinak | marah | kejam | malas | cocok | hemat | tamak | angkuh | sombong | bersih | berat | banyak | tipis | panjang | pendek | mungil | ideal | gemuk | kurus | ringan | jutek | dangkal | cokelat | merah | biru | merahmuda | kuning | kekuning-kuningan | hijau | putih | emas | abu-abu | ungu | hijaulumut | merahjambu | merahbata | kebiru-biruan | jingga | lembayung | putihlesi | hitampekat | lentur | kaku | tinggi | tabung | balok | kubus | lingkaran | kerucut | cembung | cekung | rata | bundar | datar | tajam | lonjong | jujur | bohong | puas | pudar | dewasa | jahat"
        adv = "sekali | sudah | sangat | telah | belum | akan | sedang | ingin | mau | harus | mesti | agak | cukup | terlalu"
        prep = "sejak | dalam | dengan | ke | di | jika | pada | dari | saat | untuk | atas | kepada | terhadap"
        num = "semua | suatu | setiap | banyak | satu | dua | tiga | empat | lima | enam | tujuh | delapan | sembilan"
        
        # membuat text area untuk tiap jenis lexicon dan menaruh variabel yang sesuai
        pronText = QTextEdit()
        pronText.setText(pron.replace(' ', '').replace('|', '\t')) # mengubah | menjadi newline
        nounText = QTextEdit()
        nounText.setText(noun.replace(' ', '').replace('|', '\t'))
        propText = QTextEdit()
        propText.setText(prop.replace(' ', '').replace('|', '\t'))
        verbText = QTextEdit()
        verbText.setText(verb.replace(' ', '').replace('|', '\t'))
        adjText = QTextEdit()
        adjText.setText(adj.replace(' ', '').replace('|', '\t'))
        advText = QTextEdit()
        advText.setText(adv.replace(' ', '').replace('|', '\t'))
        prepText = QTextEdit()
        prepText.setText(prep.replace(' ', '').replace('|', '\t'))
        numText = QTextEdit()
        numText.setText(num.replace(' ', '').replace('|', '\t'))
        
        # menambah komponen ke grid layout
        kamusLayout.addWidget(pronLabel, 0, 0)
        kamusLayout.addWidget(pronText, 1, 0, 1, 5)
        kamusLayout.addWidget(nounLabel, 2, 0)
        kamusLayout.addWidget(nounText, 3, 0, 1, 5)
        kamusLayout.addWidget(propLabel, 4, 0)
        kamusLayout.addWidget(propText, 5, 0, 1, 5)
        kamusLayout.addWidget(verbLabel, 6, 0)
        kamusLayout.addWidget(verbText, 7, 0, 1, 5)
        kamusLayout.addWidget(adjLabel, 8, 0)
        kamusLayout.addWidget(adjText, 9, 0, 1, 5)
        kamusLayout.addWidget(advLabel, 10, 0)
        kamusLayout.addWidget(advText, 11, 0, 1, 5)
        kamusLayout.addWidget(prepLabel, 12, 0)
        kamusLayout.addWidget(prepText, 13, 0, 1, 5)
        kamusLayout.addWidget(numLabel, 14, 0)
        kamusLayout.addWidget(numText, 15, 0, 1, 5)


class CFG(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplikasi Parsing Bahasa Baku Bahasa Indonesia")
        self.resize(300,200)
        self.window1 = ListLexicon()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # membuat komponen untuk GUI lalu dimasukkan ke layout
        self.inputLabel = QLabel("Masukkan kalimat disini:")
        self.checkButton = QPushButton("Check")
        self.checkButton.clicked.connect(self.klik)
        self.kalimatEntry = QLineEdit()
        self.statusLabel = QLabel("Status:")
        layout.addWidget(self.inputLabel)
        layout.addWidget(self.kalimatEntry)
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.checkButton)

        # membuat button untuk membuka window kamus
        kamusButton = QPushButton("Lihat Kamus")
        kamusButton.clicked.connect(self.toggle_window1)
        layout.addWidget(kamusButton)


    def klik(self):
        # ambil kalimat dalam entry (ambil per kata dan ubah ke lowercase)
        kalimat = self.kalimatEntry.text().lower().split(' ')
        
        # cek jika tidak ada kalimat
        if len(kalimat[0]) == 0:
            alert = QMessageBox(self)
            alert.setWindowTitle('Input Kosong')
            alert.setText('Mohon untuk memasukkan kalimat terlebih dahulu.')
            alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            alert.setIcon(QMessageBox.Icon.Warning)
            alert.exec()
            return
        
        # cek jika kata dalam kalimat ada di kamus
        for k in kalimat:
            for val in cfg.produksi.values():
                if k in val:
                    exist = True
                    break
                else:
                    exist = False
                    
            if not exist: # jika tidak ada maka keluar dari fungsi
                alert = QMessageBox(self)
                alert.setWindowTitle('Kata Tidak Ditemukan')
                alert.setText('Kata "' + k + '" tidak ditemukan dalam kamus. Silahkan coba lagi.')
                alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                alert.setIcon(QMessageBox.Icon.Warning)
                alert.exec()
                return
        
        # cek jika hitungCYK me-return True maka kalimat diterima, berlaku sebaliknya jika False
        
        if cfg.hitungCYK(kalimat, 'K'):
            self.statusLabel.setText("Status: Baku")
        else:
            self.statusLabel.setText("Status: Tidak Baku")
            
 
    def toggle_window1(self):
        # membuka window kamus
        if not self.window1.isVisible():
            self.window1.show()

# start program    
app = QApplication(sys.argv)
window = CFG()
window.show()
sys.exit(app.exec())
