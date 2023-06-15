class Node:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.next = None

class Tournament:
    def __init__(self):
        self.head = None
    
    def add_participant(self, name, rating):
        new_participant = Node(name, rating)
        
        if self.head is None:
            self.head = new_participant
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_participant
    
    def remove_loser(self, name):
        if self.head is None:
            return
        
        if self.head.name == name:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.name == name:
                    current.next = current.next.next
                    break
                current = current.next
    
    def print_participants(self):
        if self.head is None:
            print("Tidak ada peserta terdaftar.")
        else:
            current = self.head
            while current is not None:
                print(f"Nama: {current.name}, Peringkat: {current.rating}")
                current = current.next

# Contoh penggunaan program
tournament = Tournament()

# Menambahkan peserta
tournament.add_participant("John", 1500)
tournament.add_participant("Alice", 1700)
tournament.add_participant("Bob", 1300)
tournament.add_participant("Sarah", 1600)

# Mencetak daftar peserta
tournament.print_participants()

# Menghapus peserta yang kalah
tournament.remove_loser("Bob")

# Mencetak daftar peserta setelah penghapusan
tournament.print_participants()