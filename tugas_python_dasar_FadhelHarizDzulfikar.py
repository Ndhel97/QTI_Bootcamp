"""
Nama: Fadhel Hariz Dzulfikar
"""

"""
APLIKASI PARKIR SEDERHANA

input = JAM BERAPA MASUK PARKIRAN (1-12)
        PAGI ATAU MALAM?
        JAM BERAPA KELUAR PARKIRAN (1-12)
        PAGI ATAU MALAM?
output = ANDA PARKIR SELAMA ... JAM, Anda harus bayar Rp ...
HARGA = 3 jam pertama 3000/jam
        setelah 3 jam pertama 1000/jam
        biaya maksimal 25000
"""
def parking_calc(time_in, set1, time_out, set2):
        if ((1 <= time_in <= 12) and (1 <= time_out <= 12) and (set1 in ['PAGI', 'MALAM'] and set2 in ['PAGI', 'MALAM'])):
                if(set1 == set2):
                        if(time_in > time_out):
                                hour = time_out + 24 - time_in
                        else:
                                hour = time_out - time_in
                else:
                        hour = time_out + 12 - time_in
                
        else:
                print('Waktu harus bernilai di antara 1-12 dan nilai set harus PAGI atau MALAM')
                return 'Error'
        
        if(hour > 23):
                return 25000
        else:
                return 3000 + (hour - 1) * 1000

# Test cases
print(parking_calc(7, 'PAGI', 7, 'MALAM'))
print(parking_calc(8, 'PAGI', 7, 'PAGI'))
print(parking_calc(8, 'MALAM', 7, 'PAGI'))
print(parking_calc(6, 'MALAM', 7, 'PAGI'))



"""
APLIKASI CONVERTER HARI DAN DETIK

input
Mau Menghitung apa? Hari atau Detik?

output:
361 hari = 1 tahun 0 bulan 1 hari

Ketentuan:
1 tahun = 360 hari
1 bulan = 30 hari
1 jam = 3600 detik
1 menit = 60 detik

"""

def time_convert(time):
        x = time.split();
        if (len(x) != 2):
                print('Argumen tidak sesuai')
                return 'Error'
        else:
                try:
                        t = int(x[0])
                except :
                        print('Argumen waktu bukan integer')
                        return 'Error'
                
                if (x[1].lower() == 'hari'):
                        tahun = t // 365
                        hari = t - 365 * tahun
                        bulan = hari // 30
                        hari = hari - 30 * bulan
                        return (time + ' = ' + str(tahun) + ' tahun ' + str(bulan) + ' bulan ' + str(hari) + ' hari')
                elif (x[1].lower() == 'detik'):
                        jam = t // 3600
                        detik = t - 3600 * jam
                        menit = detik // 60
                        detik = detik - 60 * menit
                        return (time + ' = ' + str(jam) + ' jam ' + str(menit) + ' menit ' + str(detik) + ' detik')
                else:
                        print('Argumen jenis waktu harus "Hari" atau "Detik"')
                        return 'Error'

# Test cases
print(time_convert('356 HARI '))
print(time_convert('3600 Detik'))


