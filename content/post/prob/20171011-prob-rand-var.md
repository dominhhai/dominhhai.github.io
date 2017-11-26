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
Với các biến ngẫu nhiên ta còn quan tâm xem xác suất tại mỗi tại 1 giá trị $x$ nào đó trong miền giá trị của nó là bao nhiêu, hàm xác suất như vậy đối với biến ngẫu nhiên rời rạc được gọi là *hàm khối xác suất* (*PMF - Probability Mass Function*). Giả sử miền xác định của $X$ là $D$, tức $X: \Omega \mapsto \mathsf D$ thì hàm khối xác suất được xác định như sau:
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
<canvas id="ex1"></canvas>

Hàm phân phối tích luỹ $F$ của biến ngẫu nhiên rời rạc có thể được biểu diễn qua hàm khối xác suất bằng cách lấy tổng:
$$F_X(x) = \sum\_{\text{all }x_i \le x}p(x_i) ~~~, x \in \mathbb{R}$$
Lúc này, hàm phân phối tích luỹ sẽ có dạng bậc thang ứng với mỗi bậc là khoảng $(x_i, x\_{i+1})$.
Ví dụ hàm phân phối tích luỹ của ví dụ trên sẽ có dạng như sau:
$$F(x)=\begin{cases}
0 &\text{if } x < 1 \\cr
{1}/{36} &\text{if } 1 \le x < 2 \\cr
{3}/{36} &\text{if } 2 \le x < 3 \\cr
{6}/{36} &\text{if } 3 \le x < 4 \\cr
{10}/{36} &\text{if } 4 \le x < 5 \\cr
{15}/{36} &\text{if } 5 \le x < 6 \\cr
{21}/{36} &\text{if } 6 \le x < 7 \\cr
\text{so on... }
\end{cases}
$$
và biểu đồ tương ứng là:
<canvas id="ex2"></canvas>

## 2.2. Hàm mật độ xác suất của biến liên tục
Với các biến ngẫu nhiên liên tục ta có khái niệm *hàm mật độ xác suất* (*PDF - Probability Density Function*) để ước lượng độ tập trung xác suất tại lân cận điểm nào đó. Hàm mật độ xác suất $f(x)$ tại điểm $x$ được xác định bằng cách lấy đạo hàm của hàm phân phối tích luỹ $F(x)$ tại điểm đó:
$$f(x) = F^{\prime}(x)$$

Như vậy thì nơi nào $f(x)$ càng lớn thì ở đó mức độ tập xác suất càng cao. Từ đây ta cũng có thể biểu diễn hàm phân phối tích luỹ như sau:
$$F(x)=\int\_{-\infty}^xf(t)dt$$

Xác suất trong 1 khoảng $(\alpha,\beta)$ cũng có thể được tính bằng hàm mật độ xác suất:
$$P(\alpha \le X \le \beta)=\int_\alpha^\beta f(x)dx$$

Hàm mật độ xác suất cũng có 2 tính chất như xác suất như sau:

* Không âm: $f(x) \ge 0 ~~~, \forall x \in \mathbb{R}$
* Tổng toàn miền bằng 1: $\int\_{-\infty}^\infty f(x)dx = 1$

Ví dụ, thời gian tính bằng đơn vị giờ mà một máy tính hoạt động trước khi xảy ra lỗi được coi như một biến ngẫu nhiên liên tục và được xác định với hàm mật độ xác suất sau:
$$f(x)=\begin{cases}
\lambda e^{{-x}/{100}} &\text{if } x \ge 0 \\cr
0 &\text{else}
\end{cases}$$
Hãy tính xác suất của:

* (a) Một máy tính hoạt động từ 50 giờ tới 150 giờ trước khi xảy ra lỗi?
* (b) Một máy tính hoạt động dưới 100 giờ trước khi xảy ra lỗi?

