import pandas as pd
from sqlalchemy import false

data = {
    "name" : ["thanh","tu","vy","hoang","khanh",'linh','trang','truc','phi','hoang','phuc'],
    "age" :[25,18,23,24,28,25,18,23,24,28,21],
    "gender": ['nu','nam','nu','nam','nu','nu','nam','nu','nam','nu','nam'],
    'score': [3,6,9,2,3,4,6,9,7,10,9]
}
danhsach = pd.DataFrame(data)
print('\nToàn bộ dữ liệu của bảng')
print(danhsach)
print("\n3 dong dau tien")
print(danhsach.head(3))
print("\nTheo index=2 và cột Name")
print(danhsach.at[2,'name'])
print("\nTheo index=10 và cột Age")
print(danhsach.at[10,'age'])
print("\nCác cột Name và Score")
print(danhsach[["name",'score']])
print("\nThêm một cột tên Pass với giá trị True nếu giá trị cột Score >= 5, ngược lại là False.")
danhsach['pass'] = danhsach['score'] >= 5
print(danhsach)
print("\nDanh sach giam dan")
danhsachgiamdan = danhsach.sort_values(by ='score',ascending=False )
print(danhsachgiamdan)
