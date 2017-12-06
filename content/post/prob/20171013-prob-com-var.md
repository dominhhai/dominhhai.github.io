---
title: "[Xác Suất] Một số phân phối phổ biến"
slug: prob-com-var
date: 2017-10-13
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
Cho tới thời điểm này ta đã có các khái niệm quan trọng trong xác suất như sự kiện, biến ngẫu nhiên, phân phối xác suất và các đặc trưng của phân phối. Giờ là lúc ta đề cập tới một số phân phối xác suất phổ biến để có thể áp dụng vào thực tế khi quan sát các mô hình xác suất.
<!--more-->

<!--toc-->
# 1. Biến rời rạc
## 1.1. Phân phối đều - *Discrete Uniform distribution*
Là phân phối mà xác suất xuất hiện của các sự kiện là như nhau. Biến ngẫu nhiên $X$ tuân theo phân phối đều rời rạc $X \sim \mathcal{Unif}(a, b)$ với tham số $a, b \in \mathbb Z; a < b$ là khoảng giá trị của $X$, đặt $n = b-a+1$, ta sẽ có:

| Định nghĩa | Giá trị |
|---|---|
| PMF - $p(x)$ | $\dfrac{1}{n}, \forall x \in [a,b]$ |
| CDF - $F(x;a,b)$ | $\dfrac{x-a+1}{n}, \forall x \in [a,b]$ |
| Kỳ vọng - $E[X]$ | $\dfrac{a+b}{2}$ |
| Phương sai - $Var(X)$ | $\dfrac{n^2-1}{12}$ |

Thường người ta hay lấy $a=1$ và khi đó phân phối đều của $X$ sẽ được kí hiệu là $X \sim \mathcal{Unif}(n)$. Lúc đó hàm phân phối xác suất CDF sẽ là: $F(k;n)=\dfrac{k}{n}$.

## 1.2. Phân phối Béc-nu-li - *Bernoulli distribution*
Như đã đề cập về phép thử Béc-nu-li rằng mọi phép thử của nó chỉ cho 2 kết quả duy nhất là $A$ với xác suất $p$ và $\bar A$ với xác suất $q=1-p$. Biến ngẫu nhiên $X$ tuân theo phân phối Béc-nu-li $X \sim \mathcal{Bern}(p)$ với tham số $p \in \mathbb{R}, 0 \le p \le 1$ là xác suất xuất hiện của $A$ tại mỗi phép thử thì sẽ có những đặc tính như sau:  

| Định nghĩa | Giá trị |
|---|---|
| PMF - $p(x)$ | $p^x(1-p)^{1-x} ~~~,x \in \\{0,1\\}$ |
| CDF - $F(x;p)$ | $\begin{cases}0 &\text{for } x < 0 \\cr1-p &\text{for } 0 \le x < 1 \\cr1 &\text{for } x \ge 1\end{cases}$ |
| Kỳ vọng - $E[X]$ | $p$ |
| Phương sai - $Var(X)$ | $p(1-p)$ |

## 1.3. Phân phối nhị thức - *Binomial distribution*
Là phân phối của phép thử Béc-nu-li với biến ngẫu nhiên $X$ thể hiện số lần xuất hiện sự kiện $A$. Biến ngẫu nhiên $X$ tuân theo phân phối nhị thức $X \sim \mathcal{Bin}(n,p)$ với tham số $n \in \mathbb N$ là số lần xuất hiện của $A$ và $p \in \mathbb{R}, 0 \le p \le 1$ là xác suất xuất hiện của $A$ tại mỗi phép thử, ta có:

| Định nghĩa | Giá trị |
|---|---|
| PMF - $p(x)$ | $\dbinom{n}{x}p^x(1-p)^{n-x} ~~~,x \in [0,n]$ |
| CDF - $F(x;n,p)$ | $\displaystyle\sum\_{i=0}^x\dbinom{n}{i}p^i(1-p)^{n-i}$ |
| Kỳ vọng - $E[X]$ | $np$ |
| Phương sai - $Var(X)$ | $np(1-p)$ |

$\dbinom{n}{x}=\dfrac{n!}{x!(n-x)!}$ được gọi là hệ số nhị thức và tên của phân phối này cũng xuất phát từ điểm này :)

Như vậy ta có thể thấy phép thử Béc-nu-li có thể coi là 1 trường hợp đặc biệt của phân phối nhị thức với $n=1$, nên phân phối Béc-nu-li còn có thể kí hiệu là: $X \sim \mathcal{Bin}(1,p)$.

