---
title: "[Giải Tích] Đạo hàm của hàm nhiều biến số"
slug: multi-var-func
date: 2017-09-28
categories:
- Toán
- Giải Tích
tags:
- Giải Tích
- Đạo Hàm
keywords:
- Calculus
- Giải Tích
- Đạo Hàm Nhiều Biến
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/math/katex.png
metaAlignment: center
---
Hàm nhiều số có ứng dụng rất rộng rãi trong các bài toán học máy vì đa số các các thuộc tính của hiện tượng ta theo dõi không phải chỉ có 1 mà rất nhiều tham số.
Các tham số này được liên kết với nhau một cách đặc biệt bởi các hàm số khác nhau để có thể đưa ra được các kết quả mong muốn.
Nên việc tìm hiểu về hàm nhiều biến là rất cần thiết để có thể hiểu được các lý thuyết của học máy.
Trong bài viết này tôi sẽ tóm tắt lại đôi chút về hàm nhiều biến và đạo hàm của chúng chứ không đi sâu vào các vấn đề khác của hàm nhiều biến.

<!-- toc -->
# 1. Hàm nhiều biến số
Là một hàm số có nhiều biến số từ một tập xác định nào đó và cho ra kết quả là một số thực.
$$ \mathsf{D} \subset \mathbb{R}^n, f: \mathsf{D} \mapsto \mathbb{R} $$
Hay:
$$ (x_1, x_2, ..., x_n) \mapsto f(x_1, x_2, ..., x_n) \in \mathbb{R} $$

Hay biểu diễn dưới dạng véc-tơ:
$$ [x]_n \in \mathbb{R}^n \mapsto f(x) \in \mathbb{R} $$

Ví dụ, cho $ x, y \in \mathbb{R} $ và khi đó ánh xạ $ z = f(x, y) = x^2 + y^2 $ gọi là hàm số của biến $ x, y $.

Khi làm việc với các bài toán học máy đầu ra của ta có thể không phải là một số mà là 1 tập các số nên ta thường xuyên phải làm việc với các hàm nhiều biến dạng mở rộng kiểu này. Tập các số đầu ra này ta có thể biểu diễn dưới dạng một véc-tơ, hay nói cách khác hàm nhiều biến của ta sẽ cho kết quả là một véc-tơ. Ví dụ:
$$
f(x, y) = \begin{bmatrix} x^2 + \sin(y) \\cr 2xy + y^2 \end{bmatrix}
$$

Để tiện giải thích và minh hoạ, trong bài này tôi sẽ đề cập tới trường hợp hàm của ta có 2 biến số. Tuy nhiên các tính chất, phép toán và phương pháp làm việc có thể mở rộng ra cho các hàm nhiều biến số hơn.

# 2. Đạo hàm riêng
Đạo hàm riêng theo 1 biến của một hàm số là đạo hàm theo biến đó với giả thuyết rằng các biến khác là hằng số. Cụ thể, cho hàm số $ f(x, y) $ và một điểm $ M(x_0, y_0) $ thuộc tập xác định của hàm, khi đó đạo hàm theo biến $ x $ tạo điểm $ M $ được gọi là đạo hàm riêng của $ f $ theo $ x $ tại $ M $. Lúc này $ y $ sẽ được cố định bằng giá trị $ y_0 $ và hàm của ta có thể coi là hàm 1 biến của biến $ x $.

Đạo hàm riêng của $ f $ theo $ x $ lúc này sẽ được kí hiệu là: $ f_x^{\prime}(x_0, y_0) $ hoặc $\displaystyle \frac{\partial{f(x_0, y_0)}}{\partial{x}} $, còn đạo hàm theo biến $ y $ được biểu diễn tương tự: $ f_y^{\prime}(x_0, y_0) $ hoặc $\displaystyle \frac{\partial{f(x_0, y_0)}}{\partial{y}} $.

Với tôi thì tôi thích biểu diễn dưới dạng $ f_x^{\prime} $ vì dễ nhìn và không bị nhầm lẫn với phân số.

Ví dụ: $ f(x, y) = x^2y + \sin(y) $ sẽ có đạo hàm $ f_x^{\prime} = 2xy $ và $ f_y^{\prime} = x^2 + \cos(y) $.

