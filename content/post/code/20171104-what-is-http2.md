---
title: "[Web] HTTP2 là gì?"
slug: what-is-http2
date: 2017-11-04
categories:
- Lập Trình
- Web
tags:
- HTTP2
keywords:
- HTTP2
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/nodejs_svg.svg
metaAlignment: center
draft: true
---
Nhân tiện bản `Node v9x` mới ra cho phép ta có thể sử dụng ngay API thử nghiệm `HTTP/2` nên cũng tò mò tìm hiểu đôi chút xem kiến trúc, đặc điểm và cách sử dụng thế nào.
Sau 2 năm ra chính thức ra lò, phiên bản tiếp theo của `HTTP` này dần được nhiều máy chủ Web lẫn trình duyệt hỗ trợ bởi tính vượt trội của nó so với phiên bản `HTTP/1.1`.
<!--more-->

<div style="position: relative; text-align: center; margin-top: 10px;">
  <div style="display: inline-block; vertical-align: top; width: 49%; min-width: 350px;">
    <iframe src="https://http1.akamai.com/demo/h2_demo_frame.html" marginheight="0" frameborder="0" scrolling="no" width="100%" height="420px">
      <p>Your browser does not support iframes.</p>
    </iframe>
  </div>
  <div style="display: inline-block; vertical-align: top; width: 49%; min-width: 350px;">
    <iframe src="https://http2.akamai.com/demo/h2_demo_frame.html" marginheight="0" frameborder="0" scrolling="no" width="100%" height="420px">
      <p>Your browser does not support iframes.</p>
    </iframe>
  </div>
  <span class="caption">Source: https://http2.akamai.com/demo</span>
</div>

<!--toc-->

# 1. Nhược điểm của HTTP/1.1



# 2. HTTP/2 là gì

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-history.png" title="Source: https://codezine.jp/article/detail/8663" >}}

{{< image classes="fancybox center" src="https://developers.google.com/web/fundamentals/performance/http2/images/binary_framing_layer01.svg" title="Source: https://developers.google.com/web/fundamentals/performance/http2/" >}}


# 3. Trình duyệt hỗ trợ
Hầu hết các trình duyệt chính hiện nay đều đã hỗ trợ HTTP/2 như Google Chrome, Mozilla Firefox, Microsoft Edge.
Tổng thể cả trình duyệt trên máy tính lẫn điện thoại, máy tính bảng thì có tới hơn 80% đã hỗ trợ HTTP/2 nên ta hoàn toàn có thể yên tâm khi triển khai HTTP/2.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-support.png" title="Source: https://caniuse.com/#search=http2" >}}

# 4. Thử nghiệm với Node v9x
Trước tiên ta cần phải có chứng chỉ SSL để có thể tạo được một máy chủ bảo mật,
do đã đề cập hầu hết các trình duyệt giờ chỉ hỗ trợ các máy chủ HTTP/2 bảo mật.
Nếu bạn chưa có thì có thể tạo bằng lệnh OpenSSL như dưới đây:

```
$ openssl req -x509 -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' \
  -keyout localhost-privkey.pem -out localhost-cert.pem
```

Lưu ý là chứng chỉ tạo ra này không phải là chứng chỉ được công nhận chính thức nên khi chạy với Google Chrome thì có thể bị báo lỗi SSL màu đỏ,
nhưng cứ mặc nó đi vì nó chẳng ảnh hưởng gì tới local của ta đâu.

Để tạo server bằng HTTP/2, tôi lấy luôn đoạn mã dưới từ tài liệu trên trang chủ <a href="https://nodejs.org/dist/latest-v9.x/docs/api/http2.html#http2_server_side_example" target="_blank" rel="noopener noreferrer">Nodejs.org</a>.
Bạn có thể copy nguyên file này và để cùng thư mục với chứng chỉ vừa tạo phía trên.

{{< codeblock "index.js" "js" >}}
const http2 = require('http2')
const fs = require('fs')

