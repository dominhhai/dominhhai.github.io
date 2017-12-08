---
title: "[JS] Hiểu thế nào cho đúng về biến this"
slug: js-what-is-this
date: 2015-03-21
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
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/js.svg
metaAlignment: center
---
JavaScript (JS) là một ngôn ngữ lập trình khá linh hoạt và thú vị. Nhưng để có được điều đó nó cũng mang tới không ít phiền phức, dễ nhầm lẫn với những người không chuyên. Với những người mới sờ vào JS, họ thường nghĩ ngay chắc JS cũng lơ lớ như các ngôn ngữ lập trình khác như Java hay C#. Nhưng nhiều điểm ở JS lại khá khác với suy nghĩ ở các ngôn ngữ khác gây nên những hiểu lầm cho người mới vào nghề. Một trong những điểm dễ nhầm lẫn đó là biến `this` vì trong JS nó không chỉ đơn giản là đại diện cho đối tượng hiện thời như các ngôn ngữ lập trình hướng đối tượng khác. Cụ thể ra sao ta cùng nhau xem xét ở bài viết này.

{{< codeblock "test1.js" "js" >}}
// app.js
// câu hỏi vui: Đoán kết quả lệnh (1) và lệnh (2) :cười:
var obj = {
    mMethod: function() {
        console.log(this)
    }
}

obj.mMethod(); // (1)

var _mMethod = obj.mMethod;
_mMethod();  // (2)
{{< /codeblock >}}

Đọc tới đây chắc một số bạn biết về `this` rồi sẽ bật cười là sao lại viết là biến `this`. Nếu bạn nghĩ tới mức đó thì xin chúc mừng bạn, bạn đã đúng. __this__ trong JS __là__ một __từ khoá__ chứ không phải là một biến nào cả. Bạn không thể gắn giá trị trực tiếp cho `this` được cũng như chẳng thể nào `delete` nó đi. Vậy từ khoá này có gì lại rắc rối vậy?

<!--toc-->

# 1. Bản chất của từ khoá `this`

Các đoạn mã của JavaScript được thực thi trong một ngữ cảnh nhất định (Execution Context). Các ngữ cảnh này lại được sắp xếp để thực hiện chương trình một cách tuần tự. Bạn có thể tưởng tượng thế này, mỗi ngữ cảnh chứa một số đoạn mã nhất định, và toàn chương trình của ta sắp xếp các ngữ cảnh này vào một ngăn xếp (stack). Sau đó các ngữ cảnh sẽ được gọi ra thực thi dần cho tới hết, tức là ngữ cảnh trên đỉnh của ngăn xếp sẽ chứa các đoạn mã sẵn sàng chạy.

Mỗi ngữ cảnh thực thi này có tương ứng một `ThisBinding` có giá trị không đổi đại diện cho ngữ cảnh thực thi đó. Và từ khoá `this` sẽ bằng giá trị `ThisBinding` trong ngữ cảnh đang thực thi hiện thời. Như vậy `this` sẽ đại diện cho ngữ cảnh đang thực thi và nó cần được đánh giá lại tham chiếu khi ngữ cảnh thực thi thay đổi.

Có 3 kiểu ngữ cảnh thực thi là toàn cục (global), eval và hàm (function). Global là ngữ cảnh ở mức trên cùng của toàn bộ chương trình, tức là nó chứa các đoạn mã không nằm trong function hay được gọi bởi eval và global sẽ là ngữ cảnh thực thi chương trình mặc định. Eval là ngữ cảnh chứa các mã được gọi bởi hàm <a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/eval" title="eval" target="_blank"_ rel="noopener noreferrer">`eval`</a>. Còn function là các đoạn mã nằm trong một function nào đó. Ta sẽ xem chi tiết từng ngữ cảnh thực thi qua phần dưới đây.

