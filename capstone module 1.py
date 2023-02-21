list_kontak = [
    ['Jay','Pradhana','08121133905','PT Medikami','Bandung'],
    ['Fawwaz','Sanjaya','08199245178','PT Rungkad', 'Surabaya'],
    ['Tasha','Zefanya','08394133098','PT Reparodi','Jakarta'],
    ['Utari', 'Devina','08376212390','PT Sri Ratu','Semarang']
]

# function mencari index tertentu dalam list
def get_sublists(lists, keyword):
    sublists = []
    for lst in lists:
        if keyword in lst:
            sublists.append(lst)
    return sublists

# function menu utama
def menu_utama():
   
    print('''
    -- Data Kontak CEO Perusahaan di Pulau Jawa -- \n
    Menu Utama:
    1. Daftar Kontak
    2. Tambah Kontak
    3. Ubah Kontak
    4. Hapus Kontak
    5. Exit 
    ''')
    
    pilihan_menu = input('Pilih opsi menu yang ingin dijalankan [1-5]: ')

    if pilihan_menu == '1':
        read_data()
    elif pilihan_menu == '2':
        create_data()
    elif pilihan_menu == '3':
        update_data()
    elif pilihan_menu == '4':
        delete_data()
    elif pilihan_menu == '5':
        keluar = input('Apakah anda yakin ingin keluar? [Y/N]: ').upper()
        if keluar == 'Y':
            print('\n-- Terima Kasih --\n')
            quit()
        elif keluar == 'N':
            menu_utama()
        else:
            print('Input yang telah dimasukkan salah.')
            menu_utama()
    else:
        print('Input yang telah dimasukkan salah.\n')
        menu_utama()

# function read data
def read_data():
   
    while True:
        # print list daftar kontak
        print('''
        -- Daftar Kontak --\n
        1. Tampilkan seluruh data kontak
        2. Informasi kontak tertentu
        3. Kembali ke menu utama''')

        read_input = input('\nPilih Opsi Daftar Kontak [1-3]: ')

        # input 1 akan memperlihatkan seluruh data
        if read_input == '1':
            print('-- Daftar Kontak Lengkap --\n')
            print('Nama Depan \t| Nama Belakang \t| No. Telp \t| Perusahaan \t| Lokasi')

            # for loop untuk display seluruh data kontak menggunakan function range dan length
            for i in range(len(list_kontak)):
                print(f'{list_kontak[i][0]} \t\t| {list_kontak[i][1]} \t\t| {list_kontak[i][2]} \t| {list_kontak[i][3]} \t| {list_kontak[i][4]}')
        
        # input 2 akan memperlihatkan data kontak spesifik
        elif read_input == '2':
            nama_depan = input('\nMasukkan nama depan yang dicari: ').capitalize()
            print(f'\nKontak dengan Nama Depan: {nama_depan}\n')

            # ini dipakai untuk mempermudah pencarian index, berisi list dengan key yang kita cari di dalam nested list
            nama_list = get_sublists(list_kontak, nama_depan)
            
            # for loop untuk display data kontak yang telah diinput
            for listnama in nama_list:
                print(f'Nama Depan: {listnama[0]} | Nama Belakang: {listnama[1]} | No. Telp: {listnama[2]} | Perusahaan: {listnama[3]} | Lokasi: {listnama[4]}')

            # memakai function any untuk cek apakah input ada di dalam list 
            if not any(nama_list):
                print(f'Tidak ada nama {nama_depan} dalam Daftar Kontak.\n')
                read_data()          
                
        elif read_input == '3':
            menu_utama_back(read_data)
        else:
            print('\nInput yang telah dimasukkan salah.\n')
            read_data()

# function create data
def create_data():

    while True:
        print('''
        -- Tambah Daftar Kontak --\n
        1. Tambah data kontak
        2. Kembali ke menu utama''')

        create_input = input('\nPilih opsi yang ingin dijalankan [1-2]: ')

        if create_input == '1':
            nama_depan = input('\nMasukkan nama depan kontak: ').capitalize()

            nama_list = get_sublists(list_kontak, nama_depan)

            if any(nama_list):
                print(f'Nama {nama_depan} sudah ada di daftar kontak.')
            else:
                print('Belum ada kontak dengan nama tersebut, silahkan menambah detail: ')
                nama_belakang = input('Masukkan nama belakang: ').capitalize()
                no_telp = input('Masukkan nomor telepon: ')
                perusahaan = input('Masukkan nama perusahaan: ')
                lokasi = input('Masukkan lokasi: ').capitalize()

                while True:
                    confirm = input('Simpan kontak baru? [Y/N]: ').upper()

                    if confirm == 'Y':
                        list_kontak.append([nama_depan,nama_belakang,no_telp,perusahaan,lokasi])
                        print('\nKontak baru telah tersimpan. \n')

                        nama_list = get_sublists(list_kontak, nama_depan)

                        for listnama in nama_list:
                            print(f'Nama Depan: {listnama[0]} | Nama Belakang: {listnama[1]} | No. Telp: {listnama[2]} | Perusahaan: {listnama[3]} | Lokasi: {listnama[4]}')
                            create_data()

                    elif confirm == 'N':
                        create_data()

        elif create_input == '2':
            menu_utama_back(create_data)
        else:
            print('\nInput yang telah dimasukkan salah.\n')
            create_data()


