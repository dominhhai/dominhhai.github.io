---
title: "[Giải Tích] Đạo hàm với vec-tơ, ma trận, ten-xơ"
slug: matrix-derivs
date: 2018-04-24
categories:
- Toán
- Giải Tích
tags:
- Giải Tích
- Đạo Hàm
keywords:
- Calculus
- Giải Tích
- Đạo Hàm vertor, matrix, tensor
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/math/katex.png
metaAlignment: center
---
Bài viết này sẽ giới thiệu cách lấy đạo hàm của vec-tơ, ma trận và ten-xơ (mảng nhiều chiều) và lấy đạo hàm theo vec-tơ, ma trận và ten-xơ.

<!-- toc -->
# 1. Quy hoạch động
Làm quá nhiều việc 1 lúc rất dễ dẫn tới sai lầm, chính vì vậy mà người ta cần phân tách vấn đề ra thành các bài toán con để giải quyết rồi gộp kết quả lại. Việc tính đạo hàm vec-tơ, ma trận hay ten-xơ cũng vậy khi tính đạo hàm ta có thể gặp sai sót nếu tính đạo hàm cho nhiều thành phần đồng thời, lấy đạo hàm của các thành phần có các kí hiệu gộp như cộng, nhân, áp dụng quy tắc chuỗi cho nhiều thành phần cùng lúc. Chính vì vậy để dễ dàng hơn, trước hết ta cần phân tách ra các thành phần riêng rẽ để cho đỡ nhầm.

## 1.1. Phân rã các thành phần
Để đơn giản cho việc tính toán, trước tiên ta phân rã biểu thức ra thành các thành phần biến đơn lẻ. Bởi khi biểu diễn thông qua các biến đơn lẻ này, ta có thể dễ dàng lấy được đạo hàm như cách ta làm với các hàm đại số thông thường.

Ví dụ, giả sử ta có véc-tơ cột $\mathbf{y}\in\mathbb{R}^{n1}$ được tạo bởi tích của ma trận $\mathbf{W}\in\mathbb{R}^{nm}$ và vec-tơ cột $\mathbf{x}\in\mathbb{R}^{m1}$:

$$\mathbf{y}=\mathbf{W}\mathbf{x}$$

Giờ ta muốn lấy đạo hàm của $\mathbf{y}$ theo $\mathbf{x}$. Dễ dàng thấy, ta sẽ có $n\times m$ đạo hàm riêng của $n$ từng thành phần véc-tơ $\mathbf{y}$ theo mỗi $m$ thành phần của véc-tơ $\mathbf{x}$.

Đặt $\dfrac{\partial{y_3}}{\partial{x_7}}$ là đạo hàm riêng của thành phần thứ 3 của véc-tơ $\mathbf{y}$ theo thành phần thứ 7 của véc-tơ $\mathbf{x}$. Để tính đạo hàm riêng này, trước tiên ta viết công thức của tính $y_3$ ra như sau:

$$y_3=\sum\_{j=1}^mW\_{3,j}x_j$$

Như vậy thay vì nhìn cả ma trận phức tạp, ta bóc tách thành phần cần tính $y_3$ ra đơn giản hơn nhiều.

## 1.2. Bỏ các kí hiệu cộng, nhân
Nhìn các kí hiệu cộng, nhân ta chưa nhìn thấy ngay được sự phụ thuộc của các phần tử trong công thức, nên bước loại bỏ các kí hiệu này giúp ta có cái nhìn trực quan hơn về biến phụ thuộc.

Ở ví dụ trên ta viết lại $y_3$ như sau:

$$y_3=W\_{3,1}x_1+W\_{3,2}x_2+\ldots+W\_{3,7}x_7+\ldots+W\_{3,m}x_m$$

Từ đây ta có thể thấy $y_3$ phụ thuộc vào $x_7$ chỉ đơn giản bằng một tích $W\_{3,7}x_7$, nên đạo hàm của $y_3$ theo $x_7$ sẽ bằng $W\_{3,7}$:

