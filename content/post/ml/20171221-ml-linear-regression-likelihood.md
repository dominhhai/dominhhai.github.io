---
title: "[ML] MLE của hồi quy tuyến tính"
slug: ml-linear-regression-mle
date: 2017-12-21T12:28:26+09:00
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
Như bài viết trước đã đề cập tới phương pháp ước lượng tham số bằng công thức chuẩn cho thuật toán hồi quy tuyến tính $\theta=(\Phi^{\intercal}\Phi)^{-1}\Phi^{\intercal}\mathbf{y}$ bằng cách lấy đạo hàm hàm lỗi (*mean squared error*). Có thể bạn sẽ nghi ngờ về mức độ tin cậy thống kê của phương pháp ước lượng đó, nên bài viết này sẽ phân tích lý thuyết xác suất ước lượng bằng [MLE (*Maximum Likelihood Esitmation*)](/vi/2017/10/sampling-parameters-estimation/#2-2-mle) xem sao.
<!--more-->

# 1. Mô phỏng xác suất
Qua định lý <a href="https://en.wikipedia.org/wiki/Central_limit_theorem" target="_blank"_ rel="noopener noreferrer">giới hạn trung tâm</a> (*central limit theorem*) thì phân phối xác suất của biến ngẫu nhiên sẽ hội tụ về phân phối chuẩn. Vận dụng định lý này cho đầu ra của mỗi mô hình hồi quy tuyến tính, ta sẽ thêm 1 lượng nhiễu theo xác suất chuẩn vào đầu ra, ta sẽ được:
$$t=y(\mathbf{x},\theta)+\mathcal{N}(0,\sigma^2) ~~~,(1.1)$$

Như đã phân tích ở [phần phân phối chuẩn](/vi/2017/10/prob-com-var/#2-2-1-%C4%91%E1%BB%91i-v%E1%BB%9Bi-bi%E1%BA%BFn-1-chi%E1%BB%81u-univariate) ta có thể biểu diễn phân phối của $t$ bằng phân phối chuẩn:
$$p(t|\mathbf{x},\theta,\sigma)=\mathcal{N}(t|y(\mathbf{x},\theta),\sigma^2)$$

Đặt $\beta=\dfrac{1}{\sigma^2}$, ta có:
$$p(t|\mathbf{x},\theta,\beta)=\mathcal{N}(t|y(\mathbf{x},\theta),\beta^{-1})$$

Do $y(\mathbf{x},\theta)=\theta^{\intercal}\phi(\mathbf{x})$, nên:
$$p(t|\mathbf{x},\theta,\beta)=\mathcal{N}(t|\theta^{\intercal}\phi(\mathbf{x}),\beta^{-1})$$

Với giả sử dữ liệu huấn luyện của ta là I.I.D (mẫu ngẫu nhiên), ta sẽ thu được xác suất toàn mẫu là:
$$p(\mathbf{t}|\mathbf{X},\theta,\beta)=\prod\_{i=1}^m\mathcal{N}(t_i|\theta^{\intercal}\phi(\mathbf{x}_i),\beta^{-1})$$

Trong đó $\mathbf{t}=[t_1,t_2,...,t_m]^{\intercal}$ và $X=[\mathbf{x}_1, \mathbf{x}_2,...,\mathbf{x}_m]^{\intercal}$ lần lượt là đầu ra và đầu vào thực tế (dữ liệu từ tập huấn luyện).

# 2. MLE với phân phối chuẩn tắc

# 3. MLE với phân phối chuẩn

# 4. Kết luận
Qua quá trình phân tích này ta nhận thấy được sự tương đồng giữa việc tối thiểu hoá hàm lỗi và cực đại hoá độ hợp lý tham số. Trên cơ sở đó ta hoàn toàn có thể yên tâm về mức độ tin cậy của phương pháp tối ưu hàm lỗi của ta.
