---
title: "[Node.js] Không cần headless browser"
slug: scrape-nodejs
date: 2018-06-07
categories:
- Lập Trình
- Node.js
tags:
- Node.js
- Scraping
- Crawler
keywords:
- Scraping
- Crawler
- Headless Browser
- puppeteer
- Node Request
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/nodejs_svg.svg
metaAlignment: center
---
Trước tiên khi nghĩ tới việc lấy dữ liệu từ các trang cần phải thao tác qua vài bước như submit form, chuyển trang nọ kia người ta thường nghĩ ngay tới việc sử dụng headless browser như [Puppeteer](https://github.com/GoogleChrome/puppeteer), [Selenium / WebDriver](https://www.seleniumhq.org/), hay [PhantomJS](http://phantomjs.org/).

Nhưng dở cái này mấy cái này nó sẽ khởi động nhân của trình duyện như Chrome chẳng hạn để thực hiện việc truy cập và thao tác trang web nên cực kì nặng nề. Bạn thử bật một đống trình duyệt lên trên máy tính của bạn thì rõ. Đương nhiên là nếu server bạn trâu thì không nói làm gì. Nếu không có server trâu thì phải tìm cách thay thế headless browser để giảm chi phí cho việc thao tác trang web.

Về cơ bản thì các trang web cần thao tác qua vài bước như ấn nút nọ, submit form kia rồi chuyển trang nọ kia thì đều dựa vào **headers, cookies** để xử lý cả. Nên nếu ta duy trì xử lý khéo được các thông tin đó thì hoàn toàn có thể điều khiển được trang web cần lấy dữ liệu.

Thật may mắn là với các thư việc có sẵn như [Request](https://github.com/request/request) và [jsdom](https://github.com/jsdom/jsdom) ta có thể thao tác và duy trì được các thông tin gửi lên 1 trang bất kì. Các thư viện này chỉ đơn giản gửi đi và lấy về kết quả chứ không thực hiện việc layout hay các thao tác tốn kém khác như trình duyệt nên đương nhiên là sẽ nhanh hơn từ bước khởi động tới nhận dữ liệu.

Tùy vào mục tiêu và trang cần lấy dữ liệu mà ta chọn thư viện cho phù hợp. Với các trang mà ta không cần thực thi các mã JS trả về thì chỉ cần tới `Request` là đủ, nhưng nếu cần thực thi các mã JS thì phải sài `jsdom`. Về cụ thể, bạn có thể xem trên trang chủ của từng thư viện thì sẽ rõ ngay.

Một điểm cần lưu ý với cookies là ta nên {{<hl-text green>}}tách cookies riêng ra cho mỗi phiên{{</hl-text>}} lấy dữ liệu. Tại sao lại thế? Vì mỗi phiên lấy dữ liệu ta có thể coi như 1 lần mở trình duyệt lên và truy cập vào trang web, click click và lấy dữ liệu. Đương nhiên mỗi lần như thế ta sẽ có cookies riêng biệt rồi. Nên việc thao tác cookies ở mỗi phiên cũng sẽ làm tương tự như vậy. Đầu tiên là lấy cookies ở lần đầu truy cập trang, duy trì cookies đó trong suốt phiên làm việc.

Thường với headers thì `User-Agent` được gửi kèm là rất phổ biến, nên về cơ bản ta cũng sẽ thiết lập `User-Agent` tương ứng với trình duyệt phiên bản mới nhất là được. Với các agent trên mobile, ta có thể tham khảo [danh sách devices của puppeteer](https://github.com/GoogleChrome/puppeteer/blob/master/DeviceDescriptors.js) cũng khá ổn.

Ví dụ, việc tạo cookies riêng biệt với `jsom` tương ứng với trình duyệt Chrome 67 trên Mac, được thực hiện như sau:
```js
const cookieJar = new jsdom.CookieJar(store, options)
const dom = new JSDOM('', {
  cookieJar,
  userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
})
```

Tạo cookies riêng biệt với `Request` tương ứng với Chrome trên iPhone X như sau:
```js
const cookieJar = request.jar()
const rq = request.defaults({
  jar: cookieJar,
  headers: {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
  }
})
rq.get('https://dominhhai.github.io/vi/')
```

Để sáng tỏ hơn, ta lấy ví dụ về việc đăng nhập vào trang Github. Ở trang đăng nhập `https://github.com/login`, ta thấy có 1 form nhập id, pass và 1 nút submit. Trước khi submit form này, ta sẽ điền giá trị vào cho cả 2 mục id, pass đó đã. Có 1 mẹo nhỏ đề dễ dàng lấy được địa chỉ mỗi phần tử trong trang web với Chrome là sử dụng tính năng `Copy Selector` trong cửa sổ `inspect` như hình dưới đây:

{{< image classes="fancybox center" thumbnail-width="80%" src="https://res.cloudinary.com/dominhhai/image/upload/code/scrape-github-login.png" title="Copy Selector" >}}

Với cách đó, ta sẽ lấy được form là `#login > form`, id là `#login_field`, pass là `#password`. Giờ ta sẽ viết code để nhập và submit form này.

{{< codeblock "github.js" "js" >}}
const request = require('request-promise-native')
const cheerio = require('cheerio')

const req = request.defaults({
  headers: {
    // user Mac Chrome 67 as Agent
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
  },
  encoding: null,
  baseUrl: 'https://github.com',
  // user cheerio (jquery on server side) to transform body html
  transform: function (body) {
    return cheerio.load(body)
  }
})

function getFormQs($, form) {
  let qs = {}
  $(form).find('input').each((index, inp) => {
    let $inp = $(inp)
    qs[$inp.attr('name')] = $inp.val() || ''
  })

  return qs
}

async function github({ username, pass }) {
  // create new cookie
  const rq = req.defaults({
    jar: req.jar()
  })
  // go to login page
  let $ = await rq({
    uri: 'login'
  })
  // fill id, pass
  $('#login_field').val(username)
  $('#password').val(pass)
  // get submit form
  const form = '#login > form'
  let uri = $(form).attr('action')
  let qs = getFormQs($, form)
  // submit form
  $ = await rq.post({
    uri,
    qs
  })

  return $.html()
}

// with username_1 & password_1
github({
  username: YOUR_USERNAME_1,
  password: YOUR_PASSWORD_1
}).then(console.log)
  .catch(console.error)
// with username_2 & password_2
github({
  username: YOUR_USERNAME_2,
  password: YOUR_PASSWORD_2
}).then(console.log)
  .catch(console.error)
{{</ codeblock >}}

Giờ thử chạy với cả 2 tài khoản thì ta sẽ thu được 2 trang tương ứng với 2 tài khoản vừa đăng nhập. Ở đây, tôi chỉ viết tới đoạn sau đăng nhập, nhưng cùng với cookie riêng biệt đó, bạn có thể làm nhiều thao tác sau khi đăng nhập như tạo repo các kiểu.

Ngoài ra, cookie nếu chưa hết hạn thì hoàn toàn có thể lưu lại và lấy ra chạy tiếp cho lần sau. Việc đó cũng giúp ta tiết kiệm được lượng request cũng như thao tác tự động.

Have Fun!
