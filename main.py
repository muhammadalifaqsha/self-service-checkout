# import class and functions
from Transaction import *
from shopping_commands import *

# Initial message
print('Selamat datang!')

trnsct_123 = Transaction()

# do this while still want to shop
while True:
    
    # Show all commands to shop
    print('Tekan\n1 jika ingin memasukkan item')
    print('2 jika ingin mengubah nama item')
    print('3 jika ingin mengubah jumlah item')
    print('4 jika ingin mengubah harga item')
    print('5 jika ingin menghapus item')
    print('6 jika ingin menghapus semua transaksi')
    print('7 jika ingin memeriksa daftar transaksi')
    print('8 jika ingin memeriksa total transaksi')
    print('9 jika ingin menyelesaikan transaksi')

    command = input('Ketikkan perintah: ')
    
    if command == '1': # input items
        add_item(trnsct_123)
        
    elif command == '2': # edit item name
        update_item_name(trnsct_123)
        
    elif command == '3': # edit item qty
        update_item_qty(trnsct_123)
        
    elif command == '4':  # edit item price
        update_item_price(trnsct_123)
        
    elif command == '5':  # remove item
        delete_item(trnsct_123)
        
    elif command == '6':  # remove all items
        reset_transaction(trnsct_123)
        
    elif command == '7': # print shopping list & price total
        check_order(trnsct_123)
        
    elif command == '8': # checking price total
        total_price(trnsct_123)
        
    elif command == '9':
        break
    
    else:  # error message if command is not compatible
        print('\nPerintah Anda tidak sesuai dengan ketentuan!\n')
            