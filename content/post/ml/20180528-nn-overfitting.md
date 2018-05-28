---
title: "[NN] Mạng quá khớp - Overfitting"
slug: nn-overfitting
date: 2018-05-28T10:20:14+09:00
categories:
- Học Máy
- ML
tags:
- Học Máy
- NN
keywords:
- Học Máy
- Machine Learning
- Neural Networks
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/dl/logo.png
metaAlignment: center
---
Cũng như các bài toán ML khác, mạng NN hoàn toàn có thể bị quá khớp nếu kích cỡ lớn quá mức cần thiết. Nên khi cài đặt mạng NN, người ta thường cài thêm các phương pháp như *chính quy hoá*, *bỏ nút mạng*... nhằm giảm được vấn đề này.
<!--more-->

Như tôi đã viết ở bài [[ML] Mô hình quá khớp (Overfitting)](/vi/2017/12/ml-overfitting/) thì vấn đề quá khớp là mô hình của ta đưa ra kết quả rất ngon cho tập dữ liệu huấn luyện, nhưng khi đem thử nghiệm thực tế thì lại cho kết quả không mấy khả quan. Nguyên nhân là do mô hình quá phức tạp dẫn tới nó khớp được với nhiều dữ liệu huấn luyện nhưng lại không đủ tổng quát để khớp với các dữ liệu thực tế.

