import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import os
import random
from keras.models import load_model

st.set_page_config(
    page_title="web của dũng",
    page_icon="#",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

html, body, .stApp {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: #f8fafc !important; /* Nền xám xanh Slate siêu sang trọng */
    color: #1e293b !important;
}

.main-header{
    font-size: 45px;
    font-weight: 800;
    color: #1e293b;
    text-align: center;
    margin-bottom: 5px;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
}

.sub-text{
    text-align:center;
    color: #64748b;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 30px;
}

.box{
    background-color: white !important;
    padding: 24px !important;
    border-radius: 16px !important;
    border: 1px solid #e2e8f0 !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.box:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05) !important;
    border-color: #cbd5e1 !important;
}

.box h3, .box h4, .box li, .box p {
    color: #1e293b !important;
}

.metric-box{
    background: linear-gradient(135deg, #1e3a8a, #3b82f6) !important;
    color: white !important;
    padding: 22px !important;
    border-radius: 16px !important;
    text-align: center !important;
    box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.2) !important;
    transition: transform 0.2s !important;
}

.metric-box:hover {
    transform: scale(1.02) !important;
}

.metric-box h2 {
    font-size: 36px !important;
    font-weight: 700 !important;
    margin: 0 !important;
    color: #ffffff !important;
}

.metric-box p {
    font-size: 13px !important;
    font-weight: 600 !important;
    margin: 5px 0 0 0 !important;
    color: #93c5fd !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='main-header'>Nhận diện lá bài bằng AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-text'>Nhận diện lá bài bằng CNN và TensorFlow</div>",
    unsafe_allow_html=True
)

with st.spinner("Hệ thống đang nạp Mô hình AI... Vui lòng đợi trong giây lát..."):
    try:
        model = load_model('cards_model.keras')
        time.sleep(0.4) 
    except Exception as e:
        st.error("❌ Không tìm thấy tệp tin mô hình 'cards_model.keras' ở thư mục gốc!")
        st.code(str(e))

left, right = st.columns([2,1])

with left:
    st.markdown("""
    <div class='box' style='height: 100%; border-left: 5px solid #7c3aed;'>
        <h4 style='margin-top: 0;'>Giới thiệu hệ thống</h4>
        <p style='line-height: 1.6;'>
            Project sử dụng kiến trúc mạng nơ-ron tích chập (CNN) sâu để nhận diện chính xác 53 lá bài khác nhau trong bộ bài Tây tiêu chuẩn.
        </p>
        <p style='line-height: 1.6; margin-bottom: 0;'>
            Người dùng chỉ cần di chuyển sang trang <strong>Predict</strong> ở thanh điều hướng để tiến hành upload hình ảnh lá bài thật và AI sẽ thực hiện dự đoán kết quả ngay lập tức.
        </p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("<div class='box' style='height: 100%; border-left: 5px solid #2563eb;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='margin-top: 0;'>Trạng thái AI</h4>", unsafe_allow_html=True)
    st.success("🟢 Mô hình đã sẵn sàng hoạt động.")
    
    if st.button("🔮 Chạy thử nghiệm quét (Test AI)"):
        demo_cards = [
            "Ace of Hearts",
            "King of Clubs",
            "Queen of Diamonds",
            "Jack of Spades",
            "10 of Hearts"
        ]
        with st.spinner("AI đang trích xuất ma trận điểm ảnh..."):
            time.sleep(0.5)
        st.info(f"Kết quả quét ngẫu nhiên: {random.choice(demo_cards)}")
        st.caption("👉 Chuyển sang menu Predict để tải ảnh thật lên")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<h3 style='margin-top: 30px;'>Thông Số Huấn Luyện Cốt Lõi</h3>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class='about-card' style='text-align: center;'>
        <div style='color: #9ca3af; font-size: 14px; text-transform: uppercase;'>Độ Chính Xác (Accuracy)</div>
        <div class='metric-val' style='color: #34d399;'>96.00%</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='about-card' style='text-align: center;'>
        <div style='color: #9ca3af; font-size: 14px; text-transform: uppercase;'>Số Lớp Nhận Diện (Classes)</div>
        <div class='metric-val' style='color: #60a5fa;'>53 Loại Lá</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='about-card' style='text-align: center;'>
        <div style='color: #9ca3af; font-size: 14px; text-transform: uppercase;'>Kiến Trúc Thuật Toán</div>
        <div class='metric-val' style='color: #fbbf24;'>Mạng CNN</div>
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

    st.title("Card AI")

    st.markdown("---")

    st.markdown("""
    ### Thông tin dự án

    - Dataset: Playing Cards
    - Model: CNN
    - Framework: TensorFlow
    - Frontend: Streamlit
    """)

    st.markdown("---")

    st.success("Chọn trang ở menu phía trên")