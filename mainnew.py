import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime
from io import BytesIO
import time

# Hàm để vẽ đồng hồ kiểu Big Ben với màu nền và màu số đã chỉnh sửa
def draw_big_ben_clock():
    # Lấy thời gian hiện tại
    now = datetime.datetime.now()
    hours, minutes, seconds = now.hour, now.minute, now.second

    # Đảm bảo giờ được hiển thị theo định dạng 12 giờ (0-11)
    hours = hours % 12

    # Tạo một biểu đồ tròn (hình đồng hồ)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_ylim(0, 1)
    ax.set_yticklabels([])  # Ẩn các nhãn trên trục y

    # Thiết lập các vạch giờ theo chiều ngược kim đồng hồ với màu vàng
    ax.set_xticks(np.linspace(0, 2 * np.pi, 12, endpoint=False))
    ax.set_xticklabels(['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'], 
                       fontsize=15, color='blue')  # Thay đổi màu các con số thành xanh dương

    # Đặt số 12 ở vị trí trên cùng (đỉnh) bằng cách xoay trục
    ax.set_theta_offset(np.pi / 2)  # Xoay trục để số 12 nằm trên cùng

    # Đảm bảo rằng đồng hồ xoay theo chiều ngược kim đồng hồ
    ax.set_theta_direction(-1)

    # Màu nền và khung cho đồng hồ
    ax.set_facecolor('#f0e68c')  # Màu nền vàng nhạt (khaki)
    ax.spines['polar'].set_visible(True)
    ax.spines['polar'].set_color('black')  # Viền đồng hồ đen
    ax.spines['polar'].set_linewidth(4)

    # Vẽ kim giây (ngược chiều kim đồng hồ)
    seconds_angle = 2 * np.pi * (seconds / 60)
    ax.plot([seconds_angle, seconds_angle], [0, 0.9], color='red', lw=2)

    # Vẽ kim phút (ngược chiều kim đồng hồ)
    minutes_angle = 2 * np.pi * (minutes / 60 + seconds / 3600)  # Bao gồm giây để kim phút mượt hơn
    ax.plot([minutes_angle, minutes_angle], [0, 0.75], color='blue', lw=3)

    # Vẽ kim giờ (ngược chiều kim đồng hồ)
    hours_angle = 2 * np.pi * (hours / 12 + minutes / 720)  # Bao gồm phút để kim giờ mượt hơn
    ax.plot([hours_angle, hours_angle], [0, 0.5], color='black', lw=5)

    # Vẽ các chấm vàng kim cho vạch phút
    for i in range(60):
        angle = 2 * np.pi * (i / 60)
        radius = 0.95 if i % 5 != 0 else 0.85
        ax.plot(angle, radius, marker='o', color='gold', markersize=5 if i % 5 != 0 else 8)

    # Lưu hình ảnh vào bộ nhớ
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

# Tạo giao diện với Streamlit
st.title("Đồng hồ thời gian của Pháp Sư")

# Tạo một vùng trống để cập nhật hình ảnh
image_placeholder = st.empty()

# Vòng lặp để cập nhật đồng hồ theo thời gian thực
while True:
    # Vẽ đồng hồ và hiển thị
    buf = draw_big_ben_clock()
    image_placeholder.image(buf)

    # Dừng lại 1 giây trước khi cập nhật tiếp
    time.sleep(1)
