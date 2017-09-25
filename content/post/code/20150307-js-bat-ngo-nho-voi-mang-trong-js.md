---
title: "[JS] Bất ngờ nhỏ với mảng"
slug: js-work-with-array
date: 2015-03-07
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
thumbnailImage: //res.cloudinary.com/dominhhai/image/upload/code/js.svg
coverImage: //res.cloudinary.com/dominhhai/image/upload/code/js.svg
metaAlignment: center
---
Từng làm việc với một vài ngôn ngữ lập trình (`Java`, `C`, `C++`, `C#`, `Objective-C`, `PHP`), mỗi ngôn ngữ đều có cái hay riêng. Nhưng khi tiếp xúc với JavaScript (JS) lại tự dưng thấy yêu nó, yêu cái vẻ sexy và bất ngờ của nó. Ví như mảng trong JS rất đặc biệt và bất ngờ. Trong bài này sẽ viết lại một số điểm có thể là bất ngờ với một số người như mình.

### 1. Bạn lấy độ dài của mảng thế nào?

Hôm qua ngồi code lúc lấy độ dài mảng bằng thuộc tính `length` mới thấy khác biệt với phần tử lấy được, làm mình hơi ngạc nhiên một chút. Ngồi đọc lại tài liệu JS, mới thấy dường như nó không có thuộc tính lưu trữ số lượng phần tử hiện hữu (khác `undefined`) trong nó thì phải? Hoặc ít nhất là mình chưa rõ. Có cao thủ nào chỉ giáo cho thì tốt. Các bạn có thể thử đoạn mã sau thì sẽ thấy rằng thuộc tính `length` của mảng sẽ bằng tổng của index lớn nhất của mảng với 1.

{{< codeblock "ex1.js" "js" >}}
var arr = []
arr[10] = 0
arr[20] = 'index 20'
arr['js'] = 'JavaScript'
console.log(arr.length)
{{< /codeblock >}}

Đoạn mã trên sẽ in ra độ dài của mảng arr là 21, tức là bằng index lớn nhất (20) cộng với 1. Hơi bất ngờ chút vì lúc đầu mình nghĩ nó trả ra là 3 (số phần tử khác `undefined`) .

Còn index không phải là dạng số tự nhiên thì có ý nghĩa gì không? Câu trả lời là không có ý nghĩa gì với thuộc tính length cả. Các bạn có thể xem trong ví dụ sau thì sẽ thấy độ dài `length` sẽ không phụ thuộc vào các index không thuộc dạng số tự nhiên.

{{< codeblock "ex2.js" "js" >}}
var arr = []
arr[-1] = 100
arr['js'] = 'JavaScript'
arr['me'] = 'Java Lover'
console.log(arr.length)
{{< /codeblock >}}

Đoạn mã này sẽ luôn in ra 0, chứng tỏ các index không số tự nhiên không ảnh hưởng gì tới thuộc tính `length`.

Vậy câu hỏi đặt ra là làm thế nào để lấy được số phần tử chính xác của một mảng?

Một cách làm đơn giản là duyệt mảng để đếm số lượng các phần tử hiện hữu của mảng đúng không? Thế nhưng mọi chuyện lại không đơn giản như ta nghĩ.

### 2. Bạn duyệt mảng thế nào?

Duyệt mảng trong JS cũng rất thú vị. Cách duyệt mảng thông thường với một mảng là lấy `length` của nó rồi duyệt từ đầu tới cuối như sau.

{{< codeblock "ex3.js" "js" >}}
var arr = []
arr[10] = 0
arr[20] = 'index 20'
arr['me'] = 'Java Lover'
var counter = 0
for (var i = 0, len = arr.length; i < len; i ++) {
    console.log(i + ": " + arr[i])
    if (typeof(arr[i]) != 'undefined')
        counter ++
}
// hoặc như sau
for (var i = arr.length; i > 0; -- i) {
    console.log(i + ": " + arr[i])
    if (typeof(arr[i]) != 'undefined')
        counter ++
}
console.log('The size of array: %d', counter)
{{< /codeblock >}}

