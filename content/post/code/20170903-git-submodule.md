---
title: "[Git] submodule - cùng lúc sài nhiều repo"
slug: git-submodule-multi-repo
date: 2017-09-03
categories:
- Lập Trình
- Git
tags:
- Git
keywords:
- Git
- git submodule
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/git.png
metaAlignment: center
---
Đôi lúc ta cần phải sử dụng các repo khác như là một module của dự án hiện tại,
nhưng ta lại muốn quản lý nó riêng biệt giống như việc sử dụng các trình quản lý
gói như `npm` chẳng hạn.
Lúc này ta có thể sài <a href=“https://git-scm.com/docs/git-submodule” target=“_blank”>git submodule</a> để quản lý các module từ các repo khác.
Ví dụ, blog của mình được xây dựng với theme <a href="https://github.com/kakawait/hugo-tranquilpeak-theme" target="_blank" rel="noopener noreferrer">tranquilpeak</a>
và mình cần đưa theme này vào thư mục `themes` của dự án.
Lúc này mình có thể thoải mái làm việc với mã nguồn dự án mà không ảnh hưởng gì tới theme được lấy về. Ngoài ra còn có thể cập nhập theme với các commit mới nhất nữa.
Hệt như việc sử dụng các trình quản lý gói, rất đơn giản và tiện lợi.

```
$ ls themes
tranquilpeak

$ cd themes/tranquilpeak
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
```

# 1. Thêm module
Để thêm một module, ta dùng lệnh sau:
```
$ git submodule add <repository> [<path>]
```
Trong đó:

 * `repository` - địa chỉ của repo cần lấy về
 * `path` - đường dẫn tới thư mục lưu repo. Nếu ta không chỉ định đường dẫn thì, repo sẽ mặc định được lưu vào thư mục có tên giống với tên repo.

Ví dụ, mình thêm XXX theme vào blog, của mình như sau:
```
$ git submodule add https://github.com/kakawait/hugo-tranquilpeak-theme.git themes/tranquilpeak

```
Sau khi chạy lệnh trên, ta sẽ xem thư mục của ta có gì thay đổi:
```
$ git status
On branch dev
Your branch is up-to-date with 'origin/dev’.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   .gitmodules
	new file:   themes/tranquilpeak
```
Như vậy là ta đã thêm 2 file là `.gitmodules` và `tranquilpeak ` trong thư mục `themes`.

`.gitmodules` là nơi chứa thông tin của các module được đưa thêm vào dự án của ta.
Kiểm tra xem nội dung của file này xem sao:
```
$ cat .gitmodules
[submodule "themes/tranquilpeak"]
	path = themes/tranquilpeak
	url = https://github.com/kakawait/hugo-tranquilpeak-theme.git
```
Ở đây, `path` là nơi module được lưu và `url` là địa chỉ của repo.
Với mỗi một module, ta sẽ có 3 dòng thông tin để xác định module như vậy.

Còn `themes/tranquilpeak` sẽ chưa thông tin về commit hiện tại của repo ở local của bạn.

# 2. Cập nhập module
Khi cần cập nhập module, ta dùng lệnh:
```
$ git submodule update [--init]
```

Lựa chọn `--init` sẽ cho phép ta cập nhập các module chưa được lấy về.
Ví như ở máy tính của bạn, bạn chạy lệnh `add` để lấy repo về rồi,
thì không cần `--init` nữa.
Còn ở các máy tính khác, repo chưa được lấy về,
thì ta cần phải thêm lựa chọn này.
Tức là repo phải có sẵn trong máy rồi mới update được.

Ngoài ra, với các dự án mới khi được tải về thì các module sẽ không tự động tải về mà ta phải tải repo chính rồi chạy lệnh cập nhập thì mới được.
Tuy nhiên, sự thật không phũ phàng tới vậy,
ngay ở lệnh tải về ta có thể lấy ngay được về các module với lựa chọn `--recursive`

```
$ git clone --recursive https://github.com/dominnhhai/dominhhai.github.io.git
```

Tuy nhiên, cần lưu ý một điểm là nếu muốn cập nhập trạng thái mới nhất của
các module đã được lấy về thì ta cần phải cập nhập với lệnh `git pull`
hệt như các dự án bình thường khác.
Ví dụ dưới đây sẽ cập nhập toàn bộ các module hiện có của dự án:

```
$ git submodule foreach git pull origin master
```

# 3. Xoá module
Với các repo không cần nữa, ta có thể xoá bỏ nó đi bằng lệnh:
```
$ git rm <path>
```

Ví dụ:
```
$ git rm themes/tranquilpeak
```

# 5. Kết luận
`git submodule` cho phép ta có thể quản lý được các repo khác được sử dụng ở repo dự án chính như cách ta sử dụng trình quản lý gói.
Tuy nhiên ta cần lưu ý khi đồng bộ module giữa các máy khác nhau.
Một repo được thêm vào hay xoá đi, hay được cập nhập thì chỉ cập nhập trên máy thực hiện thao tác đó.
Vì thế, nếu ta muốn mọi người cùng cập nhập thì cần thông báo cho mọi người biết để cập nhập với lệnh `git submodule update` hoặc với dự án mới tải về thì `git clone —recursive`.

