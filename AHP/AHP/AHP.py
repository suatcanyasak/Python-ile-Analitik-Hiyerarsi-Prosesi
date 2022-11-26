import numpy as np
import math
def PrintComparisonMatrix(kriterDizisi,kriterDegerDictionary):
    print()
    for i in range(0,n):
        if(i != n-1):
            print("\t" +kriterDizisi[i], end = " ")
        else:
            print("\t"+kriterDizisi[i])
    for i in range (0,n):
            print(kriterDizisi[i],end = "\t")
            for j in range (0,n):
                print ('{:.2f}'.format(kriterDegerDictionary[kriterDizisi[i] + "/" + kriterDizisi[j]]),end="\t")
            print()    

def NormalizeKararMatrisiOlustur(kriterMatris,size):
    normalizeMatris = np.empty(shape =[size,size],dtype=float)
    toplamMatris = np.empty(shape = [1,size], dtype= float)
    for j in range(0,size):
        toplam = 0
        for i in range(0,size):
            toplam += kriterMatris[i,j]
        toplamMatris[0,j] = toplam
        
        for i in range(0,size):
            normalizeMatris[i,j]=kriterMatris[i,j]/toplamMatris[0,j]

    print("...........NORMALIZE MATRIS.........",end = "\n\n")
    for i in range (0,size):
        for j in range (0,size):
            print(normalizeMatris[i,j],end = "\t")
        print(end = "\n")

    return normalizeMatris

def OzVektorMatrisiOlustur(normalizeMatris,size):
    print("\n"+"...........OZ VEKTOR MATRIS.........",end = "\n\n")
    ozVektorMatrisi = np.empty(shape = [size,1], dtype= float)
    for i in range(0,size):
        toplam = 0
        for j in range(0,size):
            toplam += normalizeMatris[i,j]
        ozVektorMatrisi[i,0] = toplam/size
        print(ozVektorMatrisi[i,0],end = "\n")
    print()
    return ozVektorMatrisi

#n=|1  2   3     4     5     6     7     8     9     10 |  RI= random index  
RI=[0, 0, 0.52, 0.89, 1.11, 1.25, 1.35, 1.40, 1.45, 1.49]

print("\n.....KRITERLER....\n")
n = int(input("Kac adet kriter karsilastirilacak: "))
kriterler = []
kriterDegerDictionary = {}

#kriter adi alma

for i in range(1,n+1):
    kriter = input("{}. kriteri giriniz: ".format(i))
    kriterler.append(kriter)


soru_sayisi= (int) ((n * (n-1)) / 2)
print("\n","(Eðer diðer kriteri ilkine göre daha üstün buluyorsanýz parantez içindeki ondalýklý deðeri giriniz) \n","1: Eþit Önemde","\n","3: Biraz Daha Önemli (Az Üstünlük)->(0.33)","\n","5: Oldukça Önemli (Fazla Üstünlük)->(0.2)",
"\n","7: Çok Önemli (Çok Üstünlük)->(0.14)","\n","9: Son Derece Önemli (Kesin Üstünlük)->(0.11)","\n","2,4,6 ve 8: Ara Deðerler (Uzlaþma Deðerleri)")
print("")

#kriterlerin birbirine olan ustunlugunu alip matris olusturma:

for i in range(0,n):
    for j in range (i+1,n):
        while True:
            secim = float(input("{}. kriterin {}. kritere ustunlugu nedir: ".format(i+1,j+1)))
            if secim<0 or secim>10:
                print("0-10 aralýðýnda deðer girilmeli.")
            else:
                kriterDegerDictionary[kriterler[i] + "/" + kriterler[j]] = secim
                kriterDegerDictionary[kriterler[j] + "/" + kriterler[i]] = 1/secim
                break

for i in range(0,n):
        kriterDegerDictionary[kriterler[i] + "/" + kriterler[i]] = 1

kriterMatris = np.empty(shape =[n,n],dtype=float)
for i in range(0,n):
    for j in range (0,n):
        kriterMatris[i,j] = kriterDegerDictionary[kriterler[i] + "/" + kriterler[j]]

PrintComparisonMatrix(kriterler,kriterDegerDictionary)
print("\n")

normalizeMatris = NormalizeKararMatrisiOlustur(kriterMatris,n)
ozVektorMatrisi = OzVektorMatrisiOlustur(normalizeMatris,n)

# Ýki matrisin boyutlarýnýn girilmesi
while True:
    m = len(kriterler)
    n = len(kriterler)
    print("A(m,n) boyutlarý:",m,",",n)
    f = len(kriterler)
    p = 1
    print("B(f,p) boyutlarý:",f,",",p)
# Çarpým koþulunun kontrol edilmesi
    if n != f:
        print("Matrisler carpilamaz")
    else:
