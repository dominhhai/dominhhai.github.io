---
title: "[ML] Vấn đề khớp quá (Overfitting)"
slug: ml-overfitting
date: 2017-12-25T08:45:04+09:00
categories:
- Học Máy
- ML
tags:
- Học Máy
keywords:
- Học Máy
- Machine Learning
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/dl/logo.png
metaAlignment: center
draft: true
---
Lỗi ước lượng tham số có thể được chia thành 2 loại là **khớp quá** (*over-fitting*) và **chưa khớp** (*under-fitting*) với tập huấn luyện. Trong bài này sẽ nói về cách theo dõi và hạn chế các lỗi này ra sao. Trọng tâm của bài này sẽ tập trung chủ yếu vào kĩ thuật **chính quy hoá** (*regularization*) để giải quyết vấn đề khớp quá của tham số.
<!--more-->
<!--toc-->
# 1. Giới thiệu
Mô hình của ta sau khi huấn luyện có thể đạt hiểu quả không tốt khi dự đoán với một dữ liệu mới. Chuyện này xảy ra là do mô hình của ta chưa tổng quát hoá được với toàn bộ tập dữ liệu. Nguyên nhân cũng khá dễ hiểu khi mà tập huấn luyện của ta chỉ là một tập nhỏ chưa thể đại diện cho toàn thể dữ liệu được và hơn nữa có thể nó còn bị nhiễu nữa. Người ta chia nguyên nhân ra làm 2 loại chính là *chưa khớp* hoặc *quá khớp*.
## 1.1. Chưa khớp (*Underfitting*)

## 1.2. Quá khớp (*Overfitting*)
## 1.3. Vừa khớp (*Good Fitting*)
# 2. Theo dõi lỗi
## 2.1. Đánh giá lỗi
## 2.2. Phán định lỗi
# 3. Cân bằng phương sai và độ lệch
# 4. Kĩ thuật chính quy hoá
# 5. Kết luận
