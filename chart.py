import matplotlib.pyplot as plt

# Dữ liệu ví dụ
months = ['January', 'February', 'March', 'April', 'May']
sales = [200, 300, 150, 400, 350]

# Vẽ biểu đồ cột
plt.figure(figsize=(8, 6))
plt.bar(months, sales, color='skyblue')

# Thêm nhãn và tiêu đề
plt.xlabel('Months', fontsize=12)
plt.ylabel('Sales (in USD)', fontsize=12)
plt.title('Monthly Sales Data', fontsize=16)

# Hiển thị biểu đồ
plt.show()
