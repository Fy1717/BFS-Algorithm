def Taşı(diskSayısı,k1, k2, k3):
    if diskSayısı >= 1:
        Taşı(diskSayısı-1,k1,k3,k2)
        Hareket(k1,k2)
        Taşı(diskSayısı-1,k3,k2,k1)

def Hareket(nereden,nereye):
    print("Taşınma İşlemi",nereden,"-->",nereye)

Taşı(3,"A","B","C")
