nama = "Ahmad Fauzi"
print("Nama Mahasiswa : " + nama)

nama1 = "Hidayat"
print(nama + nama1)

hadir = 2
hadir2 = 4

print (hadir + hadir2) 

#print (nama + hadir)

nama1 = 20
print(nama1)

# kehadiran_fauzi_1 = 'H'
# kehadiran_fauzi_2 = 'H'
# kehadiran_fauzi_3 = 'I'
# kehadiran_fauzi_4 = 'H'
# kehadiran_fauzi_5 = 'A'
# kehadiran_fauzi_6 = 'H'

kehadiran_fauzi = ['H', 'H', 'I', 'H', 'A', 'H']
print(kehadiran_fauzi)
print(kehadiran_fauzi[2])



class data_mahasiswa :
    def __init__(self,nim,nama,kehadiran):
        self.nim = nim
        self.nama = nama
        self.kehadiran = kehadiran

# 0 = Nim, 1 = Nama, 2 = Kehadiran
["h","h","h","h","h","h","h","h","h","h",]
data = [
    [6113671,"Ultas Uniya", ["h","h","h","h","h","h","h","h","h","h",]],
    [2567113,"Namias Utita", ["h","h","h","h","h","h","h","h","h","h",]],
    [1133888,"Iopsdf Ids Edadi", ["h","h","h","h","h","h","h","h","h","h",]],
    [7484482,"Edadian Adudian", ["h","h","h","h","h","h","h","h","h","h",]],
    [1125533,"Yayiyuye Yayyi Sulaiman", ["h","h","h","h","h","h","h","h","h","h",]],
    [5672188,"Uiye Aiyi Aggogo", ["h","h","h","h","h","h","h","h","h","h",]],
]

for i in range(len(data)):
    data_mahasiswa = data[i]
    print(str(data[i][0]) + data[i][1] + data[i][2])









