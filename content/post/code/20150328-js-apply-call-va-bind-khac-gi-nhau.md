---
title: "[JS] Apply, Call và Bind khác gì nhau?"
slug: js-how-apply-call-bind
date: 2015-03-28
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
thumbnailImagePosition: left
thumbnailImage: //res.cloudinary.com/dominhhai/image/upload/code/js.svg
metaAlignment: center
---
Như trong bài về [từ khóa `this`](https://dofeet.wordpress.com/2015/03/07/js-hieu-the-nao-cho-dung-ve-bien-this-trong-javascript/) đã đề cập tới ngữ cảnh thực thi với mối tương quan tới từ khóa `this` và việc thay đổi được ngữ cảnh thực thi một cách trực tiếp bằng cách sử dụng `call`, `apply` và `bind`, thì bài viết này sẽ làm rõ ràng hơn 3 phương thức này và sự khác nhau cũng như tính hữu dụng của nó.

Về cơ bản `call` và `apply` gần giống nhau và được giới thiệu từ phiên bản 3 theo chuẩn ECMAScript, còn `bind` được giới thiệu từ phiên bản 5 thì lại khác hẳn về bản chất nhưng cũng có mối quan hệ mật thiết với 2 phương thức kia. Vậy nên trong bài này ta sẽ đi dần từ `call` với `apply` tới `bind`.

### 1. Call và Apply
Cú pháp:

* call()
> Function.prototype.call(thisArg[, arg1[ , arg2, …]])

* apply()
> Function.prototype.apply(thisArg, argArray)

Phương thức `call()` và `apply()` để ***gọi thực thi*** một hàm với một ngữ cảnh chỉ định thông qua tham số `thisArg` và các tham số đầu vào của hàm tương ứng. Tức là nó sẽ cho phép hàm thực thi được với một ngữ cảnh chỉ định nào đó tuỳ ý. Sự khác nhau giữa chúng là `call()` sẽ nhận tham số hàm qua từng biến đầu vào riêng biệt còn `apply()` thì lại nhận các tham số hàm qua một mảng chứa các biến đầu vào. Ta cùng xét ví dụ bên dưới:

```javascript
var obj = {
    firstName: "Vô",
    lastName : "Danh",

    mMethod: function(firstName, lastName) {
        var firstName = firstName || this.firstName
        var lastName = lastName || this.lastName
        console.log("Hello " + firstName + " " + lastName)
    }
}

var obj1 = {
    firstName: "Ông",
    lastName : "Ké"
};

obj.mMethod() // Hello Vô Danh

obj.mMethod.call(obj1) // Hello Ông Ké

obj.mMethod.apply(obj1) // Hello Ông Ké

obj.mMethod.call(obj1, "Thị", "Nở") // Hello Thị Nở

obj.mMethod.apply(obj1, ["Chí", "Phèo"]) // Hello Chí Phèo
```

Với đoạn mã trên ta có thể thấy rằng, sau khi gọi `call()` hoặc `apply()` ngữ cảnh thực thi của `mMethod` đã được đổi sang `obj1` và `call()` cho phép ta truyền tham số đầu vào riêng biệt còn `apply()` lại cho phép truyền vào như một mảng.

Từ phiên bản 5, `apply()` còn có thể được truyền vào một đối tượng tựa mảng (chú thích [1]) thay vì mảng:

```javascript
var obj = {
    firstName: "Vô",
    lastName : "Danh",

    mMethod: function(firstName, lastName) {
        var firstName = firstName || this.firstName
        var lastName = lastName || this.lastName
        console.log("Hello " + firstName + " " + lastName)
    }
}

var obj1 = {
    firstName: "Ông",
    lastName : "Ké"
};

obj.mMethod.apply(obj1, ["Chí", "Phèo"]) // Hello Chí Phèo

obj.mMethod.apply(obj1, {'length': 2, '0': "Chí", '1': "Phèo"}) // Hello Chí Phèo

```

Với việc sử dụng `call()` hoặc `apply()` ta có thể làm được rất nhiều việc hay ho như sử dụng phương thức của một ngữ cảnh khác như ở ví dụ trên, hay đẩy ngữ cảnh thực thi cho hàm phản hồi hoặc thay đổi cách truyền tham số hàm rất hiểu quả. Các bạn có thể xem ở ví dụ sau:

* Truyền ngữ cảnh thực thi cho hàm phản hồi

```javascript
function print() {
    console.log(this.mVal)
}

var obj = {
    mVal: "Tôi yêu thành phố Hồ Chí Minh",

    mMethod: function(callback) {
        // truyền đối tượng hiện tại cho hàm phản hồi callback
        callback.call(this)
    }
}

obj.mMethod(print)
```

* Thay đổi cách truyền tham số hàm
```javascript
// Math.min([value1[,value2[, ...]]])
// Ta sử dụng mảng cho tham số đầu vào thay vì các giá trị rời rạc
console.log (Math.min.apply(null, [100, -1, 8, 219])) // -1
```

Cũng không tồi đấy chứ, bằng `call`, `apply` ta có thể linh hoạt hơn khi lập trình, đỡ được nhiều công sức biến đổi rắc rối và tận dụng được mã nguồn rất hiệu quả.

### 2. Bind
Cú pháp:

> Function.prototype.bind( thisArg[, arg1[ , arg2, …]])

Phương thức `bind()` sẽ ***tạo*** ra một ***hàm mới*** có nội dung thực thi như hàm được gọi nhưng được gắn với một ngữ cảnh thực thi chỉ định qua tham số `thisArg`. Như vậy khác với `call()` và `apply()`, `bind()` sẽ không gọi để thực thi hàm mà sẽ lưu lại ngữ cảnh thực thi cho một hàm nào đó như ví dụ sau:

```javascript
var obj = {
    mVal: "Việt Nam",

    mMethod: function() {
        console.log("Hello " + this.mVal)
    }
}

var oMethod = obj.mMethod.bind(obj) // this trong oMethod sẽ bị ép thành giá trị obj

oMethod() // Hello Việt Nam

obj.mVal = "Hà Nội"

oMethod() // Hello Hà Nội
```

Như vậy khác với `call()` và `apply()`, khi gọi `bind()` hàm sẽ không thực thi ngay mà chỉ gắn ngữ cảnh thực thi cho phương thức mMethod. Vì `mMethod` được gắn với ngữ cảnh đối tượng `obj`, nên mỗi lần thực thi nó sẽ sử dụng `this` như là đối tượng `obj`. Như trong ví dụ phía trên, sau khi ta thay đổi giá trị của biến `mVal` trong đối tượng `obj` thì `mMethod` cũng sẽ in ra giá trị đã bị thay đổi.

Về bản chất thì `bind()` có thể được thực hiện như sau:
```javascript
Function.prototype.bind = function(context) {
    var _this = this;
    return function() {
        _this.apply(context, arguments);
    };
};
```
Bằng việc sử dụng `apply()`, ta có thể thay đổi ngữ cảnh thực thi cho một hàm, còn để lưu lại ngữ cảnh dành cho việc thực thi sau này ta tạo ra một hàm mới như trong đoạn mã trên.

Vì tính chất lưu lại được ngữ cảnh nên `bind()` rất hay được sử dụng với hàm phản hồi như xử lý sự kiện click vào một nút nào đó chẳng hạn. Ví dụ như khi sử dụng jQuery, ta có thể lấy được giá trị cho `this` bằng `button` trong các hàm phản hồi của sự kiện `click` vào một `button` vì jQuery đều đã buộc (bind) sẵn `button` cho hàm phản hồi được truyền vào.

```html
<!DOCTYPE html>
<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script>
$(document).ready(function(){
    $("#btn").click(function(){
        console.log(this)
        $(this).text(Number($(this).text()) + 1)
    });
});
</script>
</head>
<body>
    <button id="btn">0</button>
</body>
</html>
```

Ngoài ra, ta có thể làm được rất nhiều việc khá hay ho như tạo shortcut cho hàm nào đó, hay nhóm lại các tham số theo từng cụm như ví dụ bên dưới:

```javascript
var obj = {
    firstName: "Thánh",
    lastName: "Gióng",

    mMethod: function(hello, firstName, lastName) {
        var hello = hello || "Hello"
           ,firstName = firstName || this.firstName
           ,lastName = lastName || this.lastName

        console.log(hello + " " + firstName + " " + lastName);
    }
}

// tạo shortcut
var print = obj.mMethod.bind(obj)
print()

var print = obj.mMethod.bind(obj, "Hello", "Mr", "Bean")
print()

// Nhóm theo hello
print = obj.mMethod.bind(obj, "Xin chào bạn")
print()

// Nhóm theo firstName
print = obj.mMethod.bind(obj, "Kính chào ngài", "Nguyễn")
print("Trãi")
print("Xiển")
```

### 3. Vui vẻ tý
Như bên trên đã phân tích, khi ta cần thực thi một function cho một ngữ cảnh khác, ta cần sử dụng `call`, `apply` hoặc `bind`, nhưng có một cách vượt mặt để không cần sử dụng nó. Bạn có thể xem ví dụ sau:

```javascript
var obj = {
    firstName: "Vô",
    lastName : "Danh",

    mMethod: function(firstName, lastName) {
        var firstName = firstName || this.firstName
        var lastName = lastName || this.lastName
        console.log("Hello " + firstName + " " + lastName)
    }
}

var obj1 = {
    firstName: "Ông",
    lastName : "Ké"
};

obj.mMethod.apply(obj1) // Hello Ông Ké

// vượt mặt ở đây
var method = Function.call.bind(obj.mMethod)

method(obj1) // Hello Ông Ké

// vượt mặt trong prototype của object
method = Function.call.bind(Array.prototype.slice)

console.log(method([100, 20, 40], 1)) // [20, 40]
```

Với đoạn mã trên, ta có thế thấy rằng khi gọi `method` ta không cần phải gọi `call`, `apply` hay `bind` ra nữa mà chỉ cần đẩy trực tiếp đối tượng cần gọi và tham số vào là đủ. Khá hay ho đấy chứ? gọi `call`, `apply`, `bind` mãi cũng chán, overcome một tý thấy nó tiện hơn hẳn.

Ta có thể làm được như vậy là vì tất cả các function trong JavaScript đều kế thừa từ đối tượng `Function.prototype`, nên hiển nhiên nó có tất cả các function được định nghĩa từ `Function.prototype` như `call`, `apply` hay `bind`. Như vậy, ta hoàn toàn có thể gọi được các phương thức kế thừa này từ một function bất kì.

Với ví dụ trên, ta coi `obj.mMethod` là một đối tượng cần gọi tới phương thức `call` thì ta hoàn toàn có thể tạo một phương thức `method` trực tiếp từ phương thức `call` mà đã được gắn `thisVal` bằng `obj.mMethod`: `Function.call.bind(obj.mMethod)` hoặc `Function.prototype.call.bind(obj.mMethod)`. Hay nói cách khác, phương thức `method` mới được tạo ra có nội dung giống như phương thức `call` và đối tượng chứa nó (gọi nó - `this`) là đối tượng `obj.mMethod` nên `method()` ~ `obj.mMethod.call()`.

### 4. Kết luận
Bằng việc sử dụng `call`, `apply` và `bind` ta có thể thay đổi được ngữ cảnh thực thi (phạm vi chứa hàm) để sử dụng một hàm với công dụng đa năng hơn như thực thi cho một đối tượng, phạm vi khác khác giúp ta có thể tận dụng tối đa mã nguồn được đã tạo ra, hay tạo shortcut cho hàm, linh hoạt hơn tham số đầu vào. Với `call` và `apply` chúng ta sử dụng để thực thi hàm đó luôn khi gọi, còn với `bind` ta có thể thực thi hàm đó nhiều lần sau khi đã được buộc (bind) với một ngữ cảnh nhất định.

***Chú thích***
[1] đối tượng tựa mảng: Một đối tượng tựa mảng (array-like object) là một đối tượng có các thuộc tính là số tự nhiên và có một thuộc tính bắt buộc là `length` có giá trị bằng số các thuộc tính là số tự nhiên. Ví dụ: `{length: 3, 0: "Tôi", 1: "là", 2: "người Việt"}` hoặc `{'length': 3, '0': "Tôi", '1': "là", '2': "người Việt"}`.
