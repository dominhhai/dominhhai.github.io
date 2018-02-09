---
title: "[Tối Ưu] Nhân tử Lagrange với đẳng thức"
slug: lagrange-multipliers
date: 2018-02-09T11:51:56+09:00
categories:
- Toán
- Tối Ưu
tags:
- Tối Ưu
- Lagrange Multipliers
keywords:
- Lagrange Multipliers
- Optimization
- Tối ưu
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/math/katex.png
metaAlignment: center
draft: true
---
Phương pháp nhân tử Lagrange (*method of Lagrange multipliers*) là một kỹ thuật cực kì hữu dụng để giải các bài toán tối ưu có ràng buộc. Trong chuỗi bài viết này tối sẽ chia làm 3 phần: (1) Ràng buộc là đẳng thức; (2) Ràng buộc là bất đẳng thức; (3) Đối ngẫu. Bài viết đầu tiên này tôi sẽ tập trung vào tối ưu có ràng buộc là đẳng thức.
<!--more-->
<!--toc-->
# 1. Kỹ thuật Lagrange
## 1.1. Phát biểu bài toán
Tìm cực trị của hàm số đa biến $\color{#0c7f99}f(\mathbf{x})$ thoả mãn điều kiện hàm đa biến $\color{#bc2612}g(\mathbf{x})=c$ với $c$ là hằng số:
$$
\begin{aligned}
\text{maximize (or minimize)}&\color{#0c7f99}f(\mathbf{x})
\\cr\text{subject to:}~&\color{#bc2612}g(\mathbf{x}) = c
\end{aligned}
$$

## 1.2. Ứng dụng kỹ thuật nhân tử Lagrange
Để giải quyết bài toàn này, ta sử dụng kỹ thuật Lagrange như sau:

* **Bước 1**: Thêm một biến **nhân tử Lagrange** $\color{#0d923f}\lambda$ và định nghĩa một hàm **Lagrangian** $\mathcal{L}$ như sau:
$$\mathcal{L}(\mathbf{x},\textcolor{#0d923f}\lambda)=\textcolor{#0c7f99}{f(\mathbf{x})}-\textcolor{#0d923f}\lambda\big(\textcolor{#bc2612}{g(\mathbf{x})-c}\big)$$
* **Bước 2**: Giải đạo hàm (*gradient*) của $\mathcal{L}$ bằng véc-to $\mathbf{0}$:
$$\nabla\mathcal{L}(\mathbf{x},\textcolor{#0d923f}\lambda)=\mathbf{0}$$
* **Bước 3**: Dựa vào các nghiệm $(\mathbf{x^* },\textcolor{#0d923f}\lambda^* )$ tìm được ở trên, thế vào hàm $\color{#0c7f99}f(\mathbf{x})$ rồi chọn giá trị lớn nhất (nhỏ nhất) là ta được giá trị cần tìm (thực ra chỉ cần nghiệm $\mathbf{x^* }$ là đủ):
$$
\begin{cases}
\textcolor{blue}{f\_{min}} &= \displaystyle\min\_{\mathbf{x^* }}\color{#0c7f99}f(\mathbf{x^* })
\\cr
\textcolor{red}{f\_{max}} &= \displaystyle\max\_{\mathbf{x^* }}\color{#0c7f99}f(\mathbf{x^* })
\end{cases}
$$

Nếu bạn để ý một chút thì phương trình ở bước 2 tương đương với hệ phương trình sau:
$$
\begin{cases}
\nabla\textcolor{#0c7f99}{f(\mathbf{x})} &= \textcolor{#0d923f}\lambda\nabla\textcolor{#bc2612}{g(\mathbf{x})}
\\cr
\color{#bc2612}g(\mathbf{x}) &= \color{#bc2612}c
\end{cases}
$$

Bởi:
$$
\nabla\mathcal{L}(\mathbf{x},\textcolor{#0d923f}\lambda)=
\begin{bmatrix}
\dfrac{\partial\mathcal{L}}{\partial\mathbf{x}}
\\cr\\cr
\dfrac{\partial\mathcal{L}}{\partial\mathbf{\textcolor{#0d923f}\lambda}}
\end{bmatrix}=
\begin{bmatrix}
\nabla\textcolor{#0c7f99}{f(\mathbf{x})}-\textcolor{#0d923f}\lambda\nabla\textcolor{#bc2612}{g(\mathbf{x})}
\\cr
\color{#bc2612}g(\mathbf{x})-c
\end{bmatrix}
$$

Tức là ở đây, khi giải bằng tay bạn có thể làm ngơ hàm $\mathcal{L}(\mathbf{x},\textcolor{#0d923f}\lambda)$ mà vẫn giải tốt. Tuy nhiên, việc biểu diễn qua hàm *Lagrangian* này sẽ giúp ta dễ dàng sài luôn được các cách giải phổng thông khác và các chương trình máy tính có sẵn.

# 2. Ví dụ minh họa
## 2.1. Bài toán lợi nhuận
**Bài toán:**<br>Giả sử nhà máy của bạn sản suất thiết bị phụ tùng bằng thép. Chi phí nhân công mỗi giờ là $\$20$ và giá 1 tấn thép là $\$170$. Lợi nhuận $R$ được mô hình hoá như sau:

$$R(h,s)=200h^{{2}/{3}}s^{{1}/{3}}$$
Trong đó:

* $h$ là số giờ làm việc
* $s$ là số tấn thép

Hãy tính lợi nhuận lớn nhất có thể thu được nếu kinh phí của bạn là $\$20,000$.

**Lời giải:**<br>
Mỗi giờ làm việc tốn $\$20$ và mỗi tấn thép tốn $\$170$ nên tổng chi phí tính theo $h$ và $s$ là:
$$B(h,s)=20h+170s$$
Do kinh phí $B$ là $\$20,000$ nên ta có ràng buộc:
$$\color{#bc2612}20h+170s=20,000$$

Để có cái nhìn rõ ràng hơn về bài toán, ta thử biểu diễn nó qua đồ thị như sau:

{{< image classes="fancybox center" thumbnail-width="60%" src="https://res.cloudinary.com/dominhhai/image/upload/math/lagrange-multipliers-1.png" title="Đồ thị lợi nhuận và ràng buộc" >}}

Nhìn vào đồ thị trên ta có thể thấy lợi nhuận (đường màu xanh) đạt lớn nhất với điều kiện ngân quỹ (đường màu đỏ) tại điểm giao bên trái của 2 đường.

Cái nhìn trực quan là thế, còn giờ ta sẽ giải bằng phương pháp nhân tử Lagrange để tối ưu hoá hàm $\color{#0c7f99}R(h,s)$ ràng buộc bởi đẳng thức $\color{#bc2612}{B(h,s)}=20,000$. Theo phân tích ở trên ta sẽ có:
$$
\begin{cases}
\nabla\textcolor{#0c7f99}{R(h,s)} &= \textcolor{#0d923f}\lambda\nabla\textcolor{#bc2612}{B(h,s)}
\\cr
\color{#bc2612}B(h,s) &= \color{#bc2612}20,000
\end{cases}
$$

Phân tích ra ta được:
$$
\begin{cases}
\color{#0c7f99}200\cdot\dfrac{2}{3}h^{-{1}/{3}}s^{{1}/{3}} &= 20\textcolor{#0d923f}\lambda
\\cr\\cr
\color{#0c7f99}200\cdot\dfrac{1}{3}h^{{2}/{3}}s^{-{2}/{3}} &= 170\textcolor{#0d923f}\lambda
\\cr\\cr
\color{#bc2612}20h+170s &= \color{#bc2612}20,000
\end{cases}
$$

Giải ra ta có kết quả:
$$
\begin{cases}
\textcolor{#0c7f99}h &= \dfrac{2,000}{3} \approx 667
\\cr\\cr
\textcolor{#0c7f99}s &= \dfrac{2,000}{51} \approx 39
\\cr\\cr
\color{#0d923f}\lambda &= \sqrt[3]{\dfrac{8,000}{459}} \approx 2.593
\end{cases}
$$

Thế vào công thức tính lợi nhuận ta có:
$$R(667, 39)=200(667)^{{2}/{3}}(39)^{{1}/{3}} \approx \fcolorbox{red}{aqua}{51,777}$$

Như vậy, để đạt được lợi nhuận lớn nhất ta cần 667 giờ lao động với 39 tấn thép và lợi nhận có thể đạt được tối đa là $\$51,777$.

## 2.2. Cực đại hoá tích 2 véc-tơ

# 3. Phân tích Lý thuyết
## 3.1. Cái nhìn hình học
## 3.2. Hình thành
