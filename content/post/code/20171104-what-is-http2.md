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

Gần đây Gmail không cho phép gửi các file có đuôi là mã nguồn ngôn ngữ lập trình như `.js`, `.vb` chẳng hạn.
Ngay cả việc đổi đuôi của các file nén cũng không có hiệu quả như trước, nên buộc phải tìm cách đổi toàn bộ đuôi 1 phát.

Bài viết này sẽ nói về cách thay đổi toàn bộ đuôi file bằng `.bat` file của Windows, tuy nhiên hoàn toàn có thể sử dụng để làm những chuyện khác với các file này như đổi tên chẳng hạn.

Để thay đổi file ta có thể sử dụng lệnh `ren`, ví dụ đổi đuôi `js` thành `jsx` ta có thể sử dụng: `ren *.js *jsx`.


Còn để duyệt toàn bộ các file của thư mục nào đó bao gồm cả các thư mục con, ta có thể sử dụng lệnh `for` với tham số `R`, ví dụ duyệt toàn bộ các file có đuôi là `.png`: `for /R %%f in (*.png) do @echo %%f`.

Ví dụ dưới đây có thể sài để thay đổi toàn bộ đuôi `.js` thành `.xxx` trong thư mục và thư mục con của thư mục hiện tại.

{{< codeblock  "ren.bat" "bash" "https://stackoverflow.com/questions/15317647/how-to-batch-change-file-extensions-within-subfolders#15317773" >}}
@echo OFF

for /R %%f in (*.js) do ren "%%f" *.xxx

@echo "done!"
@timeout 100
{{< /codeblock >}}

Ở đây ta thêm lệnh `timeout` để cửa sổ Cmd của ta không bị đóng luôn nhằm tiện theo dõi kết quả.

Đơn giản thế thôi, nhưng không biết còn cách nào đơn giản hơn nữa không nhỉ?
