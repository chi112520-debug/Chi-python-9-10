#Km dau tien: 15.000 dong
#Tu km thu 2 den km thu 5: 12.000 dong/km
#Tu km thu 6 tro di: 10.000 dong/km
#Neu quang duong lon hon 100km, khach hang duoc giam 10% tong tien cuoc.
#Neu km<=0, in ra "Quang duong khong hop le".

km = float(input("Nhap so km: "))
if km<=0:
    print("Quang duong khong hop le")
elif km<=1:
    tien = 15000
    print ("Tien cuoc:", tien, "dong")
elif km<=5:
    tien = 15000 + (km -1) * 12000
    print("Tien cuoc:", tien, "dong")
else:
    tien = 15000 + 4 * 12000 + (km - 5) *10000
    print("Tien cuoc:", tien, "dong")
    
