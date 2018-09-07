---
title: "[Talk] Slide về RNNs, LSTM, GRU"
slug: talk-rnn
date: 2018-07-08T10:20:14+09:00
categories:
- Học Máy
- Học Sâu
- RNN
tags:
- Học Máy
- NN
- Talk
keywords:
- Học Máy
- Machine Learning
- Neural Networks
- RNN
- LSTM
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/dl/logo.png
metaAlignment: center
---
Dưới đấy là slide giới thiệu về RNNs, LSTM, GRU tại [Tokyo ML Event](https://www.facebook.com/events/1772695682776739/) hôm chủ nhật 08/07/2018 vừa qua. Tiện đây, blog mình có thêm mục **[Chém gió](/vi/talk/)** lưu trữ lại các slide trình bày của mình tại các hội nhóm.
<!--more-->

Để xem full mode dễ dàng hơn bạn có thể click [tại đây](/vi/talk/dl-rnn/#1). Để điều khiển chuyển qua lại các page, bạn có thể sử dụng các phím sang trái/phải hoặc scroll slide nhé.

<iframe id="slide"
  title="Slide RNNs"
  width="100%"
  height="600"
  src="/vi/talk/dl-rnn/#1">
</iframe>

Trong buổi này có một số câu hỏi mở khá hay như:

- Nên cắt văn bản ra thế nào để có thể dự đoán được hợp lý? Nếu cắt theo câu thì các câu có phụ thuộc ngữ cảnh vào nhau sẽ không học được. Còn cắt theo độ dài nhất định nào đó chưa chắc đã đảm bảo được ngữ nghĩa phụ thuộc nhau. Có tài liệu cho học được tham số đó, nhưng việc học thực sự khả thi hay không?

- Nếu có định độ dài đầu vào khi huấn luyện thì các câu độ dài ngắn hơn kích cỡ đó sẽ cần thêm kí tự rỗng (`0-0`) vào. Thế nhưng việc thêm ấy có ảnh hưởng tới quá trình huấn luyện hay không?

Ngoài ra, có 2 điểm mọi người tranh luận nhiều nhất là:

- Ở slide 9, các $\dfrac{\partial J_t}{\partial \mathbf W^{(k)}}$ có khác nhau không?

- Ở slide 16, việc clipping gradient thực hiện khi nào?

Ở đây tôi không đưa kết quả thảo luận cũng như câu hỏi thảo luận, tuy nhiên nếu bạn quan tâm thì cứ để lại ý kiến của mình bên dưới tôi sẽ tổng hợp và gửi lại câu trả lời sau.
