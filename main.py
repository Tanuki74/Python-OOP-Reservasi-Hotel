class Hotel(object):
    def __init__(self):
        self._nama = ""
        self._tipe = 0
        self._waktu = 0

    #getter nama
    @property
    def get_nama(self):
        return self._nama

    #setter nama
    @get_nama.setter
    def set_nama(self, inputNama):
        self._nama = inputNama

    #getter tipe
    @property
    def get_tipe(self):
        return self._tipe

    #setter tipe
    @get_tipe.setter
    def set_tipe(self, inputTipe):
        self._tipe = inputTipe

    # getter waktu
    @property
    def get_waktu(self):
        return self._waktu

    #setter waktu
    @get_waktu.setter
    def set_waktu(self, inputWaktu):
        self._waktu = inputWaktu

class Tarif(Hotel):
    # __tarif = 0
    # __kamar = ""

    def __init__(self):
        self.__tarif = 0
        self.__kamar = ""

    def harga(self):
        if self.get_tipe == 1:
            self.__tarif = 250000
            return self.__tarif
        if self.get_tipe == 2:
            self.__tarif = 500000
            return self.__tarif
        if self.get_tipe == 3:
            self.__tarif = 750000
            return self.__tarif

    def kamar(self):

        if self.get_tipe == 1:
            self.__kamar = "Deluxe"
            return self.__kamar
        if self.get_tipe == 2:
            self.__kamar = "Premium"
            return self.__kamar
        if self.get_tipe == 3:
            self.__kamar = "Superior"
            return self.__kamar

    def total(self):
        return self.__tarif * self._waktu


class Main:
    hotel = Tarif()

    def __init__(self):
        self.register()
        self.pilihKamar()
        self.berapaLama()
        self.display()

    def register(self):
        print("===== Reservasi Hotel =====")
        nama = input(f'Masukan Nama Anda: ')
        self.hotel.set_nama = nama

    def pilihKamar(self):
        print("""Pilih Jenis Kamar
        1. Deluxe Room      Rp. 250000
        2. Premium Room     Rp. 500000
        3. Superior Room    Rp. 750000
        """)
        pilih = int(input(f"Jenis Kamar Yang Dipilih: "))
        self.hotel.set_tipe = pilih

    def berapaLama(self):
        lama = int(input("Berapa Lama: "))
        self.hotel.set_waktu = lama

    def display(self):
        print(f"""
        ===== Pembayaran ====
        Nama             : {self.hotel.get_nama}
        Jenis Kamar      : {self.hotel.kamar()}
        Tarif Penginapan : {self.hotel.harga()}
        Total            : {self.hotel.total()}            
        """)

if __name__ == '__main__':
    Main()