# 2. Các ngữ cảnh thực thi
## 2.1. Toàn cục - Global
Là ngữ cảnh thực thi nằm ở trên cùng của ngăn xếp ngữ cảnh, tức là ngữ cảnh đầu tiên thực thi chương trình. Ví dụ trong các mã thực thi phía máy khách trong trang web thì ngữ cảnh toàn cục này nằm ngay sau thẻ . Trong ngữ cảnh toàn cục này thì `ThisBinding` sẽ được thiết lập giá trị là đối tượng toàn cục (Global Object). Trong Nodejs thì đối tượng toàn cục là đối tượng toàn cục của Nodejs - khởi đầu là một đối tượng trống, trong trình duyệt thì nó là đối tượng window, nhưng cần chú ý là nếu ở trong chế độ <a href="https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Strict_mode" title="strict mode" target="_blank"_ rel="noopener noreferrer">`strict mode`</a> thì đối tượng toàn cục là `undefined`. Ta có thể cùng nhau xem xét ví dụ dưới đây.

{{< codeblock "test2.js" "js" >}}
console.log(this) // đối tượng toàn cục trong ngữ cảnh toàn cục

this.mX = "I love JavaScript" // sử dụng đối tượng toàn cục

console.log(this.mX) // in ra giá trị của thuộc tính mX

var obj = {
    mMethod: function() {
        console.log(this) // in ra giá trị this hiện thời
    }
}

obj.mMethod() // không còn là đối tượng toàn cục nữa
{{< /codeblock >}}

## 2.2. Gọi mã - Eval
Với trường hợp sử dụng hàm `eval` ta phân làm 2 trường hợp.
### 2.2.1. Gọi eval trực tiếp
Gọi `eval` trực tiếp là ta gọi trực tiếp hàm `eval` như ví dụ bên dưới. Với trường hợp này thì `ThisBinding` sẽ được gắn giá trị là ngữ cảnh gốc của đoạn mã đó.

{{< codeblock "test3.js" "js" >}}
function callMe() {
    console.log(this)
}

var obj = {
    callMe: function() {
        console.log(this)
    }
}

eval("callMe()")     // đối tượng toàn cục

eval("obj.callMe()") // đối tượng obj
{{< /codeblock >}}

### 2.2.2. Gọi eval gián tiếp
Gọi `eval` gián tiếp là ta gọi hàm `eval` thông qua một biến được gắn giá trị tương ứng như truyền hàm `eval` qua tham số hàm khác hoặc gắn nó với một biến nào đó. Với trường hợp này thì `ThisBinding` sẽ được gắn giá trị là ngữ toàn cục.

{{< codeblock "test4.js" "js" >}}
// this trong mã thực thi của eval sẽ là đối tượng toàn cục
this.callMe = function () {
    console.log("callMe in Global Object")
}

var obj = {
    callMe: function() {
        console.log(this)
    },
    callMe2: function(evalFn) {
        evalFn("console.log(this)")
        evalFn("callMe()")
    }
}

obj.callMe2(eval) // gọi gián tiếp eval qua tham số hàm

var mEval = eval // gắn eval với một biến

mEval("console.log(this)") // gọi gián tiếp eval qua biến mEval
{{< /codeblock >}}

## 2.3. Hàm - Function
Khi hàm được gọi thì ngữ cảnh thực thi của nó sẽ phụ thuộc vào tham số đầu vào và ngữ cảnh gọi nó. Giả sử hàm của ta là F, với tham số là argumentsLits, và ngữ cảnh gọi F tương ứng với thisValue. Việc xác định `thisBinding` được xác định như sau:

> 1. If hàm trong chế độ strict, ThisBinding được gắn là thisValue.
> 2. Else if thisValue là null hoặc undefined, ThisBinding được gắn là đối tượng toàn cục.
> 3. Else if Type(thisValue) không là Object, ThisBinding được gắn là ToObject(thisValue).
> 4. Else ThisBinding được gắn là thisValue

