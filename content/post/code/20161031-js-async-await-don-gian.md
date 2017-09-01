---
title: "[JS] Async Await cực đơn giản"
slug: js-async-await-is-simple
date: 2016-10-31
categories:
- Lập Trình
- JS
tags:
- JS
- JS Tips
- ES2017
keywords:
- JavaScript
- JS
- ES2017
- ES6
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //lh3.googleusercontent.com/gsMKQt7DZQVs0NJJihKmR3zR-g5y-CBOH0v6IC1W7U6gQx0u5IxiQVrwNbhjAdkFbqWMTBzJRSSZln-w441biwoAMiDkj17CHRxFqUkuaWzTungp8YHS374z8BvCfPxfg91EZmZ78A=w785-h340-no
metaAlignment: center
---
### 1. Giới thiệu

Với các đặc tả JavaScript cũ, ta phải sử dụng các hàm phản hồi để xử lý các thao tác bất đồng bộ. Tuy nhiên việc này dẫn tới tình trạng [callback hell](https://stackoverflow.com/questions/25098066/what-is-callback-hell-and-how-and-why-rx-solves-it) khi ta có nhiều thao tác bất đồng bộ phải chờ nhau thực hiện. Call hell làm cho mã nguồn của ta rất rối và khó bảo trì.

```javascript
function wait(ms, cb) {
  setTimeout(cb, ms)
}

function main() {
  console.log('sắp rồi...')
  wait(2007, () => {
    console.log('chờ tí...')
    wait(2012, () => {
      console.log('thêm chút nữa thôi...')
      wait(2016, () => {
        console.log('xong rồi đấy!')
      })
    })
  })
}
```

Vì vậy, với phiên bản ES6 (ES 2016), [Promise](https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise) đã được đưa vào mặc định nhằm giải quyết tình trạng callback hell. Với Promise, mã nguồn của ta sẽ trông gần giống với phong cách đồng bộ, kết quả là trông dễ theo dõi và bảo trì hơn. Tuy nhiên sử dụng `Promise` lại làm phát sinh vấn đề "khá" tương tự là Promise hell ( lol! JavaScript Heo! ).

```javascript
function wait(ms) {
  return new Promise(r => setTimeout(r, ms))  
}

function main() {
  console.log('sắp rồi...')
  wait(2007).then(() => {
    console.log('chờ tí...')
    return wait(2007)
  }).then(() => {
    console.log('thêm chút nữa thôi...')
    return wait(2012)
  }).then(() => {
    console.log('thêm chút nữa thôi...')
    return wait(2016)
  }).then(() => {
    console.log('xong rồi đấy!')
  })
}
```

Để giải quyết vấn đề đó, ở phiên bản ES7 (ES 2017), 1 khái niệm với 2 từ khóa mới được đưa vào là hàm async (`async / await`). Hàm async cho phép ta viết các thao tác bất đồng bộ với phong cách của các mã đồng bộ. Bằng cách viết như vậy, mã nguồn của ta trông sẽ sáng sủa, dễ đọc hơn và "dễ hiểu hơn".

```javascript
function wait(ms) {
  return new Promise(r => setTimeout(r, ms))  
}

async function main() {
  console.log('sắp rồi...')
  await wait(2007)
  console.log('chờ tí...')
  await wait(2012)
  console.log('thêm chút nữa thôi...')
  await wait(2016)
  console.log('xong rồi đấy!')
}
```

### 2. Cách sử dụng

Để sử dụng hàm async, ta cần khai báo từ khóa `async` ngay trước từ khóa định nghĩa hàm. Tức là, với hàm định nghĩa với từ khóa `function` ta phải khai báo ngay trước `function`, với hàm mũi tên (arrow function) ta phải khai báo trước tập tham số đầu vào, với phương thức của lớp [`Class`](https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Classes) thì ta phải khai báo ngay trước tên hàm.

```javascript
// regular function
async function functionName() {
  let ret = await new Google().search('JavaScript')
}

// arrow function
let arr = ['JS', 'node.js'].map(async val => {
  return await new Google().search(val)
})

// Class
class Google {
  constructor() {
    this.apiKey = '...'
  }

  async search(keyword) {
    return await this.searchApi(keyword)
  }
}
```

Với từ khóa `async` này, ta có thể đợi các `Promise` (thao tác bất đồng bộ) xử lý trong hàm đó mà không tạm dùng luồng chính bằng từ khóa `await` như ví dụ trên.

Kết quả trả ra của hàm async luôn là một Promise dù bạn có gọi `await` - có xử lý bất đồng bộ hay không. Promise này sẽ ở trạng thái thành công với kết quả được trả ra với từ khóa `return` của hàm async, hoặc trạng thái thất bại với kết quả được đẩy qua từ khóa `throw` trong hàm async.

Như vậy, bản chất của hàm async chính là Promise. Nếu bạn chưa tìm hiểu về `Promise` thì nên đọc trước ở [bài viết này](https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise).

Với Promise, ta có thể xử lý ngoại lệ với [`catch`](https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/catch) khá đơn giản. Tuy nhiên cũng không dễ dàng theo dõi và dễ đọc. Nhưng với hàm async, việc này cực kì đơn giản bằng từ khóa `try catch` hệt như các thao tác đồng bộ.

```javascript
//
// test.js
//
function wait(ms) {
  return new Promise(r => setTimeout(r, ms))  
}

async function runner() {
  console.log('sắp rồi...')
  await wait(2007)
  console.log('chờ tí...')
  await wait(2012)
  console.log('thêm chút nữa thôi...')
  await wait(2016)
  throw new Error(2016)
}

async function main() {
  try {
    await runner()
    console.log('xong rồi đấy!')
  } catch (e) {
    console.log(`có vấn đề tại ${ e }`)
  }
}

// Node v7
// `$ node --harmony-async-await test.js`
// Console: ... có vấn đề tại 2016
```

Ngon! Rõ ràng là mã nguồn sử dụng `async/await` trông đơn giản, dễ theo dõi, "dễ hiểu" hơn và giải quyết được tình trạng callback - promise hell. Tuy nhiên, việc sử dụng nó cũng không phải lúc nào cũng đơn giản. Ta cùng nhau xem một số trường hợp dưới đây.

### 3. Lưu ý

####  3.1. Quên khai báo từ khóa `async`

Đương nhiên rồi, không khai báo từ khóa này thì ta không có hàm async được, không sử dụng `await` được rồi. Thường bạn sẽ nghĩ đơn giản là không thể nào quên được từ khóa này, nhưng tôi nghĩ đôi lúc có thể đấy. Ví dụ như với trường hợp khai báo một hàm trong một hàm async. Hàm khai báo trong hàm async cũng bắt buộc phải được khai báo với từ khóa `async` nếu như bạn muốn sử dụng như một hàm async.

```javascript
async function main() {
  await wait(1000)
  let arr = [100, 300, 500].map(val => wait(val))
  arr.forEach(func => await func)
  // ??? error
}
```

####  3.2. Nhập nhằng từ khóa `await`

Có 2 tình huống điển hình cho trường hợp này là:
* Quên khai báo khi cần đợi một xử lý bất đồng bộ

  Có gì đáng sợ không? Câu trả lời là có đấy! Nếu bạn không khai báo từ khóa này thì kết quả bạn nhận được sẽ là một `Promise` chứ không phải là kết quả thực thi của xử lý bất đồng bộ nhé.

  ```javascript
  async function now() {
    return Date.now()
  }

  async function main() {
    let t = now()
    console.log(t)
     // ??? `t` is a `Promise` instance
  }
  ```

* Khai báo "thừa" trước một xử lý đồng bộ

   Nếu mà sợ quên thì cứ khai báo bừa đi, đâu có sao? Ừ không sao đâu ngoại trừ 2 vấn đề là không biết cái nào là đồng bộ, cái nào là bất đồng bộ nữa, và hiệu quả đi xuống đấy. Mỗi khi bạn khai báo `await` thì mặc nhiên sau từ khóa đó là một `Promise`, nếu không phải là một `Promise` thì nó sẽ được gói lại vào `Promise` và được trả ra ngay với phương thức [`Promise.resolve(value)`](https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve). Rảnh quá ha, muốn lấy `1 + 0 = 1` mà phải đi đường vòng là tính tổng, rồi nhét vào Promise, rồi lại moi ra để sử dụng.

   ```javascript
   async function main() {
     // run with await
     console.log('run with await')
     let i = 1000000
     console.time('await')
     while(i-- > 0) {
       let t = await (1 + 0)
     }
     console.timeEnd('await')

     // run without await
     console.log('run without await')
     i = 1000000
     console.time('normal')
     while(i-- > 0) {
       let t = 1 + 0
     }
     console.timeEnd('normal')
   }
   ```

####  3.3. Quên xử lý lỗi

Cũng như với việc quên `catch` lỗi khi sử dụng Promise, việc quên `try catch` để bắt lỗi với hàm async cũng có thể xảy ra. Nếu bạn quên không bắt lỗi, thì khi đoạn mã bất đồng của bạn xảy ra lỗi có thể làm chương trình của bạn bị dừng lại.

```javascript
function wait(ms) {
  if (ms > 2015) throw new Error(ms)
  return new Promise(r => setTimeout(r, ms))
}

async function main() {
  console.log('sắp rồi...')
  await wait(2007)
  console.log('chờ tí...')
  await wait(2012)
  console.log('thêm chút nữa thôi...')
  await wait(2016)
  console.log('xong rồi đấy!')
}
```

####  3.4. Mất tính song song

Cái này có vẻ là căng nhất, bạn cứ khai báo `await` tuần tự đi rồi chương trình của bạn sẽ chậm như con rùa. hahaaa. Vì mỗi lần khai báo `await` như vậy là bạn cần phải chờ cho xử lý của await kết thúc. Kết quả là bạn có 1 con rùa chạy tuần tự qua từng nấc thang.

```javascript
function wait(ms) {
  return new Promise(r => setTimeout(r, ms))
}

async function main() {
  console.time('wait3s')
  await wait(1000)
  await wait(2000)
  console.timeEnd('wait3s')
}
```

Với đoạn mã trên bạn sẽ mất tổng cộng là `1 + 2 = 3s` để thực thi. Vì bạn phải chờ từng hàm `wait` một. Vậy làm sao để tránh được tình trạng trên? Câu trả lời là cứ cho xử lý bất đồng bộ chạy trước đi rồi lấy kết quả sau. Vì `Promise` có thể cho phép ta lấy kết quả bất cứ khi nào mà nó ở trạng thái cuối cùng, nên ta có thể chạy nó trước rồi lấy sau cũng không sao cả.

```javascript
function wait(ms) {
  return new Promise(r => setTimeout(r, ms))
}

async function main() {
  console.time('wait2s')
  let w1 = wait(1000)
  let w2 = wait(2000)
  await w1
  await w2
  console.timeEnd('wait2s')
}
```

Như đoạn mã này, ta chỉ mất `2s` để thực hiện vì đoạn `wait` của ta được thực thi song song. Ngoài cách `await` từng `Promise` như trên ta có thể sử dụng [`Promise.all`](https://developer.mozilla.org/vi/docs/Web/JavaScript/Reference/Global_Objects/Promise/all) để song song hóa các Promise.

```javascript
function wait(ms) {
  return new Promise(r => setTimeout(r, ms))
}

async function main() {
  console.time('wait2s')
  await Promise.all([wait(1000), wait(2000)])
  console.timeEnd('wait2s')
}
```

Lúc này, có thể bạn đang nghĩ `Promise.all` và `await` từng Promise là như nhau, nhưng nó khác nhau chút đấy. `Promise.all` chỉ ở trạng thái thành công khi mà tất cả các Promise được truyền vào xử lý thành công, còn nó sẽ ở trạng thái lỗi khi một trong các Promise truyền vào bị lỗi. Như vậy, nếu bạn muốn bỏ qua các Promise lỗi thì bạn không thể sử dụng `Promise.all` được đâu. Lúc đó bắt buộc bạn phải sử dụng `await` kèm với `try catch` cho từng Promise của bạn.

```javascript
function wait(ms) {
  if (ms > 2000) throw new Error(ms)
  return new Promise(r => setTimeout(r, ms))
}

async function main() {
  const dur = [1000, 2000, 3000, 4000]
  let all = dur.map(ms => wait(ms))
  try {
    await Promise.all(all)
    console.log('Promise.all - done')
  } catch (e) {
    console.error('Promise.all:', e)  
  }

  let each = dur.map(ms => wait(ms))
  each.forEach(async (func, index) => {
    try {
      await func
      console.log('each - done:', dur[index])
    } catch (e) {
      console.error('each:', e)  
    }
  })
}
```

### 4. Nền tảng/ trình duyệt hỗ trợ

  Thời điểm này (2016/10), các nền tảng và trình duyệt sau đã hỗ trợ hàm async.

   * Node.js v7.0 với cờ `--harmony-async-await`
   * Chrome v5.55
   * Microsoft Edge v21.10547

  Nếu bạn muốn chạy ở các nền tảng/ trình duyệt chưa hỗ trợ thì có thể dùng babel để chuyển đổi:

   * Babel [async-2-generator plugin](https://babeljs.io/docs/plugins/transform-async-to-generator/)


### 5. Kết luận

  Bản chất của hàm async chính là `Promise`, vì vậy để sử dụng được nó ta cần phải sử dụng `Promise` cho việc xử lý các thao tác bất đồng bộ. Bạn không thể nào sài `await` để đợi các hàm có sử dụng hàm phản hồi (callback) được, mà bắt buộc phải gắn nó với một Promise trước khi sử dụng `await`.

  Mặc dù hàm async có cú pháp rất rõ ràng, ta cũng cần phải lưu ý tránh khai báo thừa thiếu các từ khóa gây lỗi, gây hiểu lầm về lô-gíc chương trình. Và đặc biệt lưu ý tới khả năng làm mất đi tính song song của chương trình.

  Với sự tiện dụng của hàm async, ta nên cố gắng sử dụng nó ngay từ bây giờ để giảm thiểu việc bảo trì sau này. Với các nền tảng/ trình duyệt chưa hỗ trợ thì ta có thể chuyển đổi bằng [babel](https://babeljs.io/). Hiện tại Node v7 vẫn đang sử dụng Chrome v5.54 nên muốn sử dụng được async/await, ta buộc phải chạy với cờ `--harmony-async-await` và hiệu năng, bộ nhớ được sử dụng vẫn chưa hiệu quả, không khuyến khích cho các sản phẩm thực tế. Tuy nhiên, rất có thể Node v8 sẽ sử dụng phiên bản Chrome v5.55 và cho phép ta thực hiện mặc định các hàm async.

 `async` chúc các bạn `await` vui vẻ!
