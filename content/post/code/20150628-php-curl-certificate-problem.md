---
title: "[PHP] Lỗi Cetificate của Curl trong PHP"
slug: php-curl-cetificate-error
date: 2015-06-28
categories:
- Lập Trình
- PHP
tags:
- PHP
keywords:
- PHP
- PHP Curl
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //res.cloudinary.com/dominhhai/image/upload/code/php.png
metaAlignment: center
---
### Lỗi `SSL certificate problem: unable to get local issuer certificate` cho PHP curl

Chả là hôm rồi có sử dụng thư viện [`curl`](http://php.net/manual/en/book.curl.php) của PHP để gọi dịch vụ Restful Service của bên thứ 3 từ server PHP của mình thì gặp chút rắc rối nên giờ viết lại cho khỏi quên.

Chắc mọi người cũng biết lệnh [`curl`](http://linux.about.com/od/commands/l/blcmdl1_curl.htm) của linux là một lệnh khá mạnh mẽ dùng để kết nối, gửi hay lấy dữ liệu với một máy chủ nào đó, và nó hỗ trợ nhiều kiểu giao thức khác nhau như `HTTP`, `HTTPS`, `FTP`, `GOPHER`, `DICT`, `TELNET`, `LDAP` hay `FILE`. Với ngôn ngữ `PHP` lệnh này chính thức được hỗ trợ từ phiên bản `PHP 4.0.2`. Với việc hỗ trợ này, ta có thể dễ dàng biến máy chủ của ta thành một máy client để gọi dịch vụ từ các máy chủ khác một cách dễ dàng hơn.

Trong bài viết này mình sử dụng hệ điều hành Windows, có cài [`git bash`](https://git-scm.com/downloads) và PHP 5. Khi nào test trên các môi trường khác thì mình sẽ cập nhập tiếp. Mình cũng sẵn sàng đón nhận sự góp ý của các bạn để bài này được hoàn thiện hơn.

Về cơ bản, sử dụng thư viện `curl` không có gì khó khăn, nhưng nếu không biết thì debug khá là mệt. Để debug với `curl` thì mình sử dụng cách log lại thực thi lệnh này với file log. Ví dụ như đoạn mã sau:

```php
// khởi tạo với URL là `https://xxx/api/info`
$ch = curl_init("https://xxx/api/info");

// cấu hình kết nối
curl_setopt_array($ch, array(
  // phương thức `POST`
  CURLOPT_CUSTOMREQUEST => 'POST',
  // header
  CURLOPT_HTTPHEADER    => array(
    'Content-type: application/json; charset=utf-8',
    'XXX-key: 35036708522-6826-28-623525727927929276276222',
    'XXX-signature: gaaJLJLFJ=323r=+3252sfaHLlqajlaJ',
    'XXX-timestamp: 2015-06-28 19:07:10',
  ),
  // lấy dữ liệu trả về dạng text
  CURLOPT_RETURNTRANSFER => true,
  // dữ liệu `POST`
  CURLOPT_POSTFIELDS => '{"name":"dominhhai","pass":"xxx-xxx-xxx"}'
));

// file log `curl.log` nằm tại thư mục relative là `../tmp/`
$fp = fopen('../tmp/curl.log', 'a');

// cho phép `curl` xuất thông tin về kết nối
curl_setopt($ch, CURLOPT_VERBOSE, true);
// xuất thông tin lỗi ra file log
curl_setopt($ch, CURLOPT_STDERR, $fp);

// thực thi kết nối
$result = curl_exec($ch);

// đóng kết nối
curl_close($ch);
// đóng file log
fclose($fp);

// in thông tin kết quả trả về
var_dump($result);
```

Sau khi thực hiện đoạn mã trên mình thấy chương trình luôn trả về lỗi là `60` và mình để ý file log có đoạn lỗi sau:

```php
* SSL certificate problem: unable to get local issuer certificate
* Closing connection 0
```

Ngồi tra tẹo thì cần phải cấu hình định danh được máy khách cho lệnh `curl` thông qua thông tin `curl.cainfo` ở file `php.ini`. Trường hợp của mình sử dụng `git bash` cài sẵn vào Windows nên mình sử dụng luôn file certificate này của `git bash`. File này là `C:\Program Files (x86)\Git\bin\curl-ca-bundle.crt`, nên mình cần thêm đoạn mã sau vào file `php.ini`.

```php
curl.cainfo="C:\Program Files (x86)\Git\bin\curl-ca-bundle.crt"
```

Với các trường hợp khác ta cũng có thể làm tương tự, miễn sao máy có cài lệnh `curl` là có thể tìm được đường dẫn tới file định danh này.

## Tham khảo
1. http://php.net/manual/en/book.curl.php
2. http://qiita.com/iakio/items/71536dc5e615f03433a0
