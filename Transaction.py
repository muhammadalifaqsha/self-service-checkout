from tabulate import tabulate

class Transaction:
    """
    class ini mendefinisikan suatu objek
    yang menyimpan daftar transaksi 
    dan method-method untuk mengeditnya
    """
    def __init__(self):   
        # selalu membuat list kosong ketika class dibentuk
        self.shopping_list = {}
        
    def add_item(self, item_spec):
        # method menambahkan item transaksi
        self.shopping_list[item_spec[0]] = item_spec[1:]
        
    def update_item_name(self, old_item, new_item):
        # method mengubah nama salah satu item
        item_spec = self.shopping_list[old_item].copy()
        self.shopping_list.pop(old_item)
        self.shopping_list[new_item] = item_spec
        
    def update_item_qty(self, item, qty):
        # method mengubah jumlah salah satu item
        self.shopping_list[item][0] = qty
        
    def update_item_price(self, item, price):
        # method mengubah harga salah satu item
        self.shopping_list[item][1] = price
        
    def delete_item(self, item):
        # method menghapus salah satu item
        self.shopping_list.pop(item)
        
    def reset_transaction(self):
        # method me-reset semua transaksi
        self.shopping_list = {}
        
    def check_order(self):
        # method untuk cek order, print shopping list & total
        
        data = [[key, val[0], val[1], val[0]*val[1]] for key, val in self.shopping_list.items()]
        is_false1 = any(item == '' or item.isspace() for item in self.shopping_list.keys())
        is_false2 = any(num[0]<=0 or num[1]<=0 for num in self.shopping_list.values())
        print(tabulate(data, headers=['Item', 'Qty', 'Price', 'Total']))
        
        if is_false1 or is_false2:
            print('Pesanan Anda masih mengandung kesalahan!')
        else:
            print('Pesanan Anda sudah benar!')
        
    def total_price(self):
        # method to calculate total & discount
        total = sum([val[0]*val[1] for val in self.shopping_list.values()])
        
        if total <= 200_000:
            self.discount_rate = 0
        elif total <= 300_000:
            self.discount_rate = 0.05
        elif total <= 500_000:
            self.discount_rate = 0.08
        else:
            self.discount_rate = 0.1
            
        return total - self.discount_rate*total        