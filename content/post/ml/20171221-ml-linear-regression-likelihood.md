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
---
Như bài viết trước đã đề cập tới phương pháp ước lượng tham số bằng công thức chuẩn cho thuật toán hồi quy tuyến tính $\theta=(\Phi^{\intercal}\Phi)^{-1}\Phi^{\intercal}\mathbf{y}$ bằng cách lấy đạo hàm hàm lỗi (*mean squared error*). Có thể bạn sẽ nghi ngờ về mức độ tin cậy thống kê của phương pháp ước lượng đó, nên bài viết này sẽ phân tích lý thuyết xác suất ước lượng bằng [MLE (*Maximum Likelihood Esitmation*)](/vi/2017/10/sampling-parameters-estimation/#2-2-mle) xem sao.
<!--more-->
<!--toc-->
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

Trong đó $\mathbf{t}=[t_1,t_2,...,t_m]^{\intercal}$ và $\mathbf{X}=[\mathbf{x}_1, \mathbf{x}_2,...,\mathbf{x}_m]^{\intercal}$ lần lượt là đầu ra và đầu vào thực tế (dữ liệu từ tập huấn luyện).

# 2. MLE với phân phối
Trước tiên ta sẽ xét MLE cho phân phối chuẩn một cách tổng quát rồi sẽ đi vào bài toán hồi quy tuyến tính. Vì việc nắm được lý thuyết sẽ giúp phân tích trường hợp cụ thể đơn giản hơn. Ở đây tôi không nhắc lại MLE là gì nữa mà sẽ đi thẳng vào vấn đề luôn. Nếu bạn cần tìm hiểu MLE là gì thì có thể xem tại <a href="/vi/2017/10/sampling-parameters-estimation/#2-2-mle" target="_blank"_>bài viết này</a>.
## 2.1. MLE với phân phối chuẩn
Giả sử rằng ta có $\theta=[\mu,\sigma^2]$ và tập mẫu biến ngẫu nhiên $\mathbf{X}=[X_1,X_2,...,X_m]$ tuân theo phân phối chuẩn: $X_i\sim\mathcal{N}(\mu,\sigma^2)$. Giờ nhiệm vụ của ta là phải tìm được các tham số $\theta$ để phân phối toàn mẫu đạt lớn nhất có thể.

Ta có xác suất toàn mẫu là:
$$
\begin{aligned}
L(\theta)&=\prod\_{i=1}^mf(X_i|\theta)
\\cr\ &=\prod\_{i=1}^m\frac{1}{\sqrt{2\pi\theta_1}}\exp\Bigg(-\frac{(X_i-\theta_0)^2}{2\theta_1}\Bigg)
\end{aligned}
$$

Lấy log ta sẽ được:
$$
\begin{aligned}
LL(\theta)&=\sum\_{i=1}^m\log\frac{1}{\sqrt{2\pi\theta_1}}\exp\Bigg(-\frac{(X_i-\theta_0)^2}{2\theta_1}\Bigg)
\\cr\ &=\sum\_{i=1}^m\Big(-\log\sqrt{2\pi\theta_1}-\frac{(X_i-\theta_0)^2}{2\theta_1}\Big)
\\cr\ &=-\frac{m}{2}\log(2\pi\theta_1)-\frac{1}{2\theta_1}\sum\_{i=1}^m\(X_i-\theta_0)^2
\\cr\ &=-\frac{m}{2}\log(2\pi)-\frac{m}{2}\log(\theta_1)-\frac{1}{2\theta_1}\sum\_{i=1}^m\(X_i-\theta_0)^2
\end{aligned}
$$

Để tìm tham số $\theta$ cho hàm $LL(\theta)$ trên đạt cực đại, ta sẽ sử dụng đạo hàm để giải quyết.

Với tham số $\theta_0$, đạo hàm riêng sẽ là:
$$\frac{\partial{LL}}{\theta_0}=\frac{1}{\theta_1}\sum\_{i=1}^m\(X_i-\theta_0)$$
Khi đạt cực đại, đạo hàm bị triệt tiêu ta sẽ có:
$$
\begin{aligned}
\ &\frac{1}{\theta_1}\sum\_{i=1}^m\(X_i-\theta_0)=0
\\cr\iff &m\theta_0=\sum\_{i=1}^mX_i
\\cr\iff &\theta_0=\frac{1}{m}\sum\_{i=1}^mX_i
\end{aligned}
$$

Tương tự, đạo hàm theo $\theta_1$ triệt tiêu:
$$
\begin{aligned}
\ &\frac{\partial{LL}}{\theta_1}=0
\\cr\iff &-\frac{m}{2\theta_1}+\frac{1}{2\theta_1^2}\sum\_{i=1}^m\(X_i-\theta_0)^2=0
\\cr\iff &m\theta_1=\sum\_{i=1}^m(X_i-\theta_0)^2
\\cr\iff &\theta_1=\frac{1}{m}\sum\_{i=1}^m(X_i-\theta_0)^2
\end{aligned}
$$

Như vậy giá tham số ước lượng được là $\hat\theta_0=\hat\mu=\dfrac{1}{m}\displaystyle\sum\_{i=1}^mX_i$ và $\hat\theta_1=\hat\sigma^2=\dfrac{1}{m}\displaystyle\sum\_{i=1}^m(X_i-\theta_0)^2$.

## 2.2. MLE với phân phối có nhiễu dạng chuẩn
Giả sử biến ngẫu nhiên $Y=\theta X+\mathcal{N}(0,\sigma^2)$ với phương sai $\sigma^2$ là cố định (biên dao động của nhiễu không đổi) và ta chưa biết phân phối của $X$ thế nào cả. Như vậy thì nếu $X$ đã biết trước $Y$ cũng tuân theo phân phối chuẩn $Y|X\sim\mathcal{N}(\theta X,\sigma^2)$. Nhiệm vụ của ta là ước lượng tham số $\theta$ sao cho xác suất của mẫu ngẫu nhiên đạt lớn nhất.

Giả sử ta có mẫu ngẫu nhiên có $m$ cặp dữ liệu $\\{(X_1,Y_1),(X_2,Y_2),...,(X_m,Y_m)\\}$, xác suất hợp của toàn mẫu sẽ là:

$$
\begin{aligned}
L(\theta)&=\prod\_{i=1}^mf(Y_i,X_i|\theta)
\\cr\ &=\prod\_{i=1}^mf(Y_i|X_i,\theta)f(X_i|\theta)
\\cr\ &=\prod\_{i=1}^mf(Y_i|X_i,\theta)f(X_i)
\\cr\ &=\prod\_{i=1}^m\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Bigg(-\frac{(Y_i-\theta X_i)^2}{2\sigma^2}\Bigg)f(X_i)
\end{aligned}
$$

Lấy log ta được:
$$
\begin{aligned}
LL(\theta)&=\sum\_{i=1}^m\log\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Bigg(-\frac{(Y_i-\theta X_i)^2}{2\sigma^2}\Bigg)f(X_i)
\\cr\ &=-\frac{m}{2}\log(2\pi)-\frac{m}{2}\log(\sigma^2)-\frac{1}{2\sigma^2}\sum\_{i=1}^m\(Y_i-\theta X_i)^2+\sum\_{i=1}^m\log f(X_i)
\end{aligned}
$$

Nếu đặt $\beta=\dfrac{1}{\sigma^2}$ thì công thức trên sẽ thành:
$$LL(\theta)=\frac{m}{2}\log\beta-\frac{m}{2}\log(2\pi)-\frac{1}{2}\beta\sum\_{i=1}^m\(Y_i-\theta X_i)^2+\sum\_{i=1}^m\log f(X_i)$$

Giờ để ước lượng $\theta$ sao cho $LL(\theta)$ đạt cực đại thì ta chỉ cần quan tâm tới thành phần có $\theta$ tức là việc ước lượng thành:
$$\hat\theta=\arg\min_\theta\sum\_{i=1}^m\(Y_i-\theta X_i)^2$$

# 3. MLE cho hồi quy tuyến tính
Giờ áp dụng MLE ta cần tìm tham số để cho xác suất toàn mẫu là lớn nhất có thể:
$$
\begin{aligned}
(\hat\theta,\hat\beta)&=\arg\max\_{\theta,\beta}\prod\_{i=1}^m\mathcal{N}(t_i|\theta^{\intercal}\phi(\mathbf{x}_i),\beta^{-1})
\\cr\ &=\arg\max\_{\theta,\beta}\sum\_{i=1}^m\log\mathcal{N}(t_i|\theta^{\intercal}\phi(\mathbf{x}_i),\beta^{-1})
\end{aligned}
$$

Như phân tích ở trên ta đã có:
$$\sum\_{i=1}^m\log\mathcal{N}(t_i|\theta^{\intercal}\phi(\mathbf{x}_i),\beta^{-1})=\frac{m}{2}\beta-\frac{m}{2}\log(2\pi)-\frac{1}{2}\beta\sum\_{i=1}^m\Big(t_i-\theta^{\intercal}\phi(\mathbf{x}_i)\Big)^2$$

Ở đây tôi lược bỏ thành phần $X$ đi để cho đơn giản. Thế giờ bạn nhìn thấy hàm lỗi $J(\theta)$ chưa?
$$J(\theta)=\frac{1}{2m}\sum\_{i=1}^m\Big(t_i-\theta^{\intercal}\phi(\mathbf{x}_i)\Big)^2$$

Từ đây ta sẽ được:
$$
\begin{aligned}
(\hat\theta,\hat\beta)&=\arg\max\_{\theta,\beta}\Big(\frac{m}{2}\beta-\frac{m}{2}\log(2\pi)-m\beta J(\theta)\Big)
\\cr\ &=\arg\max\_{\theta,\beta}\beta\Big(1-2J(\theta)\Big)
\end{aligned}
$$

Nếu coi $\beta$ ở đây là cố định (các điểm đầu ra có mức dao động như nhau) thì việc cực đại hoá này được quy về việc cực tiểu hoá hàm lỗi $J(\theta)$:
$$\hat\theta=\arg\min_\theta J(\theta)$$

# 4. Kết luận
Qua quá trình phân tích này ta nhận thấy được sự tương đồng giữa việc tối thiểu hoá hàm lỗi và cực đại hoá độ hợp lý tham số. Trên cơ sở đó ta hoàn toàn có thể yên tâm về mức độ tin cậy của phương pháp tối ưu hàm lỗi của ta.
