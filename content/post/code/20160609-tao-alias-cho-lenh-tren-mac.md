---
title: "[Terminal] Tạo Alias cho lệnh trên MacOS"
slug: alias-for-command-on-macos
date: 2016-06-09
categories:
- Lập Trình
- Terminal
tags:
- Terminal
keywords:
- Command Alias
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //res.cloudinary.com/dominhhai/image/upload/code/terminal.jpg
metaAlignment: center
---
Để tạo được tên thay thế (alias) cho các lệnh trên Mac khá đơn giản. Ta chỉ cần thêm các lệnh alias vào file `.bash_profile` tại thư mục `home` là OK. Trường hợp máy chưa có file `.bash_profile` thì ta có thể tạo mới file này là OK.

{{< image classes="fancybox nocaption center clear" src="//res.cloudinary.com/dominhhai/image/upload/code/cli-alias1.png" title=".bash_profile" >}}

Lệnh tạo alias:

```
alias YOUR_ALIAS='YOUR_COMMAND'
```

Ví dụ ta tạo alias cho lệnh `react-native` với tên là `rn` như sau:

```
alias rn='react-native'
```

{{< image classes="fancybox nocaption center clear" src="//res.cloudinary.com/dominhhai/image/upload/code/cli-alias2.png" title="alias" >}}

Vì ta chỉ tạo alias chứ không thay đổi câu lệnh nên là vẫn có thể sài được lệnh cũ sau khi đã được tạo alias. Như ở ví dụ trên ta có thể sử dụng đồng thời lệnh `rn` và `react-native` mà không gặp phải bất kì vấn đề nào cả.

{{< image classes="fancybox nocaption center clear" src="//res.cloudinary.com/dominhhai/image/upload/code/cli-alias3.png" title="using" >}}

Sau khi thêm alias vào file `.bash_profile`, ta cần khởi động lại môi trường dòng lệnh. Để khởi động lại có nhiều cách, có thể là tắt terminal đi và bật lại hoặc có thể chạy với lệnh:

```
$ source ~./bash_profile
```

Have fun!