Dựa vào bài viết đó, tôi sẽ cài đặt kĩ thuật [**chính quy hoá**](/vi/2017/12/ml-overfitting/#4-kĩ-thuật-chính-quy-hoá) (*Regularization*) cho mạng NN. Ngoài ra, sẽ đưa ra thêm 1 phương pháp phổ biến nữa là **[bỏ nút mạng](https://en.wikipedia.org/wiki/Dropout_(neural_networks))** (*Dropout*). Nếu bạn cần tìm hiểu thêm lý thuyết cũng như các phương pháp phát hiện hiện tượng này thì có thể đọc [bài viết đó](/vi/2017/12/ml-overfitting/) để có cái nhìn chi tiết hơn. Còn ở đây, tôi chủ yếu tập trung vào việc cài đặt mạng NN mà thôi.

<!--toc-->

# 1. Regularization
Kĩ thuật chính quy hoá được thực hiện bằng cách thêm phần tử chính quy hoá vào hàm lỗi nhằm suy giảm độ lớn của các trọng số sau khi tối ưu:

$$J(\mathbb W) = J_0(\mathbb W) + \lambda\frac{1}{p}\sum\_{i=1}^n\lvert w_i\rvert^p$$

Trong đó, $J_0(\mathbb W)$ là hàm lỗi ban đầu của ta, $\lambda$ là hệ số chính quy hoá, $p$ là cấp của norm và $w_i$ là trọng số thứ $i$ của mô hình. Thông thường người ta hay lấy $p=2$ (**L2**) hoặc $p=1$ (**L1**) để thực hiện kĩ thuật này.

Bài viết này, tôi sẽ cài đặt **L2** cho mạng NN. Việc cài đặt mạng **L1** cũng hoàn toàn tương tự như vậy không khó khăn gì cả. Với $p=2$, ta có thể viết lại công thức cho hàm lỗi của mạng NN như sau:

$$
J(\mathbb{W}) = -\frac{1}{m}\sum\_{i=1}^m\sum\_{k=1}^K\Bigg(y_k^{(i)}\log\Big(\sigma_k^{(i)}\Big)+\Big(1-y_k^{(i)}\Big)\log\Big(1-\sigma_k^{(i)}\Big)\Bigg) + \frac{\lambda}{2m}\sum\_{j=1}^nw_j^2
$$

$w_j$ ở đây là trọng số thứ $j$ của mạng và nó **{{<hl-text danger>}}không bao gồm các bias{{</hl-text>}}** của mạng. Ngoài ra, ta chia cho $m$ để lấy trung bình cho toàn bộ mẫu tương tự như ý nghĩa của hàm lỗi nguyên gốc.

Nếu, ta sử dụng phép véc-tơ hoá để mô phỏng mạng có $L$ tầng có ma trận trọng lượng tương ứng $\mathbf W_l$ thì ta có thể viết lại như sau:
$$
J(\mathbb{W}) = -\frac{1}{m}\sum\_{i=1}^m\sum\_{k=1}^K\Bigg(y_k^{(i)}\log\Big(\sigma_k^{(i)}\Big)+\Big(1-y_k^{(i)}\Big)\log\Big(1-\sigma_k^{(i)}\Big)\Bigg) + \frac{\lambda}{2m}\sum\_{l=1}^L\sum_j\mathbf W_l[:,1:]^{\intercal}\mathbf W_l[:,1:]
$$

Khi đó, đạo hàm của hàm lỗi sẽ có dạng:
$$
\frac{\partial J}{\partial w_i} = \frac{\partial J_0}{\partial w_i} + \frac{\lambda}{m}w_i
$$

Trong đó, $\dfrac{\partial J_0}{\partial w_i}$ là đạo hàm của hàm lỗi không có cụm chính quy hoá $J_0(\mathbb W)$ tính được bằng [phương pháp lan truyền ngược](/vi/2018/04/nn-implement/#2-5-lan-truy%E1%BB%81n-ng%C6%B0%E1%BB%A3c) như đã biết. Việc chứng minh công thức trên hoàn toàn không khó, hi vọng là nhìn cái bạn có thể luận được luôn nên tôi không viết ra đây nữa.

Bằng lập luận như vậy, ta viết lại được mã tính hàm lỗi như sau:

{{<codeblock "nn-overfitting.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn-overfitting.py">}}
class NN():
    def cost(self, data, lamda):
        """
        Return cross-entropy cost of NN on test data
        """
        m = len(data)
        j = 0
        for x, y in data:
            _, a = self.feedforward(x)
            a_L = a[-1]
            j -= np.sum(np.nan_to_num(y*np.log(a_L) + (1-y)*np.log(1-a_L)))
        # regularization term
        j += 0.5 * lamda * sum(np.linalg.norm(W[:,1:])**2 for W in self.w)
        return j / m
{{</codeblock>}}

Việc tính đạo hàm cũng được viết lại thành:
{{<codeblock "nn-overfitting.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn-overfitting.py">}}
class NN():
    def train(self, train_data, epochs, mini_batch_size, eta, lamda=0.0):
        """
        Train NN with train data ``[(x, y)]``.
        This use mini-batch SGD method to train the NN.
        """
        # number of training data        
        m = len(train_data)
        # cost
        cost = []
        for j in range(epochs):
            start_time = time.time()
            # shuffle data before run
            random.shuffle(train_data)
            # divide data into mini batchs
            for k in range(0, m, mini_batch_size):
                mini_batch = train_data[k:k+mini_batch_size]
                m_batch = len(mini_batch)
                # calc gradient
                w_grad = [np.zeros(W.shape) for W in self.w]
                for x, y in mini_batch:
                    grad = self.backprop(x, y)
                    w_grad = [W_grad + g for W_grad, g in zip(w_grad, grad)]
                w_grad = [W_grad / m_batch for W_grad in w_grad]

                # add regularization term
                w_grad = [W_grad + (lamda/m_batch * np.insert(W[:,1:],0,0,axis=1))
                            for W, W_grad in zip(self.w, w_grad)]
                
                # check grad for first mini_batch in first epoch
                if j == 0  and k == 0 and not self.check_grad(mini_batch, w_grad):
                    print('backprop fail!')
                    return False
                
                # update w
                self.w = [W - eta * W_grad for W, W_grad in zip(self.w, w_grad)]
            
            # calc cost
            cost.append(self.cost(train_data))
            
        return cost
{{</codeblock>}}

Nếu chạy thử với mạng 1 tầng ẩn 100 nút và $\lambda=4$ thì ta có thể thu được [kết quả](https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/network-overfitting.ipynb#3.-Test) chính xác tới **96.72%**, tăng được *0.1%* so với $\lambda=0$ tức là không thực hiện việc chính quy hoá.

# 2. Dropout
Một kĩ thuật nữa rất hay được sử dụng là **[bỏ nút mạng](http://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf)** (*dropout*) rất đơn giản và cho kết quả rất khả quan. Ý tưởng của phương pháp này là trong quá trình huấn luyện ta bỏ đi ngẫu nhiêu một vài nút mạng ở tầng ẩn (thường lên tới 50% số nút mạng mỗi tầng ẩn) nhằm giảm độ phức tạp của mạng.

Ta có thể coi mạng sau khi bỏ đi các nút đó là một mạng mới tinh gọn hơn mạng gốc. Như vậy, Với mỗi các lô dữ liệu huấn luyện khác nhau mà ta thực hiện với các mạng tinh giản khác nhau thì kết quả ta thu được sẽ là một mạng trung bình của các mạng tinh gọn đó. Bằng việc lấy mạng trung bình đó, thì ta có thể hi vọng rằng mạng của ta có thể tổng quát được nhiều trường hợp hơn hay nói cách khác là bớt được vấn đề quá khớp.

Với ý tưởng như vậy, ta có thể cài đặt mạng theo quy trình sau:

* 1. Phân lô dữ liệu
* 2. Xử lý mỗi lô với mạng tinh giản
  * 2.1. Bỏ đi ngẫu nhiên một số nút mạng ẩn
  * 2.2. Học với mạng sau khi bỏ nút
  * 2.3. Hồi phục lại các nút bị bỏ đi

Cài đặt cụ thể như sau:
{{<codeblock "nn-overfitting.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn-overfitting.py">}}
class NN():
    def train(self, train_data, epochs, mini_batch_size, eta, lamda=0.0):
        """
        Train NN with train data ``[(x, y)]``.
        This use mini-batch SGD method to train the NN.
        """
        # number of training data        
        m = len(train_data)
        # cost
        cost = []
        for j in range(epochs):
            start_time = time.time()
            # shuffle data before run
            random.shuffle(train_data)
            # divide data into mini batchs
            for k in range(0, m, mini_batch_size):
                mini_batch = train_data[k:k+mini_batch_size]
                m_batch = len(mini_batch)
                # calc gradient
                w_grad = [np.zeros(W.shape) for W in self.w]
                for x, y in mini_batch:
                    grad = self.backprop(x, y)
                    w_grad = [W_grad + g for W_grad, g in zip(w_grad, grad)]
                w_grad = [W_grad / m_batch for W_grad in w_grad]

                # add regularization term
                w_grad = [W_grad + (lamda/m_batch * np.insert(W[:,1:],0,0,axis=1))
                            for W, W_grad in zip(self.w, w_grad)]
                
                # check grad for first mini_batch in first epoch
                if j == 0  and k == 0 and not self.check_grad(mini_batch, w_grad):
                    print('backprop fail!')
                    return False
                
                # update w
                self.w = [W - eta * W_grad for W, W_grad in zip(self.w, w_grad)]
            
            # calc cost
            cost.append(self.cost(train_data))
            
        return cost
{{</codeblock>}}

# 3. Kết luận
Bài này đã đưa ra 2 phương pháp làm giảm độ phức tạp của mạng NN nhằm nâng cao tính tổng quát hoá của mạng là kĩ thuật chính quy hoá - *regularization* và bỏ nút mạng - *dropout*. Trong thực tế, người ta thường kết hợp cả 2 phương pháp này với nhau vì việc cài đặt không quá phức tạp mà cho hiệu quả rất tốt. Mã nguồn của phần này, tôi cũng cài đặt theo phương pháp kết hợp cả 2, nếu bạn hứng thú thì có thể đọc [tại đây](https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn-overfitting.py) nhé.
