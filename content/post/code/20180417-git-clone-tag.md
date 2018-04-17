---
title: "[Git] Lấy mã nguồn theo tag"
slug: git-clone-tag
date: 2018-04-17T09:28:28+09:00
categories:
- Lập Trình
- Git
tags:
- Git
keywords:
- Git, Git Clone Tag
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/git.png
metaAlignment: center
---
Bài này nhằm mục đích note lại cách lấy mã nguồn theo tag với Git. Ví dụ ở đây tôi có dự án [koa-log4js](https://github.com/dominhhai/koa-log4js/tags) có được release với các tags:
<!--more-->

| No. | Ngày | Tag |
| --- | --- | --- |
| 1 | 20/04/2016 | [koa1](https://github.com/dominhhai/koa-log4js/releases/tag/koa1) |
| 2 | 20/04/2016 | [koa2](https://github.com/dominhhai/koa-log4js/releases/tag/koa2) |
| 3 | 23/02/2017 | [v2.2.0](https://github.com/dominhhai/koa-log4js/releases/tag/v2.2.0) |
| 4 | 18/10/2017 | [2.3.0](https://github.com/dominhhai/koa-log4js/releases/tag/2.3.0) |

Thường khi chạy lệnh `$ git clone` về thì chỉ tải được branch mặc định là `master` chẳng hạn về thôi, còn các tag kia thì ta phải tải riêng.

Lúc này để tải được riêng từng tag thì ta cần phải `fetch` toàn bộ tags về và `checkout` tạo branch mới với tag tương ứng:

```
$ git clone https://github.com/dominhhai/koa-log4js.git
$ cd koa-log4js
$ git fetch origin 'refs/tags/*:refs/tags/*'
```

Sau khi chạy lệnh `fetch` tags ở trên, ta có thể kiểm tra lại các tags hiện có bằng cách:

```
$ git tag -l
```

Sau đó ta chạy lệnh `checkout` để lấy mã nguồn của tag mong muốn. Ví dụ, lấy mã nguồn của tag `v2.2.0`:

```
$ git checkout tags/v2.2.0 -b v2.2.0
```

Lúc này, một branch mới tên là `v2.2.0` sẽ được tạo ra để chứa mã nguồn của tag `v2.2.0` tương ứng.

Một cách ngắn gọn, ta tổng kết 2 lệnh chính là `fetch` và `checkout` tags như sau:

```
$ git fetch origin 'refs/tags/*:refs/tags/*'
$ git checkout tags/[YOUR_TAG_NAME] -b [YOUR_TAG_NAME]
```

Have fun!
