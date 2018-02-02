---
title: "[ML] Hồi quy logistic (Logistic Regression)"
slug: ml-logistic-regression
date: 2017-12-28T11:19:53+09:00
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
Trong các phần trước ta đã tìm hiểu về phương pháp hồi quy tuyến tính để dự đoán đầu ra liên tục, phần này ta sẽ tìm hiểu thêm một thuật toán nữa trong học có giám sát là **hồi quy logistic** (*Logistic Regression*) nhằm mục đính phân loại dữ liệu.
<!--more-->
<!--toc-->
# 1. Định nghĩa
Phương pháp hồi quy logistic là một mô hình hồi quy nhằm dự đoán giá trị đầu ra *rời rạc* (*discrete target variable*) $y$ ứng với một véc-tơ đầu vào $\mathbf{x}$. Việc này tương đương với chuyện phân loại các đầu vào $\mathbf{x}$ vào các nhóm $y$ tương ứng.

Ví dụ, xem một bức ảnh có chứa một con mèo hay không. Thì ở đây ta coi đầu ra $y=1$ nếu bước ảnh có một con mèo và $y=0$ nếu bức ảnh không có con mèo nào. Đầu vào $\mathbf{x}$ ở đây sẽ là các pixel một bức ảnh đầu vào.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/ml/logistic-regression-1.png" title="Classification with 2 groups" >}}

Để đơn giản, trước tiên ta sẽ cùng đi tìm hiểu mô hình và cách giải quyết cho bài toán phân loại nhị phân tức là $y=\\{0,1\\}$. Sau đó ta mở rộng cho trường hợp nhiều nhóm sau.

# 2. Mô hình
Sử dụng phương pháp thống kê ta có thể coi rằng khả năng một đầu vào $\mathbf{x}$ nằm vào một nhóm $y_0$ là xác suất nhóm $y_0$ khi biết $\mathbf{x}$: $p(y_0|\mathbf{x})$. Dựa vào công thức xác xuất hậu nghiệm ta có:

$$
\begin{aligned}
p(y_0|\mathbf{x}) &= \dfrac{p(\mathbf{x}|y_0)p(y_0)}{p(\mathbf{x})}
\cr\ &= \dfrac{p(\mathbf{x}|y_0)p(y_0)}{p(\mathbf{x}|y_0)p(y_0) + p(\mathbf{x}|y_1)p(y_1)}
\end{aligned}
$$

Đặt:
$$a=\ln\dfrac{p(\mathbf{x}|y_0)p(y_0)}{p(\mathbf{x}|y_1)p(y_1)}$$

Ta có:
$$p(y_0|\mathbf{x})=\dfrac{1}{1+\exp(-a)}=\sigma(a)$$

Hàm $\sigma(a)$ ở đây được gọi là **hàm sigmoid** (*logistic sigmoid function*). Hình dạng chữ S bị chặn 2 đầu của nó rất đặt biệt ở chỗ dạng phân phối đều ra và rất mượt.
<canvas id="sigmoid"></canvas>


# 3. Ước lượng tham số
# 4. Lập trình
# 5. Kết luận

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
  // sigmoid: y = 1 / (1 + exp(-x))
  new Chart('sigmoid', {
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
