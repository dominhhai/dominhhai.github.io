---
title: "[Atom] Tự động hoàn thiện lệnh"
slug: atom-auto-complele
date: 2016-03-27
categories:
- Lập Trình
- Editor
tags:
- Editor
- Atom
keywords:
- Editor
- Atom
- Markdown Preview
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: //res.cloudinary.com/dominhhai/image/upload/editor/atom.png
metaAlignment: center
---
![atom.auto-complete](https://raw.githubusercontent.com/dominhhai/blog/master/imgs/atom.gif 'atom auto-complete' width="800" height="600")

Các trình soạn thảo mã lệnh hầu hết có tính năng auto-complete (tự động hoàn thiện lệnh) khi gõ. Nhờ có tính năng này mà chúng ta có thể gõ mã nhanh hơn và không cần phải nhớ hết làu làu các API của ngôn ngữ, thư viện nào đó. Hầu hết các API có tên rất dễ liên tưởng tới tính năng của nó nên chỉ cần nhìn là biết ngay nó dùng để làm gì. Thử tưởng tượng nếu không có tính năng này thì chúng ta sẽ ra sao.

* Một là cực kì pro vì nhớ được hết các API (lúc mới học code gì đó thì mình chọn cách này)
* Hai là bạn gõ code như con rùa vì vừa phải gõ vừa phải nhớ và vừa phải Google hay đọc References loạn lên.

Vậy nên khi làm sản phẩm hay biết nhất định về ngôn ngữ ta nên theo hướng sử dụng tính năng tự động hoàn thiện. Với Atom, tin vui là ta có sẵn gói [autocomplete-plus](https://atom.io/packages/autocomplete-plus) được cài mặc định.

![autocomplete+](https://cloud.githubusercontent.com/assets/744740/7656861/9fb8bcc4-faea-11e4-9814-9dca218ded93.png)

Gói này mặc định giúp ta tự động được hoàn thiện khá nhiều các lệnh cơ bản với JavaScript, HTML, CSS. Tuy nhiên điểm cool của nó là có thể hỗ trợ được rất nhiều các lệnh khác như của PHP, Ruby hay Java... bằng cách tích hợp các gói ngôn ngữ con qua [API provider](https://github.com/atom/autocomplete-plus/wiki/Provider-API). Để sử dụng được tính năng này ta chỉ việc gõ và nó sẽ tự động hiển thị ra các lệnh khả thi từ các kí tự ta nhập vào. Sau đó ta chọn bằng phím `↑↓` rồi gõ `Enter` hoặc `Tab` là xong như ví dụ bên dưới đây.

![autocomplete-plus](https://raw.githubusercontent.com/dominhhai/blog/master/imgs/acp.gif 'autocomplete-plus')

Với Node.js mình cài thêm gói [atom-ternjs](https://atom.io/packages/atom-ternjs). Gói này sẽ tự động hoàn thiện các lệnh của cả JS, Nodejs hay các thư viện nổi tiếng như jQuery, Angular, React... cực kì tiện lợi.

```json
{
  "ecmaVersion": 6,
  "libs": [
    "browser",
    "jquery"
  ],
  "loadEagerly": [
    "path/to/your/js/**/*.js"
  ],
  "dontLoad": [
    "path/to/your/js/**/*.js"
  ],
  "plugins": {
    "complete_strings": {},
    "node": {},
    "lint": {},
    "angular": {},
    "requirejs": {},
    "modules": {},
    "es_modules": {},
    "doc_comment": {
      "fullDocs": true
    }
  }
}
```

Để sử dụng [atom-ternjs](https://atom.io/packages/atom-ternjs), ta cần tạo file cấu hình cho project của mình, vì nó sẽ dự vào file cấu hình này để biết được các lệnh nào khả dĩ cho ta. Ví dụ ta cần Nodejs thì ta thêm nodejs vào là xong. Sau khi tạo file cấu hình xong bạn nhớ khởi động lại gói này nhé.

![autocomplete-plus](https://raw.githubusercontent.com/dominhhai/blog/master/imgs/atom-ternjs.gif 'atom-ternjs')

Tham khảo:

* [1] [autocomplete-plus](https://atom.io/packages/autocomplete-plus)
* [2] [atom-ternjs](https://atom.io/packages/atom-ternjs)
