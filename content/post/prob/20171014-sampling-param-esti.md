---
title: "[Xác Suất] Mẫu thống kê và ước lượng tham số"
slug: sampling-parameters-estimation
date: 2017-10-14
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
---
Trong các phần trước ta đã tìm hiểu cơ bản về xác suất và thống kê xác suất cũng như một số mô hình thống kê thông dụng, dựa vào đó ta tiếp tục lấn sang 1 phần quan trọng là thống kê và ước lượng các tham số cho các bài toán thực tế.
<!--more-->

<!--toc-->

# 1. Mẫu thống kê
Trong thực tế khi muốn thống kê để tìm quan hệ giữa các yếu tố ngẫu nhiên ta thường xuyên phải làm việc với các tập dữ liệu rất lớn tới mức không đủ thời gian và chi phí để làm việc. Vậy nên việc chọn lấy 1 tập mẫu nhỏ trong đó để mô phỏng là rất cần thiết. Quá trình lấy mẫu này đòi hỏi nhiều kĩ thuật sao cho mẫu lấy ra có thể đại diện được cho toàn bộ tập dữ liệu. Tuy nhiên, bài viết này sẽ không tập trung vào quá trình lấy mẫu đó mà sẽ tập trung vào việc tìm các đặc tính của tập mẫu đó.

## 1.1. Mẫu ngẫu nhiên
Mẫu ngẫu nhiên là tập các mẫu độc lập và có cùng một thống kê xác suất (*I.I.D - Independent, Identically Distributed*). Ví dụ ta cần thống kê mức độ xinh gái ảnh hưởng thế nào tới trí thông minh của chị em. Thì ta có thể coi độ xinh gái là một biến ngẫu nhiên. Lúc này ta lấy mẫu $n$ người và mỗi người sẽ có độ xinh gái là $X_i$ tương ứng. Khi đó ta có thể coi rằng $X_i$ là độc lập đôi một với nhau và
chúng có cùng một phân phối xác suất. Tập các mẫu này là mẫu ngẫu nhiên $X=[X_1,X_2,...,X_n]$ kích thước $n$.

Như vậy nếu gọi $p_X(x)$ là hàm trọng lượng xác suất đồng thời nếu $X_i$ là rời rạc và $f_X(x)$ là hàm mật độ xác suất đồng thời nếu $X_i$ là liên tục thì ta sẽ có:
$$p_X(x)=\prod\_{i=i}^np\_{X_i}(x_i)$$
và
$$f_X(x)=\prod\_{i=i}^nf\_{X_i}(x_i)$$

## 1.2. Thống kê
Ta đã chọn ra được mẫu ngẫu nhiên rồi và giờ là lúc ta cần xem quan hệ của chúng ra sao. Phép lấy quan hệ như vậy được gọi là thống kê. Về mặt hình thức, ta có thể định nghĩa một hàm $Y=g(X)$ bất kì là một thống kê phụ thuộc vào mẫu ngẫu nhiên $X$.

Ví dụ: $\displaystyle\overline X=g(X)=\frac{1}{n}\sum\_{i=1}^nX_i$ có thể coi là một thống kê. Thống kê này có tên là trung bình mẫu.

## 1.3. Đặc trưng mẫu
Ở đây ta sẽ xét một số thống kê cơ bản cho mẫu ngẫu nhiên và gọi chúng là các đặc trưng mẫu. Giả sử ta có mẫu ngẫu nhiên $X=[X_1,X_2,...,X_n]$ kích thước $n$ tuân theo một phân phối có kỳ vọng là $\mu$ và phương sai là $\sigma^2$.

### 1.3.1. Trung bình mẫu
Trung bình mẫu (*Mean*) hay còn gọi là kỳ vọng mẫu (*Expectation*) của một mẫu ngẫu nhiên là giá trị trung bình của mẫu đó:
$$\overline X=\frac{1}{n}\sum\_{i=1}^nX_i$$

