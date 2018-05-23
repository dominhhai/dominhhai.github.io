---
title: "[Giải Tích] Softmax và đạo hàm"
slug: softmax-derivs
date: 2018-04-25
categories:
- Toán
- Giải Tích
tags:
- Giải Tích
- Đạo Hàm
keywords:
- Calculus
- Giải Tích
- softmax
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/math/katex.png
metaAlignment: center
---
Softmax rất hay được ứng dụng trong các bài toán phân loại nhiều lớp nên việc tìm hiểu về nó giúp ta dễ dàng cài đặt thuật toán với hàm số này. Trước đây, tôi có đề cập đôi chút về hàm số này trong bài logistic regression cho việc tìm hàm lỗi với bài toán phân loại đa lớp, nếu bạn hứng thú thì có thể xem lại [tại đây](/vi/2017/12/ml-logistic-regression/#5-2-dựa-theo-mô-hình-xác-suất-nhiều-nhóm). Còn trong khuôn khổ bài viết này tôi chỉ đề cập tới việc thuần toán học mà thôi.

<!-- toc -->

# 1. Hàm softmax
## 1.1. Định nghĩa
Hàm softmax nhận đầu vào là một vec-tơ và cho đầu ra là 1 vec-tơ có cùng số chiều $s(x):\mathbb{R}^n\mapsto\mathbb{R}^n$. Công thức của hàm như sau:

$$s_i = \frac{\exp(x_i)}{\sum_j\exp(x_j)}$$

Ở đây, ta có 3 nhận xét:

* $0\le s_i\le 1$
<br>*Do $\exp(x)=e^x\ge 0$ với mọi $x$ nên $0\le s_i\le 1$ với mọi $i,x$*.
* $s$ là hàm đồng biến
<br>*$\exp(x)$ là hàm dồng biến mà mẫu số lại không đổi nên $s$ cũng là đồng biến. Tức là, nếu $x_i<x_j$ thì $s_i<s_j$. Hay nói cách khác, thứ tự các phần tử tương ứng ở vec-tơ đầu ra là không đổi*.
* $\sum_i s_i = 1$
<br>*Cái này thì có thể nhìn thấy ngay rồi!*

Nhận xét trên làm ta liên tưởng tới xác suất!

$$s_i = p(y=i|\mathbf{x})$$

Trong đó, $y$ là nhãn tương ứng với dữ liệu $\mathbf{x}$: $y=\mathbf{W}\cdot\mathbf{x}+b$, còn $i\in\[1, n\]$ là một nhãn trong tập các nhãn. Cụ thể phần này bạn có thể đọc thêm [tại đây](/vi/2017/12/ml-logistic-regression/#5-2-dựa-theo-mô-hình-xác-suất-nhiều-nhóm).

## 1.2. Cài đặt
Việc cài đặt hàm này có thể thực hiện như sau:

{{< codeblock "softmap.py" "python" >}}
def softmax(x):
  e = np.exp(x)
  
  return e / np.sum(e)
{{< /codeblock >}}

Tuy nhiên, do là hàm mũ nên rất dễ xảy ra hiện tượng tràn số nếu các giá trị của $\mathbf x$ lớn (*1000 trở lên chẳng hạn*), nên thường người ta thường sử dụng phương pháp bớt đi 1 lượng hằng số như sau:

$$s_i = \frac{\exp(x_i + C)}{\sum_j\exp(x_j + C)}$$

Không khó để chứng minh công thức này, giả sử $\xi\ne 0$ là một hằng số bất kì, ta có:
$$
\begin{aligned}
s_i &= \frac{\exp(x_i)}{\sum_j\exp(x_j)}
\\cr
&= \frac{\xi\exp(x_i)}{\sum_j\xi\exp(x_j)}
\\cr
&= \frac{\exp(x_i+\ln\xi)}{\sum_j\exp(x_j+\ln\xi)}
\end{aligned}
$$

Đặt $C=\ln\xi$ thì $C$ cũng là một hằng số, như vậy ta được điều cần chứng minh.

Giả sử rằng các giá trị của $\mathbf x$ không quá xa nhau, chọn $C=-\max(\mathbf x)$, ta có thể cài đặt như sau:

{{< codeblock "softmap.py" "python" >}}
def softmax_stable(x):
  _x = x - np.max(x)
  e = np.exp(_x)
  
  return e / np.sum(e)
{{< /codeblock >}}

# 2. Đạo hàm
## 2.1. Đạo hàm riêng
Theo tư tưởng phân tách bài toán như trình bày ở [bài viết trước](/vi/2018/04/matrix-derivs/), để đơn giản trước tiên ta tính đạo hàm riêng cho từng thành phần của $\mathbf{s}$ và $\mathbf{x}$.

Đặt: $g_i(x) = e^{x_i}$ và $h(x) = \sum_j e^{x_j}$, ta có:

$$s_i=\frac{g_i(x)}{h(x)}$$

Đặt $\partial_{ij}$ là đạo hàm riêng của $s_i$ theo $x_j$, ta có:

$$\partial_{ij}=\frac{\partial{s_i}}{\partial{x_j}}=\frac{g_i^{\prime}(x_j)h(x)-h^{\prime}(x_j)g_i(x)}{h(x)^2}~~~(1)$$

Mặt khác, $g_i^{\prime}(x)$ chỉ có 1 phần tử là $e^{x_i}$ nên đạo hàm của $g_i$ theo $x_j$ là:
$$
g_i^{\prime}(x_j) = \begin{cases}
e^{x_i} &\text{if } i = j
\\cr
0 &\text{if } i \ne j
\end{cases}
~~~(2)
$$

Tương tự, $h(x) = \sum_j e^{x_j}=e^{x_1}+e^{x_1}+\dots+e^{x_j}+\dots+e^{x_n}$ luôn chứa 1 phần tử $e^{x_j}$, nên đạo hàm của nó theo $x_j$ là:
$$h^{\prime}(x_j)=e^{x_j}~~~(3)$$

Thế $(2), (3)$ vào $(1)$, ta có:
$$
\begin{aligned}
\partial_{ij} &= \begin{cases}
\dfrac{e^{x_i}h(x)-e^{x_j}e^{x_i}}{h(x)^2} &\text{if } i = j
\\cr\\cr
\dfrac{-e^{x_j}e^{x_i}}{h(x)^2} &\text{if } i \ne j
\end{cases}
\\cr
&= \begin{cases}
\dfrac{e^{x_i}}{h(x)}\bigg(1-\dfrac{e^{x_j}}{h(x)}\bigg) &\text{if } i = j
\\cr\\cr
-\dfrac{e^{x_j}}{h(x)}\dfrac{e^{x_i}}{h(x)} &\text{if } i \ne j
\end{cases}
\\cr
&= \begin{cases}
s_i(1-s_j) &\text{if } i = j
\\cr
-s_is_j&\text{if } i \ne j
\end{cases}
\end{aligned}
$$

Như vậy, đạo hàm riêng của $s_i$ theo $x_j$ là:
$$
\partial\_{ij}=\begin{cases}
s_i(1-s_j) &\text{if } i = j
\\cr
-s_is_j&\text{if } i \ne j
\end{cases}
$$

Sử dụng hàm [Kronecker delta](https://en.wikipedia.org/wiki/Kronecker_delta):
$$
\textcolor{red}{\delta_{ij}}=\begin{cases}
1 ~~~\text{if } i=j
\\cr
0 ~~~\text{if } i\ne j
\end{cases}
$$

> Thực ra $\delta_{ij}$ là 1 phần tử của [ma trận định danh](/vi/2017/09/what-is-matrix/#2-4-ma-tr%E1%BA%ADn-%C4%91%C6%A1n-v%E1%BB%8B) $\mathbf{I_n}$.

Ta có thể thu được:

$$\partial\_{ij}=\frac{\partial{s_i}}{\partial{x_j}}=s_i(\textcolor{red}{\delta\_{ij}}-s_j)$$

## 2.2. Gradient

Gom các đạo hàm riêng lại vào ma trận Jacobi, ta sẽ được đạo hàm của $\mathbf s$ theo $\mathbf x$ như sau:
$$
\nabla_{\mathbf x}\mathbf s = \begin{bmatrix}
s_1(1-s_1) & s_2(0-s_1) & \dots & s_k(0-s_1)
\\cr
s_1(0-s_2) & s_2(1-s_2) & \dots & s_k(0-s_2)
\\cr
\vdots & \vdots & \ddots & \vdots
\\cr
s_1(0-s_k) & s_2(0-s_k) & \dots & s_k(1-s_k)
\end{bmatrix}
$$

## 2.3. Cài đặt

Việc cài đặt hàm tính đạo hàm cũng không khó khăn gì:

{{< codeblock "softmap.py" "python" >}}
def softmax_grad(s):
  Jacobi = np.diag(s)
  len = len(s)
  
  for i in range(len)
    for j in range(len)
      Jacobi[i][j] = (s[i] * (1 - s[i])) if (i == j) else (-s[i] * s[j])
  
  return Jacobi
{{< /codeblock >}}

Tuy nhiên để tận dụng khả năng tính toán của `numpy`, ta có thể cài đặt theo phép véc-tơ hoá như sau:

$$
\nabla_{\mathbf x}\mathbf s = \begin{bmatrix}
s_1 & 0 & \dots & 0
\\cr
0 & s_2 & \dots & 0
\\cr
\vdots & \vdots & \ddots & \dots
\\cr
0 & 0 & \dots & s_k
\end{bmatrix}
- \begin{bmatrix}
s_1^2 & s_2s_1 & \dots & s_ks_1
\\cr
s_1s_2 & s_2^2 & \dots & s_ks_2
\\cr
\vdots & \vdots & \ddots & \vdots
\\cr
s_1s_k & s_2s_k & \dots & s_k^2
\end{bmatrix}
$$

{{< codeblock "softmap.py" "python" >}}
def softmax_grad_vec(s):
  _s = s.reshape(-1, 1)
  
  return np.diagflat(_s) - np.dot(_s, _s.T)
{{< /codeblock >}}

# 3. Kết luận
Softmax được sử dụng như là phép đo xác xuất mỗi lớp thành phần:

$$s_i = \frac{\exp(x_i)}{\sum_j\exp(x_j)}$$

Ta có thể cài đặt hàm này khá dễ dàng:

{{< codeblock "softmap.py" "python" >}}
def softmax(x):
  e = np.exp(x)
  
  return e / np.sum(e)
{{< /codeblock >}}

Nếu giá trị các thành phần không chênh lệch nhau quá nhiều và có nguy cơ dẫn tới tràn số thì ta có thể sử dụng phép cộng thêm hằng số:

$$s_i = \frac{\exp(x_i + C)}{\sum_j\exp(x_j + C)}$$

Đoạn mã thực hiện như sau:
{{< codeblock "softmap.py" "python" >}}
def softmax_stable(x):
  _x = x - np.max(x)
  e = np.exp(_x)
  
  return e / np.sum(e)
{{< /codeblock >}}

Đạo hàm của nó được tính bằng công thức:

$$\frac{\partial{s_i}}{\partial{x_j}}=s_i(\textcolor{red}{\delta\_{ij}}-s_j)$$

Trong đó, $\color{red}\delta\_{ij}$ là hàm [Kronecker delta](https://en.wikipedia.org/wiki/Kronecker_delta):
$$
\delta_{ij}=\begin{cases}
1 &\text{if } i=j
\\cr
0 &\text{if } i\ne j
\end{cases}
$$

Ta có thể cài đặt hàm tính đạo hàm như sau:

{{< codeblock "softmap.py" "python" >}}
def softmax_grad(s):
  Jacobi = np.diag(s)
  len = len(s)
  
  for i in range(len)
    for j in range(len)
      Jacobi[i][j] = (s[i] * (1 - s[i])) if (i == j) else (-s[i] * s[j])
  
  return Jacobi
{{< /codeblock >}}

Phiên bản véc-tơ hoá có thể cài đặt như sau:

{{< codeblock "softmap.py" "python" >}}
def softmax_grad_vec(s):
  _s = s.reshape(-1, 1)
  
  return np.diagflat(_s) - np.dot(_s, _s.T)
{{< /codeblock >}}