Vì tổng xác suất toàn miền là 1 nên:
$$
\begin{aligned}
\& \int\_{-\infty}^\infty f(x)dx = 1
\\cr
\iff & \int\_{-\infty}^\infty \lambda e^{{-x}/{100}} dx = 1
\\cr
\iff & \lambda\int\_{-\infty}^\infty e^{{-x}/{100}} dx = 1
\\cr
\iff & \lambda\int_0^\infty e^{{-x}/{100}} dx = 1
\\cr
\iff & -\lambda(100)e^{{-x}/{100}} \Big|\_0^\infty = 1
\\cr
\iff & 100\lambda = 1
\\cr
\iff & \lambda = \frac{1}{100}
\end{aligned}
$$

(a) Xác suất để 1 máy tính hoạt động được trong khoảng (50, 150) giờ là:
$$
\begin{aligned}
P(50<X<150) &= \int\_{50}^{150}\frac{1}{100}e^{{-x}/{100}}dx
\\cr
\& = -e^{{-x}/{100}} \Big|\_{50}^{150}
\\cr
\& = e^{{-1}/{2}} -e^{{-3}/{2}}
\\cr
\& \approx 0.384
\\cr
\end{aligned}
$$
Như vậy, xấp xỉ 38.4 phần trăm thời gian một máy tính sẽ hoạt động trước khi lỗi trong khoảng 50 tới 150 giờ.

(b) Xác suất để 1 máy tính hoạt động được trong vòng 100 trước khi lỗi là:
$$
\begin{aligned}
P(X<100) &= \int_0^{100}\frac{1}{100}e^{{-x}/{100}}dx
\\cr
\& = -e^{{-x}/{100}} \Big|\_0^{100}
\\cr
\& = 1 -e^{-1}
\\cr
\& \approx 0.633
\\cr
\end{aligned}
$$
Nên xấp xỉ 63.3 phần trăm thời gian một máy tính sẽ lỗi sau 100 giờ sử dụng.

Ta có thể biểu diễn bằng đồ thị như sau:
<canvas id="ex3"></canvas>

Lưu ý rằng khác với hàm xác suất, hàm mật độ xác suất tại 1 điểm bất kì luôn bằng 0.
$$P(X=x)=\int_x^xf(t)dt=0$$

Ngoài ra, giá trị của hàm mật độ xác suất $f(x)$ có thể lớn hơn 1, miễn sao đảm bảo được rằng tổng xác suất toàn miền là 1: $\int\_{-\infty}^\infty f(x)dx = 1$.

# 3. Các phép toán
Tương tự như các phép toán xác suất đối với 1 sự kiện mà ta đã đề cập ở [phần trước](/vi/2017/10/what-is-prob/) thì các phép toán với xác suất của biến ngẫu nhiên cũng được áp dụng như vậy. Trong phần này ta biểu diễn xác suất của biến ngẫu nhiên:

* Rời rạc: Thông qua tổng của hàm khối xác suất: $$
* Liên tục: Tích phân của hàm mật độ xác suất: $P$

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
  var opts = {
    title: {
      display: true,
      position: 'bottom',
      text: 'Hình 1. Biểu đồ của PMF'
    },
    scales: {
      xAxes: [{
        scaleLabel: {
          display: true,
          labelString: 'x'
        }
      }],
      yAxes: [{
        ticks: {
          beginAtZero:true
        },
        scaleLabel: {
          display: true,
          labelString: 'p(x)'
        }
      }]
    }
  };
  // ex1
  new Chart('ex1', {
    type: 'bar',
    data: {
      labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      datasets: [{
        label: 'PMF Example 1',
        data: [0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36, 0],
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: opts
  });

  // ex2
  opts.title.text = 'Hình 2. Biểu đồ của CDF với PMF';
  opts.scales.yAxes[0].scaleLabel.labelString = 'p(x) | F(x)';
  new Chart('ex2', {
    type: 'bar',
    data: {
      labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      datasets: [{
        label: 'PMF Example 1',
        data: [0, 1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36, 0],
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }, {
        label: 'CDF Example 2',
        type: 'line',
        steppedLine: true,
        fill: false,
        data: [0, 1/36, 3/36, 6/36, 10/36, 15/36, 21/36, 26/36, 30/36, 33/36, 35/36, 36/36, 36/36],
        borderColor: 'rgba(255, 0, 0, 1)',
      }]
    },
    options: opts
  });
}
</script>
