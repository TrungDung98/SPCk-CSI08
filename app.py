import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.set_page_config(
    page_title="web của dũng",
    page_icon="#",
    layout="wide"
)

st.markdown("""
<style>
.main-header{
    font-size: 42px;
    font-weight: bold;
    color: #1f2937;
    text-align: center;
    margin-bottom: 10px;
}

.sub-text{
    text-align:center;
    color: gray;
    margin-bottom: 30px;
}

.box{
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.metric-box{
    background-color:#1f77b4;
    color:white;
    padding:20px;
    border-radius:12px;
    text-align:center;
}

.stApp{
    background-color:#f5f7fa;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown(
    "<div class='main-header'>🃏 Nhận diện lá bài bằng AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-text'>Nhận diện lá bài bằng CNN và TensorFlow</div>",
    unsafe_allow_html=True
)

left, right = st.columns([2,1])

with left:
    st.info("""
    Project sử dụng CNN để nhận diện 53 lá bài khác nhau.
    
    Người dùng có thể upload ảnh và AI sẽ dự đoán kết quả.
    """)

with right:
    if st.button("Test AI"):
        with st.spinner("AI đang phân tích..."):
            time.sleep(2)
        st.success("Hoàn thành")

st.markdown("---")
st.subheader("Tổng quan")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='metric-box'>
        <h2>96%</h2>
        <p>Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-box'>
        <h2>53</h2>
        <p>Classes</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-box'>
        <h2>CNN</h2>
        <p>Model</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("Thông tin về sản phẩm")

info1, info2 = st.columns(2)

with info1:
    st.markdown("""
    <div class='box'>
    
    ### Công nghệ sử dụng
    - TensorFlow
    - CNN
    - Streamlit
    - Python
    
    </div>
    """, unsafe_allow_html=True)

with info2:
    st.markdown("""
    <div class='box'>
    
    ### Chức năng chính
    - Upload ảnh lá bài
    - AI predict kết quả
    - Hiển thị độ chính xác
    - Phân tích bằng AI
    
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("Cách hoạt động")

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown("""
    <div class='box'>
    <h3>📤</h3>
    Upload ảnh
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class='box'>
    <h3>🧠</h3>
    CNN xử lý
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class='box'>
    <h3>🎯</h3>
    Predict kết quả
    </div>
    """, unsafe_allow_html=True)

with f4:
    st.markdown("""
    <div class='box'>
    <h3>📊</h3>
    Hiển thị thông tin
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown(""" <div style='text-align: center; padding: 2rem; background-color: #f0f2f6; border-radius: 10px;'> <h3> Liên Hệ Với Chúng Tôi</h3> <p><strong>Email:</strong> @dungdeptrai1234| <strong>Hotline:</strong> 888889999</p> <p>nap vip : htpps://dungdeptraiii</p> </div> """, unsafe_allow_html=True)

with st.sidebar:
    st.title("Menu")

    page = st.radio(
        "Điều hướng",
        [
            "Trang chủ",
            "Dự đoán",
            "Phân tích",
            "Giới thiệu"
        ]
    )

    st.markdown("---")

    st.info("Nhận dạng lá bài bằng CNN")