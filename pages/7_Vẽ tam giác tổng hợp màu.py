import streamlit as st 
import matplotlib.pyplot as plt
import colour
import colour.plotting
import numpy as np

st.set_page_config(
    page_title="Vẽ tam giác tổng hợp", layout="centered"
)
chon_tam_giac_mau = st.sidebar.radio("Chọn tam giác tổng hợp màu", ("Tổng hợp màu cộng", "Tổng hợp màu trừ"))

if chon_tam_giac_mau == "Tổng hợp màu cộng":
    xR = 3
    yR = 1
    label = ['Red'] 
    plt.annotate(label[0],
             xy=(xR, yR),
             xytext=(15, -5), 
             textcoords='offset points',
             fontsize=15,
             color='red')
    xG = 2
    yG = 1+3**0.5
    label = ['Green'] 
    plt.annotate(label[0],
             xy=(xG, yG),
             xytext=(15, -5), 
             textcoords='offset points',
             fontsize=15,
             color='green')
    xB = 1
    yB = 1
    label = ['Blue'] 
    plt.annotate(label[0],
             xy=(xB, yB),
             xytext=(-50, -5), 
             textcoords='offset points',
             fontsize=15,
             color='blue')
    tam_giac_x = [xR, xG, xB, xR]
    tam_giac_y = [yR, yG, yB, yR]
    # k: black
    plt.plot(tam_giac_x, tam_giac_y, 'k')

    xC = (xB + xG) / 2
    yC = (yB + yG) / 2
    label = ['Cyan'] 
    plt.annotate(label[0],
             xy=(xC, yC),
             xytext=(-55, -5), 
             textcoords='offset points',
             fontsize=15,
             color='cyan')
    xM = (xB + xR) / 2
    yM = (yB + yR) / 2
    label = ['Magenta'] 
    plt.annotate(label[0],
             xy=(xM, yM),
             xytext=(-30, -25), 
             textcoords='offset points',
             fontsize=15,
             color='magenta')
    xY = (xR + xG) / 2
    yY = (yR + yG) / 2
    label = ['Yellow'] 
    plt.annotate(label[0],
             xy=(xY, yY),
             xytext=(15, -5), 
             textcoords='offset points',
             fontsize=15,
             color='yellow')

    duong_1x = [xR, xC]
    duong_1y = [yR, yC]
    plt.plot(duong_1x, duong_1y, linestyle='--', color='black', label='Nét đứt')
    duong_2x = [xG, xM]
    duong_2y = [yG, yM]
    plt.plot(duong_2x, duong_2y, linestyle='--', color='black', label='Nét đứt')
    duong_3x = [xB, xY]
    duong_3y = [yB, yY]
    plt.plot(duong_3x, duong_3y, linestyle='--', color='black', label='Nét đứt')

    xW = (xR + xG + xB) / 3
    yW = (yR + yG + yB) / 3
    label = ['White'] 
    plt.annotate(label[0],
             xy=(xW, yW),
             xytext=(15, -5), 
             textcoords='offset points',
             fontsize=15,
             color='black')
    
    plt.plot(xR, yR, marker='o', markersize=20, color='red', linestyle='')
    plt.plot(xG, yG, marker='o', markersize=20, color='green', linestyle='')
    plt.plot(xB, yB, marker='o', markersize=20, color='blue', linestyle='')
    plt.plot(xC, yC, marker='o', markersize=20, color='cyan', linestyle='')
    plt.plot(xM, yM, marker='o', markersize=20, color='magenta', linestyle='')
    plt.plot(xY, yY, marker='o', markersize=20, color='yellow', linestyle='')
    plt.plot(xW, yW, marker='o', markersize=20, color='white', markeredgecolor='black', linestyle='')

    figure, axes = colour.plotting.render(
    show=True,
    x_tighten=True,
    y_tighten=True)
    axes.axis('off')
    
    st.pyplot(figure, clear_figure=True)

    st.write('## Tổng hợp màu cộng')
    st.write("Tổng hợp màu cộng là tổng hợp màu của ánh sáng với 3 **màu sơ cấp** (đỉnh của tam giác màu) là **Red**, **Green** và **Blue**. Khi phối các màu này với nhau thì chỉ có thể tạo ra màu sáng hơn và **không thể tạo ra màu đen**. Do đó, nếu màn hình của các thiết bị điện tử như TV, máy tính, điện thoại,... càng đen thì sẽ càng có độ tương phản tốt hơn.")
    st.write("Các **màu thứ cấp** của tam giác tổng hợp màu cộng là **Cyan**, **Magenta** và **Yellow**. Khi **kết hợp 3 màu RGB** sẽ tạo ra màu **trắng** - **White**.")

