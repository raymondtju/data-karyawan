def pilihan():
  print("=" * 36)
  print("\t  PT. Pelangi Indah")
  print("=" * 36)
  print("\t    | MAIN PAGE |\n")
  print("1. Input data karyawan")
  print("2. Lihat data per Karyawan")
  print("3. Rules Perusahaan")
  print("4. Lihat semua data")
  print("0. Exit Program\n")
  print("=" * 36)


#tempat menginput atau menampung data
listKaryawan = []
listTahun = []
listIzin = []
listAbsen = []
listProject = []
listKomisi = []
listLembur = []

gajiSenior = 8000000
gajiJunior = 4000000

#Sebagai Halaman Utama
pilihan()
choice = int(input("Pilih : "))
print("-" * 36, "\n")

#sebagai Option untuk fungsi-fungsi yang ada
while choice != 0:
  if choice == 1:
    print("=" * 36)
    print("      + INPUT DATA KARYAWAN +")
    print("=" * 36, "\n")
    namaKaryawan = str(input("Masukkan nama karyawan \t: "))
    tahunKerja = int(input("Tahun Kerja \t\t\t: "))
    totalIzin = int(input("Total Izin (DAYS)\t\t: "))
    totalAbsen = int(input("Total Absen (DAYS)\t\t: "))
    lembur = int(input("Total Lembur (HOUR) \t: "))
    komisi = 0
    project = int(input("Jumlah projek yang diselesaikan : "))
    while project != 0:
      inputKomisi = int(input("Komisi per project \t\t: "))
      komisi += inputKomisi
      project -= 1
    print("-" * 36, "\n")
    #penjelasan = jika memilih 1 maka kita dapat memasukkan data karyawan yang di perlukan,pada bagian projek digunakan pengulangan dimana selama jumlah projek bukan 0. Maka bisa mendapat komisi yang akan bertambah sesuai dengan jumlah project dan pengulangan tersebut akan diulang sebanyak jumlah project yang dimasukkan.

    listKaryawan.append(namaKaryawan)
    listTahun.append(tahunKerja)
    listIzin.append(totalIzin)
    listAbsen.append(totalAbsen)
    listProject.append(project)
    listKomisi.append(komisi)
    listLembur.append(lembur)
    pilihan()
    choice = int(input("Pilih : "))
    print("-" * 36, "\n")

  #Choice 2 sebagai tempat untuk melihat dan mengedit data karyawan yang telah di input sebelumnya
  elif choice == 2:
    if (len(listKaryawan) == 0):  #AMAN AO BANGG ok bang
      pilihan()
      choice = int(input("Pilih : "))
    else:
      print("=" * 36)
      print("\t * DATA KARYAWAN *")
      print("=" * 36, "\n")

      for x in listKaryawan:
        print(listKaryawan.index(x) + 1, end="")  #1
        print(".", x)  #1.Ceo
      print("-" * 36)
      #LEN sebagai fungsi untuk menentukan panjang data yang ada di listKaryawan
      if len(listKaryawan) > 0:
        lihatData = int(input(("Masukkan no.urut karyawan : ")))
        print("-" * 37)
        print("Nama karyawan \t\t: ", listKaryawan[lihatData - 1])
        print("Tahun kerja \t\t: ", listTahun[lihatData - 1])
        if (2022 - listTahun[lihatData - 1] >= 5):
          print("Kesenioritasan \t\t:  Senior")
        else:
          print("Kesenioritasan \t\t:  Junior")
        print("Total izin (DAYS)\t: ", listIzin[lihatData - 1])
        print("Total absen (DAYS)\t: ", listAbsen[lihatData - 1])
        print("Total lembur\t\t: ", listLembur[lihatData - 1])
        print("Total Komisi\t\t:  Rp. ", listKomisi[lihatData - 1])
        print("-" * 37)
        print("     + INFORMASI GAJI KARYAWAN +")
        print("-" * 37)
        if (2022 - listTahun[lihatData - 1] >= 5):
          print("Gaji Kotor\t\t:  Rp. ", gajiSenior)
          print("Izin\t\t\t: -Rp. ", listIzin[lihatData - 1] * 20000)
          print("Absen\t\t\t: -Rp. ", listAbsen[lihatData - 1] * 40000)
          print("Lembur\t\t\t: +Rp. ", listLembur[lihatData - 1] * 15000)
          print("Komisi\t\t\t: +Rp. ", listKomisi[lihatData - 1])
          gajiSenior = gajiSenior - (
            listAbsen[lihatData - 1] * 40000 + listIzin[lihatData - 1] * 20000
          ) + (listLembur[lihatData - 1] * 15000) + listKomisi[lihatData - 1]
          print("Gaji Bersih \t:  Rp. ", gajiSenior)
        else:
          print("Gaji Kotor\t\t:  Rp. ", gajiJunior)
          print("Izin\t\t\t: -Rp. ", listIzin[lihatData - 1] * 20000)
          print("Absen\t\t\t: -Rp. ", listAbsen[lihatData - 1] * 40000)
          print("Lembur\t\t\t: +Rp. ", listLembur[lihatData - 1] * 15000)
          print("Komisi\t\t\t: +Rp. ", listKomisi[lihatData - 1])
          gajiJunior = gajiJunior - (
            listAbsen[lihatData - 1] * 40000 + listIzin[lihatData - 1] * 20000
          ) + (listLembur[lihatData - 1] * 15000) + listKomisi[lihatData - 1]
          print("Gaji Bersih \t:  Rp. ", gajiJunior)

        print("-" * 37)
        edit = str(
          input("Apakah ingin mengedit data karyawan ? ( yes / no ) : "))
        #untuk melanjutkan atau tidak choice 2 ini
        #JIKA YES MAKA AKAN KEMBALI KE MAIN MENU
        while (edit != "yes" or edit != "no"):
          if edit == "yes":
            print("-" * 37)
            editTotalIzin = int(input("Edit Total Izin (DAYS)  : "))
            editTotalAbsen = int(input("Edit Total Absen (DAYS) : "))
            editHourLembur = int(input("Edit Total Lembur (HOUR) : "))
            listIzin[lihatData - 1] = editTotalIzin
            listAbsen[lihatData - 1] = editTotalAbsen
            listLembur[lihatData - 1] = editHourLembur
            print("-" * 37)
            print("UPDATE CONFIRMED!\n")
            print("-" * 37)
            print("Nama karyawan \t: ", listKaryawan[lihatData - 1])
            print("Tahun Kerja \t: ", listTahun[lihatData - 1])
            print("Total lembur \t: Rp. ", listLembur[lihatData - 1] * 15000)
            print("Total Izin (DAYS)\t: ", listIzin[lihatData - 1])
            print("Total Absen (DAYS)\t: ", listAbsen[lihatData - 1])
            print("Total Komisi \t: Rp. ", listKomisi[lihatData - 1])
            print("-" * 37, '\n')
            break
            #jika no maka akan kembali ke main page
          elif edit == "no":
            break
            #HARUS BERUPA YES/NO JIKA TIDAK MAKA AKAN DIULANGI KEMBALI
          else:
            edit = str(
              input("Apakah ingin mengedit data karyawan ? ( yes / no ) : "))

        pilihan()
        choice = int(input("Pilih : "))

        gajiSenior = 8000000
        gajiJunior = 4000000

    # else:
    #   choice = 1
