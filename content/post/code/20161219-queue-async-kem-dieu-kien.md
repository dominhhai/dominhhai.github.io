---
title: "[JS] Async Queue kèm điều kiện"
slug: js-conditional-async-queue
date: 2016-12-19
categories:
- Lập Trình
- JS
tags:
- JS
- Conditional Queue
keywords:
- JavaScript
- Conditional Queue
- Async Queue
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //lh3.googleusercontent.com/gsMKQt7DZQVs0NJJihKmR3zR-g5y-CBOH0v6IC1W7U6gQx0u5IxiQVrwNbhjAdkFbqWMTBzJRSSZln-w441biwoAMiDkj17CHRxFqUkuaWzTungp8YHS374z8BvCfPxfg91EZmZ78A=w785-h340-no
metaAlignment: center
---
Có lẽ nhiều người đã từng sử dụng [queue](https://caolan.github.io/async/docs.html#queue) hoặc [priority queue](https://caolan.github.io/async/docs.html#priorityQueue) của async để thực thi danh sách các tác vụ 1 lần. Nhưng nếu để ý thì ta có thể nhận thấy thư viện này không hỗ trợ việc thiết lập điều kiện thực thi cho từng tác vụ riêng biệt, mà chỉ đơn giản là có tác vụ thì sẽ chạy. Điều này làm nảy sinh vấn đề là thiếu sự đồng bộ khi cần thực thi một loạt các tác vụ có liên quan nhau. Ví dụ như thực thi các tác vụ tại một điểm thời gian nào đó, ta có thể mô phỏng như sau:

   * Sử dụng hàng đợi ưu tiên với số tác song song là 1
   * Bây giờ là 9:00:00
   * Cho tác vụ J1 chạy lúc 12:00:00 vào hàng đợi
   * Cho tác vụ J2 chạy lúc 9:10:00 vào hàng đợi

Lúc này J1 sẽ được lấy ra khỏi hàng đợi và thực thi lúc 12:00:00 nên hàng đợi của ta sẽ phải chờ ít nhất là sau 12 giờ mới có thể thực thi các tác vụ còn lại. Hay nói cách khác là tác vụ J2 sẽ phải thực thi sau 12 giờ. Như vậy là không còn đúng với mong muốn khi chạy lúc 9 giờ 10 phút nữa rồi.

Vậy có cách nào để giải quyết bài toán này? Tôi chọn cách đặt điều kiện thực thi cho các tác vụ. Tác vụ chỉ được thực thi khi và chỉ khi thỏa mãn điều kiện được đưa ra. Ví dụ như ở tình huống trên, tất cả các tác vụ chỉ được thực thi trước khi trước thời gian chạy 1 phút. Với 1 phút như vậy các tác vụ cùng thời gian, hoặc chênh lệch nhau 1 phút cũng sẽ phải chờ tác vụ đang thực thi thực hiện xong. 1 phút đó gần như không đáng gì so với 3 tiếng đồ hồ ^.^

Mình cũng đã tạo issue trên Github của dự án này nhưng có vẻ như không được ủng hộ nên quyết định bóc tách code ra làm theo cách của mình. Với đặc điểm mình chỉ cần sử dụng phía máy chủ nên đã bỏ đi tất cả các phụ thuộc của dự án và viết lại từ đâu những vẫn đảm bảo logic cũ và thêm logic điều kiện thực thi. Cụ thể hơn có thể xem mã nguồn trên [Github](https://github.com/dominhhai/job-schedule).

Ok, giờ tới lúc cách sử dụng rồi.

### 1. Cài đặt
```shell
$ npm i -S job-schedule
```

### 2. API
```javascript
const Queue = require('job-schedule')

// tham số và giá trị trả gia hệt như `priorityQueue`
let q = new Queue(worker, concurrency)

// chỉ định điều kiện thực thi tác vụ.
// tác vụ được thực thi khi hàm trả ra `true`
// nếu không, ta cần resume lại queue quét lại các tác vụ thực thi
// bằng cách gọi tới `cb`
q.when = function (node, cb) {
  if (someConditions(node)) {
    return true
  }
  doSomething(() => cb())
}
```

### 3. Ví dụ
```javascript
const Queue = require('job-schedule')

var timerId = null
var q = new Queue((task, cb) => {
  console.log('priority:hello', task.name)
  cb()
}, 1)

q.when = function (node, cb) {
  // start task if it's priority less than 2
  if (node.priority -- < 2) {
    clearTimeout(timerId)
    console.log('start:', node.data.name)
    return true
  }
  // resume queue after 1s
  timerId = setTimeout(cb, 1000)
}

// call when all tasks finished
q.drain = function () {
  console.log('all items have been processed')
}

// add some items to the queue
q.push({name: 'foo'}, 10, function (err) {
  console.log('finished processing foo', err)
})
q.push({name: 'bar'}, 2, function (err) {
  console.log('finished processing bar', err)
})

// add some items to the queue (batch-wise)
q.push([{name: 'baz'}, {name: 'bay'}, {name: 'bax'}], 6, function (err) {
  console.log('finished processing item', err)
})
```
