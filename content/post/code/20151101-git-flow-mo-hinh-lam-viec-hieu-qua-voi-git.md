---
title: "[Git] GitFlow - một mô hình làm việc hiệu quả"
date: 2015-11-01
categories:
- Lập Trình
- Git
tags:
- Git
- GitFlow
keywords:
- Git
- GitFlow
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //qiita-image-store.s3.amazonaws.com/0/53309/06140121-a0b6-427f-c149-6858c149738e.png
metaAlignment: center
---
Gần đây mới được tiếp xúc với git-flow thấy cách làm việc hay quá, muốn chia sẻ lại đôi chút. Về cơ bản git-flow là một tập hợp các lệnh mở rộng cho git nhằm hỗ trợ cho quy trình làm việc hiệu quả hơn.

・Tóm tắt: [Git-Flow Cheatsheet](http://dominhhai.github.io/git-flow-cheatsheet/index.vi_VN.html).
・Đầy đủ: [Git-Flow Repos](https://github.com/dominhhai/gitflow)

Tuy nhiên bản đầy đủ hiện giờ đang không được bảo trì nên có một số tính năng mà bạn muốn có khi lại không có ví dụ như tính năng xoá một nhánh feature chẳng hạn. Tất nhiên là bạn vẫn có thể sử dụng các lệnh thông thường của `git` để thực hiện, nhưng nếu có phần mở rộng tiện dụng hơn thì dại gì lại không dùng nhỉ. Để sử dụng thêm một số tính năng mở rộng bạn có thể sử dụng một bản fork của gitflow chính quy tại [gitflow-avh](https://github.com/petervanderdoes/gitflow-avh).

Lúc chạy mình có để ý một số thao tác muốn thực hiện khi kết thúc một giai đoạn nào đó là cùng lúc với việc xoá nhánh local thì cũng muốn xoá luôn nhánh remote. Với trường hợp vậy sử dụng thêm tham số `-F` ở lệnh finish là OK:

Feature:
```
$ git flow feature finish -F MYFEATURE
```
Release:
```
$ git flow release finish -F MYRELEASE
```

Ngoài ra, tất cả các config của git-flow đều được viết trong phần gán tag `gitflow "prefix"` ở file `.git/config`, nên trường hợp bạn muốn sửa chữa config nào đó của git-flow thì có thể sửa trực tiếp trong file này. Như bản thân mình, ban đầu gà gà đặt bừa các prefix của git-flow, sau muốn sửa lại cũng vào đây để sửa.
Tuy nhiên bây giờ mình toàn chơi mặc định của git-flow luôn cho tiện: `git flow init -d`.

Nếu nhận được nhiều request thì mình sẽ viết một bài kĩ hơn về git-flow này.