#Choice 3 sebagai Option untuk melihat Rules/Peraturan-peraturan Perusahaan
  elif choice == 3:
    print("=" * 59)
    print("||\t\t        | RULES PT. PELANGI INDAH |              ||")
    print("=" * 59, '\n')
    print("_" * 59)
    print("| \t         ** KERJA DARI SENIN - JUMAT **               |")
    print("_" * 59)
    print("| \t\t        ** TOTAL KERJA 8 JAM **                   |")
    print("_" * 59)
    print("|    ** TERLAMBAT 5 MENIT POTONG GAJI Rp. 15.000 **       |")
    print("_" * 59)
    print("|** PROJEK LEWAT DEADLINE DIPOTONG KOMISI 25% / MINGGU ** |")
    print("_" * 59)
    print("| ** SETIAP KALI IZIN 1 HARI POTONG GAJI Rp. 20.000 **    |")
    print("_" * 59)
    print("| ** SETIAP KALI ABSEN 1 HARI POTONG GAJI Rp. 40.000 **   |")
    print("_" * 59, '\n')

    backMenu = str(input("kembali ke halaman menu? ( yes / no ) : "))
    if (backMenu == "yes"):
      print("\n")
      pilihan()
      choice = int(input("Pilih : "))
    elif (backMenu == "no"):
      print("\n\t      ~~Sampai Jumpa dan Kembali Lagi~~")
      print("\t   ! Project Tugas 'Pemrograman Komputer' !")
      print("_" * 54)
      print("| Raymond Tju | Jhonsen | Devon Loen | Cecilia Ongso |")
      print("-" * 54)
      break
    else:
      backMenu = str(input("kembali ke halaman menu? ( yes / no ) : "))

#Choice 4 sebagai Option untuk melihat semua data karyawan yang ada di dalam perusahaan
  elif choice == 4:
    lens = len(listKaryawan)
    print("=" * 50)
    print("\t DATA SEMUA KARYAWAN | PT. PELANGI INDAH")
    print("=" * 50)
    for x in range(len(listKaryawan)):
      # len = listKaryawan.index(x)
      # print(listKaryawan.index(x) + 1, end="")  #1
      # print(".", x)
      print("Nama karyawan \t\t:  ", listKaryawan[x - 1])
      print("Tahun Kerja \t\t:  ", listTahun[x - 1])
      print("Total Izin (DAYS)\t:  ", listIzin[x - 1])
      print("Total Absen (DAYS)\t:  ", listAbsen[x - 1])
      print("Total lembur \t\t: Rp. ", listLembur[x - 1] * 15000)
      print("Total Komisi \t\t: Rp. ", listKomisi[x - 1])
      print("-" * 48, '\n')
    backMenu = str(input("kembali ke halaman menu? ( yes / no ) : "))
    if (backMenu == "yes"):
      print("\n")
      pilihan()
      choice = int(input("Pilih : "))
    elif (backMenu == "no"):
      print("\n~~Sampai Jumpa dan Kembali Lagi~~")
      print("! Project Tugas 'Pemrograman Komputer' !")
      print("_" * 54)
      print("| Raymond Tju | Jhonsen | Devon Loen | Cecilia Ongso |")
      print("_" * 54)
      break
    else:
      backMenu = str(input("kembali ke halaman menu? ( yes / no ) : "))
  else:
    break
