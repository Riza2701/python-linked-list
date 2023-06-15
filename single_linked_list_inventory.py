class Product:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None

class InventoryManagement:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = Product(name, code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_product

    def remove_product(self, code):
        current = self.head
        previous = None
        while current:
            if current.code == code:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        print("Product with code {} not found.".format(code))

    def print_inventory(self):
        if self.head is None:
            print("Inventory is empty.")
        else:
            current = self.head
            print("Inventory:")
            print("{:<10} {:<10} {:<10}".format("Name", "Code", "Stock"))
            print("--------------------------")
            while current:
                print("{:<10} {:<10} {:<10}".format(current.name, current.code, current.stock))
                current = current.next

# Contoh penggunaan
inventory = InventoryManagement()

# Menambahkan produk
inventory.add_product("Product 1", "P1", 10)
inventory.add_product("Product 2", "P2", 5)
inventory.add_product("Product 3", "P3", 3)

# Mencetak inventaris
inventory.print_inventory()
# Output:
# Inventory:
# Name       Code       Stock
# --------------------------
# Product 1  P1         10
# Product 2  P2         5
# Product 3  P3         3

# Menghapus produk
inventory.remove_product("P2")

# Mencetak inventaris setelah penghapusan
inventory.print_inventory()
# Output:
# Inventory:
# Name       Code       Stock
# --------------------------
# Product 1  P1         10
# Product 3  P3         3