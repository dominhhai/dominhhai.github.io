---
title: "[Xác Suất] Biến ngẫu nhiên và phân phối xác suất"
slug: prob-rand-var
date: 2017-10-11
categories:
- Xác Suất
tags:
- Xác Suất
keywords:
- Probability
- Xác Suất
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/prob/icon.png
metaAlignment: center
draft: true
---
Trong [phần trước](/vi/2017/10/what-is-prob/) ta đã có khái niệm rất cơ bản về phép thử, sự kiện, các tính chất của biến cố và cách tính xác suất của chúng. Trong phần này, ta sẽ tập trung vào các biến cố nhận giá trị ngẫu nhiên và mô hình phân phối xác suất của chúng.
<!--more-->

<!--toc-->
# 1. Biến ngẫu nhiên
Biến ngẫu nhiên (random variables) là các biến nhận 1 giá trị ngẫu nhiên đại diện cho kết quả của phép thử. Mỗi giá trị nhận được $ x $ của biến ngẫu nhiên $ X $ được gọi là một thể hiện của $ X $, đây cũng là kết quả của phép thử hay còn được hiểu là một sự kiện.

Gọi tên là một biến có vẻ hơi kì kì một chút bởi biến ngẫu nhiên thực chất là một hàm ánh xạ từ không gian sự kiện đầy đủ tới 1 số thực: $ X: \Omega \mapsto \mathbb{R} $.

Biến ngẫu nhiên có 2 dạng:

* Rời rạc: tập giá trị nó là rời rạc, tức là đếm được. Ví dụ như mặt chấm của con xúc xắc.
* Liên tục: tập giá trị là liên tục tức là lấp đầy 1 khoảng trục số. Ví dụ như giá thuê nhà ở Hà Nội.

# 2. Phân phối xác suất
Là phương pháp xác định xác suất của biến ngẫu nhiên được phân phối ra sao. Có 2 cách để xác định phân bố này là dựa vào bảng phân bố xác xuất và hàm phân phối xác suất. Ở đây, tôi chỉ đề cập tới phương pháp hàm phân bố xác suất. Hàm phân phối xác suất của biến ngẫu nhiên $ X $ được xác định như sau:

$$ F_X(x) = P(X < x) ~~~, x \in \mathbb{R} $$

Nếu để ý thì sẽ thấy rằng xác suất đồ thị của hàm $ F_X(x) $ sẽ có dạng bậc thang nếu $ X $ là rời rạc.

## 2.1. Hàm khối lượng xác suất của biến rời rạc
## 2.2. Hàm mật độ xác suất của biến liên tục
# 3. Các phương pháp
## 3.1. Xác suất biên
## 3.2. Xác suất có điều kiện
# 5. Các đặc trưng
## 5.1. Kì vọng
## 5.2. Phương sai
## 5.3. Trung vị
## 5.4. Mode
## 5.5. Hiệp phương sai
# 6. Các hàm phân phối thường gặp