Xem thêm về cách gắn `thisBinding` <a href="http://es5.github.io/#x10.4.3" title="Entering Function Code" target="_blank"_ rel="noopener noreferrer">ở đây</a>.

Để rõ ràng hơn ta xét một số tình huống cụ với việc gọi hàm.
### 2.3.1. Gọi thông qua ngữ cảnh toàn cục
Trường hợp này `this` sẽ tham chiếu tới đối tượng toàn cục.

{{< codeblock "test5.js" "js" >}}
function mMethod() {
    console.log(this) // đối tượng toàn cục - global object
}

mMethod();

var obj = {
    myMethod: function() {
        return (function(){
            console.log(this) // đối tượng toàn cục
        })();
    }
}

obj.myMethod()
{{< /codeblock >}}

### 2.3.2. Gọi thông qua đối tượng
Trường hợp này `this` sẽ tham chiếu tới đối tượng thisValue - đối tượng tương ứng chứa hàm.

{{< codeblock "test6.js" "js" >}}
// Tạo đối tượng obj
var obj = {
    mMethod: function() {
        console.log(this)
    },
    oMethod: function() {
        console.log('▼ oMethod')
        console.log(this)
        console.log('▲  oMethod')
    }
}

obj.mMethod()    // this sẽ tương ứng với đối tượng obj
obj['oMethod']() // this sẽ tương ứng với đối tượng obj

// Gắn mMethod cho đối tượng khác
var obj1 = {
    mVal: "I'm obj1"
}
obj1.mMethod = obj.mMethod;

obj1.mMethod() // this sẽ tương ứng với đối tượng obj1

// Gọi qua khởi tạo đối tượng với từ khoá new
function MyObject(val) {
    this.mVal = val || "I xxx JS";

    this.mMethod = function() {
        console.log(this)
    };
}

var mObj1 = new MyObject()
var mObj2 = new MyObject("I'm object 2")

mObj1.mMethod() // this sẽ tương ứng với đối tượng mObj1
mObj2.mMethod() // this sẽ tương ứng với đối tượng mObj2
{{< /codeblock >}}

### 2.3.3. Gọi thông qua một số hàm đặc biệt
Trong JavaScript có xây dựng sẵn một số hàm đặc biệt cho phép ta sử dụng `this` qua đối tượng đầu vào như:

* Function.prototype.apply(thisArg, argArray)
* Function.prototype.call(thisArg[, arg1[ , arg2, ...]])
* Function.prototype.bind( thisArg[, arg1[ , arg2, ...]])
* Array.prototype.every(callback[, thisArg])
* Array.prototype.some(callback[, thisArg])
* Array.prototype.forEach(callback[, thisArg])
* Array.prototype.map(callback[, thisArg])
* Array.prototype.filter(callback[, thisArg])

Bằng việc sử dụng các hàm trên ta có thể thể sử dụng `this` như là giá trị của đối tượng `thisArg`. Việc này rất tiện cho ta thay đổi `thisBinding` một cách chủ động. Ta có thể xem ví dụ sau:

{{< codeblock "test7.js" "js" >}}
var obj = {
    mMethod: function(firstName, lastName) {
        var firstName = firstName || "Vô"
        var lastName = lastName || "Danh"
        console.log("Hello " + firstName + " " + lastName)
        console.log(this)
    }
}

var obj1 = {
    mVal: "I'm obj1"
};

obj.mMethod.apply(obj1) // đối tượng obj1

obj.mMethod.apply(obj1, ["Chí", "Phèo"]) // đối tượng obj1

obj.mMethod.call(obj1, "Thị", "Nở") // đối tượng obj1
{{< /codeblock >}}

Đoạn mã trên sẽ in ra `this` là đối tượng `obj1` chứ không còn là `obj`, do `call` và `apply` đã đẩy trực tiếp `this` qua tham số đầu vào.

# 3. Một số trường hợp dễ nhầm lẫn

