---
title: "[NN] Cài đặt mạng NN"
slug: nn-implement
date: 2018-04-26T10:20:14+09:00
categories:
- Học Máy
- ML
tags:
- Học Máy
- NN
keywords:
- Học Máy
- Machine Learning
- backpropagation
- lan truyền ngược
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/dl/logo.png
metaAlignment: center
---
Bài viết này sẽ tập trung vào việc cài đặt mạng NN để nhận dạng số và đưa ra một số mẹo để thu được kết quả tốt khi làm việc với mạng NN. Nếu bạn chưa có cái nhìn tổng quan về mặt lý thuyết của mạng NN thì tôi nghĩ rằng bạn nên đọc [bài viết trước](/vi/2018/04/nn-intro/) của tôi để có thể dễ dàng hiểu bài này hơn.
<!--more-->
<!--toc-->

# 1. Giới thiệu
## 1.1. Nhận dạng số
Nhận dạng số viết tay dường như là một bài toán khó nếu áp dụng các phương pháp lập trình logic thông dụng. Tuy nhiên, bằng mạng NN ta có thể thực hiện việc này với tỉ lệ chính xác rất cao. Thông thường một bài toán nhận dạng quang học gồm có 1 số bước chính:

* 1. Nâng cao chất lượng ảnh
* 2. Phân tách các kí tự
* 3. Nhận dạng các kí tự

Các kĩ thuật xử lý ảnh như nhị phân hoá bức ảnh hiện nay giúp ta thu được ảnh có độ tương phản cao giữa nên và chữ giúp cho việc bóc tách chữ dễ dàng hơn. Để có thể nhận dạng được, thì việc cần thiết là phải bóc tách từng kí tự ra một, điều may mắn là các kí tự gần như có khung gần tương tự nhau, giúp ta có thể biết được biên giữa các kí tự. Sau khi bóc tầng kí tự ra rồi thì ta tiến hành bước nhận dạng từng kí tự đơn đó rồi ghép lại với nhau thành văn bản đầy đủ. Về cơ bản là vậy, tuy nhiên trong phần này tôi chỉ chú trọng tới bước thứ 3 là nhận dạng kí tự đơn lẻ, cụ thể là nhận dạng số từ $0$ tới $9$ bằng mạng NN.