Rõ ràng $\overline X$ cũng sẽ là một biến ngẫu nhiên và ta có thể tính được các đặc trưng của biến ngẫu nhiên này như:

| Đặc trưng | Giá trị |
|---|---|
| Kỳ vọng - $E[\overline X]$ | $\mu$ |
| Phương sai - $Var(\overline X)$ | $\dfrac{\sigma^2}{n}$ |

Chứng minh:
$$
\begin{aligned}
E[\overline X] &= E\bigg[\frac{1}{n}\sum\_{i=1}^nX_i\bigg]
\\cr\ &= \frac{1}{n}E\bigg\[\sum\_{i=1}^nX_i\bigg\]
\\cr\ &= \frac{1}{n}\sum\_{i=1}^nE[X_i]
\\cr\ &= \frac{1}{n}\sum\_{i=1}^n\mu
\\cr\ &= \mu
\end{aligned}
$$

$$
\begin{aligned}
Var[\overline X] &= Var\bigg[\frac{1}{n}\sum\_{i=1}^nX_i\bigg]
\\cr\ &= \frac{1}{n^2}Var\bigg\[\sum\_{i=1}^nX_i\bigg\]
\\cr\ &= \frac{1}{n^2}\sum\_{i=1}^nVar[X_i]
\\cr\ &= \frac{1}{n^2}\sum\_{i=1}^n\sigma^2
\\cr\ &= \frac{\sigma^2}{n}
\end{aligned}
$$

Như vậy là ta có thể thấy rằng giá trị kỳ vọng của biến ngẫu nhiên trung bình luôn là hằng số và bằng kỳ vọng của mẫu ngẫu nhiên. Tức là nếu ta lấy mẫu ngẫu nhiên từ 1 tập mẫu ra thì các tập mẫu ngẫu nhiên này luôn có cùng giá trị trung bình. Nói cách khác trung bình mẫu là không lệch (*unbiased*).

### 1.3.2. Phương sai mẫu
Phương sai mẫu $S^2$ là giá trị trung bình của phương sai của mẫu ngẫu nhiên:
$$S^2=\frac{1}{n}\sum\_{i=1}^n(X_i-\overline X)^2$$

Kỳ vọng của biến ngẫu nhiên $S^2$ sẽ là: $E[S^2]=\dfrac{n-1}{n}\sigma^2$. Như vậy là nó không còn bằng với phương sai của $X$ nữa, nên người ta thương lấy một dạng phương sai khác sao cho kỳ vọng của nó là bằng $\sigma^2$. Khái niệm này gọi là phương sai hiệu chỉnh, kí hiệu là $s^2$:
$$s^2=\frac{1}{n-1}\sum\_{i=1}^n(X_i-\overline X)^2$$

Chú ý rằng trong nhiều tài liệu người ta coi luôn phương sai hiệu chỉnh là phương sai mẫu.

Giá trị kỳ vọng của biến ngẫu nhiên phương sai hiệu chỉnh luôn là hằng số và bằng phương sai của mẫu ngẫu nhiên. Tức là nếu ta lấy mẫu ngẫu nhiên từ 1 tập mẫu ra thì các tập mẫu ngẫu nhiên này luôn có cùng giá trị kỳ vọng của phương sai. Nói cách khác phương sai hiệu chỉnh mẫu là không lệch (*unbiased*).

# 2. Ước lượng tham số
Là quá trình đi tìm tham số để mô tả quan hệ của các biến ngẫu nhiên. Trong phần [hợp nhiều biến ngẫu nhiên](/vi/2017/10/prob-rand-mulvar/) ta đã nói về khái niệm tương quan của các biến ngẫu nhiên và hệ số tương quan của chúng. Khi đó ta cũng đã nói qua về mô hình hồi quy (hay sự phụ thuộc tuyến tính) giữa 2 biến ngẫu nhiên $X,Y$: $Y=a+bX$. Tuy nhiên đó chỉ là một ví dụ đơn giản về việc tìm tham số $a,b$. Trong thực tế ta thường phải tìm tham số cho các mô hình xác suất phức tạp hơn nhiều như mô hình phân phối chuẩn chẳng hạn.

