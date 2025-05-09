import colour.plotting
import streamlit as st
import matplotlib.pyplot as plt
import colour
import numpy as np

st.set_page_config(
    page_title="Vẽ gamut màu của thiết bị RGB", layout="centered"
)

colour.plotting.plot_chromaticity_diagram_CIE1931(show=False)
R = np.array([1.0, 0.0, 0.0])
G = np.array([0.0, 1.0, 0.0])
B = np.array([0.0, 0.0, 1.0])

XYZ_R = colour.sRGB_to_XYZ(R)
xyR = colour.XYZ_to_xy(XYZ_R)
xR = xyR[0]
yR = xyR[1]

XYZ_G = colour.sRGB_to_XYZ(G)
xyG = colour.XYZ_to_xy(XYZ_G)
xG = xyG[0]
yG = xyG[1]

XYZ_B = colour.sRGB_to_XYZ(B)
xyB = colour.XYZ_to_xy(XYZ_B)
xB = xyB[0]
yB = xyB[1]

tam_giac_x = [xR, xG, xB, xR]
tam_giac_y = [yR, yG, yB, yR]

# k: black
plt.plot(tam_giac_x, tam_giac_y, 'k')

figure, axes = colour.plotting.render(
    show=True,
    x_tighten=True,
    y_tighten=True)

st.pyplot(figure, clear_figure=True)