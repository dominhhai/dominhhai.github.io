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

# 1. HTTP/2 là gì

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-history.png" title="Source: https://codezine.jp/article/detail/8663" >}}

{{< image classes="fancybox center" src="https://developers.google.com/web/fundamentals/performance/http2/images/binary_framing_layer01.svg" title="Source: https://developers.google.com/web/fundamentals/performance/http2/" >}}


# 2. Ưu điểm



# 3. Trình duyệt hỗ trợ
{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-support.png" title="Source: https://caniuse.com/#search=http2" >}}

# 4. Thử nghiệm với Node v9x

```
$ openssl req -x509 -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' \
  -keyout localhost-privkey.pem -out localhost-cert.pem
```

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

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-node-1.png" title="protocol" >}}
{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-node-2.png" title="header" >}}
