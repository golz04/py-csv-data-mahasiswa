import csv
listNim = []
listNama = []
# disini terdapat fungsi import csv yang berarti menambahkan/memasukkan/mengikutsertakan suatu file yang berekstensi .csv yang nantinya kita dapat menggunakan beberapa fungsi seperti reader, writer, dll.
# disini juga terdapat 2 variabel listNim dan listNama yang bertipe data array yang berfungsi untuk menampung data

def runApp():
    try:
        with open('DaftarNama.csv') as csv_file:
            cmdRead = csv.reader(csv_file, delimiter=";")
            for listData in cmdRead:
                if(listData):
                    listNim.append(listData[0])
                    listNama.append(listData[1].lower())
    except ValueError:
        print("Terjadi Kesalahan")
        print(ValueError)
# pada function runApp() terdapat fungsi try catch yang berfungsi sebagai penangkal kesalahan. jadi apabila terjadi error pada program ini maka program ini tidak akan langsung keluar / force close, tetapi akan menampilkan errornya
# lalu disini terdapat with open yang berfungsi untuk membuka file 'DaftarNama.csv'
# cmdRead disini merupakan variabel yang berfungsi untuk membaca file 'DaftarNama.csv'
# disini juga terdapat perulangan menggunakan looping for yang berfungsi untuk melakukan pengulangan data dang memasukkan data yang berada pada file 'DaftarNama.csv' kedalam variabel listNim dan listNama
    
def getData():
    try:
        print("---------------------------------")
        print("o> Data Mahasiswa")
        print("NIM Mahasiswa \t | Nama Mahasiswa")
        print("---------------------------------")
        countNim = len(listNim)
        countNama = len(listNama)
        checkData = int((countNim+countNama) / 2)
        if(countNim == countNama):
            for i in range(checkData):
                print("{} \t | {}".format(listNim[i], listNama[i]))
        else :
            print("Terjadi Kesalahan Data Pada file.csv")
    except ValueError:
        print("Terjadi Kesalahan")
        print(ValueError)
# pada function getData() terdapat fungsi try catch yang berfungsi sebagai penangkal kesalahan. jadi apabila terjadi error pada program ini maka program ini tidak akan langsung keluar / force close, tetapi akan menampilkan errornya
# disini terdapat variabel countNim, countNama, checkData yang berfungsi sebagai validasi data pada listNim dan listNama, maksud dari validasi disini adalah jumlah pada listNim harus sama dengan listNama, karena 1 nim = 1 nama, apabila jumlah NIM lebih banyak dari jumlah Nama atau sebaliknya, maka akan menampilkan pesan kesalahan
# disini juga terdapat looping for yang berfungsi sebagai menampilkan data nim dan nama mahasiswa
    
def addData():
    try:
        nim = input("Masukkan NIM :")
        nama = " "+input("Masukkan Nama :")
        nama.lower()
        if (nim!=""  and nama!="" and nama!=" "):
            listNim.append(nim)
            listNama.append(nama)
            print("Berhasil Menambahkan Data!")
        else:
            print("Gagal Menambahkan Data !")
            print("Data Tidak Boleh Kosong !")
    except ValueError:
        print("Terjadi Kesalahan")
        print(ValueError)
# pada function addData() terdapat fungsi try catch yang berfungsi sebagai penangkal kesalahan. jadi apabila terjadi error pada program ini maka program ini tidak akan langsung keluar / force close, tetapi akan menampilkan errornya
# disini terdapat validasi apabila menambahkan nama dan nim kedua data tersebut wajib diisi dan tidal boleh ada yang kosong

def findBinaryNim():
    listTempNimNama = []
    countNim = len(listNim)
    countNama = len(listNama)
    checkData = int((countNim+countNama) / 2)
    if(countNim == countNama):
        for i in range(checkData):
            listTempNimNama.append([listNim[i], listNama[i]])
    for w in range(len(listTempNimNama)):
        for x in range(len(listTempNimNama)-1):
            if(listTempNimNama[x][0] > listTempNimNama[x+1][0]):
                listTempNimNama[x],listTempNimNama[x+1] = listTempNimNama[x+1],listTempNimNama[x]
    keyword = input("Masukkan [NIM] yang ingin dicari : ")
    if(keyword != ""):
        try:
            countKey = 0
            top = 0
            bot = len(listTempNimNama)-1
            cek = bot//2
            mid = (top+bot)//2
            nextmid = (top+bot)//2
            if(str(listTempNimNama[mid][0]) <= keyword):
                countMid=mid
                while(countMid<=bot):
                    if(keyword in listTempNimNama[countMid][0]):
                        countKey+=1
                        print("NIM \t : {}".format(listTempNimNama[countMid][0]))
                        print("Nama\t :{}".format(listTempNimNama[countMid][1]))
                    countMid+=1
            elif(str(listTempNimNama[nextmid][0]) > keyword):
                countMid=nextmid
                while(countMid>=top):
                    if(keyword in listTempNimNama[countMid][0]):
                        countKey+=1
                        print("NIM \t : {}".format(listTempNimNama[countMid][0]))
                        print("Nama\t :{}".format(listTempNimNama[countMid][1]))
                    countMid-=1
        except:
            print("---------------------------------------------------------")
        if(countKey != 0):
            print("Data ditemukan dengan kata kunci '{}' Sebanyak '{}' data.".format(keyword,countKey))
        else:
            print("Data Tidak Ditemukan !")
    else:
        print("Gagal Mencari Data !")
        print("Data Tidak Boleh Kosong !")

