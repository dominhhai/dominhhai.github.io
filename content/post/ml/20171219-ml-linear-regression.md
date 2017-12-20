---
title: "[ML] Hồi quy tuyến tính (Linear Regression)"
slug: ml-linear-regression
date: 2017-12-19T12:54:51+09:00
categories:
- Học Máy
- ML
tags:
- Học Máy
keywords:
- Học Máy
- Machine Learning
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/dl/logo.png
metaAlignment: center
customJS:
- https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js
draft: true
---
Học có giám sát (*Supervised Learning*) được chia ra làm 2 dạng lớn là **hồi quy** (*regression*) và **phân loại** (*classification*) dựa trên tập dữ liệu mẫu - tập huấn luyện (*training data*). Với bài đầu tiên này ta sẽ bắt đầu bằng bài toán hồi quy mà cụ thể là hồi quy tuyến tính (*linear regression*).
<!--more-->

<!--toc-->

# 1. Định nghĩa
Mục tiêu của giải thuật hồi quy tuyến tính là dự đoán giá trị của một hoặc nhiều *biến mục tiêu liên tục* (*continuous target variable*) $y$ dựa trên một véc-to đầu vào $\mathbf{x}$.

Ví dụ: dự đoán giá nhà ở Hà Nội dựa vào thông tin về diện tích, vị trí, năm xây dựng của ngôi nhà thì $t$ ở đây sẽ là giá nhà và $\mathbf{x}=(x_1,x_2,x_3)$ với $x_1$ là diện tích, $x_2$ là vị trí và $x_3$ là năm xây dựng.

Nếu bạn còn nhớ thì đây chính là phương pháp <a href="https://en.wikipedia.org/wiki/Regression_analysis" target="_blank"_ rel="noopener noreferrer">phân tích hồi quy</a> của xác suất thống kê. Mọi lý thuyết cơ bản của phương pháp này vẫn được giữa nguyên nhưng khi áp dụng cho máy tính thì về mặt cài đặt có thay đổi đôi chút.

Về cơ bản thì ta sẽ có một tập huấn luyện chứa các cặp $(\mathbf{x}^{(i)},y^{(i)})$ tương ứng và nhiệm vụ của ta là phải tìm giá trị $\hat{y}$ ứng với một đầu vào $\mathbf{x}$ mới. Để làm điều này ta cần tìm được quan hệ giữa $\mathbf{x}$ và $y$ để từ đó đưa ra được dự đoán. Hay nói cách trừu tượng hơn là ta cần vẽ được một đường quan hệ thể hiện mối quan hệ trong tập dữ liệu.

<canvas id="ex1"></canvas>

Như hình minh họa phía trên thì ta có thể vẽ được một đường màu xanh `y=3+4x` để thể hiện quan hệ giữa `x` và `y` dựa vào các điểm dữ liệu huấn luyện đã biết. Thuật toán hồi quy tuyến tính sẽ giúp ta tự động tìm được đường màu xanh đó để từ đó ta có thể dự đoán được `y` cho một `x` chưa từng xuất hiện bao giờ.

> Lưu ý về kí hiệu: xem danh sách kí hiệu <a href="/vi/2017/10/math-notation/" target="_blank"_>tại đây</a>.

# 2. Mô hình
Mô hình đơn giản nhất là mô hình kết hợp tuyến tính của các biến đầu vào:
$$y(\mathbf{x},\theta)=\theta_0+\theta_1x_1+...+\theta\_{n-1}x\_{n-1} ~~~(2.1)$$
trong đó $\mathbf{x}\in\\mathbb{R}^{n-1}$ là véc-to biến đầu vào và $\theta\in\\mathbb{R}^n$ là véc-to trọng số tương ứng. Thường $\theta$ được gọi là tham số của mô hình. Giá trị của tham số sẽ được ước lượng bằng cách sử dụng các cặp giá trị $(\mathbf{x}^{(i)},y^{(i)})$ của tập huấn luyện.

