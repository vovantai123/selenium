from collections import Counter

def bai1(taivo1122):
    hdjks22 = taivo1122.split()
    if not hdjks22:
        return ""
    hdhfjfj = [hdjks22[0].capitalize()] + [x.lower() for x in hdjks22[1:]]
    taivuie12 = " ".join(hdhfjfj)
    return taivuie12

def bai2(hdhfjfj):
    taivo1122 = hdhfjfj.split()
    kfj39dh = taivo1122[::-1]
    hf93dhf = " ".join(kfj39dh)
    return hf93dhf

def bai3(taivo1122):
    hdhfjfj = Counter(taivo1122)
    kytu, sl = hdhfjfj.most_common(1)[0]
    return kytu, sl

if __name__ == "__main__":
    # Bài 1 test
    print("Bài 1:", bai1("tôi yêu LẬP trình Python lắm"))

    # Bài 2 test
    print("Bài 2:", bai2("đảo ngược thứ tự các từ"))

    # Bài 3 test
    kq = bai3("taivo1122 thích lập trình Python nhiều nhiều")
    print(f"Bài 3: Ký tự '{kq[0]}' xuất hiện {kq[1]} lần")
