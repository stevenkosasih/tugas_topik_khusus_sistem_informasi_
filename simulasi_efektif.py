import calendar as calendar
def simulasiKredit(pinjaman,sukuBungaTahunan,tenor,biayaAdmBulan):
    tempPinjaman=pinjaman
    pinjamanPerBulan=tempPinjaman/tenor
    angsuranPokokBulan=0
    totalAngsuranPokok=0
    totalBunga=0
    bungaBulanan=0
    totalAngsuran=0
    counterBulan=1
    angsuranPokok=0
    for n in range(tenor):
        bungaBulanan=tempPinjaman*sukuBungaTahunan
        angsuranPokokBulan=pinjamanPerBulan+bungaBulanan+biayaAdmBulan
        totalAngsuranPokok=totalAngsuranPokok+angsuranPokokBulan
        totalBunga=totalBunga+bungaBulanan
        tempPinjaman=tempPinjaman-pinjamanPerBulan
        if counterBulan>12:
            counterBulan-=12       
        print("Periode :",calendar.month_name[counterBulan])
        print("Angsuran Pokok :",angsuranPokokBulan)
        print("Bunga: ",bungaBulanan)
        print("BiayaAdmin:",biayaAdmBulan)
        counterBulan+=1
        print("-------------------------------")

    print("Total Bunga:",totalBunga)
    print("Total biaya admin:",biayaAdmBulan*tenor)
    print("Total Angsuran: ",totalAngsuranPokok)
       
def test(b):
    print("t")
