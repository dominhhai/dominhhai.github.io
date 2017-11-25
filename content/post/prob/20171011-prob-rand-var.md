---
title: "[Xác Suất] Biến ngẫu nhiên và phân phối xác suất"
slug: prob-rand-var
date: 2017-10-11
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
customJS:
- https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js
---
Trong [phần trước](/vi/2017/10/what-is-prob/) ta đã có khái niệm rất cơ bản về phép thử, sự kiện, các tính chất của biến cố và cách tính xác suất của chúng. Trong phần này, ta sẽ tập trung vào các biến cố nhận giá trị ngẫu nhiên và mô hình phân phối xác suất của chúng.
<!--more-->

<!--toc-->
# 1. Biến ngẫu nhiên
Biến ngẫu nhiên (random variables) là các biến nhận 1 giá trị ngẫu nhiên đại diện cho kết quả của phép thử. Mỗi giá trị nhận được $x$ của biến ngẫu nhiên $X$ được gọi là một thể hiện của $X$, đây cũng là kết quả của phép thử hay còn được hiểu là một sự kiện.

Gọi tên là một biến có vẻ hơi kì kì một chút bởi biến ngẫu nhiên thực chất là một hàm ánh xạ từ không gian sự kiện đầy đủ tới 1 số thực: $X: \Omega \mapsto \mathbb{R}$.

Biến ngẫu nhiên có 2 dạng:

* Rời rạc: tập giá trị nó là rời rạc, tức là đếm được. Ví dụ như mặt chấm của con xúc xắc.
* Liên tục: tập giá trị là liên tục tức là lấp đầy 1 khoảng trục số. Ví dụ như giá thuê nhà ở Hà Nội.

# 2. Phân phối xác suất
Là phương pháp xác định xác suất của biến ngẫu nhiên được phân phối ra sao. Có 2 cách để xác định phân bố này là dựa vào bảng phân bố xác xuất và hàm phân phối xác suất. Ở đây, tôi chỉ đề cập tới phương pháp hàm phân bố xác suất. Hàm phân phối xác suất của biến ngẫu nhiên $X$ được xác định như sau:

$$F_X(x) = P(X \le x) ~~~, x \in \mathbb{R}$$

Hàm phân phối xác suất còn có tên là hàm phân phối tích luỹ (*CDF - Cumulative Distribution Function*) do đặc trưng là lấy xác suất của các biến ngẫu nhiên bên trái của một giá trị $x$ bất kì nào đó. Hàm này có đặc điểm là một hàm không giảm, tức là nếu $a<b$ thì $F_X(a) \le F_X(b)$ vì sự kiện $b$ đã bao gồm cả sự kiện $a$ rồi.

## 2.1. Hàm khối xác suất của biến rời rạc
Với các biến ngẫu nhiên ta còn quan tâm xem xác suất tại mỗi tại 1 giá trị $x$ nào đó trong miền giá trị của nó là bao nhiêu, hàm xác suất như vậy được gọi là *hàm khối xác suất* (*PMF - Probability Mass Function*). Giả sử miền xác định của $X$ là $D$, tức $X: \Omega \mapsto \mathsf D$ thì hàm khối xác suất được xác định như sau:
$$p(x)=p_X(x)=
\begin{cases}
P(X=x) &\text{if } x \in \mathsf D \\cr
0 &\text{if } x \notin \mathsf D
\end{cases}
$$

Như vậy ta có thể thấy rằng hàm khối xác suất thực chất cũng là một xác suất nên nó mang đầy đủ tất cả các tính chất của xác suất như:

* $0 \le p(x) \le 1 $
* $\displaystyle\sum\_{x_i \in \mathsf D}p(x_i)=1$

Ví dụ, ta có hàm phân phối xác suất như sau:
$$p(x)=
\begin{cases}
\frac{x}{36} &\text{if } x \in \mathbb R, 0 \le x \le 6 \\cr
\frac{12-x}{36} &\text{if } x \in \mathbb R, x \ge 7 \\cr
0 &\text{else}
\end{cases}
$$
thì ta có thể biểu diễn bằng biểu đồ phân phối như sau:
<canvas id="myChart" width="400" height="400"></canvas>

## 2.2. Hàm mật độ xác suất của biến liên tục
# 3. Các phương pháp
## 3.1. Xác suất biên
## 3.2. Xác suất có điều kiện
# 5. Các đặc trưng
## 5.1. Kì vọng
## 5.2. Phương sai
## 5.3. Trung vị
## 5.4. Mode
## 5.5. Hiệp phương sai
# 6. Các hàm phân phối thường gặp
<script>
function fnMain() {
  var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});
}
</script>
