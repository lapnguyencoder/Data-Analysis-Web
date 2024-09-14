import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime
from io import BytesIO
import time

# Hàm để vẽ đồng hồ
def draw_clock():
    # Lấy thời gian hiện tại
    now = datetime.datetime.now()
    hours, minutes, seconds = now.hour % 12, now.minute, now.second
    
    # Tạo một biểu đồ tròn (hình đồng hồ)
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_ylim(0, 1)
    ax.set_yticklabels([])  # Ẩn các nhãn trên trục y
    
    # Thiết lập các vạch giờ theo chiều ngược kim đồng hồ
    ax.set_xticks(np.linspace(0, 2 * np.pi, 12, endpoint=False))  
    ax.set_xticklabels(['12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])

    # Đặt số 12 ở vị trí trên cùng (đỉnh) bằng cách xoay trục
    ax.set_theta_offset(np.pi / 2)  # Xoay trục để số 12 nằm trên cùng
    
    # Đảm bảo rằng đồng hồ xoay theo chiều ngược kim đồng hồ
    ax.set_theta_direction(-1)

    # Vẽ kim giây (ngược chiều kim đồng hồ)
    seconds_angle = 2 * np.pi * (seconds / 60)
    ax.plot([seconds_angle, seconds_angle], [0, 0.9], color='red', lw=2)

    # Vẽ kim phút (ngược chiều kim đồng hồ)
    minutes_angle = 2 * np.pi * (minutes / 60 + seconds / 3600)
    ax.plot([minutes_angle, minutes_angle], [0, 0.75], color='blue', lw=3)

    # Vẽ kim giờ (ngược chiều kim đồng hồ)
    hours_angle = 2 * np.pi * (hours / 12 + minutes / 720)
    ax.plot([hours_angle, hours_angle], [0, 0.5], color='black', lw=5)

    # Lưu hình ảnh vào bộ nhớ
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf

# Tạo giao diện với Streamlit
st.title("Đồng hồ thời gian thực")

# Tạo một vùng trống để cập nhật hình ảnh
image_placeholder = st.empty()

# Vòng lặp để cập nhật đồng hồ theo thời gian thực
while True:
    # Vẽ đồng hồ và hiển thị
    buf = draw_clock()
    image_placeholder.image(buf)

    # Dừng lại 1 giây trước khi cập nhật tiếp
    time.sleep(1)
