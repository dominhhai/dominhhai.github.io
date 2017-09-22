---
title: "[Node.js] Cài đặt Node OracleDB trên Windows"
slug: install-node-oracledb-on-windows
date: 2016-03-28
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
Bài viết này nhằm mục tiêu lưu lại 1 ngày vất vả vật lộn với cái [node-oracledb](https://github.com/oracle/node-oracledb) trên con Windows Server 2008 của mình.

### Môi trường có sẵn

* Windows Server 2008, 64 bit.
* Oracle Client 11.2
* Visual Studio 2012

### Cài đặt
1. [Node v01.2.x](https://nodejs.org/dist/v0.12.9/)
2. [Python 2.7](https://www.python.org/downloads/) (nhớ chọn thiết lập biến môi trường)
3. [Oracle Instant Client v12.x](http://www.oracle.com/technetwork/database/features/instant-client/index-100365.html)

Để cài đặt Oralce Instant Client v12.x, ta cần tải 2 gói `basic` và `sdk` từ [đây](http://www.oracle.com/technetwork/database/features/instant-client/index-100365.html). Sau khi download Oracle Instant Client, cần giải nén ra một thư mục nào đó như: `C:\Oracle\instantclient`. Sau đó ta cần thiết lập biến môi trường cho hệ thống (System Environment Variables) như sau:

##### Instant Client Home
```
Path: C:\Oracle\instantclient;...
```

##### Instant Client SDK
```
OCI_LIB_DIR=C:\oracle\instantclient\sdk\lib\msvc
OCI_INC_DIR=C:\oracle\instantclient\sdk\include
```

Sau đó ta chỉ việc cài gói node-oracledb bằng lệnh `npm` như sau:

```
$ npm install oracledb --save
```

Với __đúng__ môi trường và chỉ dẫn như trên bạn có thể cài đặt được node-oracledb thành công.

### Lưu ý
#### Python
Cần cài đúng phiên bản `2.7` vì [node-gyp](https://github.com/nodejs/node-gyp) chưa hỗ trợ dịch các add-on native của Node với phiên bản Python cao hơn.

#### Visual Studio và Node
Đây chính là điểm mà mình mắc phải. Cần phải cài phiên bản Node khớp với VS. Node add-on được xây dựng trên C++ nên khi dịch cần phải có môi trường dịch và thực thi C++ phù hợp. Với Visual Studio 2012, ta không dịch được Node `4.x` và `5.x`. Muốn dịch được Node `4.x` trở nên ta cần phải cài đặt [Visual Studio 2015](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx) (có thể sử dụng bản Comunity cũng được). Do đặc điểm môi trường của mình có sẵn VS 2012 nên mình phải cài đặt Node v0.12.x. Do là máy công ty nên không thể nào tự ý nâng cấp được. Dùng Node v0.12.x hơi chán vì nhiều module giờ không còn hỗ trợ nữa nên lúc lập trình hơi nhọc nhằn ;( .

#### Oracle Instant Client
Cần cài đặt đúng phiên bản 64 hoặc 32 bit tương ứng với môi trường hệ điều hành. Ví dụ như mình sử dụng 64 bit nên cần cài đặt đúng gói 64 bit là: `instantclient_basic-windows.x64-12.1.0.2.0.zip` và `instantclient_sdk-windows.x64-12.1.0.2.0.zip`.

Sau khi cài đặt xong vì thằng Instant Client chiếm mất đường dẫn môi trường Oracle Client cũ nên thằng [SI Object Browser for Oracle](https://www.seshop.com/special/systemintegrator/siob_oracle/) lăn đùng ra chết do `ori.dll` phiên bản của nó bị thành của Instant Client mất rồi. Lúc này mình config thêm biến `ORACLE_HOME` và trỏ đường dẫn biến này cho SI thế là lại chạy ngon lành.

Cài đặt mất nguyên 1 ngày của mình, tù thật. Nhưng cũng học được thêm là cần chú ý tới môi trường C++ hiện có với việc chọn phiên bản Node phù hợp. Hi vọng bài viết bổ ích cho các bạn có ý định cài `node-oracle` hay các add-on native module khác.

### Thông tin
Do việc cài đặt các gói add-on native trên Windows quá vất vả vì phải cài đặt thằng VS quá nặng nhọc (3GB bộ nhớ và 30 phút cài đặt). Nên nhóm phát triển Node của Microsoft đang phát triển 1 bản cài đặt gọn của VS chỉ gồm các gói C++ tên là [Visual C++ Build Tools](https://www.microsoft.com/en-us/download/details.aspx?id=49983). Gói VC++ này hiện vẫn đang được phát triển và chưa được hoàn thiện nên vẫn còn có thể phát sinh lỗi khi cài.

### Tham khảo
1. [Install node-oracledb for windows](https://github.com/oracle/node-oracledb/blob/master/INSTALL.md#instwin)
2. [win,build: support Visual C++ Build Tools 2015](https://github.com/nodejs/node/pull/5627)
3. [Ví dụ với ExpressJS](https://github.com/dominhhai/express-oracledb)
