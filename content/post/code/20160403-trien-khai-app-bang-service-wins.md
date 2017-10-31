---
title: "[Node.js] Triển khai dịch vụ Node.js trên Windows"
slug: deploy-nodejs-on-windows
date: 2016-04-04
categories:
- Lập Trình
- Node.js
tags:
- Windows
keywords:
- Node.js Deploy
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //res.cloudinary.com/dominhhai/image/upload/code/nodejs_svg.svg
metaAlignment: center
---
Để triển khai ứng dụng Node.js bằng Windows, ta có nhiều phương án như dưới đây:

1. Sử dụng [forever](https://github.com/foreverjs/forever)
2. Sử dụng [issnode](https://github.com/tjanczuk/iisnode)
3. Sử dụng [NSSM](https://nssm.cc/)

Cả 3 softwares trên đều có hướng dẫn rất chi tiết trên trang chủ tương ứng, nhưng ta nên chọn cái nào để triển khai ứng dụng? Trong bài này ta sẽ liệt kê 1 vài điểm mạnh yếu của chúng.
<!--more-->

|     | Tên     | Điểm mạnh  | Điểm yếu  |
| --- | ------- | ----- | ----- |
|  1  | forever | Lệnh đơn giản, có API phong phú. | Lăn ra chết nếu logoff khỏi server, mà sau khi thoát remote khỏi server vài phú là server logoff ngày được.|
|  2  | issnode | Có API, sử dụng ISS của Wins để chạy nên quản lý tiến trình rất tốt, được Microsoft khuyến khích sử dụng. | Lệnh hơi phức tạp, cài đặt node modules khó khăn vì không chơi `npm` được. |
|  3  | NSSM    | Lệnh cực kì đơn giản, chạy service rất ngon | Không sử dụng ISS để quản lý tiến trình được, mà chỉ đơn giản là chạy chương trình node bằng service wins thôi. Và cũng không có API luôn. |

Như vậy trên Windows, khả thi vẫn là chọn `issnode` hoặc `NSSM` mà tốt nhất là `issnode`. Tuy nhiên do không cài đặt trực tiếp từ `npm` đơn giản được nên cũng khá vất vả, thậm chí các module dạng node add-on còn có trường hợp không cài đặt được ví dụ như `node-oracledb` chẳng hạn.
Nên với các trường hợp không chơi `issnode` được ta phải sử dụng `NSSM`.

`NSSM` chỉ đơn giản là 1 chương trình giúp ta đăng kí, quản lý các phần mềm trên Windows chạy như Windows service. Như vậy các chương trình viết bằng nodejs thực chất ta đăng kí và quản lý `Node.js` với tham số chạy của `Node.js` là chương trình tương ứng chứ không phải là quản lý chương trình của của mình. Điểm may là `NSSM` chạy bằng dòng lệnh nên ta hoàn toàn có thể viết wrapper bằng chương trình node để chạy được các lệnh này. Các bạn có thể tham khảo 1 đoạn mã nhỏ mình viết sẵn để sử dụng được `NSSM` [ở đây](https://github.com/dominhhai/node-nssm).

Nếu không khoái viết script cho chương trình thì có thể sử dụng `.bat` file cũng rất tiện lợi.
```
@echo off
echo Uninstall Service ...
nssm stop <SERVICE_NAME>
nssm remove <SERVICE_NAME>

echo Install Service ...
nssm install <SERVICE_NAME> "node"

echo Setting Parameters ...
nssm set <SERVICE_NAME> AppDirectory "path\to\app"
nssm set <SERVICE_NAME> AppParameters "index.js"
nssm set <SERVICE_NAME> AppEnvironmentExtra "NODE_ENV=production"
nssm set <SERVICE_NAME> AppStdout "path\to\logs\nssm_out.log"
nssm set <SERVICE_NAME> AppStderr "path\to\logs\nssm_err.log"

echo Start Service ...
nssm start <SERVICE_NAME>

timeout 10
```
