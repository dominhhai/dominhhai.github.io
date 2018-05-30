---
title: "[Vim] Cấu hình cơ bản trên CentOS"
slug: vim-config
date: 2018-05-08
categories:
- Lập Trình
- Editor
tags:
- Editor
- Vim
keywords:
- Editor
- Vim
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/editor/vim.png
metaAlignment: center
---
`Vim` là một trình soạn thảo mạnh mẽ nhưng cấu hình mặc định của nó làm cho mình có chán giác ngán ngẩm vô cùng. Mã nguồn chẳng highlight cũng chẳng hiện thị số dòng nhìn rất chi ức chế >.<
<!--more-->

Vì vậy mới quyết định viết lại một số cấu hình cơ bản ở đây để còn sài cho các lần sau.

# 1. Cách cấu hình
Các file dùng để cấu hình cho `Vim` có thể được tìm thấy bằng cách gõ lệnh:
```
$ vim --version
```

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/vim/vim-ver.png" title="Vim Features" >}}

Với lệnh trên thì ta sẽ thu được 2 file cấu hình quan trọng là:

* `system vimrc file`: File cấu hình cho toàn hệ thống
* `user vimrc file`: File cấu hình cho riêng user hiện tại

Thường để an toàn và không làm phiền người khác, ta nên sử dụng file cấu hình cho user hiện tại. Về cơ bản file này được đặt ngay trong thư mục home: `$HOME/.vimrc` hay `~/.vimrc`.

# 2. Cài màu mè
Bình thường khi chạy lệnh `vim --version` xong thì ta có thể kiểm tra được các tính năng được bật/tắt. Mặc định bạn sẽ thấy dòng `-syntax` tức là chế độ highlight đang bị tắt đi. Giờ muốn hiển thị màu mè cho code thì ta cần phải bật tính năng này lên.

Để làm điều này, ta có thể cài đặt thêm gói `vim-enhanced`:
```
$ yum install vim-enhanced
```

Và ở file cấu hình `~/.vimrc`, ta thêm dòng `syntax on` vào như sau:
```
$ echo syntax on >> ~/.vimrc
```

Sau đó, chạy lại lệnh `vim --version` ta sẽ thấy dòng `+syntax` ý chỉ rằng tính năng highlight đã được bật lên.

Okey, giờ khi mở file với `Vim` ta được màn hình khá cool:
{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/vim/vim-hl.png" title="Vim Highlight" width="80%">}}

# 3. Hiển thị số dòng
Để hiển thị số dòng ta có thể thêm `set nu` vào file `~/.vimrc`:
```
$ echo set nu >> ~/.vimrc
```

Thử mở 1 file xem sao:
{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/vim/vim-ln.png" title="Vim Line Number" >}}

Còn tiếp ...
