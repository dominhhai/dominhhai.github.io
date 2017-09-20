---
title: "[SQL] Tạo lượng lớn dữ liệu test"
slug: sql-test-data
date: 2017-09-20
categories:
- Lập Trình
- SQL
tags:
- SQL
keywords:
- SQL
- sql test data
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: /images/sql.png
metaAlignment: center
---
Ta thường xuyên cần một lượng vừa đủ các dữ liệu để test và dev trong quá trình phát triển hệ thống.
Để làm việc này ta có thể viết code để migrate và seed dữ liệu.
Tuy nhiên ta cũng có thể sử dụng chính lệnh SQL để tạo dữ liệu cực kì đơn giản.

Trước hết ta phân tách bài toán của ta thành 2 phần riêng biệt là:

  1. Tạo một lượng lớn dữ liệu
  2. Làm dữ liệu mang tính ngẫu nhiên

Trong bài viết này, ta sẽ đi cụ thể từng vấn đề một nhằm tạo ra được một lượng lơn dữ liệu test ngẫu nhiên.

### 1. Tạo một lượng dữ liệu
Giả sử ta có bảng dữ liệu `item` được tạo bằng câu lệnh sau:
```sql
CREATE TABLE item (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(10),
  description VARCHAR(30),
  price INT UNSIGNED,
  created_at DATETIME
);
```

Lúc này để tạo một số lượng lớn bản ghi cho bảng dữ liệu này,
ta có thể sử dụng lệnh `INSERT` mặc định như sau:
```sql
INSERT INTO item () VALUES (); -- 1 bản ghi
INSERT INTO item (id) SELECT 0 FROM item; -- 2 bản ghi
INSERT INTO item (id) SELECT 0 FROM item; -- 4 bản ghi
INSERT INTO item (id) SELECT 0 FROM item; -- 8 bản ghi
INSERT INTO item (id) SELECT 0 FROM item; -- 16 bản ghi
INSERT INTO item (id) SELECT 0 FROM item; -- 32 bản ghi
```
Mỗi một lần thực hiện lệnh `INSERT` như trên ta sẽ có một số lượng gấp đôi dữ liệu.
Tức là sau `n` lần, ta sẽ có `2 ^ (n - 1)` bản ghi.
Như vậy, để tạo một số lượng dữ liệu nhất định nào đó,
ta có thể tính toán số lệnh `INSERT` cần thực thi rồi chạy 1 lần là xong.

Giờ ta đã có một số lượng cần thiết các dữ liệu rồi,
tuy nhiên các dữ liệu đó đều giống nhau cả và mang giá trị mặc định của từng trường dữ liệu.
Bước tiếp theo là cần làm cho chúng khác nhau một cách ngẫu nhiên.

### 2. Làm dữ liệu mang tính ngẫu nhiên
Để tạo dữ liệu ngẫu nhiên cho các bản ghi đó,
trước hết ta cần biết cách tạo dữ liệu ngẫu nhiên riêng biệt cho từng trường một.

Với `INT`
```sql
-- 1~100
CEIL(RAND() * 100)
```

Với `VARCHAR` hay `TEXT`
```sql
-- độ dài là 10
SUBSTRING(MD5(RAND()), 1, 10)
```

Với `DATE`
```sql
-- trong vòng 1 năm từ 19/9/2917
DATE_ADD('2017-09-19', INTERVAL 365*RAND() DAY)
```

Với `DATETIME`
```sql
-- trong vòng 31 ngày từ 20/9/2017 00:00:00
ADDTIME(CONCAT_WS(' ','2017-09-20' + INTERVAL 31*RAND()  DAY, '00:00:00'), SEC_TO_TIME(FLOOR(0 + (86401*RAND()))))
```

Với những cách tạo dữ liệu như trên,
ta có thể kết hợp chúng lại với lệnh `UPDATE` để tạo ra dữ liệu ngẫu nhiên.
```sql
UPDATE item SET
  name        = CONCAT('prod ', id),
  description = SUBSTRING(MD5(RAND()), 1, 30),
  price       = CEIL(RAND() * 10000),
  created_at  = ADDTIME(CONCAT_WS(' ','2017-09-20' + INTERVAL 31*RAND()  DAY, '00:00:00'), SEC_TO_TIME(FLOOR(0 + (86401*RAND()))))
;
```

Tới đây, ta đã có được một bộ dữ liệu test tương đối lớn và mang tính ngẫu nhiên.
