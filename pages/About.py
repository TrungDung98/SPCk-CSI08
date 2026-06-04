import streamlit as st

st.set_page_config(
    page_title="Giới thiệu Dự án AI",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, .stApp {
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
        background: linear-gradient(to right, #0f172a, #1e1b4b, #111827) !important;
    }

    .about-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s ease;
    }
    
    .about-card:hover {
        transform: translateY(-3px);
        border-color: rgba(99, 102, 241, 0.4);
        background: rgba(255, 255, 255, 0.05);
    }

    .card-subtitle {
        color: #818cf8;
        font-weight: 600;
        font-size: 18px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .tech-item {
        margin-bottom: 12px;
        line-height: 1.6;
    }
    .tech-tag {
        background: rgba(99, 102, 241, 0.2);
        color: #a5b4fc;
        padding: 2px 8px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-size: 42px; font-weight: 600; margin-bottom: 5px; color: #ffffff;'>Tổng Quan Dự Án</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 16px; margin-bottom: 30px;'>Hệ thống nhận diện quân bài Tây ứng dụng Trí tuệ nhân tạo thời gian thực</p>", unsafe_allow_html=True)
st.markdown("---")

col_info, col_func = st.columns([1, 1], gap="large")

with col_info:
    st.markdown("""
    <div class='about-card'>
        <div class='card-subtitle'>Nền Tảng Công Nghệ (Tech Stack)</div>
        <div class='tech-item'><span class='tech-tag'>Python 3.15</span> Ngôn ngữ lập trình cấu trúc chính, tối ưu xử lý ma trận và mảng dữ liệu ảnh toán học.</div>
        <div class='tech-item'><span class='tech-tag'>TensorFlow & Keras</span> Framework học sâu cao cấp dùng để thiết lập lớp, biên dịch toán học và huấn luyện mạng nơ-ron tích chập.</div>
        <div class='tech-item'><span class='tech-tag'>Kiến trúc CNN</span> Mạng Neural tuần tự (Sequential) với các tầng Conv2D để trích xuất hoa văn đặc trưng và Softmax để phân loại đa lớp.</div>
        <div class='tech-item'><span class='tech-tag'>Streamlit UI</span> Thư viện mã nguồn mở giúp biến các tệp mã Python gốc thành giao diện Web App tương tác trực quan tốc độ cao.</div>
    </div>
    """, unsafe_allow_html=True)

with col_func:
    st.markdown("""
    <div class='about-card'>
        <div class='card-subtitle'>Các Tính Năng Cốt Lõi</div>
        <div class='tech-item'><strong>1. Tiếp nhận và Tiền xử lý dữ liệu:</strong> Cho phép người dùng đăng tải tệp tin ảnh linh hoạt (PNG, JPG, JPEG). Hệ thống tự động chuyển đổi định dạng về chuẩn ma trận màu RGB.</div>
        <div class='tech-item'><strong>2. Nhận diện tự động bằng AI:</strong> Nạp ảnh qua tệp trung gian, quét toán học qua các trọng số đã học của mô hình để phân tích ra kết quả phân lớp của lá bài trong chưa đầy 0.5 giây.</div>
        <div class='tech-item'><strong>3. Đánh giá độ tin cậy (Confidence):</strong> Xuất ra chỉ số phần trăm chắc chắn của thuật toán đối với kết quả dự đoán, giúp người dùng kiểm chứng hiệu năng mô hình một cách trực quan.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; margin-bottom: 20px;'>Quy trình xử lý của hệ thống (Pipeline)</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='about-card' style='text-align: center; padding: 15px;'>
        <h4 style='color: #3b82f6; margin: 0;'>Bước 1</h4>
        <p style='margin: 5px 0 0 0; font-size: 14px;'>Tải ảnh lên<br>(Input Image)</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='about-card' style='text-align: center; padding: 15px;'>
        <h4 style='color: #10b981; margin: 0;'>Bước 2</h4>
        <p style='margin: 5px 0 0 0; font-size: 14px;'>Chuẩn hóa dữ liệu ảnh<br>(Resize 128x128 RGB)</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='about-card' style='text-align: center; padding: 15px;'>
        <h4 style='color: #f59e0b; margin: 0;'>Bước 3</h4>
        <p style='margin: 5px 0 0 0; font-size: 14px;'>Mạng CNN dự đoán<br>(Model Inference)</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='about-card' style='text-align: center; padding: 15px;'>
        <h4 style='color: #ec4899; margin: 0;'>Bước 4</h4>
        <p style='margin: 5px 0 0 0; font-size: 14px;'>Trích xuất kết quả %<br>(Output Visual)</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #6b7280; font-size: 13px;'>Sản phẩm được tối ưu giao diện và vận hành trên nền tảng Keras & Streamlit Cloud</p>", unsafe_allow_html=True)