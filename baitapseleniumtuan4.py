from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
chromedriver_path = "chromedriver.exe"
service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)
driver.get(" https://www.saucedemo.com")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "login-button").click()
products = driver.find_elements(By.CLASS_NAME, "inventory_item")
data = []

for product in products:
    driver.implicitly_wait(30)
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
    data.append({"Product Name": name, "Price": price})

# Lưu vào Excel
df = pd.DataFrame(data)
df.to_excel("products.xlsx", index=False)

print("✅ Đã lưu danh sách sản phẩm vào 'products.xlsx'.")


driver.get("https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep")
driver.implicitly_wait(10)

# Lấy dữ liệu từ class
elements = driver.find_elements(By.CLASS_NAME, "item_mst") + driver.find_elements(By.CLASS_NAME, "item_mst_o")

data = []
for el in elements:
    lines = el.text.strip().split("\n")
    if len(lines) >= 3:
        mst = lines[0].strip()
        ten_dn = lines[1].strip()
        ngay_cap = lines[2].strip()
        data.append({
            "Mã số thuế": mst,
            "Tên doanh nghiệp": ten_dn,
            "Ngày cấp": ngay_cap
        })

df = pd.DataFrame(data)
with pd.ExcelWriter("1_trang_mst.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Trang_1", index=False)

driver.quit()

