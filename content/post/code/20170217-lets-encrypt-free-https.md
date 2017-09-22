---
title: "[Web] Cài đặt SSL miễn phí với Let's Encrypt"
slug: free-ssl-with-let-encrypt
date: 2017-02-17
categories:
- Lập Trình
- Web SSL
tags:
- Lets Encrypt
keywords:
- Lets Encrypt
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //res.cloudinary.com/dominhhai/image/upload/code/let-encrypt.svg
#thumbnailImage: //letsencrypt.org/images/le-logo-twitter.png
metaAlignment: center
---
Bài viết này hướng dẫn cài đặt [Let's Encrypt](https://letsencrypt.org/) - một dịch vụ ngon-bổ-miễn phí cho việc HTTPS hóa máy chủ. Ở đây, mình sử dụng máy chủ CentOS 7 và Nginx để thực hiện, nhưng các bạn hoàn toàn có thể làm tương tự với các môi trường khác.

Để cài đặt được `Let's Encrypt`, ta cần có môi trường `Python v2.7.x` trở lên. Nên nếu máy của bạn chưa có thì cài đặt hoặc cập nhập bản mới đi nhé.

### 1. Kiểm tra phiên bản Python
```
$ python --version
```
### 2. Kiểm tra xem ta đã mở cổng 443 hay chưa
```
$ sudo cat /etc/sysconfig/iptables
```

Nếu chưa mở cổng này thì các bạn mở nó ra nhé vì https chạy qua cổng 443 này.

### 3. Tải về certbot từ Github
```
$ git clone https://github.com/certbot/certbot
```

### 4. Chuyển qua thư mục certbot để tiện làm việc
```
$ cd certbot
```

### 5. Lấy và tạo file Cert
```
$ ./certbot-auto certonly --standalone --email EMAIL_ADDRESS_HERE -d DOMAIN_HERE
```

### 6. Kiểm tra các file cert được sinh ra
```
$ sudo ls /etc/letsencrypt/live/DOMAIN_HERE
```

### 7. Backup các file cert
```
$ sudo cp -r /etc/letsencrypt/live/DOMAIN_HERE ../sslcert
```

### 8. Cấu hình Nginx
```
$ sudo vi /etc/nginx/conf.d/default.conf
```

Nội dung:
```
...
# tự động chuyển toàn bộ url http sang https
server {
     listen  80;
     server_name  localhost;
     return 301 https://$host$request_uri;
}

#cấu hình server https
server {
    listen       443 ssl;
    server_name  localhost;
    #use fullchain.pem instead of cert.pem
    ssl_certificate         /etc/letsencrypt/live/DOMAIN_HERE/fullchain.pem;
    ssl_certificate_key     /etc/letsencrypt/live/DOMAIN_HERE/privkey.pem;
    ...
}
...
```
### 9. Khởi động lại Nginx
```
$ sudo systemctl reload nginx
```

### 10. Tự động gia hạn chứng nhận HTTPS
```
$ sudo crontab -e
```

Nội dung:
```
00 04 14 * * ~/certbot/certbot-auto renew --post-hook "systemctl restart nginx" 1 > /dev/null 2 > /dev/null
```
Ở đây mình lấy ví dụ là tự động gia hạn vào lúc 4h sáng ngày 14 hàng tháng. Tùy vào tình huống mà bạn có thể thay đổi cho linh hoạt với lịch máy chủ của mình.

Quá đơn giản phải không :x