def findBinaryNama():
    listTempNamaNim = []
    countNim = len(listNim)
    countNama = len(listNama)
    checkData = int((countNim+countNama) / 2)
    if(countNim == countNama):
        for i in range(checkData):
            listTempNamaNim.append([listNama[i], listNim[i]])
    for w in range(len(listTempNamaNim)):
        for x in range(len(listTempNamaNim)-1):
            if(listTempNamaNim[x][0] > listTempNamaNim[x+1][0]):
                listTempNamaNim[x],listTempNamaNim[x+1] = listTempNamaNim[x+1],listTempNamaNim[x]
    keyword = input("Masukkan [Nama] yang ingin dicari : ")
    if(keyword != ""):
        try:
            countKey = 0
            top = 0
            bot = len(listTempNamaNim)-1
            cek = bot//2
            mid = (top+bot)//2
            nextmid = (top+bot)//2
            if(str(listTempNamaNim[mid][0]) < keyword):
                countMid=mid
                while(countMid<=bot):
                    if(keyword in listTempNamaNim[countMid][0]):
                        countKey+=1
                        print("NIM \t : {}".format(listTempNamaNim[countMid][1]))
                        print("Nama\t :{}".format(listTempNamaNim[countMid][0]))
                    countMid+=1
            elif(str(listTempNamaNim[nextmid][0]) > keyword):
                countMid=nextmid
                while(countMid>=top):
                    if(keyword in listTempNamaNim[countMid][0]):
                        countKey+=1
                        print("NIM \t : {}".format(listTempNamaNim[countMid][1]))
                        print("Nama\t :{}".format(listTempNamaNim[countMid][0]))
                    countMid-=1
        except:
            print("---------------------------------------------------------")
        if(countKey != 0):
            print("Data ditemukan dengan kata kunci '{}' Sebanyak '{}' data.".format(keyword,countKey))
        else:
            print("Data Tidak Ditemukan !")
    else:
        print("Gagal Mencari Data !")
        print("Data Tidak Boleh Kosong !")

def findDataLinear():
    try:
        keyword = input("Masukkan [NIM/Nama] yang ingin dicari :")
        countKey = 0
        if(keyword != ""):
            for i in range(len(listNim)):
                if(keyword in listNim[i]):
                    countKey+=1
                    print("NIM \t : {}".format(listNim[i]))
                    print("Nama \t :{}".format(listNama[i]))
                    print("-------------------------------")
                elif(keyword in listNama[i]):
                    countKey+=1
                    print("NIM \t : {}".format(listNim[i]))
                    print("Nama \t :{}".format(listNama[i]))
                    print("-------------------------------")
            if(countKey != 0):
                print("Data ditemukan dengan kata kunci '{}' Sebanyak '{}' data.".format(keyword,countKey))
            else:
                print("Data Tidak Ditemukan !")
        else:
            print("Gagal Mencari Data !")
            print("Data Tidak Boleh Kosong !")
    except:
        print("Data Tidak Ada")
    
def deleteData():
    try:
        delete = input("Masukkan NIM Mahasiswa yang akan dihapus :")
        if(delete in listNim):
            indexDelete = listNim.index(delete)
            print("NIM \t : {}".format(listNim[indexDelete]))
            print("Nama \t :{}".format(listNama[indexDelete]))
            print("-------------------------------")
            validasi = input("Apakah anda ingin menghapus data ini ? [ya/tidak] : ")
            if(validasi=="ya" or validasi=="Ya" or validasi=="y" or validasi=="Y"):
                listNim.pop(indexDelete)
                listNama.pop(indexDelete)
                print("Data Berhasil Dihapus !")
            else:
                deleteData()
        else:
            print("Data Tidak Dihapus !")
            print("NIM Tidak Ditemukan !")
    except ValueError:
        print("Terjadi Kesalahan")
        print(ValueError)
