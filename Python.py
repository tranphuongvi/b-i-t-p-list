import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Nhóm 1 Vi

df = pd.read_excel("D:/Dataset/Dataset/Book1_Temperature.xlsx")
print(df,'\n')


Tasks = [31.88,5.8,0.73]
my_labels = 'Salinity','Temperature','CHLFa'
plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%')
plt.title('Salinity,Temperature,CHLFa')
plt.axis('equal')
plt.show()

## Biểu đồ tròn ##
sal = df.iloc[300,3:]       # Lấy dữ liệu của hàng 300 với 3 cột cuối cùng là Salinity, Temperature, CHLFa
print(sal)
my_labels = df.iloc[0,3:]   # Nhãn lấy từ 3 cột cuối cùng là Salinity, Temperature, CHLFa của hàng đầu tiên

plt.pie(sal,labels=my_labels,autopct='%1.1f%%')
plt.title('Salinity, Temperature, CHLFa')
plt.axis('equal')
plt.show()

## Biểu đồ phân tán ##
x = df.iloc[1:16,3]       # Lấy 15 hàng dữ liệu của cột Salinity
y = df.iloc[1:16,5]       # Lấy 15 hàng dữ liệu của cột CHLFa
plt.scatter(x, y,color='green')
plt.title('Salinity và CHLFa', fontsize=14)
plt.xlabel('Salinity', fontsize=14)
plt.ylabel('CHLFa', fontsize=14)
plt.grid(True)
plt.show()

## Biểu đồ thanh ngang ##
table = pd.pivot_table(df, values='Temperature', index='Year', aggfunc='max')    # Tạo bảng nhiệt độ max theo từng năm
print('\n Nhiệt độ max theo năm: ','\n',table)

table.plot.barh()
plt.title('Max Temperature by years')
plt.ylabel('Year')
plt.xlabel('Temperature')
plt.show()

## Biểu đồ cột kép ##
# Dữ liệu
dl = df.groupby("Season")['Temperature'].max()       # Groupby nhiệt độ max theo Mùa
dl1 = df.groupby("Season")['Temperature'].min()         # Groupby độ muối max theo Mùa
print('Max Temperature theo Mùa: ',dl,'\n')
print('Min Temperature theo Mùa: ',dl,'\n')

n = len(dl)

## Vẽ biểu đồ cột chồng ##
fig, ax = plt.subplots()
ind = range(n)
width = 0.35
p1 = ax.bar(ind, dl, width)
p2 = ax.bar(ind, dl1, width, bottom=dl)

# Thiết lập các thông số cho biểu đồ
ax.set_title('Temperature and Salinity by Season')
ax.set_xticks(ind)
ax.set_xticklabels(('Thu', 'Xuân', 'Hạ', 'Đông'))
ax.legend((p1[0], p2[0]), ('Temperature', 'Salinity'))

# Hiển thị biểu đồ
plt.show()