Thực ra mô hình tuyến tính là chỉ cần ở mức tuyến tính giữa tham số $\theta$ và $y$ là đủ. Và mình cho rằng tên gọi tuyến tính là xuất phát giữa $\theta$ và $y$, chứ không phải giữa $\mathbf{x}$ và $y$. Nói cách khác, ta có thể kết hợp các $\mathbf{x}$ một cách phi tuyến trước khi hợp với $\theta$ để được $y$. Một cách đơn giản là sử dụng hàm phi tuyến cho $\mathbf{x}$ như sau:
$$y(\mathbf{x},\theta)=\theta_0+\theta_1\phi_1(\mathbf{x})+...+\theta\_{n-1}\phi\_{n-1}(\mathbf{x}) ~~~(2.2)$$

Các hàm phi tuyến $\phi_i(\mathbf{x})$ này được gọi là các **hàm cơ bản** (*basic function*). Thường người ta sẽ đặt $\phi_0(\mathbf{x})=1$ và viết lại công thức trên như sau:
$$y(\mathbf{x},\theta)=\sum\_{i=0}^{n-1}\theta_i\phi_i(\mathbf{x})=\theta^{\intercal}\phi(\mathbf{x}) ~~~(2.3)$$

Như <a href="/vi/2017/10/math-notation/#s%E1%BB%91-v%C3%A0-ma-tr%E1%BA%ADn" target="_blank"_>quy ước</a> thì tất cả các véc-to nếu không nói gì thì ta ngầm định với nhau rằng nó là véc-to cột nên ta có được cách viết nhân ma trận như trên.

# 3. Ước lượng tham số
Giả sử ta có $m$ cặp dữ liệu huấn luyện và $\hat{y}\in\mathbb{R}^m$ là kết quả dự đoán. Ta có thể đánh giá mức độ chênh lệch kết quả $\hat{y}$ và $y$ bằng một **hàm lỗi** (*lost function*) như sau:

$$
\begin{aligned}
J(\theta) &= \frac{1}{2m}\sum\_{i=0}^m(\hat{y}_i-y_i)^2
\\cr\ &= \frac{1}{2m}\sum\_{i=0}^m\Big(\theta^{\intercal}\phi(\mathbf{x}_i)-y_i\Big)^2 &(3.1)
\end{aligned}
$$

Công thức trên thể hiện trung bình của độ lệch (*khoảng cách*) giữa các điểm dữ liệu thực tế và kết quả dự đoán sau khi ta ước lượng tham số. Còn tại sao ta lại chia cho 2 thì tôi sẽ giải thích sau. Hàm lỗi còn có tên gọi khác là **hàm lỗi bình phương** (*squared error function*) hoặc **hàm lỗi trung bình bình phương** (*mean squared error function*) hoặc **hàm chi phí** (*cost function*).

Không cần giải thích ta cũng có thể hiểu với nhau rằng tham số tốt nhất là tham số giúp cho hàm lỗi $J$ đạt giá trị nhỏ nhất.
$$\hat\theta=\arg\min_{\theta}J(\theta) ~~~(3.2)$$
Kết quả tối ưu nhất là $\hat{y}=y$, tức là $J(\theta)=0$. Để giải quyết bài toán này ta có thể sử dụng đạo hàm của $J(\theta)$ và tìm $\theta$ sao cho $J(\theta)^{\prime}=0$.
$$
\begin{aligned}
\ &0 = \frac{1}{m}\sum\_{i=0}^m(\theta^{\intercal}\phi(\mathbf{x}_i)-y_i)\phi(\mathbf{x}_i)^{\intercal} &(3.3)
\\cr\iff& \sum\_{i=0}^m\theta^{\intercal}\phi(\mathbf{x}_i)\phi(\mathbf{x}_i)^{\intercal} = \sum\_{i=0}^my_i\phi(\mathbf{x}_i)^{\intercal}&(3.4)
\\cr\iff&\theta = (\Phi^{\intercal}\Phi)^{-1}\Phi^{\intercal}\mathbf{y} &(3.5)
\end{aligned}
$$