Còn $\displaystyle f(x, y) = \begin{bmatrix} x^2 + \sin(y) \\cr 2xy + y^2 \end{bmatrix} $ có đạo hàm là $\displaystyle f_x^{\prime} = \begin{bmatrix} 2x \\cr 2y \end{bmatrix} $ và $\displaystyle f_y^{\prime} = \begin{bmatrix} \cos(y) \\cr 2x + 2y \end{bmatrix} $

Trường hợp tổng quát với hàm có nhiều biến thì đạo hàm riêng theo 1 biến nào đó một cách tương tự như trên là đạo hàm theo biến đó với giả thuyết tất cả các biến còn lại là hằng số.

# 3. Đạo hàm riêng của hàm hợp
Chúng ta vừa xem xét tới đạo hàm của hàm nhiều biến vậy với các hàm hợp thì đạo hàm được tính thế nào?

> Hàm hợp là hàm hợp bởi nhiều hàm số khác nhau, ví dụ: $ f(u, v) $ trong đó $ u(x, y) $ và $ v(x, y) $ là các hàm số theo biến $ x, y $, lúc này $ f $ được gọi là hàm hợp của $ u, v $.

Giả sử, $ f $ có đạo hàm riêng theo $ u, v $ và $ u, v $ có đạo hàm theo $ x, y $ thì khi đó:

$$
\begin{cases}
f_x^{\prime} = f_u^{\prime}u_x^{\prime} + f_v^{\prime}v_x^{\prime} \\cr
f_y^{\prime} = f_u^{\prime}u_y^{\prime} + f_v^{\prime}v_y^{\prime}
\end{cases}
$$

Nhìn hơi khó nhớ phải không? Giờ ta viết lại dưới dạng giống như phân số thì chắc là dễ nhớ hơn chút:

$$
\begin{cases}
\displaystyle{\frac{\partial{f}}{\partial{x}} = \frac{\partial{f}}{\partial{u}}\frac{\partial{u}}{\partial{x}} + \frac{\partial{f}}{\partial{v}}\frac{\partial{v}}{\partial{x}}}
\\cr\\cr
\displaystyle{\frac{\partial{f}}{\partial{y}} = \frac{\partial{f}}{\partial{u}}\frac{\partial{u}}{\partial{y}} + \frac{\partial{f}}{\partial{v}}\frac{\partial{v}}{\partial{y}}}
\end{cases}
$$

Nhìn dạng phân số, ta có thể luận rằng hàm thành phần sẽ bị triệt tiêu để lại còn hàm hợp với biến gốc. Đây chỉ là cách để nhớ thôi nhé chứ kí hiệu đạo hàm không phải là phân số đâu nên đừng có áp dụng phương pháp tính và tính chất của phân số vào đây nha.

Trường hợp tổng quát với các hàm hợp có nhiều hàm thành phần cũng được tính một cách tương tự bằng cách lấy tổng của tích đạo hàm từng hàm thành phân một. Ví dụ với hàm hợp 3 biến $ f(u, v, w) $, trong đó $ u(x, y) $, $ v(x, y) $ và $ w(x, y) $ thì đạo hàm được tính như sau:

$$
\begin{cases}
\displaystyle{\frac{\partial{f}}{\partial{x}} = \frac{\partial{f}}{\partial{u}}\frac{\partial{u}}{\partial{x}} + \frac{\partial{f}}{\partial{v}}\frac{\partial{v}}{\partial{x}} + \frac{\partial{f}}{\partial{w}}\frac{\partial{w}}{\partial{x}}}
\\cr\\cr
\displaystyle{\frac{\partial{f}}{\partial{y}} = \frac{\partial{f}}{\partial{u}}\frac{\partial{u}}{\partial{y}} + \frac{\partial{f}}{\partial{v}}\frac{\partial{v}}{\partial{y}} + \frac{\partial{f}}{\partial{w}}\frac{\partial{w}}{\partial{y}}}
\end{cases}
$$

# 4. Đạo hàm của hàm ẩn
Hàm ẩn là một hàm mà ta chưa biết dạng của nó nhưng ta biết rằng nó có thể biểu diễn qua một biến khác trong hàm số. Hơi khó hiểu chút ha!

