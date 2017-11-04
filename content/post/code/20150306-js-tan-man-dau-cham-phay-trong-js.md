---
title: "[JS] Tản mạn dấu chấm phẩy"
slug: js-do-not-need-semicolon
date: 2015-03-06
categories:
- Lập Trình
- JS
tags:
- JS
- JS Tips
keywords:
- JavaScript
- JS
autoThumbnailImage: true
thumbnailImagePosition: "left"
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/js.svg
coverImage: https://res.cloudinary.com/dominhhai/image/upload/code/js.svg
metaAlignment: center
---
JavaScript cho phép chúng ta lược bỏ dấu kết thúc lệnh (dấu chấm phẩy). Nhưng trường hợp nào ta phải bắt buộc dùng dấu chấm phải, trường hợp nào thì không và có khi nào ta nên bỏ nó đi?
Trước mắt ta xem một chút bộ dịch JavaScript sẽ làm gì với các lệnh của ta.
<!--more-->
<!-- toc -->

{{< codeblock "ex1.js" "js" >}}
var a = 10
var b = a + 20
console.log('The result is that: a = %d, and b = %d', a, b)

function add(a, b) {
    var
        c = 10
    return
        a + b
}
{{< /codeblock >}}

# 1. JavaScript sẽ tự thêm dấu chấm phẩy

Mặc dù JavaScript cho phép lược bỏ dấu chấm phẩy (;) nhưng về bản chất nó vẫn thêm (;) vào mỗi lệnh đầy đủ khi thực thi chương trình. Tại sao lại là lúc thực thi chương trình? Lý do rất đơn giản là JavaScript là ngôn ngữ thông dịch, lúc chạy chương trình nó mới được dịch chứ không cần phải dịch toàn bộ trước như các ngôn ngữ biên dịch như C, C++ hay Java.
Đoạn chương trình phía trên khi chạy sẽ được chuyển thành dạng sau:

{{< codeblock "ex2.js" "js" >}}
var a = 10;
var b = a + 20;
console.log('The result is that: a = %d, and b = %d', a, b);

function add(a, b) {
    var
        c = 10;
    return;
        a + b;
}
{{< /codeblock >}}

Ồ hay nhỉ? Nó tự động thêm cho ta nhưng cũng không được thông minh cho lắm, vì như đoạn mã trên `return;` đã là một lệnh đầy đủ rồi nên nó sẽ bị chèn dấu (;) vào. Như vậy kiểu như đoạn mã trên thì hàm `add` sẽ không trả ra gì nữa, quả là tai hại. Vì vậy cần lưu ý là không xuống dòng ngày sau `return` trừ khi ta sử dụng dấu (;) để kết thúc lệnh.

# 2. Khi nào bắt buộc phải dùng dấu chấm phẩy

Ta buộc phải dùng (;) giữa các lệnh gắn (bao gồm cả tính toán), lệnh gọi hàm trên cùng một dòng như ví dụ dưới đây.

{{< codeblock "ex3.js" "js" >}}
var a = 10; b = a + 20; console.log('The result is that: a = %d, and b = %d', a, b);

var b -= a; var b2 = Math.pow(b)

var c = a
b++

function add(a, b) {
    return
        a + b
}
{{< /codeblock >}}

# 3. Khi nào ta lược bỏ được dấu chấm phẩy

Ta lược bỏ được (;) cho các lệnh trên các dòng khác nhau như ví dụ trên đã đưa ra.
Ta cũng bỏ được nó khi gắn các block cho biến như ví dụ dưới đây.

{{< codeblock "ex4.js" "js" >}}
var square, add = function add(a, b) {
    return a + b
}

var sub = function sub(a, b) {
    return a - b;
}    square = function (a) { return a * a }
{{< /codeblock >}}

# 4. Cận thận với câu lệnh rỗng

Câu lệch rỗng là một câu lệch chỉ bao gồm dấu kết thúc lệnh (;) hoặc các lệnh không có nghĩa.

{{< codeblock "ex5.js" "js" >}}
; var a = 5,    // -> lệch rỗng ;
        b = 8;
for (;a < b; a ++);    // -> lệch rỗng for (;a < b; a ++); do vòng for ở đây không còn khối lệch thực thi
    console.log('a comes to b');

for (i = 0; i < 100; i ++) {
    a += i + b;
};;    // -> 2 câu lệch rỗng ; và ;
console.log('a = %d', a)

function add(a, b) {
    return a + b;
};    // -> lệch rỗng ;
{{< /codeblock >}}

Với các lệnh rỗng chúng vẫn thực thi nhưng với chúng ta thì dường như chúng lại vô dụng, nên khi code cần cẩn thận ở điểm này, nhất là các khối lệnh thực hiện bằng hàm hay lệch điều khiển.
Lệch rỗng không hẳn là không có tác dụng tốt, chúng tốt khi chúng ta ghép file mã nguồn như phần 5.5 mô tả.

# 5. Ta có nên bỏ dấu chấm phẩy