Quá trình ước lượng tham số này cũng chính là ý tưởng bên dưới của các bài toán học máy và nó được gọi là quá trình huấn luyện. Một bài toán học máy có chung 2 giai đoạn:

* ① Mô hình hoá tập mẫu (dữ liệu huấn luyện) bằng một mô hình xác suất với các tham số tương ứng
* ② Tìm các tham số đó bằng tập mẫu đã có. Hay còn gọi là học các tham số đó bằng dữ liệu huấn luyện.

Trong phần này ta sẽ coi tập mẫu là mẫu ngẫu nhiên và ta tìm hiểu 2 phương pháp tìm tham số chính là MLE và MAP.

## 2.1. Tham số
Tham số là các giá trị quyết định sự phụ thuộc xác suất của các biến ngẫu nhiên trong mô hình thống kê tương ứng. Các tham số này được kí hiệu là $\theta$ và nó là một véc-to có số chiều bằng với số lượng tham số thành phần. Ví dụ:

| Mô hình | Tham số |
|---|---|
| Phân phối đều - $X \sim \mathcal{Unif}(a, b)$ | $\theta=[a,b]$ |
| Phân phối Béc-nu-li - $X \sim \mathcal{Bern}(p)$ | $\theta=b$ |
| Phân phối nhị thức - $X \sim \mathcal{Bin}(n,p)$ | $\theta=[n,p]$ |
| Phân phối Poa-xông - $X \sim \mathcal{Poi}(\lambda)$ | $\theta=\lambda$ |
| Phân phối hình học - $X \sim \mathcal{Geo}(p)$ | $\theta=p$ |
| Phân phối nhị thức âm - $X \sim \mathcal{NegBin}(r,p)$ | $\theta=[r,p]$ |
| Phân phối chuẩn - $X \sim \mathcal{N}(\mu, \sigma^2)$ | $\theta=[\mu,\sigma^2]$ |
| Phân phối mũ - $X \sim \mathcal{Exp}(\beta)$ | $\theta=\beta$ |

Có nhiều phương pháp để ước lượng các tham số này từ tập mẫu ta có nhưng được đề cập nhiều nhất là 2 phương pháp:

* MLE (Maximum Likelihood Estimation): Cực đại ước lượng hợp lý
* MAP (Maximum A Posteriori): Cực đại xác suất hậu nghiệm

Về cái nào hơn cái nào thì không có đánh giá chính thức nên chỉ có cách là áp dụng và tự đánh giá.

## 2.2. MLE
### 2.2.1. Khái niệm
Ý tưởng của MLE là chọn tham số $\theta$ sao cho đầu ra của mô hình gần nhất với tập mẫu quan sát được. Ví dụ ta cần tìm tham số cho mô hình thống kê của bài toán xinh gái ảnh hưởng thế nào tới thông minh. Thì ta sẽ tìm tham số $\theta$ sao cho các biến các đầu vào là *"xinh gái"* - $X$ có kết quả gần với đầu ra *"thông minh"* - $Y$ nhất có thể.

Vì các mẫu quan sát được hay nói cách khác là đã xảy ra rồi nên chúng có xác suất là 1, giờ nếu ta muốn đầu ra của ta gần với chúng nhất thì xác suất của đầu ra của ta phải gần với 1 nhất. Hay nói cách khác ta phải tìm tham số sao cho xác suất đầu ra của mô hình là lớn nhất có thể.

Để mô tả xác suất đầu ra ta sử dụng một *hàm hợp lý* (*Likelihood function*) như sau:
$$L(\theta)=\prod\_{i=1}^nf(X_i|\theta)$$

Bạn đang nhìn thấy nó giống với xác suất đồng thời? Yes, chính nó đấy! Tuy nhiên ta phải phân biệt ra một chút để hiểu cho đúng về *hàm hợp lý*:

* $X$ là rời rạc: *hàm hợp lý* là hàm trọng lượng xác suất (*PMF*)
* $X$ là liên tục: *hàm hợp lý* là hàm mật độ xác suất (*PDF*)

Ta biểu diễn $f(X|\theta)$ với ý nghĩa rằng ta đầu ra của ta sẽ phụ thuộc vào tham số mô hình, mỗi tham số khác nhau sẽ cho đầu ra là khác nhau. Ngoài ra, ta cần lấy xác suất đồng thời bởi ta cần phải lấy mức độ giống nhau tổng thể của toàn bộ tập mẫu.

Vấn đề của ta bây giờ là làm sao có thể tìm được tham số $\theta$ sao cho xác suất đầu ra là lớn nhất có thể, tức:
$$\hat\theta=\underset{\theta}{\mathrm{argmax}}L(\theta)$$

> $\underset{\theta}{\mathrm{argmax}}$ là hàm trả ra giá trị của tham số $\theta$ mà tại đó khiến hàm đạt được giá trị lớn nhất.

Tuy nhiên do các $f(X_i|\theta)$ là nhỏ (có thể là bé hơn 1) nên với tập mẫu lớn $L(\theta)$ rất có thể sẽ rất nhỏ và khó khăn để xử lý sai số. Hơn nữa việc tối ưu tích là khó khăn hơn so với tối ưu tổng nên nếu ta có thể biến đổi tương đương thành tổng thì quá nhẹ nhàng. May mắn là nếu ta lấy $\log$ của nó thì tham số vẫn không thay đổi mà phép nhân của ta có thể biến thành phép cộng, nên trong thực tế ta sẽ sử dụng phiên bản $log$ của *hàm hợp lý* (*Log Likelihood function*):
$$LL(\theta)=\log L(\theta)=\log\prod\_{i=1}^nf(X_i|\theta)=\sum\_{i=1}^n\log f(X_i|\theta)$$

Và ta sẽ tìm $\theta$ để tối ưu hoá hàm này:
$$\hat\theta=\underset{\theta}{\mathrm{argmax}}LL(\theta)$$

Để tối ưu hoá hàm này ta có thể sử dụng nhiều phương pháp khác nhau, một trong các phương pháp phổ biến là sử dụng đạo hàm bậc nhất kết hợp chạy chương trình trên máy tính.

### 2.2.2. Ví dụ
Ví dụ 1: Giả sử ta có tập dữ liệu $X=[X_1,X_2,...,X_n]$ tuân theo luật phân phối Bec-nu-li $X \sim \mathcal{Bern}(p)$ với tham số $p$. Giờ ta sẽ sử dụng phương pháp MLE để tìm tham số $p$.

Hàm hợp lý của ta lúc này sẽ có dạng:
$$L(\theta)=\prod\_{i=1}^nf(X_i|\theta)=\prod\_{i=1}^np^{X_i}(1-p)^{1-X_i}$$

Phiên bản $\log$:
$$
\begin{aligned}
LL(\theta)&=\sum\_{i=1}^n\log\Big(p^{X_i}(1-p)^{1-X_i}\Big)
\\cr\ &=\sum\_{i=1}^n\log\Big(p^{X_i}\Big)+\log\Big((1-p)^{1-X_i}\Big)
\\cr\ &=\sum\_{i=1}^nX_i\log(p)+(1-X_i)\log(1-p)
\end{aligned}
$$

Đặt $Y=\sum\_{i=1}^nX_i$, ta có:
$$LL(\theta)=Y\log(p)+(n-Y)\log(1-p)$$

Giờ ta cần chọn $\hat p$ sao cho hàm trên đạt giá trị lớn nhất:
$$\hat p=\underset{p}{\mathrm{argmax}}\Big(Y\log(p)+(n-Y)\log(1-p)\Big)$$