if chon_tam_giac_mau == "Tổng hợp màu trừ":
    xC = 3
    yC = 1
    label = ['Cyan'] 
    plt.annotate(label[0],
             xy=(xC, yC),
             xytext=(15, -5), 
             textcoords='offset points',
             fontsize=15,
             color='cyan')
    xM = 2
    yM = 1+3**0.5
    label = ['Magenta'] 
    plt.annotate(label[0],
             xy=(xM, yM),
             xytext=(15, -5), 
             textcoords='offset points',
             fontsize=15,
             color='magenta')
    xY = 1
    yY = 1
    label = ['Yellow'] 
    plt.annotate(label[0],
             xy=(xY, yY),
             xytext=(-60, -5), 
             textcoords='offset points',
             fontsize=15,
             color='yellow')
    tam_giac_x = [xC, xM, xY, xC]
    tam_giac_y = [yC, yM, yY, yC]
    # k: black
    plt.plot(tam_giac_x, tam_giac_y, 'k')

    xR = (xM + xY) / 2
    yR = (yM + yY) / 2
    label = ['Red'] 
    plt.annotate(label[0],
             xy=(xR, yR),
             xytext=(-45, -5), 
             textcoords='offset points',
             fontsize=15,
             color='red')
    xG = (xC + xY) / 2
    yG = (yC + yY) / 2
    label = ['Green'] 
    plt.annotate(label[0],
             xy=(xG, yG),
             xytext=(-25, -25), 
             textcoords='offset points',
             fontsize=15,
             color='green')
    xB = (xM + xC) / 2
    yB = (yM + yC) / 2
    label = ['Blue'] 
    plt.annotate(label[0],
             xy=(xB, yB),
             xytext=(15, -5), 
             textcoords='offset points',
             fontsize=15,
             color='blue')

    duong_1x = [xR, xC]
    duong_1y = [yR, yC]
    plt.plot(duong_1x, duong_1y, linestyle='--', color='black', label='Nét đứt')
    duong_2x = [xG, xM]
    duong_2y = [yG, yM]
    plt.plot(duong_2x, duong_2y, linestyle='--', color='black', label='Nét đứt')
    duong_3x = [xB, xY]
    duong_3y = [yB, yY]
    plt.plot(duong_3x, duong_3y, linestyle='--', color='black', label='Nét đứt')

    xK = (xC + xM + xY) / 3
    yK = (yC + yM + yY) / 3
    label = ['Black'] 
    plt.annotate(label[0],
             xy=(xK, yK),
             xytext=(15, -5), 
             textcoords='offset points',
             fontsize=15,
             color='black')
    
    plt.plot(xR, yR, marker='o', markersize=20, color='red', linestyle='')
    plt.plot(xG, yG, marker='o', markersize=20, color='green', linestyle='')
    plt.plot(xB, yB, marker='o', markersize=20, color='blue', linestyle='')
    plt.plot(xC, yC, marker='o', markersize=20, color='cyan', linestyle='')
    plt.plot(xM, yM, marker='o', markersize=20, color='magenta', linestyle='')
    plt.plot(xY, yY, marker='o', markersize=20, color='yellow', linestyle='')
    plt.plot(xK, yK, marker='o', markersize=20, color='black', markeredgecolor='black', linestyle='')

    figure, axes = colour.plotting.render(
    show=True,
    x_tighten=True,
    y_tighten=True)
    axes.axis('off')
    
    st.pyplot(figure, clear_figure=True)

    st.write('## Tổng hợp màu trừ')
    st.write("Tổng hợp màu trừ là tổng hợp màu của vật thể với 3 **màu sơ cấp** (đỉnh của tam giác màu) là **Cyan**, **Magenta** và **Yellow**. Khi phối các màu này với nhau thì chỉ có thể tạo ra màu tối hơn và **không thể tạo ra màu trắng**. Do đó, nếu màu nền giấy càng trắng thì sẽ càng có độ tương phản tốt hơn. Đối với các loại màng trong suốt, người ta sẽ in thêm một lớp lót trắng bên dưới để tăng độ tương phản cho hình ảnh, đảm bảo khả năng phục chế đạt chất lượng.")
    st.write("Các **màu thứ cấp** của tam giác tổng hợp màu cộng là **Red**, **Green** và **Blue**. Khi **kết hợp 3 màu CMY** sẽ tạo ra màu **đen** - **Black**.")

    