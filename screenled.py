import math



def manhinh192(A, B, C, D):

    print('-------------------------------------------------------------------------------------------------------')
    D = int(A) / 1.77
    chieudai = int(A)
    dodaimiengled = int(C)
    somiengchieudai = chieudai // dodaimiengled
    print('So mieng led chieu dai la :', somiengchieudai, 'mieng')
    chieudaicantinh = (somiengchieudai * dodaimiengled) + 120
    print('Chieu dai man hinh la :',chieudaicantinh, 'mm')
    print('-------------------------------------------------------------------------------------------------------')

    chieucao = int(D)
    dodaimiengled = int(C)
    somiengchieucao = chieucao // dodaimiengled 
    print('So mieng chieu cao la :', somiengchieucao, 'mieng')
    chieucaocantinh = (somiengchieucao * dodaimiengled) + 120
    print('Chieu cao man hinh la :',chieucaocantinh,"mm")
    print('-------------------------------------------------------------------------------------------------------')

    chieudaimiengled = int(C)
    somiengchieudai = int(A) // chieudaimiengled
    somiengchieucao = int(D) // chieudaimiengled 
    tong = somiengchieucao * somiengchieudai
    print('So mieng led la :',tong,'mieng')
    print('-------------------------------------------------------------------------------------------------------')

    chieudaimiengled = int(C)
    somiengchieudai = int(A) // chieudaimiengled
    somiengchieucao = int(D) // chieudaimiengled 
    tong = somiengchieucao * somiengchieudai
    card = int(tong) // 12
    phandu = int(tong) % 12
    if int(phandu) > 0:
        carddieukhien = card + 1
    print('So card dieu khien la :',carddieukhien, 'cai')
    nguon = carddieukhien * 2
    print('So bo nguon la :',nguon)
    print('-------------------------------------------------------------------------------------------------------') 

    chieudai = int(A)
    dodaimiengled = int(C)
    somiengchieudai = chieudai // dodaimiengled
    chieudaicantinh = (somiengchieudai * dodaimiengled) + 120
    chieucao = int(D)
    somiengchieucao = chieucao // dodaimiengled 
    chieucaocantinh = (somiengchieucao * dodaimiengled) + 120
    
    dientichAlu1 = (chieudaicantinh * int(C)) * 2 + (chieudaicantinh * 50 * 2)
    dientichAlu2 = (chieucaocantinh * int(C)) * 2 + (chieucaocantinh * 50 * 2)
    dientichAlutong = round((dientichAlu1 + dientichAlu2) / 1000000,2)
    print('Dien tich Alu can tinh la :',dientichAlutong, 'm2')
    print('-------------------------------------------------------------------------------------------------------')

    chieudai = int(A)
    dodaimiengled = int(C)
    somiengchieudai = chieudai // dodaimiengled
    chieudaicantinh = (somiengchieudai * dodaimiengled) + 120
    chieucao = int(D)
    somiengchieucao = chieucao // dodaimiengled 
    chieucaocantinh = (somiengchieucao * dodaimiengled) + 120

    binhphuongchieudai = chieudaicantinh * chieudaicantinh
    binhphuongchieucao = chieucaocantinh * chieucaocantinh  
    kichthuocduongcheo = math.sqrt(binhphuongchieudai + binhphuongchieucao)
    quydoi = kichthuocduongcheo / 1000
    kichthuoc = float(round(quydoi, 2)) * 39.370
    kichthuoc1 = round(kichthuoc,2)
    print('Kich thuoc man hinh la :',kichthuoc1,"inch")

    return




def manhinh320(A, B, C, D):
    
    print('-------------------------------------------------------------------------------------------------------')
    somiengledchieudai = int(A) // C
    chieudaimanhinh = (somiengledchieudai * 320) + 110
    chieucaomanhinh = round((chieudaimanhinh) / 1.77) + 110
    duongcheomanhinh = round((math.sqrt(chieudaimanhinh * chieudaimanhinh + chieucaomanhinh * chieucaomanhinh) / 1000) * 39.370)

    print('Kich thuoc chieu dai man hinh la : ',chieudaimanhinh, 'mm')
    print('Kich thuoc chieu cao man hinh la : ',chieucaomanhinh, 'mm')
    print('Kich thuoc man hinh la : ',duongcheomanhinh, 'inch')
    print('-------------------------------------------------------------------------------------------------------')


    E = 160
    somiengledchieudai = chieudaimanhinh // C
    somiengledchieucao = chieucaomanhinh // E
    tong = somiengledchieudai * somiengledchieucao
    print('So mieng chieu dai la :',somiengledchieudai,"mieng")
    print('So mieng chieu cao la :',somiengledchieucao,"mieng")
    print('Tong so mieng led :',tong,'mieng')
    print('-------------------------------------------------------------------------------------------------------')
    dientichalu1 = chieudaimanhinh 






def main():
    try:
        A = input('Xin hay nhap chieu dai can tinh bang mm : ')
        B = int(A) / 1.77
        C = int(input('Xin hay nhap kich thuoc miếng led : ' ))
        D = int(A) / 1.77
        if C == 192:
            kichthuoc192 = manhinh192(A, B, C, D)
        elif C == 320:
            kichthuoc320 = manhinh320(A, B, C, D)
        else:
            print('Xin hay nhap lai kich thuoc')        
    except:
        print('Xin hay nhap gia tri la so')


if __name__ == "__main__":
    main()






    