Đây chính là **công thức chuẩn** (*normal equation*) của bài toán ta cần giải. Trong đó ma trận $\Phi\in\\mathbb{R}^{n\times m}$ là:
$$\Phi=
\begin{bmatrix}
\phi_0(x_1)&\phi_1(x_1)&...&\phi\_{m-1}(x_1)\\cr
\phi_0(x_2)&\phi_1(x_2)&...&\phi\_{m-1}(x_2)\\cr
\vdots&\vdots&\ddots&\vdots\\cr
\phi_0(x_n)&\phi_1(x_n)&...&\phi\_{m-1}(x_n)
\end{bmatrix}$$

Ở phép lấy đạo hàm `(3.3)` ta thấy rằng mẫu số 2 bị triệt tiêu và giúp bỏ đi được thừa số 2 khi tính đạo hàm. Đấy chính là lý do mà người ta để mẫu số 2 cho hàm lỗi.

# 4. Lập trình
Chém gió loằng ngoằng mãi rồi, giờ phải bắt tay vào code thử xem đúng hay sai.
## 4.1. Ví dụ 1
Ví dụ khởi động này tôi sẽ lấy dữ liệu đơn giản $y=3+4x$ để làm việc.
Trước tiên tôi đã chuẩn bị tập dữ liệu huấn luyện gồm 100 cặp dữ liệu được sinh ra theo nhiễu của hàm $y=3+4x$ tại <a href="https://github.com/dominhhai/mldl/blob/master/dataset/1_linearinput.csv" target="_blank"_ rel="noopener noreferrer">Repo trên Github</a>.

Ở đây tôi sẽ sử dụng các thư viện `pandas` (xử lý dữ liệu), `mathplotlib` (đồ hình dữ liệu) và `numpy` (thao tác toán học) để làm việc:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Dữ liệu của ta chỉ có 1 chiều nên dễ dàng đồ hình hoá, việc này cũng giúp ta ước lượng được đôi chút việc chọn các tiêu chí ràng buộc cho mô hình của ta.
```python
# load data
df = pd.read_csv(DATA_FILE_NAME)
# plot data
df.plot(x='x', y='y', legend=False, marker='o', style='o', mec='b', mfc='w')
# expected line
plt.plot(df.values[:,0], df.values[:,1], color='g')
plt.xlabel('x'); plt.ylabel('y'); plt.show()
```
<canvas id="ex2"></canvas>

Nhìn vào biểu đồ của dữ liệu ta có thể nghĩ rằng $x$ ở đây tuyến tính với $y$, tức là ta có thể chọn $\phi(\mathbf{x})=\mathbf{x}$. Lúc này, $\Phi$ của ta sẽ bằng ma trận $X$.

Do $(\Phi^{\intercal}\Phi)$ có thể không khả nghịch nên ta có thể sử dụng phép giả nghịch đảo để làm việc:
```python
theta = np.dot(np.linalg.pinv(np.dot(X.T, X)), np.dot(X.T, y))
```
Phép trên sẽ cho ta kết quả: `theta=[-577.17310612, 4.16001358]`, tức:
$$
\begin{cases}
\theta_0=-577.17310612\\cr
\theta_1=4.16001358
\end{cases}
$$
Giờ ta thử đưa kết quả lên hình vẽ xem sao.
<canvas id="ex3"></canvas>

Như vậy ta thấy rằng $\theta_1$ khá khớp còn $\theta_0$ lại lệch rất nhiều, nhưng kết quả lại khá khớp với tập dữ liệu đang có. Nên ta có thể kì vọng rằng nếu gia tăng khoảng dữ liệu thì công thức chuẩn sẽ cho ta kết quả khá hợp lý.

Bạn có thể xem toàn bộ mã nguồn đầy đủ của phần này trên <a href="https://github.com/dominhhai/mldl/blob/master/code/linear_regression/one_var_linearinput.py" target="_blank"_ rel="noopener noreferrer">Github</a> hoặc dễ dàng hơn với <a href="https://github.com/dominhhai/mldl/blob/master/code/linear_regression/one_var_linearinput.ipynb" target="_blank"_ rel="noopener noreferrer">IPython</a>.