## 3.1. Gọi thông qua ngữ cảnh khác
Ta xét trường hợp sau:

{{< codeblock "test8.js" "js" >}}
var obj = {
    mVal: "Việt Nam",

    mMethod: function() {
        console.log("Hello " + this.mVal)
    }
}

var oMethod = obj.mMethod // oMethod nằm trong ngữ cảnh toàn cục

oMethod()
{{< /codeblock >}}

Khi thực hiện đoạn mã trên kết quả in ra sẽ là `Hello undefined`, vì ta đã đẩy `this` ra đối tượng toàn cục mất rồi. Vậy làm sao để có được đúng kết quả là `Hello Việt Nam`? Để giải quyết được cái này ta sẽ sử dụng hàm `bind` để đẩy giá trị đối tượng `obj` cho biến `this` ở đây như sau:

{{< codeblock "test9.js" "js" >}}
var obj = {
    mVal: "Việt Nam",

    mMethod: function() {
        console.log("Hello " + this.mVal)
    }
}

var oMethod = obj.mMethod.bind(obj) // this trong oMethod sẽ bị ép thành giá trị obj

oMethod()
{{< /codeblock >}}

Vì sao lại là `bind` mà không phải là `call` hay `apply`? Vì `bind` sẽ giữ giá trị của `obj` để gọi nhiều lần chứ không chỉ gọi một lần như với `call` hay `apply`. Các bạn có thể đọc thêm <a href="/vi/2015/03/js-how-apply-call-bind/" title="[JS] apply, call và bind khác gì nhau?" target="_blank"_ rel="noopener noreferrer">ở đây</a>.
Với trường hợp gọi một lần với `call` hoặc `apply` ta có thể cùng nhau xem ví dụ sau:

{{< codeblock "test10.js" "js" >}}
var obj = {
    mVal: "Việt Nam",

    mMethod: function() {
        console.log("Hello " + this.mVal)
    }
}

var obj1 = {
    mVal: "Nhật Bản"
}

obj.mMethod.call(obj1) // in ra là: Hello Nhật Bản
{{< /codeblock >}}

Đoạn mã trên sẽ gọi hàm `mMethod` của đối tượng `obj` nhưng `this` trong hàm `mMethod` đã được ép thành đối tượng `obj1`. Với việc gọi 1 lần này ta có thể mượn phương thức `mMethod` của đối tượng `obj` để thực thi cho đối tượng `obj1` mà không cần tạo phương thức này cho đối tượng `obj1`. Cái này khá <em>kool</em> đúng hem ^.^

## 3.2. Hàm phản hồi - Callback
Gọi thông qua hàm phản hồi cũng chính là một trường hợp của gọi thông qua ngữ cảnh khác vì hàm phản hồi được thực thi trong một ngữ cảnh khác. Ta xét ví dụ sau:

{{< codeblock "test11.js" "js" >}}
var obj = {
    mVal: "Việt Nam",

    mMethod: function() {
        console.log("Hello " + this.mVal)
    }
}

var obj1 = {
    oMethod: function(callback) {
        return callback();
    }
}

obj1.oMethod(obj.mMethod)
{{< /codeblock >}}

Vì gọi trong ngữ cảnh của đối tượng `obj1` nên `mMethod` lúc này sẽ lấy giá trị cho `this` là `obj1` chứ không còn là `obj` nữa. Vẫn làm tương tự như phần 3.1, ta sử dụng `bind` để đẩy giá trị ngữ cảnh `obj` vào cho `mMethod` như sau:

{{< codeblock "test12.js" "js" >}}
var obj = {
    mVal: "Việt Nam",

    mMethod: function() {
        console.log("Hello " + this.mVal)
    }
}

var obj1 = {
    oMethod: function(callback) {
        return callback();
    }
}

obj1.oMethod(obj.mMethod.bind(obj))
{{< /codeblock >}}