Cũng như các bài toán học máy khác thì yêu cầu đầu tiên là phải có tập dữ liệu. Thật may mắn là ta có sẵn tập dữ liệu [MNIST](http://yann.lecun.com/exdb/mnist/) chứa 70,000 ảnh số viết tay kích thước 28x28 pixels đi kèm với nhãn từ $0$ tới $9$.

{{< image classes="fancybox center" thumbnail-width="60%" src="https://res.cloudinary.com/dominhhai/image/upload/ml/mnist.png" title="MNIST Database Sample" >}}

Trong đó có 60,000 dữ liệu huấn luyện và 10,000 dữ liệu kiểm tra. Dữ liệu chính thức được chia làm 4 file với đặt tả cụ thể. Tuy nhiên để tiện làm việc tôi lấy [file nén gộp](https://github.com/mnielsen/neural-networks-and-deep-learning/raw/master/data/mnist.pkl.gz) của chúng lại cùng 1 định dạng duy nhất. Trong file này, dữ liệu được tách ra làm 3 phần: (1) 50,000 dữ liệu huấn luyện - *training data*; (2) 10,000 dữ liệu kiểm định - *validation data*; (3) 10,000 dữ liệu kiểm tra - *test data*. Mỗi dữ liệu được tổ chức thành các cặp 2-tuple gồm 1 mảng 784 chiều chứ ảnh mẫu 28x28 pixels và nhãn tương ứng trong khoảng $0$ tới $9$.

## 1.2. Mô hình mạng
Đầu vào của mạng, ta có thể sử dụng mỗi điểm ảnh cho 1 đầu vào, hay nói cách khác đầu vào của ta gồm 784 nút mạng mỗi nút chứ giá trị của 1 điểm ảnh. Về mặt kĩ thuật, ta có thể coi đầu vào là 1 véc-tơ cột 784 chiều với mỗi phần từ chứa giá trị 1 điểm ảnh.

Còn đầu ra đại diện cho các số từ $0$ tới $9$. Về nguyên tắc ta có thể sử dụng 4 nút ra để mã hoá cho 10 nhãn đó bởi $4^2=16>10$, tuy nhiên nếu làm như vậy thì khó mà nhìn được xác suất dự đoán tương ứng vỡi mỗi nhãn là bao nhiêu. Nên trong bài toán này ta sử dụng 10 đầu ra tương ứng với 10 nhãn. Mỗi đầu ra sẽ nhận giá trị trong khoảng $[0, 1]$ tương ứng với xác suất dự đoán ở mỗi nhãn. Như vậy, trường hợp chắc chắn đúng thì vì trị tương ứng sẽ bằng 1 và các vị trí khác bằng 0. Về mặt thuật ngữ, nó chính là vec-to **[one-hot](https://en.wikipedia.org/wiki/One-hot)**. Ví dụ, nếu đầu ra là $5$ thì phần tử ở vị trí thứ 5 là 1 còn các vị trí khác là 0:

$$\begin{bmatrix}0&0&0&0&\textcolor{red}{1}&0&0&0&0\end{bmatrix}^{\intercal}$$

Trong bài toán này, ta sẽ sử dụng hàm *sigmoid* làm hàm kích hoạt cho các nút mạng và hàm lỗi tương ứng là cross-entropy như đã đề cập ở [bài viết trước](/vi/2018/04/nn-intro/). Dạng bài toán này, người ta còn hay sử dụng [hàm softmax](/vi/2018/04/softmax-derivs/) để làm hàm kích hoạt cho tầng ra của mạng do kết quả của hàm này tương tự như phép lấy xác suất. Việc cài đặt hàm này cũng tương tự như hàm *sigmoid*, tuy nhiên để đơn giản và phù hợp với mục đích của bài là nói về cách cài đặt mạng NN, tôi không cài đặt ở đây.

# 2. Phân tích và cài đặt
Với mô hình mạng và dữ liệu như trên ta bắt đầu tiến hành cài đặt mạng. Thay vì cố định kích cỡ mạng, tôi tạo ra 1 lớp mạng riêng để dễ dàng cấu hình kích thước gồm số tầng và số nút mỗi tầng.

Toàn bộ mã nguồn của phần này bạn có thể xem [tại đây](https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/network.ipynb). Tôi có viết toàn bộ bằng 1 file iPython cho dễ theo dõi, tuy nhiên bạn nếu muốn bạn có thể copy nội dung ra file python thông dụng để chạy mà không cần chỉnh sửa gì cả.

## 2.1. Dữ liệu
Như đã đề cập ở trên, để có thể dự đoán kết quả đầu vào của ta là một véc-tơ cột 784 chiều. Nên các dữ liệu đầu vào ta cũng phải để dạng này cho phù hợp. Đầu ra của mạng ở dạng vec-tơ cột one-hot 10 chiều nên các nhãn cũng cần biến đổi về dạng vec-tơ tương ứng này. Tuy nhiên, với tập dữ liệu kiểm tra, ta không cần biến đổi các nhãn thành vec-tơ one-hot này bởi kết quả dự đoán của mạng dù thế nào ta vẫn phải quy đổi sang nhãn tương ứng dạng không mã hoá.

{{<codeblock "data_loader.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/data_loader.py">}}
def load():
  # download data if not exist
  if not os.path.exists(DATA_FILE):
    download()
  
  # load data
  with gzip.open(DATA_FILE, 'rd') as file:
    tr_dt, v_dt, t_dt = cPickle.load(file)
  
  # training data
  inputs = [x.reshape((784, 1)) for x in tr_dt[0]]
  labels = [label_2_vec(y) for y in tr_dt[1]]
  training_data = zip(inputs, labels)
  
  # validation data
  inputs = [x.reshape((784, 1)) for x in v_dt[0]]
  validation_data = zip(inputs, v_dt[1])
  
  # test data
  inputs = [x.reshape((784, 1)) for x in t_dt[0]]
  test_data = zip(inputs, t_dt[1])
  
  return (training_data, validation_data, test_data)
{{</codeblock>}}

Hàm `load()` trên sẽ cho ta 3 tập dữ liệu riêng biệt gồm *tập huấn luyện*, *tập kiểm định* và *tập kiểm tra* tương ứng. Tập dữ liệu là 1 mảng các `2-tuples` chứa vec-tơ 784 chiều đầu vào $x\in\mathbb{R}^{784,1}$ và nhãn $y\in\mathbb{R}^{10,1}$ tương ứng dạng vec-to one-hot đầu ra. Còn 2 tập kiểm định và kiểm tra là các mảng `2-tuples` chứa vec-tơ 784 chiều đầu vào $x\in\mathbb{R}^{784,1}$ và nhãn $y\in\mathbb{N}$ tương ứng dạng số nguyên trong khoảng $[0,9]$.

## 2.2. Khởi tạo tham số
Với mạng NN, giá trị tham số khởi tạo ảnh hưởng trực tiếp tới việc mạng có chạy được hay không. Khác với các bài toán [học máy](/vi/categories/ml/) tôi đã đề cập thì ta **{{<hl-text danger>}}không thể khởi tạo tham số của mạng bằng $0$ được{{</hl-text>}}**. Bởi khi đó, đạo hàm của ta sẽ bị triệt tiêu dẫn tới tham số không thay đổi được nên mạng không thể học được. Việc chứng minh điều nay không hề khó nếu bạn xem lại [công thức tính đạo hàm](/vi/2018/04/nn-intro/#5-lan-truyền-ngược-và-đạo-hàm) trong mạng NN ở bài viết trước của tôi.

Cũng thật khó để quyết định xem nên chọn việc khởi tạo sao cho hợp lý, tuy nhiên về nguyên tắc thì tất cả các tham số không thể bằng $0$. Trong bài toán này để đơn giản tôi chọn cách khởi tạo tham số ngẫu nhiên:

{{<codeblock "nn.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn.py">}}
class NN():
    def __init__(self, layers):
        self.layers = layers
        self.L = len(layers)
        self.w = [np.random.randn(l2, l1 + 1)
                        for l2, l1 in zip(layers[1:], layers[:-1])]
{{</codeblock>}}

Để khởi tạo lớp mạng `NN`, ta cấu hình kích cỡ mạng bằng 1 mảng `layers` với số nút ở mỗi tầng tương ứng. Ví dụ, `layers = [784, 100, 200, 10]` thì ta có mạng gồm 4 tầng với tầng vào gồm 784 nút, tầng ra gồm 10 nút và 2 tầng ẩn có lần lượt là 100 và 200 nút mạng.

Trọng số `w` của mạng sẽ là 1 mảng có kích cỡ bằng số tầng, không kể tầng vào của mạng. Mỗi phần tử của mảng `w` chứ ma trận $\mathbf W$ trọng số tương ứng của mỗi tầng mạng (từ tầng 2 tới tầng ra). Mỗi hàng của ma trận $\mathbf W$ thể hiện cho nút mạng tương ứng ở tầng đó còn mỗi cột thể hiện cho trọng số của các đầu vào tầng trước đó.

Như quy ước ở bài trước, thì các giá trị độ lệch (*bias*) $b^{(l)}$ ta sẽ coi như trọng số $w_0^{(l)}$ tương ứng: $w_0^{(l)}=b^{(l)}$. Nên cột đầu của ma trận $\mathbf W$ sẽ đại diện cho các giá trị bias. Ví dụ, tầng 2 có 100 nút và tầng 3 có 200 nút thì ma trận $w[2]$ ở tầng 3 của ta có kích cỡ $[200\times 101]$.

## 2.3. Lan truyền tiến
Dựa vào công thức lan truyền tiến (*feedfoward*) ở bài trước:

$$
\begin{aligned}
\mathbf{z}^{(l+1)} &= \mathbf{W}^{(l+1)}\cdot\mathbf{a}^{(l)}
\\cr
\mathbf{a}^{(l+1)} &= f\big(\mathbf{z}^{(l+1)}\big)
\end{aligned}
$$

Ta có thể dễ dàng cài đặt hàm này như sau:

{{<codeblock "nn.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn.py">}}
class NN():
    def feedforward(self, x):
        z = []
        a = [self.add_bias(x)]
        for l in range(1, self.L):
            z_l = np.dot(self.w[l-1], a[l-1])
            a_l = self.sigmoid(z_l)
            if l < self.L - 1:
                a_l = self.add_bias(a_l)
            z.append(z_l)
            a.append(a_l) 
        return (z, a)

    def add_bias(self, a):
        """
        add a_0 = 1 as input for bias w_0
        """
        return np.insert(a, 0, 1, axis=0)

    def sigmoid(self, z):
        """
        Sigmoid function use as activation function
        """
        return 1.0 / (1.0 + np.exp(-z))
{{</codeblock>}}

Để tiện sử dụng về sau, ta lưu lại tất cả các giá trị $z, a$ trung gian trong quá trình tính toán. Như quy ước thì $a_0$ là gắn bằng đầu vào của mạng có kèm thêm đầu vào bias là $1$ nên mảng `a` sẽ có kích cỡ bằng số tầng mạng. Còn mảng `z` có kích thước đúng bằng mảng trọng số `w` thể hiện cho véc-tơ $\mathbf z$ ở mỗi tầng mạng.

Ngoài ra, tương tự như tầng vào, tại các tầng ẩn, ta gắn thêm đầu vào bias bằng $1$ để làm đầu vào cho tầng sau.

Dễ dàng ta thấy rằng phần tử cuối cùng của mảng `a` chính là vec-tơ đầu ra của mạng: `a[-1]`. Dựa vào đây, ta có thể biết được nhãn dự đoán được bằng cách lấy địa chỉ của phần tử có giá trị lớn nhất (tương ứng với xác suất lớn nhất):
{{<codeblock "nn.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn.py">}}
class NN():
    def predict(self, x):
        _, a = self.feedforward(x)
        return np.argmax(a[-1])
{{</codeblock>}}

## 2.4. Hàm lỗi
Với hàm lỗi cross-entropy:
$$
J(\mathbb{W}) = -\frac{1}{m}\sum\_{i=1}^m\sum\_{k=1}^K\Bigg(y_k^{(i)}\log\Big(\sigma_k^{(i)}\Big)+\Big(1-y_k^{(i)}\Big)\log\Big(1-\sigma_k^{(i)}\Big)\Bigg)
$$

Trong đó, $\sigma_k^{(i)}$ là đầu ra của nút thứ $k$ ở tầng ra tương ứng với dữ liệu huấn luyện thứ $i$. Hay nói cách khác chính là $a_k^{(L)}$. Bằng công thức đó, ta cài đặt được như sau:

{{<codeblock "nn.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn.py">}}
class NN():
    def cost(self, data):
        """
        Return cross-entropy cost of NN on test data
        """
        m = len(data)
        j = 0
        for x, y in data:
            _, a = self.feedforward(x)
            a_L = a[-1]
            j += np.sum(np.nan_to_num(y*np.log(a_L) + (1-y)*np.log(1-a_L)))
        return -j / m
{{</codeblock>}}

## 2.5. Lan truyền ngược
Bước tiếp theo ta cài đặt thao tác tính đạo hàm với lan truyền ngược (*backpropagation*). Ở bài trước, ta đã đề cập tới công thức tính của đạo hàm theo phương pháp lan truyền ngược:

$$
\begin{aligned}
\dfrac{\partial{J}}{\partial{\mathbf{z}^{(L)}}} &= \dfrac{\partial{J}}{\partial{\mathbf{a}^{(L)}}}\dfrac{\partial{\mathbf{a}^{(L)}}}{\partial{\mathbf{z}^{(L)}}}
\\cr
\dfrac{\partial{J}}{\partial{\mathbf{z}^{(l)}}} &= \bigg(\big(\mathbf{W}^{(l+1)}\big)^{\intercal}\dfrac{\partial{J}}{\partial{\mathbf{z}^{(l+1)}}}\bigg)\dfrac{\partial{\mathbf{a}^{(l)}}}{\partial{\mathbf{z}^{(l)}}}
\\cr
\dfrac{\partial{J}}{\partial{\mathbf{W}^{(l)}}} &= \dfrac{\partial{J}}{\partial{\mathbf{z}^{(l)}}}\big(\mathbf{a}^{(l-1)}\big)^{\intercal}
\end{aligned}
$$

Một điểm cần lưu ý ở đây là $\mathbf a^{(l)}$ và $\mathbf W^{(l)}$ với $l=\overline{1,L}$ không chứa giá trị cho bias. Bởi lẽ các $a_0=1$ ta tự thêm vào để dễ dàng sử dụng phép nhân ma trận mà thôi. Mà nếu lấy đạo hàm của $a_0$ theo $z$ bất kì thì luôn bằng $0$, nên nó cũng thực sự không có ý nghĩa.

> Kinh nghiệm là, nếu để ý số chiều của các giá trị $\mathbf W, \mathbf z, \mathbf a$ thì ta có thể biết được phép toán giữa các biến như thế nào. Nên khi lập trình ta nên in kích cỡ các biến đó ra để tiện theo dõi.

Với hàm lỗi là cross-entropy như trên thì ta có thể chứng minh đạo hàm của $J$ theo $\mathbf z^{L}$:
$$\dfrac{\partial{J}}{\partial{\mathbf{z}^{(L)}}}=\mathbf{a}^{(L)}-\mathbf{y}$$

Tôi không chứng minh ở đây, nhưng việc chứng minh này cũng không khó, nếu bạn quan tâm thì có thể vẽ vài nhát ra giấy nháp là thấy được ngay.

Đạo hàm của hàm kích hoạt *sigmoid* theo $\mathbf z$ có thể bằng công thức:
$$\dfrac{\partial{\mathbf{a}^{(l)}}}{\partial{\mathbf{z}^{(l)}}}=\mathbf{a}^{(l)}\odot\big(1-\mathbf{a}^{(l)}\big)$$

Bằng phép suy luận ở trên, cùng với [giải thuật đã đưa ra](/vi/2018/04/nn-intro/#5-lan-truyền-ngược-và-đạo-hàm), ta có thể cài đặt như sau:

{{<codeblock "nn.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn.py">}}
class NN():
    def backprop(self, x, y):
        """
        Backpropagation to calc derivatives
        """
        w_grad = [np.zeros(W.shape) for W in self.w]
        # feedforward
        z, a = self.feedforward(x)
        # backward
        dz = a[-1] - y
        for _l in range(1, self.L):
            l = -_l # layer index
            if l < -1:
                da = a[l] * (1 - a[l])
                # do not calc for w_0 (da_0 / dz = 0 because of a_0 = 1 for all z)
                dz = np.dot(self.w[l+1][:, 1:].transpose(), dz) * da
            # gradient    
            w_grad[l] = np.dot(dz, a[l-1].transpose())
        return w_grad
{{</codeblock>}}

## 2.6. Kiểm tra đạo hàm
Nói là việc cài đặt lan truyền ngược đơn giản, nhưng khi thực hiện thì rất dễ xảy ra nhầm lẫn. Cũng như các bài toán học máy khác, việc **{{<hl-text green>}}kiểm tra đạo hàm là cực kì quan trọng{{</hl-text>}}**. Như trong bài [tối ưu hàm lỗi với gradient descent](/vi/2017/12/ml-gd/#3-2-kiểm-tra-đạo-hàm) đã đề cập, ta tính được đạo hàm bằng phương pháp số học, với $\epsilon$ là 1 giá trị đủ nhỏ nhưng không quá nhỏ (thường là $10^{-4}$):
$$
f^{\prime}(x)\approx\frac{f(x+\epsilon)-f(x-\epsilon)}{2\epsilon}
$$
Khi đó, ta so sánh giá trị tính được này với giá trị tính được của giải thuật lan truyền ngược thì ta có thể rút ra kết luận rằng giải thuật ta chạy hợp lý hay chưa. Nếu chênh lệch nhau nhiều (thường là $10^{-5}$) thì giải thuật của ta nên xem xét lại. Tất nhiên là thì giá trị chênh lệch càng nhỏ thì càng tốt.

Ở đây, do có nhiều tham số nên ta có thể coi hàm lỗi $J$ là hàm nhiều biến $\mathbb W$. Như vậy, ta cần tính đạo hàm riêng của $J$ theo từng tham số $w$ thành phần và kiểm tra xem đạo hàm riêng này đúng đắn hay chưa. Để tính đạo hàm riêng theo phương pháp số học, ta cũng áp dụng việc tính 2 đầu với $\epsilon$ cho riêng tham số tương ứng:

{{<codeblock "nn.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn.py">}}
class NN():
    def check_grad(self, data, grad, epsilon=1e-4, threshold=1e-6):
        """
        Check gradient with:
        * Epsilon      : 1e-4
        * Threshold : 1e-6
        """
        for l in range(self.L - 1):
            n_row, n_col = self.w[l].shape
            for i in range(n_row):
                for j in range(n_col):
                    w_l_ij = self.w[l][i][j]
                    # left
                    self.w[l][i][j] = w_l_ij - epsilon
                    l_cost = self.cost(data)
                    # right
                    self.w[l][i][j] = w_l_ij + epsilon
                    r_cost = self.cost(data)
                    # numerical grad
                    num_grad = (r_cost - l_cost) / (2 * epsilon)
                    # diff
                    diff = abs(grad[l][i][j] - num_grad)
                    # reset w
                    self.w[l][i][j] = w_l_ij
                    
                    if diff > threshold:
                        print('Check Grad Error at (l: {0}, col: {1}, row: {2}), | num_grad: {3} vs backprop grad: {4} | : {5}'
                              .format(l, i, j, num_grad, grad[l][i][j], diff))
                        return False
        
        return True
{{</codeblock>}}

## 2.7. Huấn luyện
Tính được đạo hàm rồi thì việc tiếp theo ta cần làm là huấn luyện mạng, hay nói cách khác là tìm tập tham số $\mathbb W$ sao cho phép suy luận của ta được hợp lý bằng cách tối ưu hàm lỗi $J$. 

Trong bài này, tôi sẽ sử dụng [phương pháp mini-batch GD](/vi/2017/12/ml-gd/#5-2-mini-batch-gd) để tối ưu hàm lỗi.

{{<codeblock "nn.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn.py">}}
class NN():
    def train(self, train_data, epochs, mini_batch_size, eta):
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

Hi vọng rằng đoạn mã trên không quá khó hiểu. Nếu bạn chạy luôn hàm trên thì có lẽ sẽ rất chậm bởi việc kiểm tra đạo hàm ta đang làm cho toàn bộ tham số. Trên thực tế với các mạng lớn thì điều này sẽ gây khó khăn, nên ta có thể chấp nhận rủi ro 1 chút là chỉ tính với 1 số tham số ngẫu nhiên nào đó. Ở đây tôi không cài đặt phương pháp này, nhứng nếu bạn hứng thú thì có thể tự cài đặt coi như là 1 bài tập nhỏ nhé. Nếu có khó khăn gì thì cứ để lại [bình luận bên dưới](#disqus_thread), tôi sẽ ngoi lên bàn luận với bạn.

Chạy thử xem nào:
{{<codeblock "nn.py" "python" "https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/nn.py">}}
# load data
training_data, validation_data, test_data = data_loader.load()

# run NN
nn = NN([784, 100, 10])
nn.train(training_data, 30, 100, 3.0)
correct = nn.evaluate(test_data)
total = len(test_data)
print('Evaluation: {0} / {1} = {2}%'.format(correct, total, 100 * correct/total))
{{</codeblock>}}

Đoạn mã trên sẽ cho ta kết quả:
```
Evaluation: 9662 / 10000 = 96.62%
```

Như vậy với tập kiểm tra, ta đạt được `96.62%` kết quả chính xác! Một mạng NN cơ bản mà kết quả rất ấn tượng phải không nào!

Nếu bạn hứng thú với toàn bộ mã nguồn của phần này thì có thể [xem tại đây](https://github.com/dominhhai/dominhhai.github.io/blob/dev/code/nn-mnist/network.ipynb) nhé.

# 3. Bàn luận
Nếu bạn thử khởi tạo mạng với các giá trị khác nhau thì sẽ nhận ra rằng, việc tăng giảm kích cỡ mạng có thể cho kết quả rất khác nhau. Mạng càng nhỏ thì kết quả dự đoán sẽ càng tệ và ngược lại. Tuy nhiên, nếu kích cỡ mạng quá lớn thì kết quả cũng không hề khả quan trên tập kiểm tra mặc dù vẫn rất ngon lành với tập huấn luyện. Đó chính là [vấn đề mô hình quá khớp](/vi/2017/12/ml-overfitting/) mà tôi đã từng đề cập tới. Vấn đề này tôi sẽ viết vào bài tiếp theo trong chủ đề về mạng nơ-ron này.

Ngoài ra thì việc xây dựng mô hình mạng với các hàm khởi tạo, hàm lỗi khác nhau cũng sẽ cho hiệu năng khác nhau. Mô hình nào phù hợp thì câu trả lời là tuỳ bài toán mà ta cần giải quyết. Ví dụ, như xử lý ảnh người ta có thể xử dụng các mô hình [ConvNet](https://en.wikipedia.org/wiki/Convolutional_neural_network) hay xử lý ngôn ngữ thì sử dụng [RNN](https://en.wikipedia.org/wiki/Recurrent_neural_network) chẳng hạn.

Tất cả những vấn đề như vậy, tôi sẽ đề cập sau vì mục tiêu của bài này chỉ là thực hiện việc cài đặt cơ bản để làm sáng tỏ [lý thuyết về mạng NN ở bài trước](/vi/2018/04/nn-intro/). Còn bây giờ, nếu bạn có thắc mắc gì thì cứ để lại bình luận bên dưới nhé.