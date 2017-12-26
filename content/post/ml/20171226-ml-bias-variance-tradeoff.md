---
title: "[ML] Cân bằng phương sai và độ lệch"
slug: 20171226-ml-bias-variance-tradeoff
date: 2017-12-26T14:48:36+09:00
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
draft: true
---
Bài này sẽ tập trung vào lý thuyết đằng sau các lỗi mô hình đã trình bày ở [bài viết trước](/vi/2017/12/ml-overfitting/). Việc hiểu lý thuyết này giúp ta có được cái nhìn toàn vẹn hơn về lỗi mô hình và cơ sở đánh giá lỗi.
<!--more-->
<!--toc-->

# 1. Phân tích phương sai và độ lệch
Giả sử ta có $t=f(\mathbf{x},\theta)+\mathcal{N}(0,\sigma^2)$ là đầu ra thực tế ứng với mỗi đầu vào $\mathbf{x}$. Giờ ta cần tìm $y(\mathbf{x},\theta)$ xấp xỉ với $f(\mathbf{x},\theta)$ nhất có thể bằng cách học tham số $\theta$.

Nếu ta coi lỗi $L\big(t,y(\mathbf{x})\big)$ là độ chênh lệch giữa điểm thực tế và ước lượng với $y(\mathbf{x},\theta)$ thì ta có trung bình lỗi hay nói cách khác là kỳ vọng lỗi là:
$$E[L]=\iint L\big(t,y(\mathbf{x})\big)p(\mathbf{x},t)\text{d}\mathbf{x}\text{d}t$$

Như các bài trước đã phân tích, ta chọn:
$$L\big(t,y(\mathbf{x})\big)=\big(y(\mathbf{x})-t\big)^2$$

Như vậy:
$$E[L]=\iint\big(y(\mathbf{x})-t\big)^2p(\mathbf{x},t)\text{d}\mathbf{x}\text{d}t$$

Về cơ bản đây cũng chính là công thức tương đương của hàm lỗi $J(\theta)$ mà ta đã đề cập ở các bài trước. Giờ mục tiêu của ta cũng là tìm $\theta$ sao cho kỳ vọng lỗi $E[L]$ là nhỏ nhất.

Kỳ vọng lỗi này có thể phân tích ra phương sai và độ lệch như sau:
$$E[L]=\text{Bias}^2+\text{Var}+\text{Noise}$$
Trong đó:

* Độ lệch $\text{Bias}=E[y(\mathbf{x})-f(\mathbf{x})]$
* Phương sai $\text{Var}=E[y(\mathbf{x})^2]-E[y(\mathbf{x})]^2$
* Nhiễu $\text{Noise}=\sigma^2$

Do $\sigma^2$ được cố định từ trước bằng giả thuyết phân phối chuẩn, nên kỳ vọng lỗi của ta sẽ phụ thuộc vào 2 thành phần là độ lệch và phương sai.

# 2. Quan hệ phương sai và độ lệch
Kỳ vọng lỗi nhỏ ứng với độ lệch và phương sai nhỏ tuy nhiên để đạt được điều này thì cực kì khó khăn. Thường ta sẽ mong muốn

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/ml/bias_variance_tradeoff.jpg" title="Hình 1: Mô tả quan hệ bias-variance" >}}

# 3. Kết luận