## 4.2. Ví dụ 2
Phần này ta sẽ phức tạp vấn đề lên 1 chút bằng cách lấy $y=\sin(2\pi x)$. Tương tự như trên tôi đã chuẩn bị dữ liệu trên <a href="https://github.com/dominhhai/mldl/blob/master/dataset/1_sin2pi.csv" target="_blank"_ rel="noopener noreferrer">trên Repo đó</a>.

# 5. Kết luận
Thuật toán hồi quy tuyến tính (*linear regression*) thuộc vào nhóm học có giám sát (*supervised learning*) là được **mô hình** hoá bằng:
$$y(\mathbf{x},\theta)=\theta^{\intercal}\phi(\mathbf{x})$$
Khi khảo sát tìm tham số của mô hình ta có thể giải quyết thông qua việc tối thiểu hoá **hàm lỗi** (*loss function*):
$$J(\theta)=\dfrac{1}{2m}\displaystyle\sum\_{i=0}^m\Big(\theta^{\intercal}\phi(\mathbf{x}_i)-y_i\Big)^2$$
Hàm lỗi này thể hiện trung bình độ lệch giữa kết quả ước lượng và kết quả thực tế. Việc lấy bình phương giúp ta có thể dễ dàng tối ưu được bằng cách lấy đạo hàm vì nó có đạo hàm tại mọi điểm! Qua phép đạo hàm ta có được **công thức chuẩn** (*normal equation*) cho tham số:
$$\theta = (\Phi^{\intercal}\Phi)^{-1}\Phi^{\intercal}\mathbf{y}$$
Trong đó $\Phi\in\\mathbb{R}^{n\times m}$:
$$\Phi=
\begin{bmatrix}
\phi_0(x_1)&\phi_1(x_1)&...&\phi\_{m-1}(x_1)\\cr
\phi_0(x_2)&\phi_1(x_2)&...&\phi\_{m-1}(x_2)\\cr
\vdots&\vdots&\ddots&\vdots\\cr
\phi_0(x_n)&\phi_1(x_n)&...&\phi\_{m-1}(x_n)
\end{bmatrix}$$

Khi lập trình với `python` ta có thể giải quyết việc $(\Phi^{\intercal}\Phi)$ không khả nghịch bằng cách sử dụng **giả nghịch đảo** để tính toán:
```python
np.linalg.pinv(np.dot(X.T, X))
```

Từ đầu tới giờ ta vẫn chưa bàn về cách chọn hàm phi tuyến $\phi(\mathbf{x})$ ra sao và cũng chưa đưa ra các hạn chế cũng như cách khắc phục của mô hình này. Nhưng bài viết lần này đã khá dài, nên tôi xin phép viết vào các bài tiếp theo.

