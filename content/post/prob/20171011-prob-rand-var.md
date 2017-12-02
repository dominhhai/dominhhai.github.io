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
customJS:
- https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js
---
Trong [phần trước](/vi/2017/10/what-is-prob/) ta đã có khái niệm rất cơ bản về phép thử, sự kiện, các tính chất của biến cố và cách tính xác suất của chúng. Trong phần này, ta sẽ tập trung vào các biến cố nhận giá trị ngẫu nhiên và mô hình phân phối xác suất của chúng.
<!--more-->

<!--toc-->
# 1. Biến ngẫu nhiên
Biến ngẫu nhiên (*random variables*) là các biến nhận 1 giá trị ngẫu nhiên đại diện cho kết quả của phép thử. Mỗi giá trị nhận được $x$ của biến ngẫu nhiên $X$ được gọi là một thể hiện của $X$, đây cũng là kết quả của phép thử hay còn được hiểu là một sự kiện.

Gọi tên là một biến có vẻ hơi kì kì một chút bởi biến ngẫu nhiên thực chất là một hàm ánh xạ từ không gian sự kiện đầy đủ tới 1 số thực: $X: \Omega \mapsto \mathbb{R}$.

Biến ngẫu nhiên có 2 dạng:

* Rời rạc (*discrete*): tập giá trị nó là rời rạc, tức là đếm được. Ví dụ như mặt chấm của con xúc xắc.
* Liên tục (*continous*): tập giá trị là liên tục tức là lấp đầy 1 khoảng trục số. Ví dụ như giá thuê nhà ở Hà Nội.

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

Như vậy thì nơi nào $f(x)$ càng lớn thì ở đó mức độ tập xác suất càng cao. Từ đây ta cũng có thể biểu diễn hàm phân phối tích luỹ như sau:
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

Nhìn vào biểu đồ trên ta có thấy xác suất (a) là phần diện tích của hình thang cong phủ từ $50 < x < 150$, còn xác suất (b) là phần diện tích hình thang cong phủ tới $x <100$. $x$ càng lớn thì $f(x)$ cũng càng bé đi nên phần phần diện tích của nó càng hẹp dần đồng nghĩa với mật độ xác suất cũng giảm dần nên xác suất để máy tính hoạt động được ngày càng thấp đi.

Lưu ý rằng khác với hàm xác suất, hàm mật độ xác suất tại 1 điểm bất kì luôn bằng 0.
$$P(X=x)=\int_x^xf(t)dt=0$$

Ngoài ra, giá trị của hàm mật độ xác suất $f(x)$ có thể lớn hơn 1, miễn sao đảm bảo được rằng tổng xác suất toàn miền là 1: $\int\_{-\infty}^\infty f(x)dx = 1$.

# 4. Các đặc trưng
Qua các hàm phân phối xác suất ở phần 3 phía trên ta có thể xác định được xác suất của một biến ngẫu nhiên và dựng được đồ thị biểu diễn nó, nhưng trong thực tế ta còn phải quan tâm tới các đặc trưng của nó như vị trí trung bình và độ phân tán ra sao. Trong thực tế khi tìm xác suất ta thường chỉ xác định các đặc trưng này vì rất khó xác định được hàm phân phối xác suất như trên.
## 4.1. Kỳ vọng
Kỳ vọng (*Expectation*) của biến ngẫu nhiên là trung bình của biến ngẫu nhiên. Kỳ vọng của biến ngẫu nhiên $X$ được kí hiệu là $E[X]$:
$$E[X]=\begin{cases}
\displaystyle\sum\_{\forall i} x_ip_i &\text{if x is discrete} \\cr
\displaystyle\int\_{-\infty}^\infty xf(x)dx &\text{if x is continous}
\end{cases}
$$

> Lưu ý là trung bình của biến ngẫu nhiên ở đây là trung bình với trọng lượng chứ không phải là trung bình cộng của xác suất biến ngẫu nhiên.

Kỳ vọng còn được biết tới với những tên gọi khác như *giá trị trung bình* (*Mean*), *giá trị trung bình có trọng lượng* (*Weighted Average*),*giá mong đợi* (*Expected Value*) hay *moment bậc một* (*first moment*).

Kỳ vọng có một số tính chất như sau:

* $E\(c) = c$ với $c$ là hằng số
* $E(cX) = cE(X)$ với $c$ là hằng số
* $E[aX+b] = aE[X]+b$ với $a, b$ là các hằng số
* $E[X+Y] = E[X]+E[Y]$
* $E[XY] = E[X]E[Y]$ với $X, Y$ là độc lập
* $E[g(X)] = \begin{cases}
\displaystyle\sum\_{\forall i} g(x_i)p_X(x_i) &\text{if x is discrete} \\cr
\displaystyle\int\_{-\infty}^\infty g(x)f(x)dx &\text{if x is continous}
\end{cases}
$

Việc chứng minh các tính chất trên không khó lắm nên tôi không đề cập ở đây nữa mà chỉ lấy một số ví dụ đặc trưng để mình họa.

