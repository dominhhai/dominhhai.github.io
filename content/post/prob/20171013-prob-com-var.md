---
title: "[Xác Suất] Phân phối phổ biến"
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
Cho tới thời điểm này ta đã có các khái niệm quan trọng trong xác suất như sự kiện, biến ngẫu nhiên, phân phối xác suất và các đặc trưng của phân phối. Giờ là lúc ta đề cập tới một số phân phối xác suất phổ biến.
<!--more-->

<!--toc-->
# 1. Biến rời rạc
## 1.1. Phân phối đều - *Discrete Uniform distribution*
Là phân phối mà xác suất xuất hiện của các sự kiện là như nhau. Biến ngẫu nhiên $X$ tuân theo phân phối đều rời rạc $X \sim \mathcal{Unif}(a, b)$ với tham số $a, b \in \mathbb Z; a < b$, đặt $n = b-a+1$, ta sẽ có:

| Định nghĩa | Giá trị |
|---|---|
| PMF - $p(x)$ | $\dfrac{1}{n}, \forall x \in [a,b]$ |
| CDF - $F(k;a,b)$ | $\dfrac{k-a+1}{n}, \forall k \in [a,b]$ |
| Kỳ vọng - $E[X]$ | $\dfrac{a+b}{2}$ |
| Phương sai - $Var(X)$ | $\dfrac{n^2-1}{12}$ |

Thường người ta hay lấy $a=1$ và khi đó phân phối đều của $X$ sẽ được kí hiệu là $X \sim \mathcal{Unif}(n)$. Lúc đó hàm phân phối xác suất CDF sẽ là: $F(k;n)=\dfrac{k}{n}$.

## 1.2. Phân phối Béc-nu-li - *Bernoulli distribution*


## 1.3. Phân phối nhị thức - *Binomial distribution*
## 1.4. Phân phối Poa-xông - *Poisson distribution*
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
