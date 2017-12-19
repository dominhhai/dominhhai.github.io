---
title: "[Giải Tích] Tập các kí hiệu toán học"
slug: math-notation
date: 2017-10-05
categories:
- Toán
tags:
- Kí hiệu
keywords:
- Math Notation
- Kí hiệu toán học
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/math/katex.png
metaAlignment: center
---
Bài viết này tổng hợp lại các kí hiệu toán học được sử dụng trong blog. Về cơ bản, tôi sẽ cố gắng đồng bộ hết sức có thể các kí hiệu này với các kí hiệu thường được các nhà học máy và toán học sử dụng. Ở đây tôi không đề cập tới cách tính từng phép toán cụ thể vì tôi đã trình bày trong các chuỗi bài về [Toán](/vi/categories/to%C3%A1n/) và [Xác Suất](/vi/categories/x%C3%A1c-su%E1%BA%A5t/) rồi.

<!--more-->

<!--toc-->
# Tập hợp
| Kí hiệu | Ý nghĩa |
| --- | --- |
| $\mathbb{A}$ | Tập $\mathbb{A}$ bất kì |
| $\mathbb{N}$ | Tập số tự nhiên |
| $\mathbb{Z}$ | Tập số nguyên |
| $\mathbb{Q}$ | Tập số hữu tỉ |
| $\mathbb{I}$ | Tập số vô tỉ |
| $\mathbb{R}$ | Tập số thực |
| $\\{x,y,z\\}$ | Tập chứa các phần tử $x,y,z$ |
| $\\{a_1,a_2,...,a_n\\}$ | Tập chứa các số nguyên từ $a_1$ tới $a_n$ |
| $[a,b]$ | Tập chứa các số thực trong khoảng $a<b$, bao gồm cả $a$ và $b$ |
| $(a,b)$ | Tập chứa các số thực trong khoảng $a<b$, **không** bao gồm cả $a$ và $b$ |
| $[a,b)$ | Tập chứa các số thực trong khoảng $a<b$, gồm $a$ nhưng **không** gồm $b$ |
| $(a,b]$ | Tập chứa các số thực trong khoảng $a<b$, gồm $b$ nhưng **không** gồm $a$ |
| $x^{(i)}$ | Đầu vào thứ $i$ trong tập huấn luyện |
| $y^{(i)}$ | Đầu ra thứ $i$ trong tập huấn luyện ứng với đầu vào $x^{(i)}$ |

# Số và ma trận
| Kí hiệu | Ý nghĩa |
| --- | --- |
| $a$ | Số thực $a$ |
| $\mathbf{a}$ | Véc-to $\mathbf{a}$ |
| $\mathbf{A}$ | Ma trận $\mathbf{A}$ |
| $[a_i]_n$ hoặc $(a_1,....,a_m)$ | Véc-to hàng $\mathbf{a}$ cấp $n$ |
| $[a_i]_n^{\intercal}$ hoặc $(a_1,....,a_m)^{\intercal}$ | Véc-to cột $\mathbf{a}$ cấp $n$ |
| $\mathbf{a}\in\mathbb{R^n}$ | Véc-to số thực $\mathbf{a}$ cấp $n$ |
| $[A\_{ij}]\_{mn}$ | Ma trận $\mathbf{A}$ cấp $m \times n$ |
| $\mathbf{A}\in\mathbb{R^{m \times n}}$ | Ma trận số thực $\mathbf{A}$ cấp $m \times n$ |
| $\mathbf{I}_n$ | Ma trận đơn vị cấp $n$ |
| $\mathbf{A}^{\dagger}$ | Giả nghịch đảo của ma trận $A$ (*Moore-Penrose pseudoinverse*) |
| $\mathbf{A}\odot\mathbf{B}$ | Phép nhân phần tử Hadamard của ma trận $\mathbf{A}$ với ma trận $\mathbf{B}$ (*element-wise (Hadamard)*) |
| $\mathbf{a}\otimes\mathbf{b}$ | Phép nhân ngoài của véc-to $\mathbf{a}$ với véc-to $\mathbf{b}$ (*outer product*): $\mathbf{a}\mathbf{b}^{\intercal}$ |
| $\Vert\mathbf{a}\Vert_p$ | Norm cấp $p$ của véc-to $\mathbf{a}$: $\Vert\mathbf{a}\Vert=\bigg(\sum_i\vert x_i\vert^p\bigg)^\frac{1}{p}$ |
| $\Vert\mathbf{a}\Vert$ | Norm cấp 2 của véc-to $\mathbf{a}$ (*độ dài véc-to*) |
| $a_i$ | Phần tử thứ $i$ của véc-to $\mathbf{a}$ |
| $A_{i,j}$ | Phần tử hàng $i$, cột $j$ của ma trận $\mathbf{A}$ |
| $A_{i_1:i_2,j_1:j_2}$ | Ma trận con từ hàng $i_1$ tới $i_2$ và cột $j_1$ tới $j_2$ của ma trận $\mathbf{A}$ |
| $A_{i,:}$ hoặc $\mathbf{A}^{(i)}$ | Hàng $i$ của ma trận $\mathbf{A}$ |
| $A_{:,j}$ | Cột $j$ của ma trận $\mathbf{A}$ |