Cho $ f(x, y) = 0  $, lúc này ta nói $ y(x) $ là hàm ẩn khi tồn tại $ y = y_0 $ sao cho $ f(x, y_0) = 0 $ với mọi $ x $. Khi đó ta còn có thể coi $ f $ là hàm một biến theo $ x $.

Mặc dù chưa biết dạng của $ y(x) $ nhưng lúc này ta có thể tính được đạo hàm của nó như sau:
$\displaystyle y_x^{\prime} = -\frac{f_x^{\prime}}{f_y^{\prime}} $

Đương nhiên là khi đó $ f_y^{\prime} \not = 0 $ thì công thức mới xác định được. Ta có thể chứng minh đơn giản như sau:

$$
f(x, y) = 0
 \implies f(x, y)^{\prime} = 0
 \iff f_x^{\prime} + f_y^{\prime}y_x^{\prime} = 0
 \iff y_x^{\prime} = -\frac{f_x^{\prime}}{f_y^{\prime}}
$$

Viết dưới dạng loằng ngoằng ta sẽ được:

$$
\frac{dy}{dx} = -\frac{\displaystyle{\frac{\partial{f}}{\partial{x}}}}{\displaystyle{\frac{\partial{f}}{\partial{y}}}}
$$

Trường hợp tổng quá cũng sẽ được tính tương tự. Ví dụ: $ f(x, y, u) $ có hàm ẩn $ u(x, y) $ thì đạo hàm riêng của $ u $ sẽ được tính như sau:

$$
\begin{cases}
\displaystyle{u_x^{\prime} = -\frac{f_x^{\prime}}{f_u^{\prime}}}
\\cr\\cr
\displaystyle{u_y^{\prime} = -\frac{f_y^{\prime}}{f_u^{\prime}}}
\end{cases}
$$

# 5. Đạo hàm cấp cao
Đạo hàm có thể được gắn cấp bậc để phân biệt chúng với nhau, đạo hàm của hàm số gốc được coi là đạo hàm cấp 1, đạo hàm của đạo hàm cấp 1 được coi là đạo hàm cấp 2,...

Ví dụ, ta có hàm số $ f(x, y) = x^2y + y^2 $ thì đạo hàm cấp 1 của nó là:
$$
\begin{cases}
\displaystyle{\frac{\partial{f}}{\partial{x}}} = 2xy
\\cr\\cr
\displaystyle{\frac{\partial{f}}{\partial{y}}} = x^2 + 2y
\end{cases}
$$

và có đạo hàm cấp 2 là:

$
\begin{cases}
\displaystyle{\frac{\partial^2f}{\partial{x^2}} = \frac{\partial}{\partial{x}}\Bigg(\frac{\partial{f}}{\partial{x}}\Bigg)} = 2y
\\cr\\cr
\displaystyle{\frac{\partial^2f}{\partial{y}\partial{x}} = \frac{\partial}{\partial{y}}\Bigg(\frac{\partial{f}}{\partial{x}}\Bigg)} = 2x
\end{cases}
$　　　　　　$
\begin{cases}
\displaystyle{\frac{\partial^2f}{\partial{x}\partial{y}} = \frac{\partial}{\partial{x}}\Bigg(\frac{\partial{f}}{\partial{y}}\Bigg)} = 2x
\\cr\\cr
\displaystyle{\frac{\partial^2f}{\partial{y^2}} = \frac{\partial}{\partial{y}}\Bigg(\frac{\partial{f}}{\partial{y}}\Bigg)} = 2
\end{cases}
$

Bạn có để ý là $\displaystyle \frac{\partial^2f}{\partial{y}\partial{x}} = \frac{\partial^2f}{\partial{x}\partial{y}} $ không? Đây chính là định lý Schwarz về đạo hàm cấp cao: Đạo hàm riêng cấp cao của nhiều biến không phụ thuộc vào thứ tự lấy đạo hàm riêng của các biến thành phần đó.

Giả sử hàm $ f(x, y, z) $ có 3 biến đi chẳng nữa thì ta luôn có $\displaystyle \frac{\partial^2f}{\partial{x}\partial{y}\partial{z}} = \frac{\partial^2f}{\partial{y}\partial{x}\partial{z}} = \frac{\partial^2f}{\partial{z}\partial{x}\partial{y}} $.

