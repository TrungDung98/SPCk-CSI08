# AI Playing Card Recognition

## Giới thiệu

Dự án sử dụng Convolutional Neural Network (CNN) để nhận diện 53 loại lá bài từ hình ảnh.

## Công nghệ

* Python
* TensorFlow
* CNN
* Streamlit

## Chức năng

* Upload ảnh lá bài
* Dự đoán tên lá bài
* Hiển thị độ chính xác

## Dataset

Cards Image Dataset Classification (Kaggle)

## Cách chạy

### Train model

python train.py

### Chạy website

streamlit run app.py

## Cấu trúc project

card-project/
├── app.py
├── train.py
├── predict.py
├── requirements.txt
├── README.md
├── cards_model.h5
├── dataset/
└── pages/
