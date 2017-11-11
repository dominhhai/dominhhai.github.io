---
title: "[Node.js] Cập nhập Nodejs và npm"
slug: upgrade-node-npm
date: 2015-10-18
categories:
- Lập Trình
- Node.js
tags:
- Node.js
keywords:
- Node.js Upgrade
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/nodejs_svg.svg
metaAlignment: center
---
Thi thoảng lại có bạn hỏi làm sao cập nhập Nodejs và npm, nên làm bài ngắn gọn vài lệnh này để dành cho các bạn mới vào nghề Nodejs.
<!--more-->

# 1. Cập nhập nodejs
Đầu tiên cứ kiểm tra xem phiên bản nodejs hiện giờ là bao nhiêu đã nhé, biết đâu đang bản mới nhất rồi thì sao ^^.

```
$ node -v
```

Sau đấy mới cập nhập nodejs.

```
$ sudo npm cache clean -f
$ sudo npm install -g n
$ sudo n stable
$ node -v
```

# 2. Cập nhập npm

```
$ sudo npm install -g npm
```

Để rút gọn việc gõ các lệnh trên mình có tạo 1 file bash:

{{< gist dominhhai a767b55e460125ea9c267f74d3868ea1 >}}

Chúc các bạn tuần làm việc mới vui vẻ.
