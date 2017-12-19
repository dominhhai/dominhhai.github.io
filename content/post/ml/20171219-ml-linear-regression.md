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

> Kí hiệu: xem danh sách kí hiệu <a href="/vi/2017/10/math-notation/" target="_blank"_>tại đây</a>.

# 2. Mô hình

# 3. Ví dụ

<script>
function fnMain() {
  var opts = {
    title: {
      display: true,
      position: 'bottom',
      text: 'Hình 1. Quan hệ y=4x+3'
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
}
</script>