## 1.4. Phân phối Poa-xông - *Poisson distribution*
Là phân phối nhị thức đạt được khi $n$ rất lớn và $p$ rất nhỏ. Đặt $\lambda=np$, ta có:
$$
\begin{aligned}
p(x)&=\dfrac{n!}{x!(n-x)!}p^x(1-p)^{n-x}
\\cr\ &=\dfrac{n!}{x!(n-x)!}\bigg(\frac{\lambda}{n}\bigg)^x\bigg(1-\frac{\lambda}{n}\bigg)^{n-x}
\\cr\ &=\dfrac{n!}{n^x(n-x)!}\frac{\lambda^x}{x!}\bigg(1-\frac{\lambda}{n}\bigg)^{n-x}
\end{aligned}
$$

Khi $n$ rất lớn thì $\bigg(1-\dfrac{\lambda}{n}\bigg)^x \approx 1$, $\bigg(1-\dfrac{\lambda}{n}\bigg)^n \approx e^{-\lambda}$ và $\dfrac{n!}{n^x(n-x)!} \approx 1$

nên $p(x) \approx \dfrac{\lambda^x}{x!}e^{-\lambda}$

Từ đây, khi ta có tham số $\lambda$ thì biến ngẫu nhiên $X$ tuân theo phân phối Poa-xông $X \sim \mathcal{Poi}(\lambda)$ sẽ có đặc tính:

| Định nghĩa | Giá trị |
|---|---|
| PMF - $p(x)$ | $\dfrac{\lambda^x}{x!}e^{-\lambda}$ |
| CDF - $F(x;n,p)$ | $e^{-\lambda}\displaystyle\sum\_{i=0}^x\dfrac{\lambda^i}{i!}$ |
| Kỳ vọng - $E[X]$ | $\lambda$ |
| Phương sai - $Var(X)$ | $\lambda$ |

## 1.5. Phân phối hình học - *Geometric distribution*
## 1.6. Phân phối nhị thức âm - *Negative Binominal distribution*
## 1.7. Phân phối siêu hình học - *Hypergeometric distribution*
## 1.8. Phân phối Zeta - *Zeta (Zipf) distribution*

# 2. Biến liên tục
## 2.1. Phân phối đều - *Continuous Uniform distribution*
Tương tự như đối với trường hợp là biến rời rạc thì với phân phối đều liên tục, bất kì giá trị nào của biến ngẫu nhiên trong miền xác định cũng cho xác suất là như nhau. Biến ngẫu nhiên $X$ tuân theo phân phối đều liên tục $X \sim \mathcal{Unif}(a, b)$ với tham số $a, b \in \mathbb R; a < b$, ta sẽ có:

| Định nghĩa | Giá trị |
|---|---|
| PDF - $f(x)$ | $\begin{cases}\dfrac{1}{b-a}&, \text{if } x \in [a,b] \\cr 0 &, \text{otherwise} \end{cases}$ |
| CDF - $F(k;a,b)$ | $\begin{cases} 0 &, \text{if } k < a \\cr \dfrac{k-a}{b-a}&, \text{if } k \in [a,b) \\cr 1 &, \text{if } k \ge b \end{cases}$ |
| Kỳ vọng - $E[X]$ | $\dfrac{a+b}{2}$ |
| Phương sai - $Var(X)$ | $\dfrac{(b-a)^2}{12}$ |

## 2.2. Phân phối chuẩn - *Normal distribution*
Biến ngẫu nhiên $X$ tuân theo phân phối chuẩn $X \sim \mathcal{N}(\mu, \sigma^2)$ với tham số kỳ vọng $\mu$ và phương sai $\sigma^2$, ta sẽ có:

| Định nghĩa | Giá trị |
|---|---|
| PDF - $f(x)$ | $\dfrac{1}{\sqrt{2\pi\sigma^2}}e^{-\displaystyle\frac{(x-\mu)^2}{2\sigma^2}}$ |
| CDF - $F(x)$ | $\dfrac{1}{2}+\Phi(\dfrac{x-\mu}{\sigma})$ |
| Kỳ vọng - $E[X]$ | $\mu$ |
| Phương sai - $Var(X)$ | $\sigma^2$ |

## 2.3. Phân phối mũ - *Exponential distribution*
## 2.4. Phân bố Erlang - *Erlang distribution*
## 2.5. Phân phối bình phương
## 2.6. Phân phối Gam-ma