Hoàn hảo, đoạn mã trên đã cho ta kết quả như mong muốn. Đọc tới đây, nhiều bạn thắc mắc sao cần gì phải tách ra 3.1 với 3.2 làm gì cho rắc rối? Tách ra thế này có lợi thế là không bị vướng quá nhiều vấn đề vào cả một cụm, ví hàm phản hồi là một trường hợp rất hay được sử dụng khi lập trình với JavaScript. Ví dụ như trong Nodejs, hàm phản hồi là một thành phần quan trọng, một khái niệm cơ bản nhất cần nắm được để có thể lập trình với Nodejs. Hay nhiều bạn có sử dụng JQuery để làm phía trình duyệt, các sự kiện `click` vào một nút nào đó chẳng hạn, các bạn đều sử dụng luôn được từ khoá `this` ngay trong hàm phản hồi của các nút đó mà không cần quan tâm tới ngữ cảnh thực thi hiện tại là gì cả. Để làm được việc đó, jQuery đều đã `bind` các nút tương ứng đó cho các hàm phản hồi cho các bạn rồi đó.

## 3.3. Hàm lồng nhau
Ta cùng xét sự nhập nhằng qua ví dụ sau.

{{< codeblock "test13.js" "js" >}}
var obj = {
    mVal: "Việt Nam",

    oVal: {
        oMethod: function(callMe) {
            callMe()
        }
    },

    mMethod: function() {
        this.oVal.oMethod(function() {
            console.log("Hello " + this.mVal)
        })
    }
}

obj.mMethod() // in ra là: Hello undefined
{{< /codeblock >}}

Với đoạn mã trên ta mong muốn nó in ra được giá chỉ của biến mVal trong đối tượng obj nhưng thực tế nó sẽ in ra `Hello undefined`? Nguyên nhân là ngữ cảnh của thực thi ở `console.log` lúc này là đối tượng `oVal` mất rồi. Vậy làm sao ta có thể sử dụng được biến `mVal` của đối tượng `obj`? Muốn làm được như vậy ta cần lấy được ngữ cảnh thực thi của đối tượng `obj` bằng cách nhớ lại ngữ cảnh thực thi thông qua một biến trung gian và sử dụng biến này với ngữ cảnh của đối tượng `oVal`. Ví dụ dưới đây sẽ thực hiện theo ý tưởng này:

{{< codeblock "test14.js" "js" >}}
var obj = {
    mVal: "Việt Nam",

    oVal: {
        oMethod: function(callMe) {
            callMe()
        }
    },

    mMethod: function() {
        var this_ = this; // nhớ ngữ cảnh thực thi của obj trong biến this_

        this.oVal.oMethod(function() {
            console.log("Hello " + this_.mVal) // gọi tới ngữ cảnh thực thi của obj
        })
    }
}

obj.mMethod()
{{< /codeblock >}}

# 4. Kết luận

Từ khoá `this` hơi rắc rối một chút nên khi lập trình ta cần chú ý tới ngữ cảnh thực thi để sử dụng từ khoá này cho hiệu quả và đúng đắn dựa vào ngữ cảnh gọi nó và kiểu của ngữ cảnh thực thi. Ta cũng cần chú ý hơn ở những đoạn sử dụng tới hàm phản hồi hay hàm lồng nhau. Ngoài ra ta có thể thay đổi được ngữ cảnh thực thi của một đối tượng bằng cách sử dụng `call`, `apply` hoặc `bind` như đã mô tả phía trên.

Về việc sử dụng Call, Apply và Bind cụ thể ra sao thì các bạn đọc thêm ở [bài viết này](/vi/2015/03/js-how-apply-call-bind/ "[JS] apply, call và bind khác gì nhau?").

Ngoài ra, bạn có thể tham khảo về chuẩn ECMAScript 5.1 <a href="http://es5.github.io" title="Entering Function Code" target="_blank"_ rel="noopener noreferrer">ở đây</a>.