Như ta đã biết hàm này đạt cực trị tại điểm có đạo hàm bằng 0, tức là:
$$
\begin{aligned}
\ &LL(p)^{\prime}=0
\\cr \iff & Y\frac{1}{p}+(n-Y)\frac{-1}{1-p} = 0
\\cr \iff & p=\frac{Y}{n}
\end{aligned}
$$

Từ đây ta sẽ có điểm $\hat p=\dfrac{\sum\_{i=1}^nX_i}{n}$ là giá trị ước lượng cần tìm.

## 2.3. MAP
### 2.3.1. Khái niệm
Ý tưởng của MAP là chọn tham số $\theta$ sao chúng gần với tham số thực của dữ liệu nhất có thể. Như vậy không giống như việc khớp dữ liệu quan sát được của MLE thì MAP lại đi khớp với tham số thực của tập dữ liệu quan sát được rồi.

Do có mẫu quan sát được rồi nên xác suất của chúng và xác suất của các tham số thực tương ứng là đã được xác định và bằng 1. Nên, giờ vấn đề của là làm sao để cho xác suất các tham số ước lượng khi đã biết mẫu quan sát được là gần với 1 nhất có thể. Hay nói cách khác xác suất của tham số ước lượng khi biết xác suất của mẫu quan sát và tham số thực phải lớn nhất có thể.

Tương tự như MLE, ta cũng sẽ biểu diễn xác suất này như sau:
$$P(\theta)=f(\theta|X)$$

> $X$ ở đây là vec-to $X=[X_1,...,X_n]^{\intercal}$

