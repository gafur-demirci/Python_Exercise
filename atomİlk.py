def dikdortgenAlan():
    kenar1 = float(input("İlk kenar uzunluğunu giriniz: "))
    kenar2 = float(input("İkinci kenar uzunluğunu giriniz: "))
    if kenar1 == kenar2:
        dikdortgenAlan()
    else:
        dA = kenar1*kenar2
        print("İlk kenar uzunluğu {} ve ikinci kenar uzunluğu {} olan dikdörtgenin alanı = {} dır.".format(kenar1,kenar2,dA))

dikdortgenAlan()
