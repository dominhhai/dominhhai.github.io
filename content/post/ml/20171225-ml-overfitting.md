---
title: "[ML] Vấn đề khớp quá (Overfitting)"
slug: ml-overfitting
date: 2017-12-25T08:45:04+09:00
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
Lỗi ước lượng tham số có thể được chia thành 2 loại là **khớp quá** (*over-fitting*) và **chưa khớp** (*under-fitting*) với tập huấn luyện. Trong bài này sẽ nói về cách theo dõi và hạn chế các lỗi này ra sao. Trọng tâm của bài này sẽ tập trung chủ yếu vào kĩ thuật **chính quy hoá** (*regularization*) để giải quyết vấn đề khớp quá của tham số.
<!--more-->
<!--toc-->
# 1. Giới thiệu
Mô hình của ta sau khi huấn luyện có thể đạt hiệu quả không tốt khi dự đoán với một dữ liệu mới. Chuyện này xảy ra là do mô hình của ta chưa tổng quát hoá được với toàn bộ tập dữ liệu. Nguyên nhân cũng khá dễ hiểu khi mà tập huấn luyện của ta chỉ là một tập nhỏ chưa thể đại diện cho toàn thể dữ liệu được và hơn nữa có thể nó còn bị nhiễu nữa. Người ta chia nguyên nhân ra làm 2 loại chính là *chưa khớp* hoặc *quá khớp*.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/ml/sin2pi.png" title="Hình 1: y=sin(2πx) model. Underfit: degree 1 (left); Goodfit: degree 3 (center); Overfit: degree 15 (right)" >}}

## 1.1. Chưa khớp (*Underfitting*)
Mô hình được coi là chưa khớp nếu nó chưa được chưa phù hợp với tập dữ liệu huấn luyện và cả các mẫu mới khi dự đoán. Nguyên nhân có thể là do mô hình chưa đủ độ phức tạp cần thiết để bao quát được tập dữ liệu. Ví dụ như hình 1 phía bên trái ở trên. Tập dữ liệu huấn luyện loanh quanh khúc $y=sin(2\pi x)$ thế nhưng mô hình của ta chỉ là một đường thẳng mà thôi. Rõ ràng như vậy thì nó không những không thể ước lượng được giá trị của $y$ với $x$ mới mà còn không hiệu quả với cả tập dữ liệu $(x,y)$ có sẵn.

## 1.2. Quá khớp (*Overfitting*)
Mô hình rất hợp lý, rất khớp với tập huấn luyện nhưng khi đem ra dự đoán với dữ liệu mới thì lại không phù hợp. Nguyên nhân có thể do ta chưa đủ dữ liệu để đánh giá hoặc do mô hình của ta quá phức tạp. Mô hình bị quá phức tạp khi mà mô hình của ta sử dụng cả những nhiễu lớn trong tập dữ liệu để học, dấn tới mất tính tổng quát của mô hình. Ví dụ như ở hình 1 phía bên phải ở trên. Mô hình của ta gần như mong muốn bao được hết tất cả các điểm làm cho biên độ dao động của nó lớn quá mức. Mô hình này mà dự đoán với 1 giá trị mới của $x$ thì khả năng $y$ sẽ bị lệch đi rất nhiều.

## 1.3. Vừa khớp (*Good Fitting*)
Mô hình này nằm giữa 2 mô hình chưa khớp và quá khớp cho ra kết quả hợp lý với cả tập dữ liệu huấn luyện và các giá trị mới, tức là nó mang được tính tổng quát như hình 1 ở giữa phía trên. Lý tưởng nhất là khớp được với nhiều dữ liệu mẫu và cả các dữ liệu mới. Tuy nhiên trên thực tế được mô hình như vậy rất hiếm.

# 2. Theo dõi lỗi
Với định nghĩa như trên ta cần phương pháp để đánh giá được mô hình trước khi có thể đưa ra được biện pháp cải tiến. Trước tiên ta quy định một số thông số lỗi để phục vụ cho việc đánh giá mô hình.

## 2.1. Đánh giá lỗi
Ở đây ta sẽ lấy trung bình lỗi của toàn bộ tập dữ liệu để đánh giá:
$$E(\theta)=\frac{1}{m}\sum\_{i=1}^m err(\hat y^{(i)},y^{(i)})$$

Trong đó $E(\theta)$ là lỗi ứng với tham số $\theta$ ước lượng được của tập dữ liệu gồm có $m$ mẫu. $err(\hat y,y)$ thể hiện cho sự khác biệt giữa giá trị dự đoán $\hat y$ và giá trị thực tế $y$. Đương nhiên là nếu $\hat y=y$ thì $err(\hat y^{(i)},y^{(i)})=0$. Thường người ta lấy $err(\hat y^{(i)},y^{(i)})=\Vert \hat y^{(i)}-y^{(i)}\Vert_2^2$ giống như các hàm lỗi của mô hình. Khi đó lỗi của ta được gọi là **lỗi trung bình bình phương** (*MSE - Mean Squared Error*):
$$E(\theta)=\frac{1}{m}\sum\_{i=1}^m\Vert \hat y^{(i)}-y^{(i)}\Vert_2^2$$