Giờ ta sử dụng [thuyết Bayes](/vi/2017/10/what-is-prob/#2-4-xác-suất-hậu-nghiệm-bayes) để biến đổi công thức trên một chút:
$$
\begin{aligned}
P(\theta)&=f(\theta|X)
\\cr\ &= \dfrac{f(X|\theta)g(\theta)}{h(X)}
\\cr\ &= \dfrac{g(\theta)\prod\_{i=1}^nf(X_i|\theta)}{h(X)}
\end{aligned}
$$

> $g, h$ ở đây cũng mang ý nghĩa tương tự như $f$. Tức, chúng là PMF nếu biến là rời rạc và PDF nếu biến là liên tục.

Ta cũng sẽ tìm được tham số $\theta$ sao cho xác suất trên là lớn nhất, tức:
$$
\begin{aligned}
\hat\theta&=\underset{\theta}{\mathrm{argmax}}P(\theta)
\\cr\ &=\underset{\theta}{\mathrm{argmax}}\dfrac{g(\theta)\prod\_{i=1}^nf(X_i|\theta)}{h(X)}
\\cr\ &=\underset{\theta}{\mathrm{argmax}}\prod\_{i=1}^nf(X_i|\theta)g(\theta)
\end{aligned}
$$

Ở trên ta giản lược được $h(X)$ là do xác suất của mẫu quan sát được rồi là không đổi. Giờ ta lại lấy $\log$ tương tự như MLE:
$$
\begin{aligned}
\hat\theta&=\underset{\theta}{\mathrm{argmax}}\prod\_{i=1}^nf(X_i|\theta)g(\theta)
\\cr\ &=\underset{\theta}{\mathrm{argmax}}\log\bigg(\prod\_{i=1}^nf(X_i|\theta)g(\theta)\bigg)
\\cr\ &=\underset{\theta}{\mathrm{argmax}}\bigg(\log g(\theta) + \sum\_{i=1}^n\log f(X_i|\theta)\bigg)
\end{aligned}
$$

Từ công thức trên ta thấy rằng MAP chỉ khác MLE ở chỗ thêm $\log g(\theta)$ hay còn gọi là xác suất tiền nghiệm vào hàm mục tiêu. Nói vậy thôi nhưng vấn đề lại phát sinh rồi! Ta hiện giờ đã biết được mô hình phân phối của tập mẫu $f(X)$ nhưng lại chưa biết mô hình phân phối của tham số $g(\theta)$ nên việc tính toán có vẻ bất khả thi.

### 2.3.2. Siêu tham số
Tiếp tục với vấn đề chọn mô hình phân phối nào cho các tham số $\theta$. Trong thực tế người ta chọn mô hình của tham số $\theta$ sao cho cùng dạng với mô hình của tham số $\theta$ có điều kiện $X$. Hiểu theo nghĩa của Bayes là mô hình thống kê xác suất tiền nghiệm và hậu nghiệm là cùng họ với nhau. Mô hình thống kê kiểu này được gọi là **xác suất tiền nghiệm liên hợp** (<a href="https://en.wikipedia.org/wiki/Conjugate_prior" target="_blank"_ rel="noopener noreferrer">*conjugate prior*</a>) của hàm khả năng (*likelihood function*).

Ví dụ, nếu mẫu của ta tuân theo phân phối Béc-nu-li $X \sim \mathcal{Bern}(p)$ với tham số $\theta=p$ thì phân phối xác suất tiền nghiệm liên hợp của nó là phân phối Beta $\theta \sim \mathcal{Beta}(\alpha,\beta)$ bởi khi kết hợp với Beta thì xác suất hậu nghiệm của nó cũng sẽ là Beta. Ở đây tôi không đề cập sâu về dạng mô hình này nhưng bạn nên đọc thêm để hiểu về nó cũng nhưng các ứng dụng của nó.

Do các phân phối của tham số cũng được quy định bởi các tham số của phân phối tương ứng. Tức là các tham số $\theta$ cần tìm của ta giờ phải phụ thuộc vào cả các tham số của phân phối xác suất của nó. Để phân biệt người ta gọi các tham số này là **siêu tham số** (*hyperparameters*).

Khi làm việc các siêu tham số này được thiết lập *dựa vào cảm quan* của người giải quyết bài toán. Việc chọn được siêu tham số hợp lý là một việc vô cùng cần thiết để thu được tham số $\theta$ tốt. Chính vì vậy mà các bài toán học máy sau này, ta thường xuyên phải xem xét nhiều bộ siêu tham số để được kết quả mong đợi là thế.

Để thuận tiện khi làm việc, ta liệt kê một số xác suất tiền nghiệm liên hợp như dưới đây:

| Tham số | Liên hợp |
|---|---|
| Béc-nu-li - $X \sim \mathcal{Bern}(p)$ | Beta - $\theta \sim \mathcal{Beta}(\alpha,\beta)$ |
| Nhị thức - $X \sim \mathcal{Bin}(n,p)$ | Beta - $\theta \sim \mathcal{Beta}(\alpha,\beta)$ |
| Poa-xông - $X \sim \mathcal{Poi}(\lambda)$ | Gamma  - $\theta \sim \mathcal{Gama}(\alpha,\beta)$ |
| Phân phối hình học - $X \sim \mathcal{Geo}(p)$ | Beta - $\theta \sim \mathcal{Beta}(\alpha,\beta)$ |
| Phân phối nhị thức âm - $X \sim \mathcal{NegBin}(r,p)$ | Beta - $\theta \sim \mathcal{Beta}(\alpha,\beta)$ |
| Phân phối chuẩn - $X \sim \mathcal{N}(\mu,\\_)$ | Phân phối chuẩn - $\theta \sim \mathcal{N}(\mu_0,\sigma_0^2)$ |
| Phân phối chuẩn - $X \sim \mathcal{N}(\\_,\sigma^2)$ | Gamma đảo - $\theta \sim \mathcal{InvGama}(\alpha,\beta)$ |
| Phân phối mũ - $X \sim \mathcal{Exp}(\beta)$ | Gamma - $\theta \sim \mathcal{Gama}(\alpha,\beta)$ |

Tới đây thì ta có thể sử dụng các phương pháp tối ưu hàm mục tiêu hệt như với MLE chỉ khác là ta thêm các siêu tham số vào khi tính toán. Các siêu tham số này sẽ được thiết lập từ trước dựa vào cảm quan của người quan sát.

### 2.3.3. Ví dụ
Ta xét lại ví dụ tìm $p$ của $X \sim \mathcal{Bern}(p)$ ở trên bằng phương pháp MAP. Vì đây là phân phối Bec-nu-li nên ta chọn phân phối Beta làm phân phối xác suất tiền nghiệm liên hợp $\theta \sim \mathcal{Beta}(\alpha,\beta)$ cho tham số $\theta=p$.

Như vậy ước lượng $\hat p$ cần tìm là:
$$
\begin{aligned}
\hat p&=\underset{\theta}{\mathrm{argmax}}\bigg(\log Beta(p)+\sum\_{i=1}^n\log Bern(X_i|p)\bigg)
\\cr\ &=\underset{\theta}{\mathrm{argmax}}\bigg(\log\Big(\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}p^{\alpha-1}(1-p)^{\beta-1}\Big)+Y\log(p)+(n-Y)\log(1-p)\bigg)
\end{aligned}
$$