# Matrislerin oluþturulmasý
        A = [[0 for i in range(n)] for i in range(m)]
        B = [[0 for i in range(p)] for i in range(f)]
        C = [[0 for i in range(p)] for i in range(m)]
    # “A” matrisinin girilmesi
        print("karþýlaþtýrma matrisini giriniz:")
        for i in range(m):
            for j in range(n):
                print('A[{}][{}]'.format(i+1, j+1))
                A[i][j] = float(input("").format(i+1,j+1))
    # “B” matrisinin girilmesi
        print("Özvektör matrisini giriniz:")
        for i in range(f):
            for j in range(p):
                print('B[{}][{}]'.format(i+1, j+1))
                B[i][j] = float(input("").format(i+1,j+1))
    # Çarpýmýn hesaplanmasý 
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]

    print("toplam: ",C)
    toplamdeðerler=[]
    for i in range(0,len(kriterler)):
        a=C[i]/ozVektorMatrisi[i]
        toplamdeðerler.append(a)
    print(toplamdeðerler)
    
    ortalama=(sum(toplamdeðerler))/len(kriterler)
    print("ortalama deðer: ",ortalama)

    lambdamax=ortalama

    sonuc=(lambdamax-len(kriterler))/(len(kriterler)-1)
    print("tutarlýlýk oraný hesaplanacak: ",sonuc)
    tutarlýlýkoraný=sonuc*RI[len(kriterler)-1]
    print("tutarlýlýk oraný: ",tutarlýlýkoraný)
    if tutarlýlýkoraný>0.10:
        print("tutarsýz")
    else:
        break
n = int(input("Kac adet alternatifi karsilastirmak istiyorsunuz: ")) 
alternatifler= []
alternatifDictionaryList = []
alternatifDegerDictionary = {}

for i in range(1,n+1):
   alternatif = input("{}. alternatifi giriniz: ".format(i))
   alternatifler.append(alternatif)

soru_sayisi= (int) ((n * (n-1)) / 2)

print("\n","(Eðer diðer alternatifi ilkine göre daha üstün buluyorsanýz parantez içindeki ondalýklý deðeri giriniz) \n","1: Eþit Önemde","\n","3: Biraz Daha Önemli (Az Üstünlük)->(0.33)","\n","5: Oldukça Önemli (Fazla Üstünlük)->(0.2)",
"\n","7: Çok Önemli (Çok Üstünlük)->(0.14)","\n","9: Son Derece Önemli (Kesin Üstünlük)->(0.11)","\n","2,4,6 ve 8: Ara Deðerler (Uzlaþma Deðerleri)")
print("")

#alternatiflerin birbirlerine olan üstünlüðünün sorulmasý ve verilerin dict'e atilmasi.
for k in range(0,len(kriterler)):
    for i in range(0,n):
        for j in range (i+1,n):
            while True:
                secim = float(input(kriterler[k]+ " icin {}. alternatifin {}. alternatife ustunlugu nedir: ".format(i+1,j+1)))
                if secim<0 or secim>9:
                    print("0-9 aralýðýnda deðer girilmeli.")
                else:
                    alternatifDegerDictionary[alternatifler[i] + "/" + alternatifler[j]] = secim
                    alternatifDegerDictionary[alternatifler[j] + "/" + alternatifler[i]] = 1/secim
                    break

    for i in range(0,n):
            alternatifDegerDictionary[alternatifler[i] + "/" + alternatifler[i]] = 1
    alternatifDictionaryList.append(alternatifDegerDictionary)
    alternatifDegerDictionary = {}    

alternatifMatris = np.empty(shape =[n,n],dtype=float)
alternatifMatrisArray = []
alternatifNormalizeMatrisArray = []
alternatifOzVektorMatrisArray = []

#Üstteki list yapýlarýna atýlan verilerden en yukarda oluþturulan fonksiyonlarý kullanarak matrýs oluþturma.

for k in range (0,len(kriterler)):
    for i in range(0,n):
        for j in range (0,n):
            alternatifMatris[i,j] = alternatifDictionaryList[k][alternatifler[i] + "/" + alternatifler[j]]
    alternatifMatrisArray.append(alternatifMatris)
    alternatifNormalizeMatrisArray.append(NormalizeKararMatrisiOlustur(alternatifMatris,n))
    alternatifOzVektorMatrisArray.append(OzVektorMatrisiOlustur(alternatifNormalizeMatrisArray[k],n))

#Alternatýflerin karþýlaþtýrma matrisin boyutunu belirleme ve ve verileri dizilere aktarma.

alternatifKarsilastirmaMatrisi = np.empty(shape = [len(alternatifler),len(kriterler)],dtype=float)
for j in range (0,len(kriterler)):
    for i in range (0, len(alternatifler)):
        alternatifKarsilastirmaMatrisi[i,j] = alternatifOzVektorMatrisArray[j][i,0]
        #print(alternatifKarsilastirmaMatrisi[i,j])

# Alternatiflerin birbiri arasýnda deðerlendirildiði ve bunun her kriter için yapýldýðý matrislerin birleþtirilmesi.

for i in range (0,len(alternatifler)):
    for j in range (0, len(kriterler)):
        print(alternatifKarsilastirmaMatrisi[i,j],end = "\t")
    print("\n\n")

# Yukarda oluþturulan alternatiflerin karþýlaþtýrma matrisi ile özvektör matrisininö matris çarpýmýç

sonucMatrisi = np.matmul(alternatifKarsilastirmaMatrisi,ozVektorMatrisi)

# Sonuç matrisine göre en büyük deðeri alma ve en iyi alternatifi belirleme.

enBuyukEleman = alternatifler[0]
maximum = -math.inf
for i in range (sonucMatrisi.shape[0]):
    print(alternatifler[i],end = "\t")
    for j in range (sonucMatrisi.shape[1]):
        print(sonucMatrisi[i,j],end = "\t")
        if sonucMatrisi[i,j]>maximum:
            maximum = sonucMatrisi[i,j]
            alternatif[i]
    print("\n\n")

print("En iyi alternatif {}".format(enBuyukEleman))
