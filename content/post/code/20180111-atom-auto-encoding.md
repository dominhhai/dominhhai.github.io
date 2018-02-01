---
title: "[Atom] Tự động phát hiện và hiển thị mã hoá"
slug: atom-auto-encoding
date: 2018-01-11T09:28:28+09:00
categories:
- Lập Trình
- Editor
tags:
- Editor
- Atom
keywords:
- Editor
- Atom
- Auto Encoding
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/editor/atom.png
metaAlignment: center
---
Bạn đã bao giờ mở 1 file ra bằng auto mà các chữ trong đó hiển thị như con giun con dế chưa? Những tình huồng như vậy có thể là do atom mặc định mở file với định dạng UTF-8, nhưng file của ta lại ở dạng khác như Shift-JIS chẳng hạn.
<!--more-->

Mã hoá mặc định này có thể xem và cấu hình được trong mục cài đặt của Atom (`Setting` →　`Core` →　`File Encoding`). Ví dụ như hình bên dưới, ta có thể thấy được mã hoá mặc định sẽ là `UTF-8`. Tức là các file khi được mở ra sẽ được đọc dưới định dạng mặc định là `UTF-8` và khi lưu lại cũng được mặc định luôn là mã hoá này. Ban đầu khi mình tìm xem có kiểu mặc định phát hiện mã hoá tự động không thì không hề thấy luôn 😥

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/atom/auto-encoding-0.png" title="Default Encoding" >}}

Đương nhiên là trong hoàn cảnh như vậy, muốn xem được file đó ta cần phải chỉ định đúng định dạng mã hoá của nó. Để làm được vậy ta có 2 cách thực hiện là thủ công và tự động.

Cách thực hiện thủ công cũng không nhọc nhằn cho lắm. Ta chỉ việc ấn tổ hợp phím `Ctr+Shift+U` thì một cửa sổ chọn mã hoá sẽ hiện lên và ta chỉ cần chọn đúng mã hoá của file cần mở hoặc đơn giản là chọn một cách tự động (`Auto Detect`) là xong. Ngoài ra ta có thể click vào chữ thể hiện mã hoá hiện tại bên thanh menu dưới cũng sẽ cho kết quả tương tự.

Ví dụ như hình dưới đây, tôi cài đặt mặc định là `Shift-JIS` và mở một file định dạng `UTF-8` ra thì atom sẽ không hiển thị được chính xác nội dung của file đó. Sau đó tôi click vào chữ `Shift-JIS` ở menu dưới thì cửa sổ chọn mã hoá sẽ chọn lên. Khi đó tôi chọn `UTF-8` thì nội dung file của tôi lại hiển thị một cách ngon lành.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/atom/auto-encoding-1.gif" title="Ctr+Shift+U for Detecting Encoding" >}}

Việc làm thủ công cũng không hề khó, tuy nhiên mỗi lần mở 1 file ra mà không thấy nội dung thì ta lại phải lặp lại thao tác như vậy. Nên ta cần một giải pháp tự động thay thế.

Thật may là ta có thể sử dụng gói [auto-encoding](https://atom.io/packages/auto-encoding) để làm việc đó. Sau khi cài đặt gói này, ta thử mở file ra thì nó ngay lập tức sẽ phát hiện định dạng mã hoá và hiển thị cho ta luôn.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/atom/auto-encoding-2.gif" title="Auto Detecting and Adapting Encoding with auto-encoding" >}}

Như vậy để phát hiện và hiển thị đúng nội dung file với Atom, ta có thể sử dụng tổ hợp phím `Ctr+Shift+U` để thực hiện một cách thủ công hoặc gói [auto-encoding](https://atom.io/packages/auto-encoding) để thực hiện tự động cực kì đơn giản và tiện lợi.
