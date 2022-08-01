from os import system

Item = []
Buy = []

def showItem():
    for i in range(len(Item)):
        number = i+1
        print(number, ".", end=' ')
        for j in range(len(Item[i])):
            if j == 0:
                print(Item[i][j], end=' ')
            else:
                print("Rp.", f"{Item[i][j]:,}", end=' ')
        print()
        
def showBuy():
    for i in range(len(Buy)):
        number = i+1
        print(number, ".", end=' ')
        for j in range(len(Buy[i])):
            if j == 0:
                print(Buy[i][j], end=' ')
            elif j == 1:
                print(Buy[i][j], "PCS", end=' ')
            else:
                print("Rp.", f"{Buy[i][j]:,}", end=' ')
        print()

loop = 'y'
while loop == 'y':
    system('cls')
    print("Selamat Datang Di Shopedia")
    print("Ingin login Menggunakan?")
    print("Admin / Buyer")
    print('Untuk Keluar Dari Aplikasi Ketik "-1 / Quit"')
    print("")
    page = input("Masukan Pilihan : ")
    
    # Admin Menu
    if page == 'admin' or page == 'ADMIN' or page == 'Admin':
        loop1 = 'y'
        while loop1 == 'y':
            system('cls')
            print("Welcome Admin")
            print("1. Tambah Barang")
            print("2. Tampilkan Barang")
            print("3. Hapus Semua Data")
            print("4. Logout")
            choice = input("Masukkan Pilihan Anda : ")
            system('cls')
            # Create Item
            if choice == '1':
                loop2 = 'y'
                while loop2 == 'y' or loop2 == 'Y':
                    row = []
                    for j in range(2):
                        if j == 0:
                            element = input("Nama Barang \t: ")
                            row.append(element)
                        else:
                            element = int(input("Harga Barang \t: "))
                            row.append(element)
                    loop2 = input("Ingin Menambah Barang Lagi? (Y/N) : ")
                    Item.append(row)
                    
            # Read Item
            elif choice == '2':
                if not Item:
                    print("Data Barang Kosong")
                else:
                    showItem()
                system('pause')
                
            # Delete Item
            elif choice == '3':
                Item = []
                print ("Barang Telah Dihapus")
                system("pause")
                
            # Exit from Admin Page
            elif choice == '4':
                loop1 = "n"
                
            # Wrong Input
            else:
                print('WARNING!')
                print('INPUT TIDAK VALID')
                system('pause')

    # Buyer Menu
    elif page == 'buyer' or page == 'Buyer' or page == 'BUYER':
        system("cls")
        loop3 = 'y'
        while loop3 == 'y':
            print("Welcome Buyer")
            print("1. Beli Barang")
            print("2. Logout")
            choice = input("Masukkan Pilihan Anda : ")
            system ('cls')
            # Buy Item
            if choice == '1' :
                loop4 = 'y'
                while loop4 == 'y' or loop4 == 'Y':
                    print("Daftar Menu")
                    showItem()
                
                    selectItem = int(input("Pilih Nomor Barang : "))
                    selectItem = selectItem-1
                    
                    print("Barang Yang Ingin Anda Beli Adalah", Item[selectItem][0], "Dengan Harga", Item[selectItem][1])
                    totalBuy = int(input("Jumlah Barang Yang Ingin Dibeli : "))
                    price = Item[selectItem][1]
                    totalB_Item = jumlahBeli*price
                    print("Total Harga Anda Membeli", Item[selectItem][1], "Adalah", totalB_Item)
                    
                    row = []
                    for j in range(3):
                        if j == 0:
                            row.append(Item[selectItem][0])
                        elif j == 1:
                            row.append(jumlahBeli)
                        else:
                            row.append(totalB_Item)
                    Buy.append(row)
                   
                    loop4 = input("Apakah Anda Ingin Membeli Lagi? (Y/N) : ")
                    system("cls")
                    if loop4 == 'n':
                        # After Buy
                        loop5 = 'y'
                        while loop5 == 'y':
                            print("1. Beli Lagi? ")    
                            print("2. Keranjang")
                            print("3. Bayar")                    
                            choice= input("Masukan Pilihan Anda : ")
                            system("cls")
                            # Buy Again
                            if choice== '1':
                                loop5 = 'n'

                            # Show the Cart
                            elif choice== '2':   
                                showBuy()    
                                system('pause')
                                system("cls")

                            # Buying Process
                            elif choice== '3':
                                showBuy()
                                print()
                                total = 0
                                for i in range(len(Buy)):
                                    total += Buy[i][2]
                                print("Total \t\t:", total)
                                pay = int(input("Bayar \t\t: "))
                                print("Kembalian \t: ", pay-total)
                                loop5 = 'n'
                                system("pause")
                                system("cls")
                                
                            # Wrong Input                              
                            else:
                                loop5 = 'y'
                                print('WARNING!')
                                print('INPUT TIDAK VALID')
                                system('pause')
                                system('cls')
                                
            else:
                loop3 = 'n'
    elif page == '-1' or page == 'quit' or page == 'Quit':
        break
    
    else:
        system('cls')
        print('WARNING!')
        print('INPUT TIDAK VALID')
        system('pause')