---
title: "[Gitlab] Đồng bộ giữa Gitlab và Github"
slug: sync-gitlab-github
date: 2021-03-04
categories:
  - Lập Trình
  - Git
tags:
  - Git
  - Gitlab
keywords:
  - Git
  - Gitlab
  - Github
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/code/git.png
metaAlignment: center
---

Gần đây mới biết một tính năng rất thú vị trên Gitlab là cho phép đồng bộ mã nguồn với các repo ở các nền tảng khác nhau như Github, Bitbucket. Dựa vào tính năng này có thể giúp ta lưu trữ được mã nguồn cùng lúc ở nhiều nơi mà không tốn nhiều công. Việc lưu mã nguồn ở nhiều nơi có 1 lợi thế rất lớn là chẳng may nền tảng nào phát sinh vấn đề như anh Github thi thoảng lại die thì vẫn có thể chuyển ngay qua nền tảng khác để sử dụng.

Tính năng này được gọi là mirroring, thao tác cực kì đơn giản. Trong bài viết này, mình sẽ ghi lại cách để đồng bộ được code giữa Gitlab và Github.

Đầu tiên, vào Github để tạo ra personal token nhằm mục đích thay thế password thật khi thao tác với API của Github. Để vào được chức năng này ta có thể vào menu: `Settings` ==> `Developer settings` ==> `Personal access tokens` ==> Ấn vào nút `Generate new token`. Hoặc bạn có thể truy cập nhanh vào đường dẫn: [https://github.com/settings/tokens/new](https://github.com/settings/tokens/new). Màn hình lúc này sẽ như bên dưới:

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/gitlab/github-token.png" title="Generate Github Token" >}}

Tại màn hình này, ta nhập vào mục Note để dễ nhớ Token sau đó click **chọn toàn bộ** mục `repo` như trên hình trên. Sau đó kéo xuống dưới, ấn vào nút `Generate token`. Khi đó Github sẽ sinh ra 1 token mới cho bạn.

Bước tiếp theo, vào repo mong muốn đồng bộ trên Gitlab và vào mục `Settings` ==> `Repository`. Tại đây, mở mục `Mirroring repositories` ra như hình bên dưới:

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/gitlab/gitlab-mirror.png" title="Mục cấu hình font cho terminal tích hợp" >}}

Tại mục này, ta nhập:

- `Git repository URL`: Link Repo trên Github với định dạng `https://YOUR-NAME/@github.com/YOUR-GROUP/YOUR-PROJECT.git`
- `Mirror direction`: chọn `Push` để đồng bộ cho Github, hoặc `Pull` để đồng bộ từ Github
- `Password`: nhập token được sinh ra bên Github vào

Nhập xong thì ấn nút `Mirror repository` để lưu lại. Gitlab mặc định là cứ 5 phút sẽ đồng bộ 1 lần, giờ muốn test thử luôn việc đồng bộ có được hay không thì ta chỉ việc ấn vào nút đồng bộ ngay là sẽ được.