Như đã đề cập trong phần [các bước của học máy](/vi/2017/12/ml-intro/#3-c%C3%A1c-b%C6%B0%E1%BB%9Bc-h%E1%BB%8Dc-m%C3%A1y) thì dữ liệu của ta sẽ được phân chia làm 3 phần là **tập huấn luyện** (*training set*) 60%, **tập kiểm chứng** (*cross validation set*) 20% và **tập kiểm tra** (*test set*) 20%. Ứng với mỗi phần ta sẽ đưa ra thông số lỗi tương ứng:

* **Tập huấn luyện**: $\displaystyle E\_{train}(\theta)=\frac{1}{m\_{train}}\sum\_{i=1}^{m\_{train}}err(\hat y\_{train}^{(i)},y\_{train}^{(i)})$
* **Tập kiểm chứng**: $\displaystyle E\_{CV}(\theta)=\frac{1}{m\_{CV}}\sum\_{i=1}^{m\_{CV}}err(\hat y\_{CV}^{(i)},y\_{CV}^{(i)})$
* **Tập kiểm tra**: $\displaystyle E\_{test}(\theta)=\frac{1}{m\_{test}}\sum\_{i=1}^{m\_{test}}err(\hat y\_{test}^{(i)},y\_{test}^{(i)})$

Với mô hình hồi quy tuyến tính ta có thể lấy luôn hàm lỗi $\displaystyle J(\theta)=\frac{1}{2m}\sum\_{i=1}^m(\hat y^{(i)}-y^{(i)})^2$ để đánh giá lỗi. Đương nhiên là ứng với mỗi phần dữ liệu ta phải sử dụng dữ liệu của phần tương ứng để đánh giá:
$$
\begin{cases}
E\_{train}(\theta)=\displaystyle\frac{1}{2m\_{train}}\sum\_{i=1}^{m\_{train}}(\hat y\_{train}^{(i)}-y\_{train}^{(i)})^2 \\cr
E\_{CV}(\theta)=\displaystyle\frac{1}{2m\_{CV}}\sum\_{i=1}^{m\_{CV}}(\hat y\_{CV}^{(i)}-y\_{CV}^{(i)})^2 \\cr
E\_{test}(\theta)=\displaystyle\frac{1}{2m\_{test}}\sum\_{i=1}^{m\_{test}}(\hat y\_{test}^{(i)}-y\_{test}^{(i)})^2
\end{cases}
$$

## 2.2. Phán định lỗi
Với cách định nghĩa lỗi như trên thì một mô hình:

* *Chưa khớp*: Cả $E\_{train},E\_{CV},E\_{test}$ đều lớn.
* *Quá khớp*: $E\_{train}$ nhỏ còn $E\_{CV},E\_{test}$ lại lớn.
* *Vừa khớp*: Cả $E\_{train},E\_{CV},E\_{test}$ đều nhỏ.

Tuy nhiên khi huấn luyện bạn không được phép sờ tới tập kiểm tra, nên ta sử dụng 2 tập huấn luyện và kiểm chứng để dự đoán kiểu lỗi. Ví dụ hình dưới đây mô tả lỗi đồ thị của $E\_{train}(\theta)$ và $E\_{CV}(\theta)$.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/ml/diagnosing_bias_variance.png" title="Hình 2: Đồ thị của các lỗi. Source: https://www.coursera.org/learn/machine-learning/" >}}

Ở hình trên ta thấy rằng, trước điểm $d$ - bậc của đa thức hợp lý thì cả 2 lỗi đều có chiều hướng giảm dần, nhưng vượt qua điểm này thì lỗi tập huấn luyện vẫn tiếp tục nhỏ đi còn tập kiểm chứng lại vọt lên. Điều đó chứng tỏ rằng phía trước $d$ ta thu được lỗi *chưa khớp* và sau $d$ là lỗi *quá khớp*, còn ở $d$ là *vừa khớp*.

Một cách tổng quát, ta có thể dựa vào sự biến thiên của $E\_{train}$ và $E\_{CV}$ như trên để có phán định về tính chất của lỗi:

* $E\_{train}$ và $E\_{CV}$ đều lớn: Chưa khớp
* $E\_{train}$ và $E\_{CV}$ đều nhỏ: Vừa khớp
* $E\_{train}$ nhỏ còn $E\_{CV}$ lớn: Khớp quá

# 3. Cân bằng phương sai và độ lệch
# 4. Kĩ thuật chính quy hoá
$$J(\theta)=E_X(\theta)+\lambda E\_\theta(\theta)$$

$$E_\theta(\theta)=\frac{1}{2}\theta^{\intercal}\theta$$

$$\hat\theta=(\lambda\mathbf{I}+\Phi^{\intercal}\Phi)^{-1}\Phi^{\intercal}\mathbf{y}$$

# 5. Kết luận
Đánh giá mô hình có thể chia thành 3 dạng *chưa khớp* khi nó chưa đủ độ phức tạp, *quá khớp* khi nó quá phức tạp và *vừa khớp* khi mà nó vừa đủ để tổng quát hoá. Khi huấn luyện ta có thể sử dụng *tập huấn luyện* và *tập kiểm chứng* để đánh giá mô hình đang ở tình trạng nào. Nếu $E\_{train},E\_{CV}$ đều lớn thì ta nói rằng nó *chưa khớp*, còn $E\_{train}$ nhỏ và $E\_{CV}$ lớn thì ta nói rằng nó bị *quá khớp*.

Bài toán chưa khớp thì ta có thể giải quyết bằng cách phức tạp hoá mô hình lên còn với bài toán quá khớp thì ta có thể sử dụng phương pháp chính quy hoá để giải quyết:
$$J(\theta)=E_X(\theta)+\lambda E\_\theta(\theta)$$

Hệ số chính quy hoá $\lambda\ge 0$ ở đây thường nhỏ để không quá ảnh hưởng nhiều tới việc tối ưu lỗi truyền thống. Thường người ta sẽ chọn lấy 1 danh sách các $\lambda$ để huấn luyện và lấy một giá trị tối ưu nhất. Ví dụ: $\lambda=\\{0,0.01,0.02,0.04,0.08,0.16,0.32,0.64,1.28,2.56,5.12,10.24\\}$. Lưu ý rằng hệ số này không dùng cho tập *kiểm chứng* khi đối chiếu để đánh giá mô hình.
