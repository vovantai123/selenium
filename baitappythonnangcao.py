import math
import time

def kiem_tra_so_nguyen(tainjng):
    try:
        val = int(tainjng)
        return True, val
    except ValueError:
        return False, None

def la_so_chinh_phuong(tai392922):
    g = int(math.isqrt(tai392922))
    return g * g == tai392922

def bai_1_tim_so():
    while True:
        tai392922 = input("Nhập số nguyên a: ")
        valid_a, a = kiem_tra_so_nguyen(tai392922)
        tai1001 = input("Nhập số nguyên b: ")
        valid_b, b = kiem_tra_so_nguyen(tai1001)
        
        if not valid_a or not valid_b:
            print("Vui lòng nhập đúng số nguyên.")
            continue
        if a >= b:
            print("Điều kiện a < b không thỏa mãn, mời nhập lại.")
            continue
        break
    
    ketqua = []
    for tainjng in range(a, b+1):
        if tainjng % 3 == 0 and not la_so_chinh_phuong(tainjng):
            ketqua.append(str(tainjng))
    
    print("Kết quả:", ",".join(ketqua))


def tao_so_ngau_nhien():
    miligiay = int((time.time() * 1000) % 1000) + 1
    return miligiay

def kiem_tra_so_nguoi_dung(taixyz):
    try:
        val = int(taixyz)
        if 1 <= val <= 999:
            return True, val
        else:
            return False, None
    except ValueError:
        return False, None

def bai_2_minigame():
    tai392922 = tao_so_ngau_nhien()
    so_lan_sai = 0
    
    while True:
        tainjng = input("Mời bạn nhập số nguyên dương từ 1 đến 999: ")
        valid, guess = kiem_tra_so_nguoi_dung(tainjng)
        if not valid:
            print("Vui lòng nhập số nguyên dương trong khoảng 1 đến 999.")
            continue
        
        if guess == tai392922:
            print(f"Bạn đã dự đoán chính xác số {tai392922}")
            break
        else:
            so_lan_sai += 1
            
            khoang_cach = abs(guess - tai392922)
            if khoang_cach <= 10:
                print("Bạn đoán gần đúng rồi!")
            else:
                print(f"Bạn đã trả lời sai {so_lan_sai} lần")
            
            if so_lan_sai == 5:
                tai392922 = tao_so_ngau_nhien()
                so_lan_sai = 0
                print("Bạn đoán trật tất cả năm lần, kết quả đã thay đổi. Mời bạn đoán lại")


def main():
    while True:
        print("\nChọn chương trình muốn chạy:")
        print("1. Tìm số chia hết cho 3 nhưng không phải số chính phương trong đoạn [a, b]")
        print("2. Minigame đoán số")
        print("0. Thoát")
        chon = input("Nhập lựa chọn: ")
        
        if chon == "1":
            bai_1_tim_so()
        elif chon == "2":
            bai_2_minigame()
        elif chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Mời nhập lại.")

if __name__ == "__main__":
    main()