Ví dụ: cho biến ngẫu nhiên rời rạc $X$ và một hàm $g(X)=X^n$, hãy tìm kì vọng của $g(X)$.
$$
\begin{aligned}
E[g(x)] &= \sum\_{\forall i} g(x_i)p_X(x_i) \\cr
\implies E[X^n] &= \sum\_{\forall i} x_i^np_X(x_i)
\end{aligned}
$$
$E[X^n]$ ở trên còn được biết tới với tên gọi moment bậc n (*nth moment*) của $X$.

## 4.2. Phương sai
Dựa vào kì vọng ta sẽ có được trung bình của biến ngẫu nhiên, tuy nhiên nó lại không cho ta thông tin về mức độ phân tán xác suất nên ta cần 1 phương pháp để đo được độ phân tán đó. Một trong những phương pháp đó là phương sai (*variance*).

Phương sai $Var(X)$ là trung bình của bình phương khoảng cách từ biến ngẫu nhiên $X$ tới giá trị trung bình:
$$Var(X)=E[(X-E[X])^2]$$

Việc tính toán dựa vào công thức này khá phức tạp, nên trong thực tế người ta thường sử dụng công thức tương đương sau:
$$Var(X)=E[X^2]-E^2[X]$$

Chứng minh:
$$
\begin{aligned}
Var(X) &= E[(X-E[X])^2] \\cr
\ &= E[X^2-2XE[X]+E^2[X]] \\cr
\ &= E[X^2]-E[2XE[X]]+E[E^2[X]] ~~~,\text{E[X] is constant} \\cr
\ &= E[X^2]-2E[X]E[X]+E^2[X] \\cr
\ &= E[X^2]-2E^2[X]
\end{aligned}
$$

Như vậy ta có thể thấy rằng phương sai luôn là một giá trị không âm và phương sai càng lớn thì nó thể hiện mức độ phân tán dữ liệu càng rộng hay nói cách khác mức độ ổn định càng nhỏ.

Phương sai có một số tính chất sau:

* $Var\(c) = 0$ với $c$ là hằng số
* $Var(cX) = c^2Var(X)$ với $c$ là hằng số
* $Var(aX+b) = a^2Var(X)$ với $a, b$ là các hằng số
* $Var(X+Y) = Var(X)+Var(Y)$ với $X, Y$ là độc lập

## 4.3. Độ lệch chuẩn
Vì đơn vị của phương sai là bình phương nên việc tính để khớp với đơn vị của biến ngẫu nhiên là bất khả nên người ta đưa vào thêm khái niệm **độ lệch chuẩn** (*SD-standard deviation*) bằng căn bậc 2 của phương sai.
$$\sigma(X)=\sqrt{Var(X)}$$

Từ đây người ta cũng có thể sử dụng $\sigma^2(X)$ để thể hiện phương sai của biến ngẫu nhiên $X$.

Lưu ý với độ lệch chuẩn ta phải lấy trị tuyệt đối của hằng số khi nhân vì độ lệch chuẩn cũng là không âm:

* $\sigma(cX)=|c|\sigma(X)$

## 4.4. Điểm chuẩn
Độ lệch chuẩn cho phép ta biết được mức độ phân tán trung bình của toàn bộ tập dữ liệu nhưng lại chưa cho ta biết được mức độ phân tán của 1 điểm nào đó. Chính vì vậy ta thêm một thông số nữa để đánh giá điểm này là **điểm chuẩn** (*SC-Standard Score*).

Đặt $\mu$ là kì vọng và $\sigma$ là độ lệch chuẩn thì điểm chuẩn được tính như sau:
$$z=\dfrac{x-\mu}{\sigma}$$

Từ công thức trên ta có thể thấy rằng $|z|$ thể hiện cho khoảng cách từ một điểm tới điểm trung bình của theo đơn vị là độ lệch chuẩn. Khi $z$ dương ta nói rằng điểm đó nằm phía trên điểm trung bình, còn khi $z$ âm thì nó nằm bên dưới điểm trung bình. Như vậy dựa vào điểm chuẩn ta có thể biết được rằng 1 điểm có nằm trong vùng phổ biến hay là không và nằm ở vị trí nào so với trung bình của toàn bộ tập mẫu.

Điểm chuẩn còn được gọi là *giá trị z (z-value)*, *điểm z (z-score)*. Tôi thì hay gọi điểm này là *z-score* do thói quen mà thôi :)

## 4.5. Trung vị
Trung vị (*median*) là điểm chia đều xác suất thành 2 phần giống nhau, kí hiệu là $med(X)$:
$$P(X < med(X)) = P(X \ge med(X)) = 0.5$$

Như vậy trung vị là nghiệm của phương trình hàm tích lũy xác suất: $F_X(x) = 0.5$

## 4.6. Moment (mô-men)
Là khái niệm tổng quát của kì vọng và phương sai. Một moment bậc $k$ đối với $c$ được định nghĩa như sau:
$$m_k = E[(X-a)^k]$$

Nhận xét rằng:

