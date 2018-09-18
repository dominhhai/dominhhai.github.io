---
title: "[VSCode] Cấu hình Terminal Font cho ZSH"
slug: vscode-terminal-font
date: 2018-09-18
categories:
- Lập Trình
- Editor
tags:
- Editor
- VSCode
keywords:
- Editor
- VSCode
- ZSH terminal
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/editor/vscode.png
metaAlignment: center
---
Lọ mọ chuyển từ [Atom](https://atom.io/) sang [VSCode](https://code.visualstudio.com/), ấn tượng đầu tiên khá là tốt ở mặt tốc độ nhưng vẫn chưa quen lắm với giao diện và phím tắt của VSCode. Chắc cái thích nhất hiện tại là icon hiển thị ở menu của VSCode với plugin [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme). Cái đập vào mắt tiếp theo là giao diện dòng lệnh tích hợp sẵn của VSCode trông font chữ bị hỏng hết cả. Nhìn tới phát ngán!

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/vscode/vscode-terminal-font-1.png" title="Lỗi font terminal tích hợp" >}}

May sao, sau 1 hồi loay hoay thấy mục `Terminal` lọ mọ lò ra trong phần cài đặt. Và càng may hơn là ta có thể cấu hình được font chữ cho Terminal tích hợp:

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/vscode/vscode-terminal-font-before.png" title="Mục cấu hình font cho terminal tích hợp" >}}

Như hình trên, ta có thể thấy mục cấu hình font như sau:

- Setting
  - User Settings
    - Integrated: **Font Family**

Ở đây tôi chọn mục `User Settings` vì muốn cấu hình cho tất cả các project ở các mục khác nhau về sau luôn. Nếu cần cấu hình riêng cho từng project thì bạn có thể chọn `Workspace Settings`.

Giờ ta chỉ cần chọn font phù hợp với terminal thông dụng là được. Do tôi đang sử dụng [iTerm2 với zsh theme](/vi/2016/12/iterm2-cool-terminal/) nên tôi sẽ thiết lập thông số này tương ứng với font hiện tại của tôi là `Inconsolata-g for Powerline`.

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/vscode/iterm2-font.png" title="iTerm2 Font" >}}

Sau khi thiết lập xong, VSCode sẽ tự động lưu và hiển thị với font mới ngay cho ta. Kết quả đúng như kì vọng!

{{< image classes="fancybox center" src="https://res.cloudinary.com/dominhhai/image/upload/code/vscode/vscode-terminal-font-after.png" title="Cấu hình font thành công" >}}

Nhìn giờ ngon ngon rồi, nhưng vẫn khó kì vọng terminal tích hợp này làm được nhiều việc và tiện ích như iTerm2. Nên thời điểm hiện tại tôi vẫn chưa thể tắt hoàn toàn iTerm2 đi được, nhưng hi vọng thời gian tới terminal tích hợp của VSCode thông minh thêm nhiều nữa.