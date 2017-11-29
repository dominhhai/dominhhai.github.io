---
title: "[Xác Suất] Hợp nhiều biến ngẫu nhiên"
slug: prob-rand-mulvar
date: 2017-10-12
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
Trong thực tế ta thường xuyên phải làm việc với nhiều biến ngẫu nhiên cùng lúc chứ không đơn thuần là 1 biến như [bài viết trước](/vi/2017/10/prob-rand-var/) nên khảo sát việc kết hợp các biến như vậy là rất cần thiết.
<!--more-->

Lưu ý rằng ta cũng có thể coi các biến ngẫu nhiên này như 1 biến đa chiều hoặc 1 véc-tơ ngẫu nhiên có các phần tử là biến ngẫu nhiên. Sau này trong các bài toán chúng thường hay được biểu diễn dưới dạng véc-tơ nên ta cần nhớ tới điểm này. Trong bài viết này ta sẽ xem xét trường hợp 2 biến ngẫu nhiên để cho dễ biểu diễn, tuy nhiên trường hợp tổng quát thì các phép toán và tính chất hoàn toàn có thể áp dụng tương tự.
<!--toc-->

# 1. Phân phối xác suất
## 1.1. Phân phối đồng thời
Hàm phân phối xác suất đồng thời hay hàm phân phối tích luỹ xác suất đồng thời (*Joint CDF - Joint Cumulative Probability Distribution Function*) của 2 biến ngẫu nhiên $X,Y$ được định nghĩa như sau:
$$F\_{X,Y}(x,y)=P(X \le x,Y \le y) ~~~, x,y \in \mathbb R$$

Như vậy đây thực chất là hàm hợp xác suất của 2 biến ngẫu nhiên $X,Y$ và tích luỹ xác suất được lấy là phần giao tích luỹ bên trái của $X$ và bên trái của $Y$. Tương tự như với 1 biến ngẫu nhiên, hàm phân phối của 2 biến cũng là một hàm không giảm theo từng đối số 1 và ta còn có thể tính được tất cả các kiểu xác suất hợp của 2 biến $X,Y$ thông qua hàm xác suất đồng thời.

Ví dụ:
$$
\begin{aligned}
P(X>x,Y>y) &= 1 - P(\overline{X>x,Y>y})
\\cr\ &= 1 - P(\overline{X>x}\cup\overline{Y>y})
\\cr\ &= 1 - P(X \le x \cup Y \le y)
\\cr\ &= 1 - P(X \le x) - P(Y \le y) + P(X \le x,Y \le y)
\\cr\ &= 1 - F_X(x) - F_Y(y) + F\_{X,Y}(x,y)
\\cr
P(x_1 < X \le x_2,y_1 < Y \le y_2) &= F(x_1,y_1)+F(x_2,y_2)-F(x_1,y_2)-F(x_2,y_1)
\end{aligned}
$$


Hàm khối xác suất đồng thời (*Joint PMF*) của 2 biến ngẫu nhiên $X,Y$ cùng rời rạc sẽ có dạng:
$$p\_{X,Y}(x,y)=P(X=x,Y=y)$$

Khi đó với mỗi $p(x_i,y_j)$ là hàm khối xác suất đồng thời, ta có:

* $0 \le p(x_i,y_j) \le 1$
* $\displaystyle\sum\_{\forall i}\sum\_{\forall j} p(x_i,y_j) = 1$
* $F(x,y) = \displaystyle\sum\_{\forall x_i \le x}\sum\_{\forall y_j \le y} p(x_i,y_j)$

Còn hàm mật độ xác suất đồng thời (*Joint PDF*) của 2 biến ngẫu nhiên $X,Y$ cùng liên tục có dạng:
$$f(x,y)=\dfrac{\partial^2 F(x,y)}{\partial x \partial y}$$
Hay dưới dạng tích phân:
$$F(x,y)=\int\_{-\infty}^x\int\_{-\infty}^yf(u,v)dudv$$

