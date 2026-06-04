import streamlit as st
from predict import predict_card
from PIL import Image

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, .stApp {
        font-family: 'Poppins', sans-serif;
        color: #ffffff;
    }

    .stApp {
        background: linear-gradient(
            to right, 
            #1a1a2e,    
            #16213e,    
            #0f3460     
        );
    }

    .css-1r6slb0, .css-1wiv2ii, .stMarkdown {
        background-color: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    h1, h2, h3 {
        font-weight: 600 !important;
        color: #ffffff;
    }
    
    .stButton>button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

st.title("🃏 Predict Card")

uploaded_file = st.file_uploader(
    "Upload ảnh lá bài",
    type=["jpg","png","jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(
        image,
        caption="Ảnh tải lên",
        width=300
    )

    if st.button("🔮 Dự đoán ngay", use_container_width=True):
        with st.spinner("Đang xử lý..."):
            image = image.convert("RGB")
            image.save("temp.jpg")
            card_name, confidence = predict_card("temp.jpg")
            st.success(
                f"Prediction: {card_name}"
            )
            st.info(
                f"Confidence: {confidence:.2%}"
            )

else:

    st.info("👆 Hãy tải lên một hình ảnh lá bài để bắt đầu dự đoán!")
    st.markdown("""
    **📝 Hướng dẫn:**
    1. Click vào nút **Browse files** ở phía trên.
    2. Chọn file ảnh lá bài từ máy tính của bạn (hỗ trợ JPG, PNG, JPEG).
    3. Nhấn nút **Dự đoán ngay** (nút này sẽ xuất hiện sau khi bạn tải ảnh thành công).
    """)