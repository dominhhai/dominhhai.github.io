---
title: "[Node.js] Mã hoá mật khẩu với Bcrypt"
slug: nodejs-ecrypt-password-with-bcrypt
date: 2016-02-02
categories:
- Lập Trình
- Node.js
tags:
- Node.js
- Bcrypt
keywords:
- Node.js
- Bcrypt
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //nodejs.org/static/images/logo-hexagon.png
metaAlignment: center
---
Mình không thực sự hiểu nhiều về các thuật toán, kĩ thuật mã hóa mật khẩu. Mình chỉ đọc qua một số phương pháp mã hóa và các lời bình về nó trên mạng và quyết định sử dụng [`bcrypt`](https://en.wikipedia.org/wiki/Bcrypt).
Đọc thì thấy rằng thuật toán này tuy có hơi chậm hơn các thuật toán khác như [`MD5`](https://en.wikipedia.org/wiki/MD5), nhưng đổi lại nó giải quyết được các vấn đề như hack từ điển... của các thuật toán khác do có thể đối phó được với cấp độ tiến hóa của vi xử lý máy tính.
Bạn nào quan tâm thì có thể tìm hiểu thêm ở bài viết [How To Safely Store A Password](http://codahale.com/how-to-safely-store-a-password/) và bài báo khoa học [A Future-Adaptable Password Scheme - 1999 USENIX Annual Technical Conference](https://www.usenix.org/legacy/events/usenix99/provos/provos_html/index.html) này nhé.
Cũng thông qua bài này, mình mong rằng có bạn nào hiểu về kĩ thuật mã hóa có thể chỉ giáo cho mình rõ hơn vì bản thân có tìm hiểu nhưng chẳng hiểu gì :((

Giờ đi vào code thôi ^^.

Vì `bcrypt` không được hỗ trợ trực tiếp trong bộ thư viện mã hóa [`crypt`](https://nodejs.org/dist/latest-v5.x/docs/api/crypto.html) của Node.js nên ta phải sửa dụng gói nodejs bên ngoài.
Qua tìm hiểu mình thấy rằng gói [`bcrypt`](https://github.com/ncb000gt/node.bcrypt.js) này được tìm nhiều người sử dụng và đánh giá cao nên cũng quyết định sử dụng nó.

Đầu tiên là cài gói này ứng dụng đã:

```
npm install bcrypt --save
```

Gói này hỗ trợ cả 2 phương thức là bất đồng bộ và đồng bộ nhưng vì thời gian mã hóa có thể lâu nên phương thức bất đồng bộ được gợi ý sử dụng hơn cả.
Trong bài viết này sẽ đề cập tới cả 2 phương thức đó.

#### Bất đồng bộ

```javascript
const bcrypt = require('bcrypt')

bcrypt.genSalt(10, function (err, salt) {
    bcrypt.hash('B4c0/\/', salt, function (err, hash) {

        console.log(hash)

        // To check a password  
        bcrypt.compare('B4c0/\/', hash, function (err, res) {
            // res == true
            console.log('equal')
            console.log(res)
        })

        bcrypt.compare('not_bacon', hash, function (err, res) {
            // res == false
            console.log('not equal')
            console.log(res)
        })
    })
})

// Auto-gen a salt and hash
bcrypt.hash('bacon', 8, function (err, hash) {
    console.log(`Auto-gen: ${hash}`)
})
```

#### Đồng bộ

```javascript
const bcrypt = require('bcrypt')

var salt = bcrypt.genSaltSync(10)
var hash = bcrypt.hashSync('B4c0/\/', salt)

// To check a password
var res = bcrypt.compareSync('B4c0/\/', hash)   // true
console.log('equal')
console.log(res)

res = bcrypt.compareSync('not_bacon', hash)     // false
console.log('not equal')
console.log(res)

// Auto-gen a salt and hash
var hash = bcrypt.hashSync('bacon', 8)
console.log(`Auto-gen: ${hash}`)
```

2 đoạn mã trên sau khi thực thi sẽ cho kết quả như sau:

```
$2a$08$vj/8fY70VkEmVab/czGJ8euRvsGo0q0T5ETDKUusCXMXytYXeCKkC

equal
true

not equal
false

Auto-gen: $2a$10$LLsJqwOAirlXQW5DVt1pDeyPTWM5qoooqHjkAjA68iIp2mpcCfdZ2
```

Với `bcrypt` ta cần chú ý tới `rounds` (`work factor`) truyền vào để sinh [`salt`](https://en.wikipedia.org/wiki/Salt_(cryptography)). Với `rounds` càng lớn thì càng bảo mật nhưng thời gian xử lý cũng mất [nhiều hơn](https://github.com/ncb000gt/node.bcrypt.js#a-note-on-rounds).
Đơn giản chỉ có vậy thôi.

Để tìm hiểu thêm về các API của gói này bạn có thể tham khảo tại [đây](https://github.com/ncb000gt/node.bcrypt.js).