<script>
function fnMain() {
  var opts = {
    title: {
      display: true,
      position: 'bottom',
      text: 'Hình 1. Quan hệ y=3+4x'
    },
    scales: {
      xAxes: [{
        type: 'linear',
        position: 'bottom',
        ticks: {
          max: 5000
        },
        scaleLabel: {
          display: true,
          labelString: 'x'
        }
      }],
      yAxes: [{
        scaleLabel: {
          display: true,
          labelString: 'y'
        }
      }]
    }
  };
  // ex1: y=3+4x
  new Chart('ex1', {
    type: 'line',
    data: {
      datasets: [{
        label: 'Expected Line',
        backgroundColor: 'rgba(0, 128, 0, 1)',
        borderColor: 'rgba(0, 128, 0, 1)',
        fill: false,
        pointRadius: 0,
        data: [{x:1024,y:4099},{x:4968,y:19875}]
      }, {
        type: 'bubble',
        label: 'Training Data',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        data: [{x:1024,y:3041.34479672},{x:1077,y:3848.11290461},{x:1093,y:1425.14949365},{x:1114,y:3784.23651747},{x:1125,y:6153.79172866},{x:1199,y:3554.11797412},{x:1228,y:3580.0545406},{x:1254,y:3302.36707498},{x:1271,y:4411.08028247},{x:1300,y:4984.36490397},{x:1339,y:3618.27841285},{x:1377,y:3504.57835306},{x:1417,y:6589.78692837},{x:1536,y:5217.89629577},{x:1613,y:18396.38637446},{x:1636,y:5222.87799369},{x:1665,y:4999.52100524},{x:1680,y:5665.26113175},{x:1726,y:8264.58318873},{x:1726,y:8507.36647557},{x:1844,y:7770.4563142},{x:1884,y:9743.47131578},{x:1942,y:6771.49886413},{x:1962,y:9084.57940426},{x:1994,y:9043.94701116},{x:2007,y:8776.39151486},{x:2066,y:10050.1578826},{x:2239,y:8916.42555485},{x:2239,y:8165.64808713},{x:2305,y:8755.25366519},{x:2310,y:8364.34661322},{x:2322,y:8915.34859433},{x:2379,y:9197.38241427},{x:2440,y:7851.95904396},{x:2544,y:8207.20804011},{x:2549,y:8709.82913985},{x:2578,y:11755.6163048},{x:2604,y:8596.51192103},{x:2615,y:10361.0047482},{x:2638,y:9411.6197175},{x:2761,y:9319.6415672},{x:2769,y:12842.8819172},{x:2786,y:11531.2407491},{x:2820,y:8595.93288139},{x:2844,y:12229.2987937},{x:2876,y:12759.8926708},{x:3055,y:12137.8405953},{x:3068,y:11996.5109723},{x:3094,y:11800.2729985},{x:3094,y:12566.2939954},{x:3130,y:13600.3942388},{x:3132,y:14640.825237},{x:3193,y:11428.4092551},{x:3207,y:12301.4877344},{x:3322,y:12999.5669428},{x:3372,y:15054.715276},{x:3380,y:12525.3570879},{x:3455,y:14183.6408623},{x:3468,y:16607.8764098},{x:3549,y:15966.3032046},{x:3605,y:15479.7197159},{x:3696,y:16868.0934864},{x:3704,y:13931.9144869},{x:3939,y:16177.9194112},{x:3940,y:14843.2978469},{x:3954,y:17660.6273388},{x:4001,y:11626.150281},{x:4037,y:18021.1539509},{x:4040,y:15692.8771098},{x:4072,y:15529.7418794},{x:4110,y:19643.2255653},{x:4129,y:15436.0340749},{x:4161,y:16222.9260112},{x:4174,y:15331.25712},{x:4240,y:15681.3275478},{x:4291,y:19263.7251749},{x:4298,y:16254.3605446},{x:4327,y:16945.6846065},{x:4364,y:18965.7091401},{x:4420,y:17848.2934953},{x:4422,y:18893.8296387},{x:4441,y:19548.8303537},{x:4449,y:17997.3169139},{x:4509,y:17680.3094298},{x:4535,y:20888.1014948},{x:4559,y:18718.2694955},{x:4626,y:17537.3976187},{x:4710,y:18955.2873097},{x:4737,y:16783.8474195},{x:4776,y:19772.5909007},{x:4786,y:17760.8922801},{x:4809,y:20106.9348223},{x:4813,y:19525.5150033},{x:4845,y:17059.5073393},{x:4860,y:19594.6604656},{x:4884,y:19585.7409977},{x:4901,y:18295.7299998},{x:4949,y:21835.5489789},{x:4949,y:19998.4766695},{x:4968,y:20582.4548821}]
      }]
    },
    options: opts
  });
  // ex2: y=3+4x
  opts.title.text = 'Hình 2. Tập huấn luyện y=3+4x';
  new Chart('ex2', {
    type: 'line',
    data: {
      datasets: [{
        label: 'Expected Line',
        backgroundColor: 'rgba(0, 128, 0, 1)',
        borderColor: 'rgba(0, 128, 0, 1)',
        fill: false,
        pointRadius: 0,
        data: [{x:1024,y:4099},{x:4968,y:19875}]
      }, {
        type: 'bubble',
        label: 'Training Data',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        data: [{x:1024,y:3041.34479672},{x:1077,y:3848.11290461},{x:1093,y:1425.14949365},{x:1114,y:3784.23651747},{x:1125,y:6153.79172866},{x:1199,y:3554.11797412},{x:1228,y:3580.0545406},{x:1254,y:3302.36707498},{x:1271,y:4411.08028247},{x:1300,y:4984.36490397},{x:1339,y:3618.27841285},{x:1377,y:3504.57835306},{x:1417,y:6589.78692837},{x:1536,y:5217.89629577},{x:1613,y:18396.38637446},{x:1636,y:5222.87799369},{x:1665,y:4999.52100524},{x:1680,y:5665.26113175},{x:1726,y:8264.58318873},{x:1726,y:8507.36647557},{x:1844,y:7770.4563142},{x:1884,y:9743.47131578},{x:1942,y:6771.49886413},{x:1962,y:9084.57940426},{x:1994,y:9043.94701116},{x:2007,y:8776.39151486},{x:2066,y:10050.1578826},{x:2239,y:8916.42555485},{x:2239,y:8165.64808713},{x:2305,y:8755.25366519},{x:2310,y:8364.34661322},{x:2322,y:8915.34859433},{x:2379,y:9197.38241427},{x:2440,y:7851.95904396},{x:2544,y:8207.20804011},{x:2549,y:8709.82913985},{x:2578,y:11755.6163048},{x:2604,y:8596.51192103},{x:2615,y:10361.0047482},{x:2638,y:9411.6197175},{x:2761,y:9319.6415672},{x:2769,y:12842.8819172},{x:2786,y:11531.2407491},{x:2820,y:8595.93288139},{x:2844,y:12229.2987937},{x:2876,y:12759.8926708},{x:3055,y:12137.8405953},{x:3068,y:11996.5109723},{x:3094,y:11800.2729985},{x:3094,y:12566.2939954},{x:3130,y:13600.3942388},{x:3132,y:14640.825237},{x:3193,y:11428.4092551},{x:3207,y:12301.4877344},{x:3322,y:12999.5669428},{x:3372,y:15054.715276},{x:3380,y:12525.3570879},{x:3455,y:14183.6408623},{x:3468,y:16607.8764098},{x:3549,y:15966.3032046},{x:3605,y:15479.7197159},{x:3696,y:16868.0934864},{x:3704,y:13931.9144869},{x:3939,y:16177.9194112},{x:3940,y:14843.2978469},{x:3954,y:17660.6273388},{x:4001,y:11626.150281},{x:4037,y:18021.1539509},{x:4040,y:15692.8771098},{x:4072,y:15529.7418794},{x:4110,y:19643.2255653},{x:4129,y:15436.0340749},{x:4161,y:16222.9260112},{x:4174,y:15331.25712},{x:4240,y:15681.3275478},{x:4291,y:19263.7251749},{x:4298,y:16254.3605446},{x:4327,y:16945.6846065},{x:4364,y:18965.7091401},{x:4420,y:17848.2934953},{x:4422,y:18893.8296387},{x:4441,y:19548.8303537},{x:4449,y:17997.3169139},{x:4509,y:17680.3094298},{x:4535,y:20888.1014948},{x:4559,y:18718.2694955},{x:4626,y:17537.3976187},{x:4710,y:18955.2873097},{x:4737,y:16783.8474195},{x:4776,y:19772.5909007},{x:4786,y:17760.8922801},{x:4809,y:20106.9348223},{x:4813,y:19525.5150033},{x:4845,y:17059.5073393},{x:4860,y:19594.6604656},{x:4884,y:19585.7409977},{x:4901,y:18295.7299998},{x:4949,y:21835.5489789},{x:4949,y:19998.4766695},{x:4968,y:20582.4548821}]
      }]
    },
    options: opts
  });
  // ex3: y=3+4x
  opts.title.text = 'Hình 3. Kết quả dự đoán y=3+4x';
  new Chart('ex3', {
    type: 'line',
    data: {
      datasets: [{
        label: 'Expected Line',
        backgroundColor: 'rgba(0, 128, 0, 1)',
        borderColor: 'rgba(0, 128, 0, 1)',
        fill: false,
        pointRadius: 0,
        data: [{x:1024,y:4099},{x:4968,y:19875}]
      }, {
        type: 'bubble',
        label: 'Training Data',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        data: [{x:1024,y:3041.34479672},{x:1077,y:3848.11290461},{x:1093,y:1425.14949365},{x:1114,y:3784.23651747},{x:1125,y:6153.79172866},{x:1199,y:3554.11797412},{x:1228,y:3580.0545406},{x:1254,y:3302.36707498},{x:1271,y:4411.08028247},{x:1300,y:4984.36490397},{x:1339,y:3618.27841285},{x:1377,y:3504.57835306},{x:1417,y:6589.78692837},{x:1536,y:5217.89629577},{x:1613,y:18396.38637446},{x:1636,y:5222.87799369},{x:1665,y:4999.52100524},{x:1680,y:5665.26113175},{x:1726,y:8264.58318873},{x:1726,y:8507.36647557},{x:1844,y:7770.4563142},{x:1884,y:9743.47131578},{x:1942,y:6771.49886413},{x:1962,y:9084.57940426},{x:1994,y:9043.94701116},{x:2007,y:8776.39151486},{x:2066,y:10050.1578826},{x:2239,y:8916.42555485},{x:2239,y:8165.64808713},{x:2305,y:8755.25366519},{x:2310,y:8364.34661322},{x:2322,y:8915.34859433},{x:2379,y:9197.38241427},{x:2440,y:7851.95904396},{x:2544,y:8207.20804011},{x:2549,y:8709.82913985},{x:2578,y:11755.6163048},{x:2604,y:8596.51192103},{x:2615,y:10361.0047482},{x:2638,y:9411.6197175},{x:2761,y:9319.6415672},{x:2769,y:12842.8819172},{x:2786,y:11531.2407491},{x:2820,y:8595.93288139},{x:2844,y:12229.2987937},{x:2876,y:12759.8926708},{x:3055,y:12137.8405953},{x:3068,y:11996.5109723},{x:3094,y:11800.2729985},{x:3094,y:12566.2939954},{x:3130,y:13600.3942388},{x:3132,y:14640.825237},{x:3193,y:11428.4092551},{x:3207,y:12301.4877344},{x:3322,y:12999.5669428},{x:3372,y:15054.715276},{x:3380,y:12525.3570879},{x:3455,y:14183.6408623},{x:3468,y:16607.8764098},{x:3549,y:15966.3032046},{x:3605,y:15479.7197159},{x:3696,y:16868.0934864},{x:3704,y:13931.9144869},{x:3939,y:16177.9194112},{x:3940,y:14843.2978469},{x:3954,y:17660.6273388},{x:4001,y:11626.150281},{x:4037,y:18021.1539509},{x:4040,y:15692.8771098},{x:4072,y:15529.7418794},{x:4110,y:19643.2255653},{x:4129,y:15436.0340749},{x:4161,y:16222.9260112},{x:4174,y:15331.25712},{x:4240,y:15681.3275478},{x:4291,y:19263.7251749},{x:4298,y:16254.3605446},{x:4327,y:16945.6846065},{x:4364,y:18965.7091401},{x:4420,y:17848.2934953},{x:4422,y:18893.8296387},{x:4441,y:19548.8303537},{x:4449,y:17997.3169139},{x:4509,y:17680.3094298},{x:4535,y:20888.1014948},{x:4559,y:18718.2694955},{x:4626,y:17537.3976187},{x:4710,y:18955.2873097},{x:4737,y:16783.8474195},{x:4776,y:19772.5909007},{x:4786,y:17760.8922801},{x:4809,y:20106.9348223},{x:4813,y:19525.5150033},{x:4845,y:17059.5073393},{x:4860,y:19594.6604656},{x:4884,y:19585.7409977},{x:4901,y:18295.7299998},{x:4949,y:21835.5489789},{x:4949,y:19998.4766695},{x:4968,y:20582.4548821}]
      }]
    },
    options: opts
  });
}
</script>