Kết quả đoạn mã trên sẽ trả ra các phần từ có index từ 0 ~ 9 và 11 ~ 19 là `undefined`, và counter sẽ là 2.
Như vậy là `counter` không cho ra kết quả chính xác và với một mảng lớn (1000 phần tử chẳng hạn) ta không thể duyệt theo cách này được. Vậy phải có cách khác, ta thử dùng hàm `forEach` của `Array` xem sao.

{{< codeblock "ex4.js" "js" >}}
var arr = []
arr[10] = 0
arr[20] = 'index 20'
arr['me'] = 'XXX Lover'
var counter = 0
arr.forEach(function(ele, i, array) {
    console.log(i + ": " + ele)
    counter ++
})
console.log('The size of array: %d', counter)
{{< /codeblock >}}

Cách này vẫn không ăn thua, kết quả lại như duyệt theo biến length. Thêm một cách duyệt khác là với lệnh `for in` như sau.

{{< codeblock "ex5.js" "js" >}}
var arr = []
arr[10] = 0
arr[20] = 'index 20'
arr['me'] = 'Java Lover'
var counter = 0
for (var i in arr) {
    console.log(i + ": " + arr[i])
    counter ++
}
console.log('The size of array: %d', counter)
{{< /codeblock >}}

Đoạn này lại cho ra kết quả chính xác với từng phần tử được in ra và kích cỡ mảng trả về là 3.

Từ đây ta có thể thấy một điều là nên cẩn thận với biến length của mảng và nên chú ý cách duyệt mảng sao cho hợp lý. Với các dữ liệu liên tục ta hoàn toàn có thể duyệt theo biến `length` hay `Array.forEach`, nhưng dữ liệu cách đoạn và index không là số tự nhiên thì cần theo cách duyệt `for in`.

### 3. Làm sao để biết một biến là mảng?

Các bạn thử chạy đoạn mã sau xem thế nào.

{{< codeblock "ex6.js" "js" >}}
var arr = []
arr[10] = 0
arr[20] = 'index 20'
arr['me'] = 'JavaScript Lover'

console.log("Trust me, men, I'm an Array @@")
console.log("Really, I have to check your DNA.")
console.log("JavaScript checker: arr is " + typeof(arr))
{{< /codeblock >}}

??? Mày là Object mà sao lại bảo là Array?
Không cháu là mảng mà, bác thử kiểm tra với cái máy này xem.

{{< codeblock "ex7.js" "js" >}}
var arr = []
arr[10] = 0
arr[20] = 'index 20'
arr['me'] = 'JavaScript Lover'

console.log("JavaScript checker: Is arr an array ... "
            + (Object.prototype.toString.apply(arr) === "[object Array]"))
{{< /codeblock >}}

Ồ, ồ khỉ thật sao lại thế nhỉ? Đấy cháu dòng giống hoàng tộc nên phải ẩn mình thế đấy. Đúng là nhìn gái xinh thì dễ chứ nhìn gái tốt hay xấu phải có mẹo thật.

Để kết thúc bài, dành tặng cho các bạn beginner về NodeJS một đoạn mã nhỏ. Bài toán đặt ra là lấy nội dung 3 trang web (giao thức http) với địa chỉ nhập từ bàn phím theo dạng bất đồng bộ và in ra nội dung các trang đó theo đúng thứ tự đầu vào nhập từ bàn phím.
Chắc code này không phải giải thích nhiều các bạn cũng sẽ thấy có mối tương quan với nội dung mình vừa viết phía trên.
{{< codeblock "ex8.js" "js" >}}
var http = require('http')
var bl = require('bl')
var data = []
var counter = 0

function printData() {
    for (var i = 0; i< 3; i++)
        console.log(data[i])
}

function loadData(index) {
    http.get(process.argv[2 + index], function(resp) {
        resp.pipe(bl(function(err, buf) {
            if (err)
               data[index] = err.toString()
            else
               data[index] = buf.toString()
            counter ++
           if (counter === 3)
            printData()
        }))
    })
}

for (var i = 0; i < 3; i++)
    loadData(i)
{{< /codeblock >}}
Bài này tạm thời thế, khi nào gặp vấn đề lại update tiếp. Mong các cao thủ biết được gì thêm về mảng trong JavaScript thì chỉ giáo cho các hạ.