# function update data
def update_data():

    while True:
        print(''' 
        -- Ubah Daftar Kontak --\n
        1. Ubah Daftar Kontak
        2. Kembali ke menu utama''')

        update_input = input('\nPilih opsi yang ingin dijalankan [1-2]: ')

        if update_input == '1':
            print('\nDaftar Kontak\n')

            for i in range(len(list_kontak)):
                print(f'{list_kontak[i][0]} \t| {list_kontak[i][1]} \t| {list_kontak[i][2]}\t| {list_kontak[i][3]}\t| {list_kontak[i][4]}')

            nama_depan = input('\nMasukkan nama depan: ').capitalize()

            nama_list = get_sublists(list_kontak, nama_depan)

            list_kolom = ['Nama Depan','Nama Belakang','No. Telp','Perusahaan','Lokasi']

            if not any(nama_list):
                print(f'Nama {nama_depan} tidak ada di dalam Daftar Kontak.')
            else:
                print(f'Nama {nama_depan} ada di dalam Daftar Kontak.')
                confirm = input('\nUbah data? [Y/N]: ').upper()

                if confirm == 'Y':
                    print(f'{list_kolom[0]} \t| {list_kolom[1]} \t| {list_kolom[2]}\t| {list_kolom[3]}\t| {list_kolom[4]}')
                    nama_kolom = list_kolom.index(input('Data yang ingin diubah: ').title())
                    data_diubah = input('Data ingin diubah menjadi: ')

                    # memakai abcde untuk mendefine value yang dicari, enumerate untuk supaya abcde sesuai dengan index data list yang dipakai
                    for idx, (a,b,c,d,e), in enumerate(list_kontak):
                        if a == nama_depan:
                            list_kontak[idx][nama_kolom] = data_diubah

                    print('\nPerubahan data telah disimpan.\n')
                    print(f'Nama Depan: {nama_list[0][0]} | Nama Belakang: {nama_list[0][1]} | No. Telp: {nama_list[0][2]} | Perusahaan: {nama_list[0][3]} | Lokasi: {nama_list[0][4]}')
                    update_data()
                elif confirm == 'N':
                    update_data()
                else:
                    print('\nInput yang telah dimasukkan salah.\n')
                    update_data()
        
        elif update_input == '2':
            menu_utama_back(update_data)
        else:
            print('Input yang telah dimasukkan salah.')
            update_data()

            
# function delete data
def delete_data():

    while True:
        print('''
        -- Menghapus Daftar Kontak --
        1. Hapus data kontak
        2. Kembali ke menu utama''')

        sub_delete_input = input('\nPilih opsi yang ingin dijalankan [1-2]: ')

        if sub_delete_input == '1':
            print('\nDaftar Kontak\n')
            
            for i in range(len(list_kontak)):
                print(f'{list_kontak[i][0]} \t| {list_kontak[i][1]} \t| {list_kontak[i][2]}\t| {list_kontak[i][3]}\t| {list_kontak[i][4]}')

            delete_input = input('\nMasukkan nama yang ingin dihapus: \n').capitalize()

            nama_list = get_sublists(list_kontak, delete_input)
            
            if not any(nama_list):
                print(f'Nama {delete_input} tidak ada di dalam Daftar Kontak.')
                delete_data()
            else:
                print(f'Nama Depan: {nama_list[0][0]} | Nama Belakang: {nama_list[0][1]} | No. Telp: {nama_list[0][2]} | Perusahaan: {nama_list[0][3]} | Lokasi: {nama_list[0][4]}')
                
                for idx, (a,b,c,d,e) in enumerate(list_kontak):
                    if list_kontak[idx][0] == delete_input:
                        list_kontak.pop(idx)
                        print(f'Data {delete_input} telah dihapus.')

        elif sub_delete_input == '2':
            menu_utama_back(delete_data)
        else:
            print('Input yang telah dimasukkan salah.')
            delete_data()

# function kembali ke menu utama
def menu_utama_back(function):
    
    back = input('\nKembali ke menu utama? [Y/N]: ').upper()

    if back == 'Y':
        menu_utama()
    elif back == 'N':
        function()
    else:
        print('\nInput yang telah dimasukkan salah.')
        function()

menu_utama()