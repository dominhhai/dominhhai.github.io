---
title: "[Ma Trận] Một số khái niệm cơ bản"
slug: what-is-matrix
date: 2017-09-26
categories:
- Toán
- Ma Trận
tags:
- Ma Trận
keywords:
- Matrix
- Ma Trận
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/math/katex.png
metaAlignment: center
---
Đại số tuyến tính là một công cụ cơ bản cần thiết cho việc tìm hiểu học máy.
Bài đầu tiên trong [chuỗi chủ đề này](/vi/categories/ma-tr%E1%BA%ADn/)
sẽ tập trung vào định nghĩa một số khái niệm cơ bản trong đại số tuyến tính.
Lưu ý rằng các khái niệm tôi viết lại là dưới cái nhìn của người làm lập trình như tôi,
nên không chắc đảm bảo được tính chặt chẽ về mặt toán học.
<!--more-->

<!--toc-->

# 1. Một số khái niệm
## 1.1. Vô hướng (Scalar)
Một vô hướng là một số bất kì thuộc tập số nào đó.
Khi định nghĩa một số ta phải chỉ rõ tập số mà nó thuộc vào.
Ví dụ, $ n $ là số tự nhiên sẽ được kí hiệu: $ n \in \mathbb{N} $,
hoặc $ r $ là số thực sẽ được kí hiệu: $ r \in \mathbb{R} $.
Một số thường có thể định nghĩa được bằng một kiểu dữ liệu nguyên thủy của các ngôn ngữ lập trình.
Như số tự nhiên có thể là kiểu `int`, số thực có thể là kiểu `float` trong Python.

## 1.2. Véc-tơ (Vector)
Véc-tơ là 1 mảng của các vô hướng tương tự như mảng 1 chiều trong các ngôn ngữ lập trình.
Các phần tử trong véc-tơ cũng được đánh địa chỉ và có thể truy cập nó qua các địa chỉ tương ứng của nó.
Trong toán học, một véc-tơ có thể là véc-tơ cột nếu các nó được biểu diễn dạng cột,
hoặc có thể là véc-tơ hàng nếu nó được biểu diễn dưới dạng cột của các phần tử.

Một véc-tơ cột có dạng như sau:

$$
x =
\begin{bmatrix}
x_1 \\cr
x_2 \\cr
\vdots \\cr
x_n
\end{bmatrix}
$$

Một véc-tơ hàng có dạng như sau:
$$
x =
\begin{bmatrix}
x_1 &
x_2 &
\cdots &
x_n
\end{bmatrix}
$$

Trong đó, $ x_1 $, $ x_2 $, ..., $ x_n $ là các phần tử `thứ 1`, `thứ 2`, ... `thứ n` của véc-tơ.

## 1.3. Ma trận (Matrix)
Ma trận là một mảng 2 chiều của các vô hướng tương tự như mảng 2 chiều trong các ngôn ngữ lập trình. Ví dụ dưới đây là một ma trận có $ m $ hàng và $ n $ cột:
$$
A =
\begin{bmatrix}
A\_{1, 1} & A\_{1, 2} & \cdots & A\_{1, n} \\cr
A\_{2, 1} & A\_{2, 2} & \cdots & A\_{2, n} \\cr
\vdots    & \vdots    & \vdots & \vdots    \\cr
A\_{m, 1} & A\_{m, 2} & \cdots & A\_{m, n}
\end{bmatrix}
$$

Khi định nghĩa một ma trận ta cần chỉ rõ số hàng và số cột cùng trường số của các phần tử có nó.
Lúc này, $ mn $ được gọi là cấp của ma trận.
Ví dụ, ma trận số thực $ A $ có m hàng và n cột được kí hiệu là: $ A \in \mathbb{R}^{m \times n} $.

Các phần tử trong ma trận được định danh bằng 2 địa chỉ hàng $ i $ và cột $ j $ tương ứng.
Ví dụ phần tử hàng thứ 3, cột thứ 2 sẽ được kí hiệu là: $ A_{3,2} $.
Ta cũng có thể kí hiệu các phần tử của hàng $ i $ là $ A\_{i,:} $ và của cột $ j $ là $ A\_{:,j} $.
Nếu bạn để ý thì sẽ thấy $ A\_{i,:} $ chính là véc-tơ hàng, còn $ A\_{:,j} $ là véc-tơ cột.
Như vậy, véc-tơ có thể coi là trường hợp đặt biệt của ma trận với số hàng hoặc số cột là 1.

## 1.4. Ten-xơ (Ternsor)
Ten-xơ là một mảng nhiều chiều, nó là trưởng hợp tổng quát của việc biểu diễn số chiều.
Như vậy, ma trận có thể coi là một ten-xơ 2 chiều, véc-tơ là ten-xơ một nhiều còn vô hướng là ten-xơ vô chiều.

Các phần tử của một ten-xơ cần được định danh bằng số địa chỉ tương ứng với số chiều của ten-xơ đó. Ví dụ mộ ten-xơ $ \mathsf{A} $ 3 chiều có phần tử tại hàng $ i $, cột $ j $, cao $ k $ được kí hiệu là: $ \mathsf{A}\_{i,j,k} $.

# 2. Một số ma trận đặc biệt
## 2.1. Ma trận không
Ma trận không là ma trận mà tất cả các phần tử của nó đều bằng 0: $ A_{i,j} = 0, \forall{i,j}  $. Ví dụ:

$$
\varnothing =
\begin{bmatrix}
0 & 0 & 0 & 0 \\cr
0 & 0 & 0 & 0 \\cr
0 & 0 & 0 & 0
\end{bmatrix}
$$

