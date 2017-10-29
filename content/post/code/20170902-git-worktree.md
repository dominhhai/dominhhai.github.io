---
title: "[Git] worktree - cùng lúc sài nhiều branch"
slug: git-worktree-multi-branchs
date: 2017-09-02
categories:
- Lập Trình
- Git
tags:
- Git
keywords:
- Git
- git worktree
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //res.cloudinary.com/dominhhai/image/upload/code/git.png
metaAlignment: center
---
<a href="https://git-scm.com/docs/git-worktree" target="_blank" rel="noopener noreferrer">git worktree</a> cho phép ta có thể sử dụng cùng lúc nhiều nhánh của repo trong cùng một thư mục dự án.
Ví dụ, blog của mình được xây dựng với <a href="https://gohugo.io/" target="_blank" rel="noopener noreferrer">Hugo</a>, trong thư mục blog của mình có thư mục `public`
là thư mục chứa các file được dịch ra từ mã nguồn blog. Còn ở phía <a href="https://github.com/dominhhai/dominhhai.github.io" target="_blank" rel="noopener noreferrer">repo trên Github</a>, mình có 2 branch là
`dev` lưu mã nguồn và `master` lưu các file chạy. Như vậy, thư mục `blog` trên máy tính của mình sẽ trỏ tới nhánh `dev`,
còn thư mục `public` sẽ trỏ tới nhánh `master`.

```
$ pwd
/Users/haidm/Projects/blog

$ git branch
* dev
  master

$ cd public && pwd
/Users/haidm/Projects/blog/public

$ git branch
  dev
* master
```

Nếu không có `worktree` thì chuyện gì sẽ xảy ra?
Ta sẽ phải tạo 2 repo dự án riêng và tách thư mục repo trên máy tính của ta ra thành 2 thư mục riêng rẽ
hoặc phải chuyển đổi qua lại giữa các branch liên tục. Hơi bất tiện phải không?
Ngoài ra, khi bạn chỉ muốn lưu tạm 1 branch nào đó để so sánh hay copy các file giữa branch này qua branch khác,
thì `worktree` cũng là một lựa chọn rất tốt.

Trong bài này, ta sẽ đề cập cách dùng và một số lệnh cơ bản của `worktree`.

# 1. Thêm nhánh
Để thêm một nhánh vào một thư mục nào đó, ta sử dụng lệnh:
```
$ git worktree add [-f] [-b <new-branch>] <path> [<branch>]
```
Trong đó:

 * `path` - đường dẫn tới thư mục bạn muốn lưu nhánh cần lấy về
 * `branch` - nhánh cần trỏ tới
 * Lựa chọn
   * `-f`, `--force` - Mặc định thì ta không thể thêm 1 nhánh mà đã được lấy về rồi, nhưng với lựa chọn này ta có thể bắt `worktree` tải về cho ta.
   * `-b <new-branch>`, `-B <new-branch>` - Thêm một nhánh `new-branch` nếu nó chưa có trên phía máy chủ. Với lựa chọn `-B` to thì ta còn có thể ép `worktree` reset branch đã đang có ở phía local.

Ví dụ: mình tạo thư mục `public` để lưu trữ các file dịch ra của blog và liên kết nó với nhánh `master`:
```
$ pwd
/Users/haidm/Projects/blog

$ git worktree add public origin/master
```
Lúc này nhánh `master` sẽ được tải về thư mục `public` của ta.
Và mọi thay đổi trong thư mục `public` sẽ chỉ ảnhh hưởng tới nhánh `master`,
còn thay đổi ngoài thư mục `public` sẽ vẫn chỉ ảnh hướng tới nhánh `dev` của ta.

Ví dụ: mình thêm file `20170902-git-worktree.md` vào thư mục `content/post/code` của blog,
và kiểm tra xem các thư mục thay đổi ra sao.

```
$ hugo new post/code/20170902-git-worktree.md
$ git status
On branch dev
Your branch is up-to-date with 'origin/dev'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    content/post/code/20170902-git-worktree.md

$ cd public
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
``` 

# 2. Liệt kê các nhánh
Để xem ta đã lấy về các nhánh nào và ở thư mục tương ứng nào thì có thể sử dụng lệnh `list`.
Ví dụ, với lệnh `add` ta đã thực hiện phía trên, ta sẽ có kết quả như sau:
```
$ git worktree list
/Users/haidm/Projects/blog         616ce09 [dev]
/Users/haidm/Projects/blog/public  cc73e0d [master]
```
Bạn để ý sẽ thấy rằng, dòng đầu tiên chính là nhánh chính trên thư mục gốc của ta,
còn các nhánh khác là nhánh mà ta thêm vào với lệnh `add`.

# 3. Xoá nhánh
Sau khi làm việc xong, ta có thể xoá nhánh đó khỏi local bằng cách xoá thư mục chứa nó
và xoá nó từ bộ quản lý git của ta.
```
$ rm -rf <path>
$ git worktree prune <path>
```
Với `path` là đường dẫn tới thư mục chứa nhánh mà ta muốn xoá.
Nếu ta chỉ chạy lệnh để xoá thư mục thôi thì trên danh nghĩa, worktree đó vẫn tồn tại trong bộ quản lý git.
Nếu bạn không tin có thể xoá thư mục đi và chạy lại lệnh `add` sẽ thấy có báo lỗi.

# 5. Kết luận
Với `worktree` ta có thể cùng lúc làm việc được với nhiều nhánh
mà không cần phải chuyển đổi qua lại giữa các nhánh cực kì tiện lợi và dễ sài.
Tuy nhiên khi bạn thêm một nhánh vào local thì có thể gặp rắc rối nếu nhánh đó đã được lấy về,
hoặc sau khi chạy lệnh xoá mà không thông báo cho git biết.
Khi đó, ta có thể sử dụng lựa chọn `-f` để buộc `worktree` phải thêm vào cho ta.

Bài viết này đã trình bày phương pháp để làm việc với nhiều branch cùng lúc trong cùng một thư mục,
vậy nếu không phải là nhánh mà là một repo khác thì sao?
Câu trả lời là `git submodule`, mình sẽ viết về phương pháp này trong bài viết tới.

