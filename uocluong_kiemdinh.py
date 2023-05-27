import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel("D:/Dataset/Dataset/Book1_Temperature.xlsx")
#print(df,'\n')

laymau = df.sample(30) # lấy mẫu ngẫu nhiên
#print(laymau,'\n')


#lấy cột temperaature
col = laymau['Temperature']
#print('lấy dữ liệu 1 cột','\n',col,'\n')


#tính phương sai
def variance(data):
    mu = np.mean(data)
    return sum([(point-mu)**2 for point in data])/len(data)
print('phương sai: ',variance(col))

#tính độ lệch chuẩn
def stddev(data): # standard deviation
    return math.sqrt(variance(data))
print('độ lệch chuẩn: ',stddev(col))


# A) Kiểm tra mức độ tương quan giữa độ mặn và nhiệt độ
# Dữ liệu mẫu
Salinity = df['Salinity']
Temperature = df['Temperature']

# Tính toán hệ số tương quan
correlation_coefficient = np.corrcoef(Salinity, Temperature)[0, 1]

# Vẽ biểu đồ
plt.scatter(Salinity, Temperature)
plt.xlabel('Độ mặn')
plt.ylabel('Nhiệt độ')
plt.title(f'tương quan giữa độ mặn và nhiệt độ: {correlation_coefficient:.2f}')
plt.show()
#) kiểm định: Nhiệt độ trung bình của Việt Nam vào năm 1995 là 28 độ C, với độ tin cậy là 95%
temperatures_1995 = []
for i in range(len(Temperature)):
    if df['Year'][i] == 1995:
        temperatures_1995.append((Temperature[i]))
print(temperatures_1995)
# Giả thuyết h0: Nhiệt độ trung bình là 28 độ C
h0_mean = 28

# Độ tin cậy
confidence_level = 0.95

# Kiểm định t-test
t_statistic, p_value = stats.ttest_1samp(temperatures_1995, h0_mean)

# Kiểm tra xem p-value có nhỏ hơn alpha (1 - độ tin cậy) hay không
alpha = 1 - confidence_level
if p_value < alpha:
    print("Reject null hypothesis - Nhiệt độ trung bình không bằng 28 độ C.")
else:
    print("Fail to reject null hypothesis - Nhiệt độ trung bình bằng 28 độ C.")

# c) ước lượng : . Dựa trên dữ liệu sau, bạn có thể ước lượng khoảng nhiệt độ trung bình ở Việt Nam
# trong một năm 2010 với một mức độ tin cậy xác định trước (ví dụ: 95%).
# Mẫu dữ liệu


# Mẫu dữ liệu từ các năm 1990-2005
temperatures_1990_2005 = df['Temperature']
# Độ tin cậy
confidence_level = 0.95

# Ước lượng khoảng tin cậy
mean = np.mean(temperatures_1990_2005)
std_dev = np.std(temperatures_1990_2005)
n = len(temperatures_1990_2005)
margin_of_error = stats.t.ppf((1 + confidence_level) / 2, n-1) * (std_dev / np.sqrt(n))
confidence_interval = (mean - margin_of_error, mean + margin_of_error)

# Hiển thị kết quả
print(f"Khoảng nhiệt độ trung bình ở Việt Nam trong năm 2010 dựa trên dữ liệu từ các năm 1990-2005 với độ tin cậy {confidence_level * 100}%:")
print(f"Giá trị trung bình: {mean}")
print(f"Khoảng tin cậy: {confidence_interval}")
