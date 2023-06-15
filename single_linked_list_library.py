class Node:
    def __init__(self, name, book):
        self.name = name
        self.book = book
        self.next = None


class Library:
    def __init__(self):
        self.head = None

    def add_record(self, name, book):
        new_node = Node(name, book)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_records(self):
        current = self.head
        while current:
            print("Nama Pengunjung:", current.name)
            print("Judul Buku yang Dipinjam:", current.book)
            print("------------------------")
            current = current.next


# Membuat objek Library
library = Library()

# Menambahkan beberapa catatan peminjaman
library.add_record("Rina", "Harry Potter")
library.add_record("Faisal", "The Great Gatsby")
library.add_record("Siti", "To Kill a Mockingbird")

# Mencetak daftar buku yang dipinjam oleh setiap pengunjung
library.print_records()