$$
\begin{aligned}
\frac{\partial{y_3}}{\partial{x_7}} &= \frac{\partial}{\partial{x_7}}\Big(W\_{3,1}x_1+W\_{3,2}x_2+\ldots+W\_{3,7}x_7+\ldots+W\_{3,m}x_m\Big)
\\cr
&= 0 + 0 + \ldots + W\_{3,7} + \ldots + 0
\\cr
&= W\_{3,7}
\end{aligned}
$$

Tương tự với các thành phần khác của $y$ và $x$ ta sẽ có:

$$\dfrac{\partial{y_i}}{\partial{x_j}}=W\_{i,j}$$

## 1.3. Gộp kết quả lại

Nhóm kết quả lại ta sẽ thu được ma trận Jacobi $\mathbf{J}\in\mathbb{R}^{nm}$:

$$
\begin{bmatrix}
\dfrac{\partial{y_1}}{\partial{x_1}} & \dfrac{\partial{y_1}}{\partial{x_2}} & \dots & \dfrac{\partial{y_1}}{\partial{x_m}}
\\cr\\cr
\dfrac{\partial{y_2}}{\partial{x_1}} & \dfrac{\partial{y_2}}{\partial{x_2}} & \dots & \dfrac{\partial{y_2}}{\partial{x_m}}
\\cr\\cr
\vdots & \vdots & \ddots & \vdots
\\cr\\cr
\dfrac{\partial{y_n}}{\partial{x_1}} & \dfrac{\partial{y_n}}{\partial{x_2}} & \dots & \dfrac{\partial{y_n}}{\partial{x_m}}
\end{bmatrix}
=\begin{bmatrix}
W\_{1,1} & W\_{1,2} & \dots & W\_{1,m}
\\cr\\cr
W\_{2,1} & W\_{1,2} & \dots & W\_{2,m}
\\cr\\cr
\vdots & \vdots & \ddots & \vdots
\\cr\\cr
W\_{n,1} & W\_{n,2} & \dots & W\_{n,m}
\end{bmatrix}
$$

Điều này tương đương với chuyện đạo hàm của $\mathbf{y}=\mathbf{W}\mathbf{x}$ theo $\mathbf{x}$ chính là ma trận $\mathbf{W}$:
$$\frac{d\mathbf{y}}{d\mathbf{x}}=\mathbf{W}$$

Bằng phép phân tích như trên, ta có thể thấy việc tính đạo hàm không hề khó khăn nếu ta cứ bóc tách nhỏ tầng thành phần ra để tính riêng biệt rồi gộp kết quả lại.

## 1.4. Hoán đổi vec-tơ cột với hàng
Tương tự nếu, $\mathbf{y}\in\mathbb{R}^{1n}$ là véc-tơ hàng được tạo bởi tích của vec-tơ hàng $\mathbf{x}\in\mathbb{R}^{1m}$ ma trận $\mathbf{W}\in\mathbb{R}^{mn}$:

$$\mathbf{y}=\mathbf{x}\mathbf{W}$$

Thì đạo hàm riêng:

$$\dfrac{\partial{y_i}}{\partial{x_j}}=W\_{j,i}$$

Như vậy, đạo hàm của véc-tơ $\mathbf{y}$ theo véc-tơ $\mathbf{x}$ là:
$$\frac{d\mathbf{y}}{d\mathbf{x}}=\mathbf{W}$$


# 2. Trên 2 chiều thì làm thế nào?
# 2.1. Ví dụ 1
Giờ ta thử tính đạo hàm của véc-tơ $\mathbf{y}$ theo ma trận $\mathbf{W}$ xem sao:
$$\frac{d\mathbf{y}}{d\mathbf{W}}$$

Lúc này, $\mathbf{y}$ là dữ liệu 1 chiều còn $\mathbf{W}$ là dữ liệu 2 chiều, nên đạo hàm sẽ ở dạng dữ liệu mảng 3 chiều (ten-xơ 3 chiều).