* Kỳ vọng là moment bậc 1 với $a=0$
* Phương sai là moment bậc 2 với $a=E[X]$

Khi $a=E[X]$ người ta thường gọi là moment quy tâm, còn $a=0$ gọi là moment gốc. Vậy nên ta có thể gọi kỳ vọng là moment gốc bậc 1 và phương sai là moment quy tâm bậc 2.

# 5. Kết luận
Bài này đã trình bày về một khái niệm rất quan trọng của xác suất thống kê là *biến ngẫu nhiên* - tương tự như các biến trong lập trình có thể nhận một giá trị bất kì thuộc trường số thực.

Cùng với đó là các hàm phân phối xác suất dùng cho việc xác định xác suất của biến ngẫu nhiên như:

* Hàm phân phối tích lũy (*CDF*): $F_X(x) = P(X \le x)$
* Hàm khối xác suất cho biến rời rạc (*PMF*): $p(x) = P(X=x)$
* Hàm mật độ xác suất cho biến liên tục (*PDF*): $f(x) = F^{\prime}(x)$

Phân phối xác suất có 2 đặc trưng quan trọng là *kỳ vọng* (*expectation*) và *phương sai* (*variance*). Trong đó *kỳ vọng* đặc trưng cho điểm trung bình của biến ngẫu nhiên, còn *phương sai* thể hiện cho mức độ phân tán phân phối quanh điểm trung bình đó. Phương sai càng lớn thì mức độ phân tán phân phối hay độ bất định của biến ngẫu nhiên càng rộng.

Tuy nhiên trong phần này ta mới chỉ đề cập tới 1 biến ngẫu nhiên 1 chiều ($X \in \mathbb R$). Nhưng trong thực tế ta thường xuyên phải làm việc với nhiều biến ngẫu nhiên cùng lúc hay có thể coi là một biến ngẫu nhiên nhiều chiều $X \in \mathbb R^n$. Ví dụ như giá nhà phụ thuộc vào diện tích, vị trí và thời gian xây dựng. Khi đó nếu ta tính xác suất để mua được 1 căn nhà dưới 1 tỉ thì cần phải sử dụng cả 3 biến ngẫu nhiên đặc trưng cho diện tích, vị trí và thời gian xây dựng, hoặc có thể là 1 biến ngẫu nhiên có 3 chiều (diện tích; vị trí; thời gian xây dựng). Việc kết hợp sử dụng biến ngẫu nhiên đa chiều như vậy sẽ được đề cập ở bài viết tới.

*Còn bây giờ, nếu có thắc mắc hay góp ý gì thì đừng quên để lại bình luận phía dưới cho mình nhé!*

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
  // ex1: PMF
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

  // ex2: PMF & CDF
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
        borderColor: 'rgba(255, 0, 0, 1)'
      }]
    },
    options: opts
  });

  // ex3: PDF
  opts.title.text = 'Hình 3. Biểu đồ của PDF';
  opts.scales.yAxes[0].scaleLabel.labelString = 'f(x)';
  new Chart('ex3', {
    type: 'line',
    data: {
      labels: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
      datasets: [{
        label: 'PDF f(x)',
        fill: false,
        data: [Math.exp(-0/100)/100, Math.exp(-10/100)/100, Math.exp(-20/100)/100, Math.exp(-30/100)/100, Math.exp(-40/100)/100, Math.exp(-50/100)/100, Math.exp(-60/100)/100, Math.exp(-70/100)/100, Math.exp(-80/100)/100, Math.exp(-90/100)/100, Math.exp(-100/100)/100, Math.exp(-110/100)/100, Math.exp(-120/100)/100, Math.exp(-130/100)/100, Math.exp(-140/100)/100, Math.exp(-150/100)/100, Math.exp(-160/100)/100, Math.exp(-170/100)/100, Math.exp(-180/100)/100, Math.exp(-190/100)/100, Math.exp(-200/100)/100],
        borderColor: 'rgba(54, 162, 235, 1)'
      }, {
        label: 'P(50<X<150)',
        data: [null, null, null, null, null, Math.exp(-50/100)/100, Math.exp(-60/100)/100, Math.exp(-70/100)/100, Math.exp(-80/100)/100, Math.exp(-90/100)/100, Math.exp(-100/100)/100, Math.exp(-110/100)/100, Math.exp(-120/100)/100, Math.exp(-130/100)/100, Math.exp(-140/100)/100, Math.exp(-150/100)/100],
        backgroundColor: 'rgba(255, 99, 132, 0.2)'
      }, {
        label: 'P(X<100)',
        data: [Math.exp(-0/100)/100, Math.exp(-10/100)/100, Math.exp(-20/100)/100, Math.exp(-30/100)/100, Math.exp(-40/100)/100, Math.exp(-50/100)/100, Math.exp(-60/100)/100, Math.exp(-70/100)/100, Math.exp(-80/100)/100, Math.exp(-90/100)/100, Math.exp(-100/100)/100],
        backgroundColor: 'rgba(255, 206, 86, 0.5)'
      }]
    },
    options: opts
  });
}
</script>
