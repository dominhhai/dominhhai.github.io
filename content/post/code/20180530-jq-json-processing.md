---
title: "[Terminal] JSON trên dòng lệnh với JQ"
slug: jq-json-processing
date: 2018-05-30
categories:
- Lập Trình
- Editor
tags:
- Editor
- jq
keywords:
- json processing
- jq
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/terminal.jpg
metaAlignment: center
---
Mỗi lần lấy kết quả dạng JSON về trên dòng lệnh là 1 lần ức chế bởi các mục muốn xem thì cứ hiển thị dạng nửa vời. Nên trong đầu nảy ra là làm sao mà xem được toàn bộ kết quả ngay trên dòng lệnh. Đương nhiên là nếu thao tác như lọc kết quả, thống kế kết quả... nữa thì tốt.
<!--more-->

```
{ GetMatchingProductResponse:
   { '$':
      { xmlns: 'http://mws.amazonservices.com/schema/Products/2011-10-01' },
     GetMatchingProductResult: [ [Object], [Object], [Object], [Object], [Object] ],
     ResponseMetadata: [ [Object] ] } }
```

Thật may là có sẵn gói phần mềm [`jq`](https://stedolan.github.io/jq/) hỗ trợ việc xử lý JSON trên cả kì vọng của mình.

<!--toc-->

# 1. Cài đặt
Do `jq` được viết bằng C nên rất dễ cài đặt đa nền tảng. Ta có sẵn các gói build sẵn để cài đặt tuy nhiên do đây là sản phẩm nguồn mở nên ta hoàn toàn có thể tự build cho máy tính của mình.

Với MacOS thì ta có thể cài đặt khá đơn giản với [Homebrew](https://brew.sh/):

```
$ brew install jq
$ jq --version

jq-1.5
```

Còn với các nền tảng khác như Windows, Linux thì bạn có thể tham khảo thêm phần cài đặt trên [trang chủ](https://stedolan.github.io/jq/download/) nhé.

# 2. Cách sử dụng
Về cơ bản `jq` được sử dụng tương tự như lệnh `grep`. Chỉ khác chỗ đầu vào của `jq` là một luồng dữ liệu dạng JSON. Ta sẽ lấy 2 ví dụ để minh hoạ `jq` cho kết quả ngon thế nào nhé.

Ví dụ 1, khi chưa sài `jq`:
```
$ echo '{"locations":[{"id":1,"name":"Hà Nội"},{"id":2,"name":"Hồ Chí Minh"}]}'


{"locations":[{"id":1,"name":"Hà Nội"},{"id":2,"name":"Hồ Chí Minh"}]}
```

Ví dụ 2, sau khi sài `jq`:
```
$ echo '{"locations":[{"id":1,"name":"Hà Nội"},{"id":2,"name":"Hồ Chí Minh"}]}' | jq

{
  "locations": [
    {
      "id": 1,
      "name": "Hà Nội"
    },
    {
      "id": 2,
      "name": "Hồ Chí Minh"
    }
  ]
}
```

Giờ nhìn đẹp và gọn hơn nhiều rồi!

# 3. Các lệnh
Các lệnh và cách sử dụng bạn có thể rất dễ dàng đọc được tại phần hướng dẫn ngay trên [trang chủ](https://stedolan.github.io/jq/manual/).