Tương tự như phép phân tích ở trên, ta thí dụ tính đạo hàm riêng của $y\_3$ là phần tử thứ 3 của véc-tơ $\mathbf{y}$ theo $W\_{7,8}$ là phần tử ở hàng 7, cột 8 của ma trận $\mathbf{W}$:

$$y\_3=x\_1W\_{1,3}+x\_2W\_{2,3}+\dots+x\_mW\_{m,3}$$

Ở đây, rõ ràng là $y\_3$ khônng hề phụ thuộc vào $W\_{7,8}$ nên đạo hàm riêng tương ứng là $0$:

$$\frac{\partial{y_3}}{\partial{W\_{7,8}}}=0$$

Tuy vậy, $y_3$ lại phụ thuộc vào cột thứ 3 của ma trận $\mathbf{W}$ nên đạo hàm riêng của nó theo các phần tử cột này là khác không, ví dụ đạo hàm riêng của $y\_3$ theo $W\_{2,3}$ là:

$$\frac{\partial{y_3}}{\partial{W\_{2,3}}}=x_2$$

Một cách tổng quát, ta có:
$$
\frac{\partial{y_i}}{\partial{W\_{j,k}}} = \begin{cases}
x_j ~~~ \text{if } i=k
\\cr
0 ~~~ \text{otherwise}
\end{cases}
$$

Nếu ta gọi $\mathsf{F}\in\mathbb{R}^{mnn}$ là ten-xơ 3 chiều biểu diễn cho đạo hàm của vec-tơ $\mathbf{y}\in\mathbb{R}^{1n}$ theo ma trận $\mathbf{W}\in\mathbb{R}^{mn}$:
$$F\_{i,j,k}=\frac{\partial{y_i}}{\partial{W\_{j,k}}}$$

Khi đó, ta có:
$$
F\_{i,j,k} = \begin{cases}
x_j ~~~ \text{if } i=k
\\cr
0 ~~~ \text{otherwise}
\end{cases}
$$

Nếu sử dụng ma trận $\mathbf{G}\in\mathbb{R}^{mn}$, sao cho:
$$G\_{i,j}=F\_{i,j,i}$$

thì ta có thể thấy rằng $\mathbf{G}$ có thể lưu trữ đầy đủ thông tin đạo hàm riêng, hay nói cách khác ta có thể sử dụng dữ liệu 2 chiều để biểu diễn đạo hàm của thay vì dữ liệu 3 chiều như ten-xơ $\mathsf{F}$ ở trên.

> Lưu ý tới điểm này bởi nó rất hay được sử dụng khi tính đạo hàm trong mạng NN để tận dụng khả năng tính toán của các thư viện.

# 2.2. Ví dụ 2
Ở ví dụ này, thay vì véc-tơ $\mathbf{x}\in\mathbb{R}^{1,m}$ ta tổng quát hoá thành ma trận $\mathbf{X}\in\mathbb{R}^{nm}$, ta có:

$$\mathbf{Y}=\mathbf{X}\mathbf{W}$$

Lúc đó, mỗi thành phần của $\mathbf{Y}$ sẽ được biểu diễn như sau:
$$Y\_{i,j}=\sum\_{k=1}^mX\_{i,k}W\_{k,j}$$

Dễ dàng có thể thấy đạo hàm riêng của $Y\_{a,b}$ theo $X\_{c,d}$ là:
$$
\frac{\partial{Y\_{a,b}}}{\partial{X\_{c,d}}} = \begin{cases}
W\_{d,b} ~~~ \text{if } a=c
\\cr
0 ~~~ \text{otherwise}
\end{cases}
$$

Nếu lấy $\mathbf{Y}\_{i,:}$ là hàng thứ $i$ của $\mathbf{Y}$ và $\mathbf{X}\_{i,:}$ là hàng thứ $i$ của $\mathbf{X}$ thì rõ ràng:
$$\frac{\partial{\mathbf{Y}\_{i,:}}}{\partial{\mathbf{X}\_{i,:}}}=W$$