# Giải tích
| Kí hiệu | Ý nghĩa |
| --- | --- |
| $f:\mathbb{A}\mapsto\mathbb{B}$ | Hàm số $f$ với tập xác định $A$ và tập giá trị $B$ |
| $f(x)$ | Hàm số 1 biến $f$ theo biến $x$ |
| $f(x,y)$ | Hàm số 2 biến $f$ theo biến $x$ và $y$ |
| $f(\mathbf{x})$ | Hàm số $f$ theo véc-to $\mathbf{x}$ |
| $f(\mathbf{x};\theta)$ | Hàm số $f$ theo véc-to $\mathbf{x}$ có tham số véc-to $\theta$ |
| $f(x)^{\prime}$ hoặc $\dfrac{df}{dx}$ | Đạo hàm của hàm $f$ theo $x$ |
| $\dfrac{\partial{f}}{\partial{x}}$ | Đạo hàm riêng của hàm $f$ theo $x$ |
| $\nabla_\mathbf{x}f$ | Gradient của hàm $f$ theo véc-to $\mathbf{x}$ |
| $\int_a^bf(x)dx$ | Tích phân tính theo $x$ trong khoảng $[a,b]$ |
| $\int_\mathbb{A}f(x)dx$ | Tích phân toàn miền $A$ của $x$ |
| $\int f(x)dx$ | Tích phân toàn miền giá trị của $x$ |
| $\log{x}$ hoặc $\ln{x}$ | Logarit tự nhiên: $\log{x}\triangleq\ln{x}\triangleq\log_e{x}$ |
| $\sigma(x)$ | Hàm sigmoid (*logistic sigmoid*): $\dfrac{1}{1+e^{-x}}=\dfrac{1}{2}\Bigg(\tanh\bigg({\dfrac{x}{2}}\bigg)+1\Bigg)$ |

# Xác suất thống kê
| Kí hiệu | Ý nghĩa |
| --- | --- |
| $\hat{y}$ | Đầu ra dự đoán |
| $\hat{p}$ | Xác suất dự đoán |
| $\hat{\theta}$ | Tham số ước lượng |
| $J(\theta)$ | Hàm chi phí (*cost function*) hay hàm lỗi (*lost function*) ứng với tham số $\theta$ |
| I.I.D | Mẫu ngẫu nhiên (*Independent and Identical Distribution*) |
| $LL(\theta)$ | Log Likelihood của tham số $\theta$ |
| MLE | Ước lượng hợp lý cực đại (*Maximum Likelihood Estimation*) |
| MAP | Cực đại xác suất hậu nghiệm (*Maximum A Posteriori*) |