Bỏ đi những thành phần hằng số (không phụ thuộc vào $p$) ta sẽ có:
$$
\begin{aligned}
\hat p&=\underset{\theta}{\mathrm{argmax}}\bigg(\log\Big(p^{\alpha-1}(1-p)^{\beta-1}\Big)+Y\log(p)+(n-Y)\log(1-p)\bigg)
\\cr\ &=\underset{\theta}{\mathrm{argmax}}\bigg((\alpha-1)log(p)+(\beta-1)\log(1-p)+ Y\log(p)+(n-Y)\log(1-p)\bigg)
\\cr\ &=\underset{\theta}{\mathrm{argmax}}\bigg((\alpha-1+Y)log(p)+(\beta-1+n-Y)\log(1-p)\bigg)
\end{aligned}
$$

Giải bằng cách lấy đạo hàm tương tự như trên ta sẽ được:
$$\hat p=\frac{\alpha-1+\sum\_{i=1}^nX_i}{n+\alpha+\beta-2}$$

Các siêu tham số $\alpha,\beta$ lúc này sẽ được chọn từ trước. Tuỳ vào giá trị của siêu tham số mà $\hat p$ thể hiện khác nhau dẫn tới kết quả của mô hình là khác nhau. Việc chọn $\alpha,\beta$ thế nào ta sẽ cùng xem xét sau trong các bài về học máy.

# 3. Kết luận
Chọn mẫu là một quá trình rất quan trọng để tìm ra quan hệ giữa các sự kiện và tính chất của dữ liệu. Trong thực tế ta thường chỉ làm việc với các mẫu ngẫu nhiên tức là các mẫu độc lập đôi một và cùng phân phối (*I.I.D*) rồi đi tìm tham số của các mô hình thống kê với mẫu ngẫu nhiên.

Việc tìm tham số hay còn gọi là quá trình học tham số là ý tưởng chính của các bài toán học máy nhằm tìm được mối tương quan giữa các đầu vào và đầu ra dựa trên tập dữ liệu huấn luyện. Có 2 phương pháp chính để tìm tham số là **MLE** (Maximum Likelihood Estimation) và **MAP** (Maximum A Posteriori). Ý tưởng của MLE là tìm tham số sao cho đầu ra của mô hình là khớp với tập dữ liệu quan sát được nhất có thể, còn của MAP là tìm tham số sao cho gần với tham số thực tế của tập dữ liệu nhất có thể.

Cả 2 phương pháp này đều lấy hàm mục tiêu phiên bản $\log$ (*Log Likehood function*) để cực đại hoá. Việc tìm tham số để tối ưu hàm này có thể thực hiện bằng các phương pháp của giải thích như đạo hàm cấp 1 kết hợp với sức mạnh tính toán của máy tính để giải quyết.

Từ các tham số và mô hình đó, ta có thể khai phá và dự đoán được các sự kiện trong tương lai. Nghe vẫn hơi mông lung phải không? Không sao cả, bài kế tiếp ta sẽ cùng bàn về cách áp dụng các kiến thức xác suất cho bài toán học máy ra sao.
