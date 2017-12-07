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
| CDF - $F(x;\lambda)$ | $e^{-\lambda}\displaystyle\sum\_{i=0}^x\dfrac{\lambda^i}{i!}$ |
| Kỳ vọng - $E[X]$ | $\lambda$ |
| Phương sai - $Var(X)$ | $\lambda$ |

## 1.5. Phân phối hình học - *Geometric distribution*
Là phân phối của xác suất xuất hiện lần đầu tiên của sự kiện $A$ trong phép thử Béc-nu-li. Phân phối hình học được kí hiệu là $X \sim \mathcal{Geo}(p)$, trong đó tham số $p$ là xác suất xuất hiện của sự kiện $A$ trong mỗi phép thử.

| Định nghĩa | Giá trị |
|---|---|
| PMF - $p(x)$ | $p(1-p)^x$ |
| CDF - $F(x;p)$ | $1-(1-p)^{x+1}$ |
| Kỳ vọng - $E[X]$ | $\dfrac{1-p}{p}$ |
| Phương sai - $Var(X)$ | $\dfrac{1-p}{p^2}$ |

## 1.6. Phân phối nhị thức âm - *Negative Binominal distribution*
Là phân phối xác suất xuất hiện lần thứ $r$ của sự kiện $A$ trong phép thử Béc-nu-li. Như vậy đây là phân phối tổng quát của phân phối hình học và phân phối hình học là phân phối nhị thức âm với $r=1$. Ta kí hiệu phân phối này là $X \sim \mathcal{NegBin}(r,p)$ với tham số $r$ là số lần xuất hiện của $A$ cùng với $p$ là xác suất xuất hiện của $A$ trong mỗi phép thử.

| Định nghĩa | Giá trị |
|---|---|
| PMF - $p(x)$ | $\dbinom{x+r+1}{x}p^r(1-p)^x$ |
| CDF - $F(x;r,p)$ | $p^r\displaystyle\sum\_{i=0}^x\dbinom{x+r+1}{x}(1-p)^x$ |
| Kỳ vọng - $E[X]$ | $\dfrac{r(1-p)}{p}$ |
| Phương sai - $Var(X)$ | $\dfrac{r(1-p)}{p^2}$ |

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
Phân phối chuẩn hay còn được gọi là phân phối Gao-xo (*Gauss*) là một trong những phân phối quan trọng nhất và được ứng dụng rất rộng rãi trong thực tế. Ở đây ta sẽ khảo sát phân phối chuẩn cho 1 biến ngẫu nhiên hay nói cách khác là biến ngẫu nhiên một chiều và cho cả nhiều biến ngẫu nhiên hay véc-to ngẫu nhiên - biến ngẫu nhiên nhiều chiều.

### 2.2.1 Đối với biến 1 chiều (*Univariate*)
Biến ngẫu nhiên $X$ tuân theo phân phối chuẩn $X \sim \mathcal{N}(\mu, \sigma^2)$ với tham số kỳ vọng $\mu$ và phương sai $\sigma^2$, ta sẽ có:

| Định nghĩa | Giá trị |
|---|---|
| PDF - $f(x)$ | $\dfrac{1}{\sqrt{2\pi\sigma^2}}exp\bigg(-\dfrac{(x-\mu)^2}{2\sigma^2}\bigg)$ |
| CDF - $F(x;\mu,\sigma^2)$ | $\dfrac{1}{2}+\Phi\bigg(\dfrac{x-\mu}{\sigma}\bigg)$ |
| Kỳ vọng - $E[X]$ | $\mu$ |
| Phương sai - $Var(X)$ | $\sigma^2$ |

$\Phi\bigg(\dfrac{x-\mu}{\sigma}\bigg)$ ở đây là 1 phân phối chuẩn đã được tính toán từ trước.

Biểu đồ của hàm mật độ xác suất tuân theo phân phối chuẩn có dạng như sau:

{{< image classes="center" src="https://res.cloudinary.com/dominhhai/image/upload/prob/normal_dis.svg" title="Probability density function. Source: https://en.wikipedia.org/wiki/Normal_distribution" >}}

Để ý rằng phương sai $\sigma^2$ càng lớn thì mức độ phân tán xác suất cũng càng rộng, đỉnh thấp hơn và trải rộng hơn. Đường màu đỏ với $\mu=0$ và $\sigma^2=1$ thể hiện phân phối chuẩn tắc $f(x)=\dfrac{1}{\sqrt{2\pi}}exp\bigg(-\dfrac{x^2}{2}\bigg)$ (đây là hàm *Gao-xo* (**Gauss function**)). Phân phối này thường được dùng để tính các phân phối chuẩn khác qua các phép biến đổi tuyến tính.

Thường các phân phối chuẩn được tính toán theo các phép biến đổi tuyến tính tức là dựa vào các phân phối chuẩn dễ tính và tính được từ trước (như phân phối chuẩn tắc) để ước lượng cho phân phối cần tính. Giờ ta sẽ tìm cách biểu diễn 1 phân phối chuẩn bất kì qua phân phối chuẩn tắc.

Giả sử $Y=aX+b$ thì $Y$ cũng sẽ là phân phối chuẩn có luật phân phối là: $Y \sim \mathcal{N}(a\mu+b, a^2\sigma^2)$.

