---
title: "[Tối Ưu] Nhân tử Lagrange với bất đẳng thức"
slug: lagrange-multipliers-2
date: 2018-02-13T11:51:56+09:00
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
---
Trong phần trước ta đã cùng bàn về phương pháp nhân tử Lagrange với điều kiện ràng buộc là các đẳng thức. Trong phần này ta sẽ cùng tổng quát hoá bài toán với điều kiện ràng buộc bao gồm cả các bất đẳng thức. Nhóm các điều kiện tổng quát như vậy có tên gọi là **KKT** (*Karush–Kuhn–Tucker conditions*).
<!--more-->
<!--toc-->
# 1. Kỹ thuật Lagrange
## 1.1. Phát biểu bài toán
Tìm cực trị của hàm số đa biến $\color{#0c7f99}f(\mathbf{x})$ thoả mãn điều kiện hàm đa biến $\color{#bc2612}g(\mathbf{x})=c$ và $\color{#bc2612}h(\mathbf{x})=r$ với $c,r$ là hằng số:
$$
\begin{aligned}
\text{maximize (or minimize)}&\color{#0c7f99}f(\mathbf{x})
\\cr\text{subject to:}~&\color{#bc2612}g(\mathbf{x}) = c
\\cr\text{and}~&\color{#bc2612}h(\mathbf{x})\le r
\end{aligned}
$$

## 1.2. Ứng dụng kỹ thuật nhân tử Lagrange
Để giải quyết bài toàn này, ta sử dụng kỹ thuật Lagrange như sau:

* **Bước 1**: Định nghĩa một hàm **Lagrangian** $\mathcal{L}$ như sau:
$$\mathcal{L}(\mathbf{x},\textcolor{#0d923f}{\lambda,\mu})=\textcolor{#0c7f99}{f(\mathbf{x})}-\textcolor{#0d923f}\lambda\big(\textcolor{#bc2612}{g(\mathbf{x})-c}\big)-\textcolor{#0d923f}\mu\big(\textcolor{#bc2612}{h(\mathbf{x})-r}\big)$$
Trong đó, $\color{#0d923f}{\lambda,\mu}$ là các biến (hằng số) thêm vào.
* **Bước 2**: Giải hệ phương trình để tìm các điểm rơi:
$$
\begin{cases}
\nabla\mathcal{L}(\mathbf{x},\textcolor{#0d923f}{\lambda,\mu})=\mathbf{0}
\\cr
\textcolor{#0d923f}\mu\big(\textcolor{#bc2612}{h(\mathbf{x})-r}\big)=0
\end{cases}
$$
* **Bước 3**: Dựa vào các nghiệm $(\mathbf{x^* },\textcolor{#0d923f}{\lambda^* ,\mu^* })$ tìm được ở trên, thế vào hàm $\color{#0c7f99}f(\mathbf{x})$ rồi chọn giá trị lớn nhất (nhỏ nhất) là ta được giá trị cần tìm (thực ra chỉ cần nghiệm $\mathbf{x^* }$ là đủ):
$$
\begin{cases}
\textcolor{blue}{f\_{min}} &= \displaystyle\min\_{\mathbf{x^* }}\color{#0c7f99}f(\mathbf{x^* })
\\cr
\textcolor{red}{f\_{max}} &= \displaystyle\max\_{\mathbf{x^* }}\color{#0c7f99}f(\mathbf{x^* })
\end{cases}
$$
Lưu ý rằng:
  * **Cực đại** chỉ đạt được khi $\textcolor{#0d923f}\mu^* \ge 0$, tức: $-\textcolor{#0d923f}\mu^* \big(\textcolor{#bc2612}{h(\mathbf{x})-r}\big) \ge 0$
  * **Cực tiểu** chỉ đạt được khi $\textcolor{#0d923f}\mu^* \le 0$, tức: $-\textcolor{#0d923f}\mu^* \big(\textcolor{#bc2612}{h(\mathbf{x})-r}\big) \le 0$

## 1.3. Ví dụ minh họa
**Bài toán:**<br>Tìm giá trị lớn nhất của hàm số:
$$f(x)=x^3-3x$$
Biết rằng: $x\le 2$.

**Lời giải:**<br>
Với $\mu\ge 0$ (bài toán tìm cực đại), hàm Lagrangian lúc này:
$$\mathcal{L}(\mathbf{x},\textcolor{#0d923f}\mu)=x^3-3x-\mu(x-2)$$
Để tìm các điểm rơi, ta giải hệ sau:
$$
\begin{cases}
3x^2-3-\mu=0
\\cr
\mu(x-2)=0
\\cr
x\le 2
\\cr
\mu\ge 0
\end{cases}
$$

Ta phân làm 2 trường hợp để thoả mãn: $\mu(x-2)=0$ là *(i)* $\mu=0$; *(ii)* $x=2$.

* *(i)* Nếu $\mu=0$ thì $x=1$ hoặc $x=-1$, từ đó ta có $f(1)=-2$ và $f(1)=2$
* *(ii)* Nếu $x=2$ thì $\mu=9$, từ đó ta có $f(2)=2$

Dựa vào các điểm rơi ở trên, ta thấy rằng $x=-1$ hoặc $x=2$ thì ta sẽ được giá trị lớn nhất của $f(x)$ là 2.

# 2. Tổng quát hoá
Tương tự như tổng quát hoá của điều kiện đẳng thức, ta cũng có thể tổng quát hoá điều kiện bất đẳng thức cho nhiều ràng buộc bất đẳng thức.

Giả sử ta cần tối ưu hàm số đa biến:
$$
\begin{aligned}
\text{maximize (or minimize)}&\color{#0c7f99}f(\mathbf{x})
\\cr\text{subject to:}~&\color{#bc2612}g_i(\mathbf{x}) = c_i
\\cr\text{and}~&\color{#bc2612}h_j(\mathbf{x})\le r_j
\end{aligned}
$$

Lúc này để dựng hàm Lagrangian, ta thêm vào các biến $\color{#0d923f}\lambda_i$ tương ứng với mỗi điều kiện $\color{#bc2612}g_i(\mathbf{x})=c_i$ và các biến $\color{#0d923f}\mu_j$ tương ứng với mỗi điều kiện $\color{#bc2612}h_i(\mathbf{x})\le r_j$:
$$\mathcal{L}(\mathbf{x},\textcolor{#0d923f}{\lambda,\mu})=\textcolor{#0c7f99}{f(\mathbf{x})}-\sum\_{i=1}^m\textcolor{#0d923f}{\lambda_i}\big(\textcolor{#bc2612}{g_i(\mathbf{x})-c_i}\big)-\sum\_{j=1}^n\textcolor{#0d923f}{\mu_j}\big(\textcolor{#bc2612}{h_j(\mathbf{x})-r_j}\big)$$

Ở đây, $\textcolor{#0d923f}{\lambda,\mu}$ được hiểu là véc-to chứa tất cả các $\textcolor{#0d923f}{\lambda_i,\mu_j}$ thành phần nhé.

Tiếp theo, để tìm điểm rơi, ta có hệ phương trình:
$$
\begin{cases}
\nabla\mathcal{L}(\mathbf{x},\textcolor{#0d923f}{\lambda,\mu})=\mathbf{0}
\\cr
\textcolor{#0d923f}\mu_j\big(\textcolor{#bc2612}{h_j(\mathbf{x})-r_j}\big)=0
\end{cases}
$$

Để có cực trị thì các $\textcolor{#0d923f}\mu\neq\mathbf{0}$, tức là các $\color{#0d923f}\mu_j$ không đồng thời bằng $0$, hơn nữa:

* **Cực đại** chỉ đạt được khi $\textcolor{#0d923f}{\mu_j} \ge 0 ~~~,\forall{j}$, tức: $-\textcolor{#0d923f}\mu_j\big(\textcolor{#bc2612}{h_j(\mathbf{x})-r_j}\big)\ge 0$
* **Cực tiểu** chỉ đạt được khi $\textcolor{#0d923f}{\mu_j}\le 0 ~~~,\forall{j}$, tức: $-\textcolor{#0d923f}\mu_j\big(\textcolor{#bc2612}{h_j(\mathbf{x})-r_j}\big)\le 0$

Như vậy ta có thể thấy bằng phương pháp Lagrange, ta có thể giải quyết một lớp kha khá các bài toán tối ưu có ràng buộc bằng cách giải đạo hàm của hàm Lagrangian khá mạnh mẽ và tiện lợi.
