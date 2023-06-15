class Node:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_task = Node(description, priority)
        if self.head is None:
            self.head = new_task
        else:
            current = self.head
            prev = None
            while current is not None and current.priority > priority:
                prev = current
                current = current.next
            if prev is None:
                new_task.next = self.head
                self.head = new_task
            else:
                prev.next = new_task
                new_task.next = current

    def remove_task(self, description):
        if self.head is None:
            print("Daftar tugas kosong.")
            return
        if self.head.description == description:
            self.head = self.head.next
            print(f"Tugas '{description}' telah dihapus.")
            return
        current = self.head
        prev = None
        while current is not None and current.description != description:
            prev = current
            current = current.next
        if current is None:
            print(f"Tugas '{description}' tidak ditemukan.")
        else:
            prev.next = current.next
            print(f"Tugas '{description}' telah dihapus.")

    def print_tasks(self):
        if self.head is None:
            print("Daftar tugas kosong.")
        else:
            current = self.head
            print("Daftar tugas:")
            while current is not None:
                print(f"Deskripsi: {current.description}, Prioritas: {current.priority}")
                current = current.next

# Membuat objek LinkedList
task_list = LinkedList()

# Menambahkan tugas ke dalam daftar
task_list.add_task("Mengerjakan tugas matematika", 2)
task_list.add_task("Membaca buku", 1)
task_list.add_task("Berlatih olahraga", 3)

# Mencetak daftar tugas
task_list.print_tasks()

# Menghapus tugas dari daftar
task_list.remove_task("Membaca buku")

# Mencetak daftar tugas setelah penghapusan
task_list.print_tasks()