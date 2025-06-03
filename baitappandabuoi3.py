import pandas as pd

# Tạo dữ liệu cho 10 sinh viên
data = {
    "Name": ["An", "Bình", "Cường", "Dương", "Em", "Hà", "Khang", "Linh", "Minh", "Phương"],
    "Age": [20, 21, 19, 22, 20, 21, 23, 19, 22, 20],
    "Gender": ["M", "M", "M", "M", "F", "F", "M", "F", "M", "F"],
    "Score": [7.5, 8.0, 4.0, 6.5, 5.0, 3.0, 9.0, 7.0, 8.5, 4.5]
}

# Tạo DataFrame
df_students = pd.DataFrame(data)

# Hiển thị toàn bộ dữ liệu
print("Toàn bộ dữ liệu:")
print(df_students)

# Hiển thị 3 dòng đầu tiên
print("\n3 dòng đầu tiên:")
print(df_students.head(3))

# Lấy giá trị tại index=2 và cột Name
print("\nTên sinh viên ở index=2:")
print(df_students.at[2, "Name"])

# Lấy giá trị tại index=10 và cột Age
print("\nGiá trị index=10 và cột Age:")
try:
    print(df_students.at[10, "Age"])
except KeyError:
    print("Không có index=10 trong DataFrame")

# Hiển thị các cột Name và Score
print("\nCột Name và Score:")
print(df_students[["Name", "Score"]])

# Thêm cột Pass (True nếu Score >= 5, False nếu < 5)
df_students["Pass"] = df_students["Score"] >= 5

print("\nDataFrame sau khi thêm cột Pass:")
print(df_students)

# Sắp xếp theo Score giảm dần
df_sorted = df_students.sort_values(by="Score", ascending=False)

print("\nDanh sách sinh viên sắp xếp theo Score giảm dần:")
print(df_sorted)
