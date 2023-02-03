from Transaction import *

def add_item(trnsct_123):
    # a function for user to input items
    item = input('\nMasukkan nama item: ')
        
    try:
        qty = int(input('Masukkan jumlah item: '))
        price = float(input('Masukkan harga barang per item: '))
        trnsct_123.add_item([item, qty, price])        
        print(f'{item} sebanyak {qty} dengan harga Rp{price:,}/item telah ditambahkan!')
        print(f'Shopping cart: {trnsct_123.shopping_list}\n')

    except ValueError:
        print(f'Format tidak sesuai!\n')
            
def update_item_name(trnsct_123):
    # a function for user to change item name
    old_item = input('\nMasukkan nama item lama: ')
    new_item = input('Masukkan nama item baru: ')

    try:
        trnsct_123.update_item_name(old_item, new_item)
        print(f'Nama item {old_item} telah diganti menjadi {new_item}')

    except KeyError:  # error if old item name is not in list
        print(f'Tidak ada nama item {old_item} di daftar transaksi!')
    
    finally:
        print(f'Shopping cart: {trnsct_123.shopping_list}\n')
            
def update_item_qty(trnsct_123):
    # a function for user to change qty of item
    
    try:
        item = input('\nMasukkan nama item: ')
        qty = int(input('Masukkan jumlah item baru: '))
        trnsct_123.update_item_qty(item, qty)
        print(f'Jumlah item {item} telah diganti menjadi sebanyak {qty}')

    except ValueError:  # error if qty is not a number
        print(f'Format tidak sesuai!')

    except KeyError:  # error if item name is not in list
        print(f'Tidak ada nama item {item} di daftar transaksi!')
        
    finally:
        print(f'Shopping cart: {trnsct_123.shopping_list}\n')
            
def update_item_price(trnsct_123):
    # a function for user to change price of item
    
    try:
        item = input('\nMasukkan nama item: ')
        price = float(input('Masukkan harga item baru: '))
        trnsct_123.update_item_price(item, price)
        print(f'Harga {item} telah diganti menjadi sebanyak {price}/item')

    except ValueError:  # error if price is not a number
        print(f'Format tidak sesuai!')

    except KeyError:  # error if item name is not in list
        print(f'Tidak ada nama item {item} di daftar transaksi!')
        
    finally:
        print(f'Shopping cart: {trnsct_123.shopping_list}\n')
        
def delete_item(trnsct_123):
    # a function for user to remove an item
    item = input('\nMasukkan nama item yang ingin dihapus: ')
        
    try:
        trnsct_123.delete_item(item)
        print(f'Item {item} telah dihapus!')

    except KeyError:  # error if item name is not in list
        print(f'Tidak ada nama item {item} di daftar transaksi!')
        
    finally:
        print(f'Shopping cart: {trnsct_123.shopping_list}\n')
        
def reset_transaction(trnsct_123):
    # a function for user to remove all items from shopping list
    
    # warning message before removing all items
    want_to_reset = input('\nIngin me-reset transaksi? Ketik 1 jika iya, 0 jika tidak: ')

    if want_to_reset == '1':
        trnsct_123.reset_transaction()
        print(f'Transaksi Anda telah di-reset!')
    elif want_to_reset == '0':
        pass
    else:
        print(f'Perintah Anda tidak sesuai dengan ketentuan!')
        
    print(f'Shopping cart: {trnsct_123.shopping_list}\n')
        
def check_order(trnsct_123):
    # a function for user to check all current orders
    print(f'\nDaftar sementara transaksi Anda:')
    trnsct_123.check_order()
    print('')
    
def total_price(trnsct_123):
    # a function for user to check total price
    print(f'\nShopping cart: {trnsct_123.shopping_list}')
    try:
        print(f'Total harga akhir: Rp{trnsct_123.total_price():,} (sudah termasuk diskon {trnsct_123.discount_rate*100}%)\n')
    except:
        print(f'Anda belum berbelanja apa-pun!\n')