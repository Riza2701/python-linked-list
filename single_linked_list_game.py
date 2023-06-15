class Item:
    def __init__(self, nama, kepentingan):
        self.nama = nama
        self.kepentingan = kepentingan
        self.next = None


class Tas:
    def __init__(self):
        self.head = None

    def tambah_item(self, nama, kepentingan):
        item_baru = Item(nama, kepentingan)
        if self.head is None:
            self.head = item_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = item_baru

    def hapus_item(self, nama):
        if self.head is None:
            return

        if self.head.nama == nama:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.nama == nama:
                current.next = current.next.next
                return
            current = current.next

    def cetak_daftar_item(self):
        if self.head is None:
            print("Tas kosong.")
        else:
            current = self.head
            print("Daftar item dalam tas:")
            while current:
                print("Nama: " + current.nama + ", Kepentingan: " + str(current.kepentingan))
                current = current.next


# Contoh penggunaan
tas = Tas()

tas.tambah_item("Buku", 3)
tas.tambah_item("Potion", 2)
tas.tambah_item("Pedang", 5)
tas.tambah_item("Kunci", 1)

tas.cetak_daftar_item()

tas.hapus_item("Potion")

tas.cetak_daftar_item()