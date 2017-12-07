---
title: "[Xác Suất] Mẫu thống kê và ước lượng tham số"
slug: sampling-parameters-estimation
date: 2017-10-14
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
Trong các phần trước ta đã tìm hiểu cơ bản về xác suất và thống kê xác suất cũng như một số mô hình thống kê thông dụng, dựa vào đó ta tiếp tục lấn sang 1 phần quan trọng là thống kê và ước lượng các tham số cho các bài toán thực tế.
<!--more-->

<!--toc-->

# 1. Mẫu thống kê
Trong thực tế khi muốn thống kê để tìm quan hệ giữa các yếu tố ngẫu nhiên ta thường xuyên phải làm việc với các tập dữ liệu rất lớn tới mức không đủ thời gian và chi phí để làm việc. Vậy nên việc chọn lấy 1 tập mẫu nhỏ trong đó để mô phỏng là rất cần thiết. Quá trình lấy mẫu này đòi hỏi nhiều kĩ thuật sao cho mẫu lấy ra có thể đại diện được cho toàn bộ tập dữ liệu. Tuy nhiên, bài viết này sẽ không tập trung vào quá trình lấy mẫu đó mà sẽ tập trung vào việc tìm các đặc tính của tập mẫu đó.

## 1.1. Mẫu ngẫu nhiên
Mẫu ngẫu nhiên là tập các mẫu độc lập và có cùng một thống kê xác suất (*I.I.D - Independent, Identically Distributed*). Ví dụ ta cần thống kê mức độ xinh gái ảnh hưởng thế nào tới trí thông minh của chị em. Thì ta có thể coi độ xinh gái là một biến ngẫu nhiên. Lúc này ta lấy mẫu $n$ người và mỗi người sẽ có độ xinh gái là $X_i$ tương ứng. Khi đó ta có thể coi rằng $X_i$ là độc lập đôi một với nhau và
chúng có cùng một phân phối xác suất. Tập các mẫu này là mẫu ngẫu nhiên $X=[X_1,X_2,...,X_n]$ kích thước $n$.

Như vậy nếu gọi $p_X(x)$ là hàm trọng lượng xác suất đồng thời nếu $X_i$ là rời rạc và $f_X(x)$ là hàm mật độ xác suất đồng thời nếu $X_i$ là liên tục thì ta sẽ có:
$$p_X(x)=\prod\_{i=i}^np\_{X_i}(x_i)$$
và
$$f_X(x)=\prod\_{i=i}^nf\_{X_i}(x_i)$$

## 1.2. Thống kê
Ta đã chọn ra được mẫu ngẫu nhiên rồi và giờ là lúc ta cần xem quan hệ của chúng ra sao. Phép lấy quan hệ như vậy được gọi là thống kê. Về mặt hình thức, ta có thể định nghĩa một hàm $Y=g(X)$ bất kì là một thống kê phụ thuộc vào mẫu ngẫu nhiên $X$.

Ví dụ: $\displaystyle\bar X=g(X)=\frac{1}{n}\sum\_{i=1}^nx_i$ có thể coi là một thống kê.

## 1.3. Đặc trưng mẫu
Ở đây ta sẽ xét một số thống kê cơ bản cho mẫu ngẫu nhiên và gọi chúng là các đặc trưng mẫu.

### 1.3.1. 

# 2. Ước lượng tham số