Đây cũng chính là trường hợp tổng quát của công thức tính đạo hàm ở [phần 1](#1-4-ho%C3%A1n-%C4%91%E1%BB%95i-vec-t%C6%A1-c%E1%BB%99t-v%E1%BB%9Bi-h%C3%A0ng).

# 3. Quy tắc chuỗi
Quy tắc chuỗi dùng để tính [đạo hàm của hàm hợp](/vi/2017/10/multi-var-func/#5-đạo-hàm-riêng-của-hàm-hợp) sẽ được áp dụng thế nào cho các phép kết hợp của véc-tơ, ma trận?

Giả sử, ta có các véc-tơ cột $\mathbf{y}$ và $\mathbf{x}$:
$$\mathbf{y} = \mathbf{V}\mathbf{W}\mathbf{x}$$

Thử tính đạo hàm của $\mathbf{y}$ theo $\mathbf{x}$ xem sao. Đầu tiên ta nhận xét rằng, tích của 2 ma trận $\mathbf{V}$ và $\mathbf{W}$ chỉ đơn giản là một ma trận khác $\mathbf{U}$, vì thế ta có:
$$\frac{d\mathbf{y}}{d\mathbf{x}}=\mathbf{V}\mathbf{W}=\mathbf{U}$$

Tuy nhiên, để hiểu được quy tắc chuỗi áp dụng ra sao thì ta sẽ đưa vào các kết quả trung gian để sử dụng được quy tắc chuỗi trong trường hợp này. Giả sử véc-tơ $\mathbf{z}$ được định nghĩa như sau:
$$\mathbf{z}=\mathbf{W}\mathbf{x}$$

Thì:
$$\mathbf{y}=\mathbf{V}\mathbf{z}$$

Từ đây, ta có thể sử dụng quy tắc chuỗi như sau:
$$\frac{d\mathbf{y}}{d\mathbf{x}}=\frac{d\mathbf{y}}{d\mathbf{z}}\frac{d\mathbf{z}}{d\mathbf{x}}$$

Để chắc chắn rằng ta thực sự hiểu ý nghĩa của nó là gì, ta lại vận dụng chiến lược phân tách ở trên để phân tích các thành phần ra, bắt đầu với mỗi thành phần của véc-tơ $\mathbf{y}$ với mỗi thành phần của véc-tơ $\mathbf{x}$:

$$\frac{dy_i}{dx_j}=\frac{dy_i}{d\mathbf{z}}\frac{d\mathbf{z}}{dx_j}$$

Áp dụng tiếp [quy tắc chuỗi của hàm nhiều biến](/vi/2017/10/multi-var-func/#5-đạo-hàm-riêng-của-hàm-hợp), giả sử rằng $\mathbf{z}$ có $K$ thành phần thì ta có:
$$\frac{dy_i}{dx_j}=\sum\_{k=1}^K\frac{dy_i}{dz_k}\frac{dz_k}{dx_j}$$

Như đã chứng minh ở trên (đạo hàm của véc-tơ theo véc-tơ) thì ta có:
$$
\begin{aligned}
\frac{dy_i}{dz_k} &= V\_{i,k}
\\cr
\frac{dz_k}{dx_j} &= W\_{k,j}
\end{aligned}
$$

Nên ta có:

$$\frac{dy_i}{dx_j}=\sum\_{k=1}^KV\_{i,k}W\_{k,j}=\mathbf{V}\_{i,:}\mathbf{W}\_{:,j}$$

Tới đây, ta được điều phải chứng minh.

Như vậy, ta có thể sử dụng quy tắc chuỗi trong nhóm của các véc-tơ và ma trận bằng cách:

* Bóc tách các kết quả và biến trung gian để biểu diễn
* Biểu diễn quy tắc chuỗi cho từng thành phân riêng của đạo hàm đích
* Lấy tổng lại các kết quả trung gian với quy tắc chuỗi.

> Tham khảo: http://cs231n.stanford.edu/vecDerivs.pdf