const server = http2.createSecureServer({
  key: fs.readFileSync('localhost-privkey.pem'),
  cert: fs.readFileSync('localhost-cert.pem')
})
server.on('error', console.error)
server.on('socketError', console.error)

server.on('stream', (stream, headers) => {
  // stream is a Duplex
  stream.respond({
    'content-type': 'text/html',
    ':status': 200
  })
  stream.end('<h1>Hello World</h1>')
})

server.listen(8443)
{{</ codeblock >}}

Giờ chạy đoạn mã này với lệnh: `$ node index.js`, rồi bật trình duyệt lên với địa chỉ: `https://localhost:8443` xem sao nhé.
*Lưu ý là bắt buộc phải nhập `https` vì server của ta là dạng SSL*.

{{< alert info >}}
Để xem máy chủ có dạng HTTP/2 hay không, ta có thể xem cột `Protocol` ở mục `Network` của Developer Console lên bằng cách chuột phải ở 1 tiêu đề cột bất kì nào đó sau đó chọn mục `Protocol` là được.
Ví dụ, sau khi mở Developer Console lên, bạn vào tab `Network` rồi ấn vào 1 tiêu đề của cột `Status` (tức là ấn vào chữ `Status`),
sau đó ấn chuột phải ở vị trí này thì sẽ thấy mục `Protocol`, lúc đó chỉ cần ấn để chọn mục đó là được.
Ở đây, tôi có chọn thêm mục `Priority` để xem các request có mức độ ưu tiên thế nào nữa.
{{< /alert >}}

Dưới đây là kết quả mà tôi thu được sau khi chạy đoạn mã trên.
Nhìn hình bên dưới ta có thể thấy `Protocol` của ta lúc này là `h2`, tức là máy chủ của ta là HTTP/2.
Ngoài ra, nhìn vào mức độ ưu tiên `Priority` ta có thể thấy file html (`localhost`) mà ta cần lấy có độ ưu tiên là cao nhất.
Điều này cũng dễ hiểu thôi vì khi cần lấy về 1 trang web thì file html này là file đầu tiên ta cần phải lấy về.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-node-1.png" title="HTTP/2 Protocol" >}}

Bước tiếp theo ta có thể kiểm tra các header xem khác gì so với phiên bản HTTP cũ bằng cách click vào 1 request nào đó.
Ví dụ dưới đây, file html được lấy về có các request header giống như mô ta của ta ở phía trên rồi.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-node-2.png" title="HTTP/2 Header" >}}

# 5. Kết luận
HTTP/2 là phiên bản kế tiếp của HTTP/1.1 nhằm mở rộng hiệu năng và vẫn giữ được tính tương thích của phiên bản cũ.
Với ưu điểm nổi trội của nó nên ngày càng nhiều trình duyệt bắt đầu hỗ trợ giao thức mới này để mang lại trải nghiệm tốt nhất cho người dùng.
Tuy nhiên hiện nay các trình duyệt mới chỉ hỗ trợ các máy chủ bảo mật mà thôi.
Nhìn chung đây cũng là xu hướng của Web hiện đại, khi mà các máy chủ bảo mật ngày càng được khuyến khích sử dụng.

Hiện nay các gói thư viện hỗ trợ cho việc phát triển cũng như nâng cấp phiên bản HTTP cũ lên HTTP/2 cũng đang bắt đầu nở rộ như HTTP/2 của Node Core, HTTP/2 của ngôn ngữ Go...
Không tránh nổi xu thế, trong thời gian tới đây việc sử dụng HTTP/2 chắc sẽ được khuyến khích sử dụng mạnh mẽ như HTTPS hiện thời.

Để tránh việc bảo trì nhọc công sau này, tôi cho rằng nếu có thể ta nên sử dụng ngay HTTP/2.
Một phần khác cũng là để mang lại hiệu quả tốt hơn cho người dùng của ta.
Ví như các công ty lớn như Google, Facebook, Twitter hay Amazon giờ đều đã chuyển qua HTTP/2 cả.
Nên bạn không cần phải lo lắng chuyện đi sai nước hay lạc loài trong dòng chảy công nghệ hiện nay.