## 2.2. Ma trận vuông
Ma trận vuông là ma trận có số hàng bằng với số cột: $ A \in R^{n \times n} $.
Ví dụ một ma trận vuông cấp 3 (số hàng và số cột là 3) có dạng như sau:

$$
A =
\begin{bmatrix}
2 & 1 & 9 \\cr
4 & 5 & 9 \\cr
8 & 0 & 5
\end{bmatrix}
$$

Với ma trận vuông, đường chéo bắt đầu từ góc trái trên cùng tới góc phải dưới cùng được gọi là đường chéo chính: $ \\{ A\_{i,i} \\} $

## 2.3. Ma trận chéo
Ma trận chéo là ma trận vuông có các phần từ nằm ngoài đường chéo chính bằng 0: $ A_{i,j} = 0, \forall{i \not = j} $.
Ví dụ ma trận chéo cấp 4 (có 4 hàng và 4 cột) có dạng như sau:

$$
A =
\begin{bmatrix}
1 & 0 & 0 & 0 \\cr
0 & 2 & 0 & 0 \\cr
0 & 0 & 3 & 0 \\cr
0 & 0 & 0 & 4
\end{bmatrix}
$$

> Lưu ý rằng ma trận vuông không (ma trận vuông có các phần tử bằng 0) cũng là một ma trận chéo.

## 2.4. Ma trận đơn vị
Là ma trận chéo có các phần tử trên đường chéo bằng 1:
$$
\begin{cases}
A\_{i,j} = 0, \forall{i \not = j} \\cr
A\_{i,j} = 1, \forall{i = j}
\end{cases}
$$

Ma trận đơn vị được kí hiệu là $ I_n $ với $ n $ là cấp của ma trận. Ví dụ ma trận đơn vị có cấp 3 được biểu diễn như sau:

$$
I_{3} =
\begin{bmatrix}
1 & 0 & 0 \\cr
0 & 1 & 0 \\cr
0 & 0 & 1
\end{bmatrix}
$$

## 2.5. Ma trận cột
Ma trận cột chính là véc-tơ cột, tức là ma trận chỉ có 1 cột.

## 2.6. Ma trận hàng
Tương tự như ma trận cột, ma trận hàng chính là véc-tơ hàng, tức là ma trận chỉ có 1 hàng.

## 2.7. Ma trận chuyển vị
Ma trận chuyển vị là ma trận nhận được sau khi ta đổi hàng thành cột và cột thành hàng.

$$
\begin{cases}
A \in \mathbb{R}^{m,n} \\cr
B \in \mathbb{R}^{n,m} \\cr
A\_{i,j} = B\_{j,i}, \forall{i,j}
\end{cases}
$$

Ma trận chuyển vị của $ A $ được kí hiệu là $ A^\intercal $. Như vậy: $ (A^\intercal)_{i,j} = A\_{j,i} $.

Véc-tơ cũng là một ma trận nên mọi phép toán với ma trận đều có thể áp dụng được, bao gồm cả phép chuyển vị ma trận.
Sử dụng phép chuyển vị ta có thể biến một véc-tơ hàng thành véc-tơ cột và ngược lại.
Đôi lúc để viết cho ngắn gọi người ta thường sử dụng phép chuyển vị để định nghĩa véc-tơ cột giống như: $ x = [x_1, x_2, ..., x_n]^\intercal $.

# 3. Các kí hiệu
Để thuận tiện, từ nay về sau tôi sẽ mặc định các vô hướng, phần tử của ma trận (bao gồm cả véc-tơ) mà chúng ta làm việc là thuộc trường số thực $ \mathbb{R} $. Tôi cũng sẽ sử dụng một số kí hiệu bổ sung như dưới đây.

Các ma trận sẽ được kí hiệu: $ [A\_{ij}]\_{mn} $, trong đó $ A $ là tên của ma trận;
$ m, n $ là cấp của ma trận; còn $ A\_{ij} $ là các phần tử của ma trận tại hàng $ i $ và cột $ j $.

Các véc-tơ ta cũng sẽ biểu diễn tương tự.
Véc-tơ hàng: $ [x_i]_n $, trong đó $ x $ là tên của véc-tơ;
$ n $ là cấp của véc-tơ; $ x_i $ là phần tử của véc-tơ tại vị trí $ i $.
Véc-tơ cột ta sẽ biểu diễn thông qua phép chuyển vị của véc-tơ hàng: $ [x_i]_n ^\intercal  $.

Ngoài ra, nếu một ma trận được biểu diễn dưới dạng: $ [A\_{1j}]\_{1n} $ thì ta cũng sẽ hiểu ngầm luôn nó là véc-tơ hàng.
Tương tự, với $ [A\_{i1}]\_{m1} $ thì ta có thể hiểu ngầm với nhau rằng nó là véc-tơ cột.

Một điểm cần lưu ý nữa là các giá trị $ m, n, i, j $ khi được biểu điễn tường minh dưới dạng số,
ta cần phải chèn dấu phẩy `,` vào giữa chúng.
Ví dụ: $ [A\_{ij}]\_{9,4} $ là ma trận có cấp là `9, 4`. $ A\_{5,25} $ là phần tử tại hàng `5` và cột `25`.
Việc này giúp ta phân biệt được giữa ma trận và véc-tơ, nếu không ta sẽ bị nhầm ma trận thành véc-tơ.

Trên đây là một số khái niệm cơ bản để làm việc với ma trận, trong phần sau tôi sẽ đề cập tới các phép toán của ma trận.
Việc biến đổi ma trận và các phép toán trên ma trận là rất cần thiết để làm việc với các bài toán về học máy sau này. *Nếu bạn có thắc mắc hay góp ý gì thì đừng quên bình luận ở bên dưới nhé* m(.)_(.)m.
