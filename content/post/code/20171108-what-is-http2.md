---
title: "[Web] HTTP2 là gì?"
slug: what-is-http2
date: 2017-11-08
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
HTTP/1.1 có một nguyên tắc là phải xử lý gọn từng request một, tức là một request nào đó tới máy chủ sau khi được xử lý xong mới có thể gửi 1 request khác đi.
Ví dụ, trang web của ta cần lấy 2 file `main.css` và `main.js` với thứ tự gửi tin tương ứng thì file `main.css` được trả về xong thì máy chủ mới lại xử lý yêu cầu lấy file `main.js`.
Cứ lần lượt một cách máy móc như vậy để xử lý nên khi lượng request nhiều lên thì thời gian chờ để lấy về tất cả các dữ liệu sẽ rất tốn kém, điều này dẫn tới chuyện trang web của ta hiển thị chậm gây khó chịu cho người dùng.

Để phần nào xử lý được hạn chế này, người ta đã đề ra cơ chế pipeline cho các request.
Với cơ chế này, ta có thể gửi nhiều request đi với cùng một kết nối TCP mà không cần phải đợi request trước đó được xử lý xong.

{{< image classes="fancybox center" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/HTTP_pipelining2.svg/640px-HTTP_pipelining2.svg.png" title="Time diagram of non-pipelined vs. pipelined connection. Source: https://en.wikipedia.org/wiki/HTTP_pipelining" >}}

Tuy nhiên phía máy chủ vẫn phải đảm bảo nguyên tắc là xử lý lần lượt từng request một.
Tức là nếu 1 nhóm request nào đó được gửi đi bằng 1 kết nối mà trong đó có 1 request rất mất thời gian xử lý thì kết quả là cả nhóm request ấy sẽ rất mất thời gian để lấy về.
Ngoài ra, một hạn chế nữa là làm sao để xử lý hài hòa được các gói tin để biết chúng thuộc về request nào.
Vậy nên việc thực hiện cơ chế này ở cả 2 phía máy chủ và trình duyệt là không hề đơn giản tí nào. Thường các trình duyệt có cài đặt mặc đinh là không xử lý request kiểu này, mà bắt buộc gửi từng request đi một.

Lưu ý là ở trình duyệt Google Chrome cho phép ta gửi đồng thời nhiều request, nhưng các request này không phải ở cùng 1 kết nối TCP nhé.

Cùng với <a href="http://httparchive.org/trends.php" target="_blank"_ rel="noopener noreferrer">lượng giao dịch tăng chóng mặt</a> người ta phải dùng nhiều tiểu sảo khác nhau để nâng cao hiệu quả trang web với HTTP/1.1 như:

* Giảm request
 * Gom các file lại với nhau <br/>
    Ví dụ ta gom tất cả các file CSS thành 1 file CSS duy nhất, tất cả các file JS thành 1 file JS duy nhất để có thể giảm lượng request đi.
 * Sử dụng kĩ thuật CSS Sprite <br/>
    Gom nhiều ảnh nhỏ thành 1 ảnh lớn rồi dùng 1 request lấy ảnh lớn đó về, sau đó các icon nhỏ cần hiển thị sẽ được *cắt* từ ảnh lớn bằng CSS để hiển thị lên màn hình. Bạn có thể tưởng tượng các ảnh con trong đó là các sprite, các sprite này sẽ được hiển thị bằng CSS.
 * Nhúng các ảnh bằng dữ liệu mã hóa <br/>
   Thay vì gửi request để lấy ảnh về hiển thị ta nhúng nó luôn vào file HTML, ví dụ như: `<img src="data:image/png;base64,iVBORw+AAA0KGgoAAA/nFfx2hANSUhEUgAA3eesgAAAVORK5CYII=">`.
* Tăng các request đồng thời
 * Phân bổ các tài nguyên cho nhiều máy chủ khác nhau <br/>
   Việc này giúp ta tránh được hạn chế xử lý lần lượt của một máy chủ, ví như trình duyệt Chrome có thể cho phép ta gửi đồng thời tới 6 request 1 lúc, tức là 1 lúc ta có thể lấy đồng thời thông tin từ 6 server liền.

Như vậy có thể thấy việc cải thiện tốc độ cho trang web với HTTP/1.1 rất nhọc công! Phải nói là **KHỔ**!

# 2. HTTP/2 là gì
Với các hạn chế của HTTP/1.1 thì <a href="https://http2.github.io/http2-spec/" target="_blank"_ rel="noopener noreferrer">HTTP/2</a> được ra đời với các mục tiêu chính sau:

* Giảm độ trễ của các trang web bằng cách
  * Ghép kênh cho nhiều request bằng 1 kết nối TCP
  * Tạo cơ chế pipeline cho các request
  * Nén dữ liệu và các header
  * Cho phép máy chủ có thể gửi dữ liệu trước khi có request tới
* Giữ được tính tương thích với HTTP/1.1
* Cho phép cả trình duyệt lẫn máy chủ có thể chọn loại giao kết nối

Khởi nguyên của HTTP/2 là dự án <a href="https://en.wikipedia.org/wiki/SPDY" target="_blank"_ rel="noopener noreferrer">SPDY</a> của Google nhằm giải quyết các vấn đề cơ bản mà HTTP/1.1 gặp phải từ năm 2009. Mãi cho tới năm 2015 nó mới được chuẩn hóa thành đặc tả chính thức HTTP/2. Lúc ấy trình duyệt Chrome vẫn hỗ trợ giao thức SPDY cũ cho tới 1 năm sau khi HTTP/2 ra đời. Rồi dần dần các trình duyệt khác cũng bắt đầu hỗ trợ HTTP/2 do nhận thấy được lợi điểm của nó.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-history.png" title="Source: https://codezine.jp/article/detail/8663" >}}

Về cơ bản, HTTP/2 có thể được mô tả bằng hình vẽ dưới đây.

{{< image classes="fancybox center" src="https://developers.google.com/web/fundamentals/performance/http2/images/binary_framing_layer01.svg" title="Source: https://developers.google.com/web/fundamentals/performance/http2/" >}}

Mỗi kết nối của TCP có thể có nhiều `dòng` (`stream`), trong mỗi `dòng` có thể mang nhiều `thông điệp` (`message`), mỗi `thông điệp` được cấu tạo bởi các `khung` (`frame`) chưa thông tin đã mã hóa dạng nhị phân. Trong `khung` này luôn chứa phần đầu `header` mang thông tin về `dòng` mà nó thuộc về.

Chính nhờ kiến trúc kiểu này mà ta có thể truyền cùng lúc nhiều thông tin 2 chiều giữa máy chủ và trình duyệt dựa vào các dòng thông tin của chúng. Bạn có thể tưởng tượng rằng mỗi dòng là 1 request-response của HTTP/1.1, các dòng này là độc lập với nhau nên việc lấy thông tin dòng này sẽ không phụ thuộc và không ảnh hưởng tới dòng kia.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-multiplexing.png" title="HTTP/2 Multiplexing" >}}

Ngoài ra các dòng này còn có thể được gắn độ ưu tiên truyền tin. Điều này rất có lợi thế khi ta cần gửi-nhận các thông tin cần độ ưu tiên. Ví dụ như khi truy cập 1 trang web nào đó, trang HTML cần phải lấy về ngay trước khi có thể lấy các file JS hay CSS khác. Trong số các file JS ta có thể tùy chỉnh file nào cần lấy trước và file nào chưa cần lấy ngay bằng cách thiết lập độ ưu tiên truyền tin này. Các khung thông tin đều mang thông tin về dòng chứa nó nên chúng có thể được truyền mà không bắt buộc phải đúng thứ tự. Tức là cùng 1 dòng dữ liệu nhưng thứ tự dữ liệu trong đó hoàn toàn có thể được truyền bất định mà không bắt buộc phải đợi nhau cho đúng thứ tự gói tin.

Như đã đề cập, các gói tin của HTTP/2 đều được mã hoá dạng nhị phân chứ không phải dạng văn bản như HTTP/1.1 nên rất tiện và dễ làm việc cho cả 2 phía giúp nâng cao hiệu năng phân tích gói tin nhận được. Các đầu gói tin (header) cũng nén lại với giải thuật Huffman giúp cho thông tin truyền đi ít đi mà vẫn đủ thông tin cần thiết cho việc xử lý. Tuy nhiên cả 2 phía đều cần phải cập nhập danh sách mã hoá đồng bộ nhau để có thể giải mã được gói tin nhận được. Bạn có thể tưởng tượng đơn giản rằng các đầu tin gửi đi chỉ cần gửi phần khác nhau sau mỗi request thôi còn phần giống nhau đã được mã hoá với Huffman rồi nên chỉ cẩn phần khác nhau giữa 2 gói tin trước và sau là ta có thể giải mã được gói tin.

Một tính năng tuyệt vời nữa của HTTP/2 là Server Push. Tính năng này giúp cho ta giảm được lượng request cần gửi bằng cách gửi trước tài nguyên cho máy khách (trình duyệt). Giả sử, ta có 1 trang web cần 2 file `main.js` và `main.css`. Khi ta tạo request lấy về trang `index.html` thì máy chủ sẽ trả về luôn 2 file `main.js` và `main.css` song song cùng luôn. Sau khi nhận được tài nguyên trả về từ máy chủ rồi, trình duyệt của ta sẽ giữ chúng trong bộ nhớ tạm (cache memory) và khi cần lấy các file này thì trình duyệt có thể lấy nó ra từ bộ nhớ tạm mà không cần gửi request lên máy chủ nữa.
Tất cả gói tin kiểu này sẽ được báo trước với máy khách thông qua khung thông tin `PUSH_PROMISE`, dựa vào đây trình duyệt có thể từ chối hoặc chấp nhận lấy về tài nguyên đó hay không. Ngoài ra trình duyệt còn có thể giới hạn được cả số gói tin gửi trước này giúp cho cả 2 phía có thể xử lý trơn tru tài nguyên trao đổi cho nhau.

# 3. Trình duyệt hỗ trợ
Hầu hết các trình duyệt chính hiện nay đều đã hỗ trợ HTTP/2 như Google Chrome, Mozilla Firefox, Microsoft Edge.
Tổng thể cả trình duyệt trên máy tính lẫn điện thoại, máy tính bảng thì có tới hơn 80% đã hỗ trợ HTTP/2 nên ta hoàn toàn có thể yên tâm khi triển khai HTTP/2.

Nếu bạn muốn kiểm tra xem trình duyệt của mình và trang đang truy cập có hỗ trợ HTTP/2 hay không thì đọc tiếp phần 4 bên dưới nhé.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/web/http2-support.png" title="Source: https://caniuse.com/#search=http2" >}}

Một điểm cần lưu ý là ngay khi bạn truy cập vào 1 trang web nào đó thì trình duyệt không thể biết được trang web đó hỗ trợ truyền tin HTTP/2 hay không nên hiện giờ khi kết nối với 1 máy chủ nào đó, trình duyệt vẫn sẽ gửi request lên với thông tin là HTTP/1.1 như bình thường.
Sau đó, nếu nhận được thông tin từ máy chủ rằng nó hỗ trợ HTTP/2 thì trình duyệt một lần nữa sẽ gửi thông tin lấy về tài nguyên dựa vào thao tác kết nối HTTP/2.

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

Để tạo server bằng HTTP/2, tôi lấy luôn đoạn mã dưới từ tài liệu trên trang chủ <a href="https://nodejs.org/dist/latest-v9.x/docs/api/http2.html#http2_server_side_example" target="_blank"_ rel="noopener noreferrer">Nodejs.org</a>.
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

Trong bày này tôi chỉ nói rất vắn tắt về HTTP/2 còn chi tiết thì các bạn nên xem đặc tả của nó <a href="https://http2.github.io/http2-spec/" target="_blank"_ rel="noopener noreferrer">tại đây</a> và cả bản tóm tắt về HTTP/2 trên <a href="https://developers.google.com/web/fundamentals/performance/http2" target="_blank"_ rel="noopener noreferrer">Google Developer</a> nữa nhé.
