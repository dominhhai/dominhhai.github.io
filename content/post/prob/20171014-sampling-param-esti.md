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

Ví dụ: $\displaystyle\overline X=g(X)=\frac{1}{n}\sum\_{i=1}^nX_i$ có thể coi là một thống kê. Thống kê này có tên là trung bình mẫu.

## 1.3. Đặc trưng mẫu
Ở đây ta sẽ xét một số thống kê cơ bản cho mẫu ngẫu nhiên và gọi chúng là các đặc trưng mẫu. Giả sử ta có mẫu ngẫu nhiên $X=[X_1,X_2,...,X_n]$ kích thước $n$ tuân theo một phân phối có kỳ vọng là $\mu$ và phương sai là $\sigma^2$.

### 1.3.1. Trung bình mẫu
Trung bình mẫu (*Mean*) hay còn gọi là kỳ vọng mẫu (*Expectation*) của một mẫu ngẫu nhiên là giá trị trung bình của mẫu đó:
$$\overline X=\frac{1}{n}\sum\_{i=1}^nX_i$$

Rõ ràng $\overline X$ cũng sẽ là một biến ngẫu nhiên và ta có thể tính được các đặc trưng của biến ngẫu nhiên này như:

| Đặc trưng | Giá trị |
|---|---|
| Kỳ vọng - $E[\overline X]$ | $\mu$ |
| Phương sai - $Var(\overline X)$ | $\dfrac{\sigma^2}{n}$ |

Chứng minh:
$$
\begin{aligned}
E[\overline X] &= E\bigg[\frac{1}{n}\sum\_{i=1}^nX_i\bigg]
\\cr\ &= \frac{1}{n}E\bigg\[\sum\_{i=1}^nX_i\bigg\]
\\cr\ &= \frac{1}{n}\sum\_{i=1}^nE[X_i]
\\cr\ &= \frac{1}{n}\sum\_{i=1}^n\mu
\\cr\ &= \mu
\end{aligned}
$$

$$
\begin{aligned}
Var[\overline X] &= Var\bigg[\frac{1}{n}\sum\_{i=1}^nX_i\bigg]
\\cr\ &= \frac{1}{n^2}Var\bigg\[\sum\_{i=1}^nX_i\bigg\]
\\cr\ &= \frac{1}{n^2}\sum\_{i=1}^nVar[X_i]
\\cr\ &= \frac{1}{n^2}\sum\_{i=1}^n\sigma^2
\\cr\ &= \frac{\sigma^2}{n}
\end{aligned}
$$

Như vậy là ta có thể thấy rằng giá trị kỳ vọng của biến ngẫu nhiên trung bình luôn là hằng số và bằng kỳ vọng của mẫu ngẫu nhiên. Tức là nếu ta lấy mẫu ngẫu nhiên từ 1 tập mẫu ra thì các tập mẫu ngẫu nhiên này luôn có cùng giá trị trung bình. Nói cách khác trung bình mẫu là không lệch (*unbiased*).

### 1.3.2. Phương sai mẫu
Phương sai mẫu $S^2$ là giá trị trung bình của phương sai của mẫu ngẫu nhiên:
$$S^2=\frac{1}{n}\sum\_{i=1}^n(X_i-\overline X)^2$$

Kỳ vọng của biến ngẫu nhiên $S^2$ sẽ là: $E[S^2]=\dfrac{n-1}{n}\sigma^2$. Như vậy là nó không còn bằng với phương sai của $X$ nữa, nên người ta thương lấy một dạng phương sai khác sao cho kỳ vọng của nó là bằng $\sigma^2$. Khái niệm này gọi là phương sai hiệu chỉnh, kí hiệu là $s^2$:
$$s^2=\frac{1}{n-1}\sum\_{i=1}^n(X_i-\overline X)^2$$

Chú ý rằng trong nhiều tài liệu người ta coi luôn phương sai hiệu chỉnh là phương sai mẫu.

Giá trị kỳ vọng của biến ngẫu nhiên phương sai hiệu chỉnh luôn là hằng số và bằng phương sai của mẫu ngẫu nhiên. Tức là nếu ta lấy mẫu ngẫu nhiên từ 1 tập mẫu ra thì các tập mẫu ngẫu nhiên này luôn có cùng giá trị kỳ vọng của phương sai. Nói cách khác phương sai hiệu chỉnh mẫu là không lệch (*unbiased*).

# 2. Ước lượng tham số
Là quá trình đi tìm tham số để mô tả quan hệ của các biến ngẫu nhiên. Trong phần [hợp nhiều biến ngẫu nhiên](/vi/2017/10/prob-rand-mulvar/) ta đã nói về khái niệm tương quan của các biến ngẫu nhiên và hệ số tương quan của chúng. Khi đó ta cũng đã nói qua về mô hình hồi quy (hay sự phụ thuộc tuyến tính) giữa 2 biến ngẫu nhiên $X,Y$: $Y=a+bX$. Tuy nhiên đó chỉ là một ví dụ đơn giản về việc tìm tham số $a,b$. Trong thực tế ta thường phải tìm tham số cho các mô hình xác suất phức tạp hơn nhiều như mô hình phân phối chuẩn chẳng hạn.

Quá trình ước lượng tham số này cũng chính là ý tưởng bên dưới của các bài toán học máy và nó được gọi là quá trình huấn luyện. Một bài toán học máy có chung 2 giai đoạn:

* ① Mô hình hoá tập mẫu (dữ liệu huấn luyện) bằng một mô hình xác suất với các tham số tương ứng
* ② Tìm các tham số đó bằng tập mẫu đã có. Hay còn gọi là học các tham số đó bằng dữ liệu huấn luyện.

Trong phần này ta sẽ coi tập mẫu là mẫu ngẫu nhiên và ta tìm hiểu 2 phương pháp tìm tham số chính là MLE và MAP.

## 2.1. Tham số mô hình phổ biến

## 2.2. MLE

## 2.3. MAP

# 3. Kết luận