# pada function deleteData() terdapat fungsi try catch yang berfungsi sebagai penangkal kesalahan. jadi apabila terjadi error pada program ini maka program ini tidak akan langsung keluar / force close, tetapi akan menampilkan errornya
# disini dalam penghapusan data harus menggunakan NIM saja, karena apabila kita menghapus data menggunakan nama, sedangkan nama bisa jadi lebih dari 1 nama yang sama, maka disini saya menggunakan NIM selain itu ketika mencari nim harus lengkap
# karena hapus data ini sangat sensitif maka dari itu setelah mencari nim disini akan menampilkan data mahasiswa yang ingin dihapus, dan akan menampilkan pesan pesan ingin menghapus / tidak

def sortingData():
    try:
        listTempSorting = []
        countNim = len(listNim)
        countNama = len(listNama)
        checkData = int((countNim+countNama) / 2)
        if(countNim == countNama):
            for i in range(checkData):
                listTempSorting.append([listNim[i], listNama[i]])
            print("-----------------------------")
            print("1. Urut Berdasarkan NIM (0-9)")
            print("2. Urut Berdasarkan NIM (9-0)")
            print("3. Urut Berdasarkan Nama (A-Z)")
            print("4. Urut Berdasarkan Nama (Z-A)")
            print("-----------------------------")
            pilih = input("Masukkan Pilihan Anda (1-4) : ")
            if(pilih == "1"):
                for x in range(len(listTempSorting)):
                    for y in range(len(listTempSorting)-1):
                        if(listTempSorting[y][0] > listTempSorting[y+1][0]):
                            listTempSorting[y],listTempSorting[y+1] = listTempSorting[y+1],listTempSorting[y]
                print("=========Data Mahasiswa=========")
                print("========Sorting NIM(0-9)========")
                for z in range(len(listTempSorting)):
                    print("NIM \t : {}".format(listTempSorting[z][0]))
                    print("Nama \t :{}".format(listTempSorting[z][1]))
                    print("--------------------------------")
                loop = 0
                lTemp = len(listTempSorting)-1
                while(loop<=lTemp):
                    listNim[loop] = listTempSorting[loop][0]
                    listNama[loop] = listTempSorting[loop][1]
                    loop+=1
            elif(pilih == "2"):
                for x in range(len(listTempSorting)):
                    for y in range(len(listTempSorting)-1):
                        if(listTempSorting[y][0] < listTempSorting[y+1][0]):
                            listTempSorting[y],listTempSorting[y+1] = listTempSorting[y+1],listTempSorting[y]
                print("=========Data Mahasiswa=========")
                print("========Sorting NIM(9-0)========")
                for z in range(len(listTempSorting)):
                    print("NIM \t : {}".format(listTempSorting[z][0]))
                    print("Nama \t :{}".format(listTempSorting[z][1]))
                    print("--------------------------------")
                loop = 0
                lTemp = len(listTempSorting)-1
                while(loop<=lTemp):
                    listNim[loop] = listTempSorting[loop][0]
                    listNama[loop] = listTempSorting[loop][1]
                    loop+=1
            elif(pilih == "3"):
                for x in range(len(listTempSorting)):
                    for y in range(len(listTempSorting)-1):
                        if(listTempSorting[y][1] > listTempSorting[y+1][1]):
                            listTempSorting[y],listTempSorting[y+1] = listTempSorting[y+1],listTempSorting[y]
                print("=========Data Mahasiswa=========")
                print("========Sorting Nama(A-Z)========")
                for z in range(len(listTempSorting)):
                    print("NIM \t : {}".format(listTempSorting[z][0]))
                    print("Nama \t :{}".format(listTempSorting[z][1]))
                    print("--------------------------------")
                loop = 0
                lTemp = len(listTempSorting)-1
                while(loop<=lTemp):
                    listNim[loop] = listTempSorting[loop][0]
                    listNama[loop] = listTempSorting[loop][1]
                    loop+=1
            elif(pilih == "4"):
                for x in range(len(listTempSorting)):
                    for y in range(len(listTempSorting)-1):
                        if(listTempSorting[y][1] < listTempSorting[y+1][1]):
                            listTempSorting[y],listTempSorting[y+1] = listTempSorting[y+1],listTempSorting[y]
                print("=========Data Mahasiswa=========")
                print("========Sorting Nama(Z-A)========")
                for z in range(len(listTempSorting)):
                    print("NIM \t : {}".format(listTempSorting[z][0]))
                    print("Nama \t :{}".format(listTempSorting[z][1]))
                    print("--------------------------------")
                loop = 0
                lTemp = len(listTempSorting)-1
                while(loop<=lTemp):
                    listNim[loop] = listTempSorting[loop][0]
                    listNama[loop] = listTempSorting[loop][1]
                    loop+=1
            else:
                print("Inputan hanya boleh angka 1-4 saja !")
        else :
            print("Terjadi Kesalahan Data Pada file.csv")
    except ValueError:
        print("Terjadi Kesalahan")
        print(ValueError)