Ta có *Z-score* của phân phối chuẩn là: $Z=\dfrac{X-\mu}{\sigma}$. Nếu đặt $a=\dfrac{1}{\sigma}$ và $b=-\dfrac{\mu}{\sigma}$ ta sẽ biểu diễn được $Z$ tuyến tính theo $X$ với dạng: $Z=aX+b$. Như vậy $Z$ sẽ tuân theo phân phối chuẩn:
$$
\begin{aligned}
Z &\sim \mathcal{N}(a\mu+b, a^2\sigma^2)
\\cr\ &\sim \mathcal{N}\bigg(\dfrac{1}{\sigma}\mu-\dfrac{\mu}{\sigma}, \dfrac{1}{\sigma^2}\sigma^2\bigg)
\\cr\ &\sim \mathcal{N}(0,1)
\end{aligned}
$$

Như vậy $Z$ tuân theo phân phối chuẩn tắc nên ta có thể biến đổi ngược lại để thu được phép biểu diễn phân phối chuẩn qua phân phối của $Z$.
$$
\begin{aligned}
F_X(x) &= P(X \le x)
\\cr\ &= P\bigg(\dfrac{X-\mu}{\sigma} \le \dfrac{x-\mu}{\sigma}\bigg)
\\cr\ &= P\bigg(Z \le \dfrac{x-\mu}{\sigma}\bigg)
\\cr\ &= \Phi\bigg(\dfrac{x-\mu}{\sigma}\bigg)
\end{aligned}
$$

Phân phối tích luỹ chuẩn tắc $\Phi\bigg(\dfrac{x-\mu}{\sigma}\bigg)$ có thể tra sử dụng các bảng tính có sẵn nên ta hoàn toàn có thể tính được các phân phối chuẩn khác qua nó.

### 2.2.2 Đối với biến đa chiều (*Multivariate*)
Đây là tổng quát hoá của phân phối chuẩn đối với biến ngẫu nhiên một chiều và sử dụng cho hợp của nhiều biến ngẫu nhiên - vécto ngẫu nhiên. Giả sử véc-tơ ngẫu nhiên có số chiều là $k$: $X=[X_1, X_2, ...,X_k]^{\intercal}$. Lúc đó phân phối chuẩn của nó sẽ được tham số hoá bởi:

* Vec-to kì vọng: $\mu=E[X]=[E[X_1], E[X_2], ...,E[X_k]]^{\intercal}$
* Ma trận hiệp phương sai: $\Sigma=E[(X-\mu)(X-\mu)^{\intercal}]=[Cov(X_i,X_j)~~~,1 \le i,j \le k]$

Phân phối này sẽ được kí hiệu là: $X \sim \mathcal{N}_k(\mu, \Sigma)$ hoặc giản lược $k$ là: $X \sim \mathcal{N}(\mu, \Sigma)$ và có hàm mật độ xác suất:
$$f(x)=\dfrac{1}{\sqrt{\det(2\pi\Sigma)}}exp\bigg(-\dfrac{1}{2}(x-\mu)^{\intercal}\Sigma^{-1}(x-\mu)\bigg)$$

Ví dụ với trường hợp có 2 biến ngẫu nhiên $x,y$ ($k=2$) ta sẽ có véc-to kỳ vọng $\mu=\begin{bmatrix}\mu_X \\cr \mu_Y\end{bmatrix}$ và  ma trận hiệp phương sai $\Sigma=\begin{bmatrix}\sigma_X^2 & \rho\sigma_X\sigma_Y \\cr \rho\sigma_X\sigma_Y & \sigma_Y^2\end{bmatrix}$. Hàm mật độ xác suất lúc đó sẽ có dạng:
$$f(x)=\dfrac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}}exp\bigg(-\dfrac{1}{2(1-\rho^2)}\bigg[\dfrac{(x-\mu_x)^2}{\sigma_X^2}+\dfrac{(y-\mu_y)^2}{\sigma_Y^2}-\dfrac{2(x-\mu_x)(y-\mu_y)}{\sigma_X\sigma_Y}\bigg]\bigg)$$

## 2.3. Phân phối mũ - *Exponential distribution*
Là phân phối biểu diễn xác suất thời gian giữa các lần một sự kiện xảy ra. Biến ngẫu nhiên $X$ tuần theo phân phối mũ $X \sim \mathcal{Exp}(\lambda)$ với tham số $\lambda$ là là tỉ lệ xảy ra của sự kiện $A$.

| Định nghĩa | Giá trị |
|---|---|
| PDF - $f(x)$ | $\lambda e^{-\lambda x} ~~~,\text{for } x \ge 0$ |
| CDF - $F(x;\lambda)$ | $1-e^{-\lambda x}$ |
| Kỳ vọng - $E[X]$ | $\dfrac{1}{\lambda}$ |
| Phương sai - $Var(X)$ | $\dfrac{1}{\lambda^2}$ |

Nếu đặt $\beta=\dfrac{1}{\lambda}$ là kỳ vọng ta có thể sử dụng $\beta$ là tham số của phân phối mũ. Khi đó phân phối này có thể kí hiệu là: $X \sim \mathcal{Exp}(\beta)$ và có $f(x)=\dfrac{1}{\beta}exp(-\dfrac{x}{\beta})$.
