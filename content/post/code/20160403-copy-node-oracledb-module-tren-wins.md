---
title: "[Node.js] Copy Node OracleDB Module trên Windows"
slug: copy-node-oracledb-on-windows
date: 2016-04-03
categories:
- Lập Trình
- Node.js
tags:
- Windows
- OracleDB
keywords:
- Node.js OracleDB
- OralceDB Windows
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //res.cloudinary.com/dominhhai/image/upload/code/nodejs.png
metaAlignment: center
---
Trong bài [Chạy Oracle DB trên Nodejs](https://dofeet.wordpress.com/2016/03/27/node-oracledb-chay-oracle-db-tren-nodejs/) mình đã viết lại quá trình cài đặt node-oracle trên wins, thì bài này sẽ tập trung vào việc triển khai node-oracle khi deploy ứng dụng.

Việc cài đặt node-oracledb không đơn giản tẹo nào khi ta phải cài thằng Visual Studio mất tới 20 phút rồi. Nếu việc này mà lặp lại lần nữa khi muốn deploy hay dev trên một máy khác thì đúng là ác mộng. Nhưng thật may node-oracledb cho phép ta [copy các bản đã build sẵn sang các máy khác](https://github.com/oracle/node-oracledb/blob/master/INSTALL.md#winbins) với các điều kiện sau:

1. Node.js: Cùng kiến trúc và phiên bản
2. Oracle Instant Client: Cùng kiến trúc và phiên bản
3. Cài sẵn Visual Studio Redistributable

Việc cài đặt Node.js và Instant Client thì đã được trình bày ở [bài viết trước](https://dofeet.wordpress.com/2016/03/27/node-oracledb-chay-oracle-db-tren-nodejs/), nên bài này sẽ đề cập các đoạn tiếp theo.

Vì node-oracledb chạy bằng việc bind mã C++ trên với Windows ta phải cài Visual Stuido Redistribute - một thư viện khá nhẹ để chạy được các chương trình C/ C++ trên Windows. Về cơ bản ta có thể cài phiên bản Visual Studio Redistribute 2010 là có thể chạy được các phiên bản Oracle Instant Client 12.x trở về trước. Khi cài đặt VC 2010, ta cần lưu ý chọn phiên bản cho đúng với máy tính hiện hành, ví dụ máy 64 bit thì cần tải bản 64 bit để cài đặt. Việc cài đặt gói này cực kì đơn giản mất chưa tới 3 phút là cài xong, cực kì nhẹ nhàng chứ không vất vả như thằng Visual Studio 0_0.

Sau khi chuẩn bị xong các phần mềm, ta cần phải tiến hành đặt biến môi trường nhằm giúp node-oracle nhận diện được Instant Client hiện có. Việc cài đặt này cũng tương tự như ở bài viết trước, có điều ta không cần tạo biến môi trường link tới sdk nữa. Ta chỉ cần link tới thư mục home của Instant Client là đủ bằng cách thêm thư mục home này vào biến môi trường `Path` của hệ thống:

> `Path: C:\Oracle\instantclient;...`

Nếu cần sử dụng file ` tnsnames.ora` để kết nối thì ta cần thêm biến môi trường `ORACLE_HOME` vào biến môi trường nữa là xong.

> `ORACLE_HOME: D:\Oracle\product\12.1\client`

Sau khi chuẩn bị xong môi trường như trên, ta chỉ việc copy module `oracledb` từ thư mục `node_modules` của máy này sang `node_modules` của máy khác là OK.

Việc cài đặt khá là nhẹ nhàng nhỉ :D , trong bài viết sau mình sẽ viết tiếp về việc triển khai ứng dụng có sử dụng node-oracledb bằng service của Wins.
