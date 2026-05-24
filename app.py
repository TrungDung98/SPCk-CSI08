import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# Cấu hình trang
st.set_page_config(
    page_title="web của dũng",
    page_icon="#",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #0f172a;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #ff7f0e;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
    background-color: #1f77b4;
    padding: 2rem;
    border-radius: 15px;
    color: white;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    transition: 0.3s ease;
    }

    .metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #1f77b4;
    }
    .feature-card:hover {
    transform: translateY(-3px);
    transition: 0.3s;
    }
    .stApp {
    background-color: #f5f7fb;
    }
    </style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<h1 class="main-header">Trang chủ</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Web nóng</p>', unsafe_allow_html=True)

# Banner với nút CTA
banner_col1, banner_col2 = st.columns([2, 1])
with banner_col1:
    st.info("tìm hết cả kiếm")
with banner_col2:
    if st.button("hello world", type="primary", use_container_width=True):
        st.balloons()

# Metrics Section
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #2E86AB;'>abc</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="metric-card">
        <h2 style='font-size: 2.5rem;'>10 tỉ</h2>
        <p>Người Dùng</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2 style='font-size: 2.5rem;'>10000%</h2>
        <p>Uptime</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2 style='font-size: 2.5rem;'>2000 app</h2>
        <p>Ứng Dụng</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h2 style='font-size: 2.5rem;'>khong ho tro</h2>
        <p>Hỗ Trợ</p>
    </div>
    """, unsafe_allow_html=True)

# Features Section
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #2E86AB;'>tinh lang</h2>", unsafe_allow_html=True)

features_data = [
    {
        "icon": "#",
        "title": "Tốc Độ Cao",
        "desc": "Xử lý dữ liệu nhanh chóng với hiệu suất tối ưu"
    },
    {
        "icon": "#", 
        "title": "Bảo Mật Tuyệt Đối",
        "desc": "Dữ liệu được mã hóa end-to-end"
    },
    {
        "icon": "#",
        "title": "Đa Nền Tảng",
        "desc": "Hoạt động mượt mà trên mọi thiết bị"
    },
    {
        "icon": "#",
        "title": "Luôn sử dụng AI",
        "desc": "Tích hợp trí tuệ nhân tạo tiên tiến"
    }
]

cols = st.columns(4)
for i, feature in enumerate(features_data):
    with cols[i]:
        st.markdown(f"""
        <div class="feature-card">
            <h3 style='color: #1f77b4;'>{feature['icon']} {feature['title']}</h3>
            <p>{feature['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# About Section
st.markdown("---")
about_col1, about_col2 = st.columns([2, 1])

with about_col1:
    st.markdown("""
    abc
    """)

with about_col2:
    st.markdown("""
    ###  Thành Tựu
    - Top 1% hiệu suất
    - ⭐⭐⭐⭐⭐ đánh giá
    - Giải thưởng công nghệ 2024
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; background-color: #f0f2f6; border-radius: 10px;'>
    <h3> Liên Hệ Với Chúng Tôi</h3>
    <p><strong>Email:</strong> @dungdeptrai1234| <strong>Hotline:</strong> 888889999</p>
    <p>nap vip : htpps://dungdeptraiii</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Trang chủ")
    st.markdown("Tìm kiếm")
    
    page_options = ["Trang Chủ", "Dashboard", "Phân Tích", "Cài Đặt"]
    selected_page = st.selectbox("Đi đến:", page_options, index=0)
    
    if st.button("Refresh", type="secondary"):
        st.rerun()
    
    st.markdown("---")
    st.markdown("Thông tin về web")
    st.info("web vippp proo")