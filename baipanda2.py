import pandas as pd
import numpy as np
pd.set_option('future.no_silent_downcasting', True)
nhanvien = {
    "ID"        :  [101, 102, 103, 104, 105, 106],
    "Name"      :  ['An', 'Bình', 'Cường', 'Dương', pd.NA, 'Hạnh'],
    "Age"       :  [25, pd.NA, 30, 22, 28, 35],
    "Department": ['HR', 'IT', 'IT', 'Finance', 'HR', pd.NA],
    "Salary"    :  [700, 800, 750, pd.NA, 710, 770]
}
danhsachnhanvien = pd.DataFrame(nhanvien)
phongban = {
    'Department':  ['HR', 'IT', 'Finance', 'Marketing'],
    "Manager"   :   ['Trang', 'Khoa', 'Minh', 'Lan']
}
danhsachphongban = pd.DataFrame(phongban)
print(danhsachnhanvien.isnull().sum())
xoadongbithieu = danhsachnhanvien[danhsachnhanvien.isnull().sum(axis=1)<=2]
print(xoadongbithieu)

danhsachnhanvien['Name'] = danhsachnhanvien['Name'].fillna("chưa rõ")
trungbinh = danhsachnhanvien['Age'].mean()
danhsachnhanvien['Age'] = danhsachnhanvien['Age'].fillna(trungbinh)
danhsachnhanvien['Department'] = danhsachnhanvien['Department'].fillna('Unknown')
danhsachnhanvien['Salary']= danhsachnhanvien['Salary'].ffill()
print(danhsachnhanvien)



danhsachnhanvien['Age']=danhsachnhanvien['Age'].astype(int)
danhsachnhanvien['Salary']=danhsachnhanvien['Salary'].astype(int)


danhsachnhanvien['Salary_after_tax'] = (danhsachnhanvien['Salary'] * 0.9).astype(int)

nhanvienit25 = danhsachnhanvien[(danhsachnhanvien['Department'] =='IT') & (danhsachnhanvien['Age'] > 25)]


danhsachSalary_after_taxgiamdan = danhsachnhanvien['Salary_after_tax'].sort_values()


tinhtrungbinhDepartment  = danhsachnhanvien.groupby('Department')['Salary'].mean().reset_index()

noi2bangnhanvienvaphongban = pd.merge(danhsachnhanvien, danhsachphongban, on='Department', how='left')
nhanvienmoi = pd.DataFrame({
    "Name": ['Lan', 'Minh'],
    "Age": [27, 25],
    "Department": ['HR', 'IT'],
    "Salary": [5800, 6200]
})

# Thêm nhân viên mới vào bảng cũ
nhanviensaukhigopthanhcong = pd.concat([danhsachnhanvien, nhanvienmoi], ignore_index=True)
