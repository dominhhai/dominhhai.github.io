---
title: "[Make] Sử dụng trên Windows"
slug: gnu-make-windows
date: 2017-09-20
categories:
- Lập Trình
- Makefile
tags:
- Makefile
keywords:
- Make
- Make on Windows
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/gnu.png
metaAlignment: center
---
<a href="https://www.gnu.org/software/make/" target="_blank" rel="noopener noreferrer">Makefile</a> là một công cụ giúp ta có thể dễ dàng
thực thi các các khối lệnh mà không cần nhờ tới ngôn ngữ lập trình.
Mặc dù `Make` được sử dụng rất rộng rãi trên Unix, Linux hay MacOS, thì trên Windows chắc vẫn còn hiếm hoi.
Trên Windows, ta thường file `.bat` để thực thi các khối lệnh,
tuy nhiên các file này chỉ thực thi được trên môi trường Windows.

Vậy làm sao để thực thi các khối lệnh trên nhiều hệ điều hành với cùng một file mã nguồn?
Thật may mắn là ta có thể sài được lệnh `Make` trên Windows với gói phần mềm
<a href="http://gnuwin32.sourceforge.net/packages/make.htm" target="_blank" rel="noopener noreferrer">`GnuWi32 - Make for Windows`</a>

Trước tiên ta cần tải về gói cài đặt tại [đây](http://gnuwin32.sourceforge.net/downlinks/make.php),
sau đó click vào file cài đặt đã tải về và cài đặt tương tự như các phần mềm khác.

Sau đó, ta cần cấu hình lại đường dẫn cho biến môi trường `Path`
để có thể sài lệnh `make` ở bất kì đâu trong hệ thống.
Ví dụ, ta cài đặt `Make` tại: `C:\Program Files\GnuWin32`, thì `Path` sẽ có dạng như sau:

```
Path := C:\Program Files\GnuWin32\bin;Path
```

Tới đây là ta có thể sử dụng ngon lành lệnh `make` giống như trên Linux rồi:
```
$ make -v
Copyright (C) 2006  Free Software Foundation, Inc.
これはフリーソフトウェアです. 利用許諾についてはソースを
ご覧ください.
商業性や特定の目的への適合性の如何に関わらず, 無保証です.

This program built for i386-pc-mingw32
```