Tương tự như trường hợp 1 biến ta có:

* $f(x,y)>0$
* $\displaystyle\int\_{-\infty}^\infty\int\_{-\infty}^\infty f(x,y)dxdy = 1$
* $P(x_1 \le X \le x_2, y_1 \le Y \le y_2) = \displaystyle\int\_{x_1}^{x_2}\int\_{y_1}^{y_2}f(x,y)dxdy$
* $P(X=x,Y=y) = \displaystyle\int\_{x}^{x}\int\_{y}^{y}f(x,y)dxdy=0$

Như vậy nếu để ý thì ta có thể nhớ 1 cách rằng trường hợp biến rời rạc ta lấy tổng còn biến là liên tục ta lấy tích phân. Đương nhiên là với biến rời rạc ta phải sử dụng hàm khối xác suất còn biến liên tục là hàm mật độ xác suất.

## 1.2. Phân phối biên
Phân phối biên (*Marginal Probability*) là phân phối của riêng từng biến một.
$$
\begin{aligned}
F_X(x)&=P(X \le x)
\\cr\ &=P(X \le x,Y < +\infty)
\\cr\ &=F\_{X,Y}(x,+\infty)
\\cr
F_Y(y)&=P(Y \le y)
\\cr\ &=P(+\infty,Y \le y)
\\cr\ &=F\_{X,Y}(+\infty,y)
\end{aligned}
$$

Đối với các biến rời rạc, ta có hàm khối xác suất biên (*Marginal PMF*):
$$
\begin{aligned}
p_X(x)&=P(X=x)
\\cr\ &=\sum\_{\forall j}P(x,y_j)
\\cr
p_Y(y)&=P(Y=y)
\\cr\ &=\sum\_{\forall i}P(x_i,y)
\end{aligned}
$$

Đối với các biến liên tục, ta có hàm mật độ xác suất biên (*Marginal PDF*):
$$
\begin{aligned}
f_X(x)&=P(X=x)
\\cr\ &=\int\_{-\infty}^{\infty}f(x,y)dy
\\cr
f_Y(y)&=P(Y=y)
\\cr\ &=\int\_{-\infty}^{\infty}f(x,y)dx
\end{aligned}
$$

Nếu bạn để ý sẽ thấy rằng công thức này khá giống với công thức xác suất đầy đủ khi tính xác suất của 1 sự kiện theo toàn bộ 1 sự kiện khác.

## 1.3. Biến độc lập
2 biến $X,Y$ độc lập khi xác suất của chúng không phụ thuộc vào nhau. Như ta đã biết 2 sự kiện $A,B$ độc lập khi và chỉ khi $P(AB)=P(A)P(B)$, tương tự với biến ngẫu nhiên chúng độc lập khi và chỉ khi
$$F\_{X,Y}(x,y)=F_X(x)F_Y(y) ~~~,\forall x,y \in \mathbb R$$

Với trường hợp các biến ngẫu nhiên rời rạc:
$$p\_{X,Y}(x,y)=p_X(x)p_Y(y) ~~~,\forall x,y \in \mathbb R$$

Với trường hợp các biến ngẫu nhiên liên tục:
$$f\_{X,Y}(x,y)=f_X(x)f_Y(y) ~~~,\forall x,y \in \mathbb R$$

Như vậy từ đây ta có thể thấy rằng nếu các biến ngẫu nhiên là độc lập thì xác suất đồng thời của chúng có thể tính qua các xác suất biên của chúng bằng cách lấy tích chúng lại với nhau.

## 1.4. Xác suất có điều kiện
# 2. Các đặc trưng
## 2.1. Kì vọng
## 2.2. Phương sai
## 2.3. Hiệp phương sai
## 2.4. Hệ số tương quan
## 2.5. Đặc trưng có điều kiện
# 3. Hàm các biến ngẫu nhiên
## 3.1. Phân phối xác suất
## 3.2. Các đặc trưng
# 4. Kết luận