Riêng với đạo hàm cấp 2 ta còn có thể sử dụng cách kí hiệu tương tự như đạo hàm cấp 1 như sau: $ f^{\prime\prime}_x $ cho đạo hàm cấp 2 của theo biến x, $ f^{\prime\prime}_y $ cho đạo hàm cấp 2 của theo biến y và $ f^{\prime\prime}\_{xy} $ cho đạo hàm cấp 2 của theo cả 2 biến x, y. Lưu ý là kí hiệu này chỉ dùng cho cấp 2 thôi nhé, các cấp cao hơn ta không sử dụng cách này nữa vì nhìn sẽ rất loạn.

# 6. Gradient và đạo hàm có hướng
Nếu ta kết hợp các đạo hàm riêng lại thành một véc-tơ và tính đạo hàm theo véc-tơ đó thì ta sẽ thu được đạo hàm toàn phần. Hay nói cách khác là đạo hàm theo tất cả các biến hay đạo hàm theo véc-tơ hợp thành đó. Đạo hàm này được gọi là gradient của hàm theo véc-tơ tương ứng.

Ta có thể nói một cách hình thức theo dạng toán học như sau. Cho hàm số $ f(x, y) $ và một điểm $ M(x_0, y_0) $ thuộc tập xác định của $ f $, ta có gradient tại $ M $ là:

$$\displaystyle \nabla{f(x_0, y_0)} = \Bigg(\frac{\partial{f}}{\partial{x}}(x_0, y_0), \frac{\partial{f}}{\partial{y}}(x_0, y_0)\Bigg) $$

Ở đây tôi viết dưới dạng hàng ngang cho dễ nhìn, nhưng về mặt hình thức gradient là véc-tơ cột đấy nha.

Hay viết dưới dạng kí hiệu véc-tơ như sau:

$$\displaystyle \nabla = \Bigg[\frac{\partial{f}}{\partial{x}}\Bigg]\text{\^{i}} + \Bigg[\frac{\partial{f}}{\partial{y}}\Bigg]\text{\^{j}} $$

Trong đó $ \overrightarrow{u}(\text{\^{i}}, \text{\^{j}}) $ là véc-tơ đơn vị.

Ví dụ, hàm số $ f(x, y) = x^2 + y^2 $ sẽ có gradient là: $\displaystyle \nabla{f} = \begin{bmatrix} 2x \\cr 2y \end{bmatrix} $

Nếu nhìn cách trừu tượng thì gradient là độ biến thiên của hàm số theo sự biến thiên của tất cả các biến số của nó. Như vậy, ta có thể thấy rằng chiều của gradient sẽ cùng chiều với véc-tơ lấy đạo hàm. Cụ thể với ví dụ trên thì $ \nabla{f(x_0, y_0)} $ sẽ có cùng chiều với véc-tơ $ (x_0, y_0) $.

Hay nói một cách khác, hàm số tăng nhanh nhất theo hướng của gradient và giảm nhanh nhất khi ngược hướng với gradient của nó. Bạn nhớ lấy điểm này nhé vì nó rất quan trọng cho việc tối ưu hàm số sau này trong các bài toán học máy đấy.

Ta vừa nói về gradient là đạo hàm theo hướng tăng nhanh nhất của hàm số, vậy nếu tất cả các biến của hàm số biến thiên theo 1 hướng (véc-tơ) bất kì nào đó thì cách tính đạo hàm lúc đó thế nào? Giả sử ta có hàm số $ f(x, y) $ có gradient là $ \nabla{f} $ và 1 véc-tơ $ \overrightarrow{v} $ thể hiện cho sự biến thiên của 2 biến $ x, y $. Lúc này đạo hàm theo véc-tơ $ \overrightarrow{v} $ sẽ là:

$$ \nabla_{\overrightarrow{v}}f =  \overrightarrow{v}\nabla{f} $$.

Hay phát biểu thành lời thì đạo hàm theo véc-tơ $ \overrightarrow{v} $ sẽ là một véc-tơ hình thành bởi tích của $ \overrightarrow{v} $ với gradient của hàm.