# pada function sortingData() terdapat fungsi try catch yang berfungsi sebagai penangkal kesalahan. jadi apabila terjadi error pada program ini maka program ini tidak akan langsung keluar / force close, tetapi akan menampilkan errornya
# disini terdapat variabel listTempSorting yang berfungsi sebagai variabel temporer untuk menampung data listNim dan listNama
# disini menggunakan logika bubbleSort, karena mudah dipahami
# terdapat looping for x dan y yang nantinya berfungsi sebagai penghitung data dan pembanding
# terdapat kondisi if else. jika data pada array ke-y lebih besar daripada data array ke-y+1, maka posisi data tersebut akan ditukar

def exitApp():
    try:
        with open('DaftarNama.csv', 'w') as csv_file:
            cmdWrite = csv.writer(csv_file, delimiter=";")
            countNim = len(listNim)
            countNama = len(listNama)
            checkData = int((countNim+countNama) / 2)
            if(countNim == countNama):
                for i in range(checkData):
                    cmdWrite.writerow([listNim[i],listNama[i]])
            else :
                print("Terjadi Kesalahan Data Pada file.csv")
    except ValueError:
        print("Terjadi Kesalahan")
        print(ValueError)
# pada function exitApp() terdapat fungsi try catch yang berfungsi sebagai penangkal kesalahan. jadi apabila terjadi error pada program ini maka program ini tidak akan langsung keluar / force close, tetapi akan menampilkan errornya
# disini terdapat with open yang berfungsi memanggil file 'DaftarNama.csv' dan juga terdapat huruf 'w' yang berarti mode write
# selain itu juga terdapat variabel cmdWrite yang berfungsi sebagai menulis / menambahkan data ke dalam file 'DaftarNama.csv'
# disini juga ada variabel untuk mengecek data pada listNim dan listNama
# terdapat looping for untuk menambahkan data yang berada di listNim dan listNama untuk di kirim ke file 'DaftarNama.csv'

try:
    runApp() #memanggil function runApp()
    coreLoop = True #mendeklarasikan variabel coreLoop dengan default value True
    while(coreLoop == True): #looping while terjadi ketika variabel coreLoop bernilai True
        print("|============================|")
        print("|---Program Data Mahasiswa---|")
        print("|============================|")
        print("|1. Tambah Data Mahasiswa    |")
        print("|2. Lihat Data Mahasiswa     |")
        print("|3. Hapus Data Mahasiswa     |")
        print("|4. Cari Data Mahasiswa      |")
        print("|5. Sorting Data Mahasiswa   |")
        print("|6. Keluar & Simpan          |")
        print("|----------------------------|")
        menu = input("Masukkan Pilihan Anda (1-6) : ") #variabel menu yang berupa inputan
        if(menu == "1"):
            addData() #memanggil function adadData()
        elif(menu == "2"):
            getData() #memanggil function getData()
        elif(menu == "3"):
            deleteData() #memanggil function deleteData()
        elif(menu == "4"):
            print("--------------------------------------")
            print("1. Cari Data Menggunakan Binary Search")
            print("2. Cari Data Menggunakan Linear Search")
            print("--------------------------------------")
            menuFind = input("Masukkan Pilihan Anda (1-2) : ")
            if(menuFind == "1"):
                print("-----------------------")
                print("1. Cari berdasarkan NIM")
                print("2. Cari berdasarkan Nama")
                print("-----------------------")
                menuBy = input("Masukkan Pilihan Anda (1-2) : ")
                if(menuBy == "1"):
                    findBinaryNim()
                elif(menuBy == "2"):
                    findBinaryNama()
                else:
                    print("Inputan hanya boleh angka 1-2 saja !")
            elif(menuFind == "2"):
                findDataLinear() #memanggil function findDataLinear()
            else:
                print("Inputan hanya boleh angka 1-2 saja !")
        elif(menu == "5"):
            sortingData() #memanggil function sortingData()
        elif(menu == "6"):
            exitApp() #memanggil function exitApp()
            print("=============================================================")
            print("===Terima Kasih Telah Menggunakan Program Sederhana Ini :)===")
            print("=============================================================")
            coreLoop = False #merubah nilai variabel coreLoop menjadi False
        else:
            print("Inputan hanya boleh angka 1-6 saja !")
except ValueError:
    print("Terjadi Kesalahan")
    print(ValueError)