Bỏ dấu kết thúc này có tác dụng gì không? Hay chỉ mang lại phiền toái. Ta cùng xét một vài tiêu chí dưới đây.
## 5.1. Kích thước file khi bỏ dấu chấm phẩy
Dường như bỏ dấu chấm phẩy đi ta có thể tiết kiệm được chút dung lượng file. Nhưng quả thực chẳng đáng là bao vì mỗi dấu chỉ chiếm 1 byte. Nhưng rất nhiều người code JS vẫn bỏ dấu (;), đặc biệt là với những người hay code bằng [Coffee Script](http://coffeescript.org/ "Coffee Script").

## 5.2. Sử dụng bộ rút gọn file JS
Với những file JS phía Server, ít khi chúng ta sử dụng việc rút gọn file. Nhưng với phía Client như các mã thực thi phía trình duyệt, ta thường xuyên sử dụng các công cụ rút gọn file như [Google Closure](http://closure-compiler.appspot.com/home).
Bằng các công cụ rút gọn file ta có thể thu gọn các tên biến, tên hàm lại, loại bỏ các khoảng trống không cần thiết như các dấu space, tab và cả enter, và loại bỏ cả các biến, các hàm không sử dụng trong mã nguồn. Như vậy file rút gọn của ta sẽ nhẹ đi rất nhiều và làm cho người lấy được file đó cũng khó hiểu hơn.
Tất nhiên cũng có những công cụ cho phép chúng ta revert lại mã đã thu gọn, nhưng các tên được thu gọn thì không có cách nào revert được ^^.
Ngoài ra, ta cũng có thể sử dụng các công cụ nén file mã nguồn như gzip. Về việc sử dụng gzip để nén mã nguồn mình sẽ viết vào một bài khác.
Miên man hơi nhiều, vậy việc sử dụng bộ rút gọn có tai hại gì liên quan tới dấu (;). Như vừa đề cập phía trên, các bộ rút gọn sẽ lược bỏ các khoảng trống không cần thiết, nhưng việc xác định khoảng nào là cần, khoảng nào là không là dựa vào dấu kết thúc lệnh và các dấu bao khối lệnh ({}). Nên với các lệnh không kết thúc bằng (;) hoặc ({}) sẽ được thu lại dính vào các lệnh phía trước hết. Ta có thể xem ví dụ sau.

{{< codeblock "ex6.js" "js" >}}
var a = 10
var b = a + 20
function add (a, b) {
    return a + b
}
a = add (a, b)
{{< /codeblock >}}

Đoạn mã trên sẽ được thu gọn lại như sau.

{{< codeblock "ex7.js" "js" >}}
var a=10var b=a+20function add(a,b){return a+b}a=add(a,b)
{{< /codeblock >}}

Với đoạn lệnh thu gọn phía trên, ta coi như công cốc.
Nhưng tin không buồn tới vậy, Google khá thông minh hơn các công cụ khác. Google cũng xác định được khi nào cần thêm dấu (;) vào lệnh, nhưng với các mã nguồn phức tạp thì cũng không chắc là nó đúng 100% được. Ví dụ đoạn mã nguồn đơn giản như trên thì Google chạy vẫn rất ngon với kết quả như sau:

{{< codeblock "ex8.js" "js" >}}
var a=10;var b=a+20;function add(a,b){return a+b}a=add(a,b);
{{< /codeblock >}}

Đoạn đơn giản này thì ta có thể kiểm tra nhanh được, nhưng với các bộ mã nguồn phức tạp và dài như dùng lồng callback chẳng hạn thì việc kiểm tra không hề đơn giản.


## 5.3. Thống nhất style mã nguồn
Cái này hiển nhiên rồi, vì tất cả các lệch đều được kết thúc với (;) làm cho mã nguồn đồng bộ về style hơn. Tất nhiên là với một số bạn thì việc không dùng trông lại cool và pro hơn ^^.

## 5.4. Cận thận với trường hợp function tự thực thi
Trường hợp có function tự gọi thực thi thì rất dễ bị nhầm lẫn như ví dụ sau.

{{< codeblock "ex9.js" "js" >}}
var a = 10
// hàm bất kì nào đó
var fn = function () {
}
// hàm tự thực thi
(function (b) {
    console.log(b)
})(a);
{{< /codeblock >}}

Khi thực thi đoạn mã lệnh này sẽ được trình thông dịch hiểu như sau:

{{< codeblock "ex10.js" "js" >}}
var a = 10;
var fn = function () {
}(function (b) {
    console.log(b);
})(a);
{{< /codeblock >}}

Làm gì có hàm nào lại có định dạng `function() {}()` như thế này nhỉ? Khi chạy đoạn trên sẽ bị lỗi `Uncaught TypeError: undefined is not a function`. Bạn nào không tin có thể thực thi bằng cách chạy trên trình duyện. Có thể dùng [JS Fiddle](https://jsfiddle.net/) chạy cũng OK.

## 5.5. Ghép file
Khi ghép 2 file lại với nhau, chuyện gì xảy ra nếu không có dấu (;)?
Câu trả lời là rất dễ nhầm lẫn vì khi ghép file thường ta ghép điểm cuối file nọ vào đầu file kia trên cùng một dòng và kết quả là 2 lệch cùng 1 dòng mà không có dấu (;) giữa các lệnh. Thậm chí nếu khác dòng thì vẫn có thể dính trường hợp 5.4 phía trên.
Để giải quyết vấn đề này thì ta có thể thêm một lệch rỗng ở đầu file mã nguồn.

{{< codeblock "ex11.js" "js" >}}
; var a = 10
var b = (a < 8) ? a : 8
{{< /codeblock >}}

# 6. Kết luận
Ta nên sử dụng dấu (;) để kết thúc mỗi lệch khi viết mã cho client với các lý do vừa đề cập phía trên. Còn phía server, do đặc điểm không mấy ai thu gọn hay nén file nên ta "có thể" lược bỏ, nhưng cần lưu ý với update file mã nguồn dễ bị xảy ra các trường hợp như 5.4. Mà để đỡ đau đầu và rắc rối thì cứ thêm vào cho chắc ăn.
