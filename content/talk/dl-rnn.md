---
title: "Recurrent Neural Networks"
date: 2018-06-25
keywords:
- RNN & LSTM
description: "Introduction to RNNs, LSTM, GRU"
renderMath: true
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/dl/logo.png
metaAlignment: center
draft: true
---

layout: true
class: center, middle
---
# Recurrent Neural Networks
*08-07-2018*

Do Minh Hai

[<i class="fab fa-github"> @dominhhai</i>](https://github.com/dominhhai)
---
layout: false
class: left

# Outline

- Time Series problem

- Recurrent Neural Networks - RNN

  - Lost Function

  - Backpropagation Through Time - BPPT

- Vanishing and Exploding Gradient problem

- Long Short-Term Memory - LSTM

- Gated Reccurent Unit - GRU
---
# Time Series problem
- Input: .red[variable-length] sequences of dependent input variables
$$P(\mathbf{x\_t}|\mathbf{x\_{t-1}},...,\mathbf{x\_1})$$

- Output: .red[variable-length] sequences of dependent output values
$$P(\mathbf{y\_t}|\mathbf{y\_{t-1}},...,\mathbf{y\_1},\mathbf{x})$$

### Language Model:
- Chữ tài đi với chữ .red[tai] tai một vần.
- He is Vietnames. But he can not speak .red[Vietnames]. 😳

### Language Translation:
- Tao hôn nó.　 😍 　.red[彼女にキスした。]
- Nó hôn tao.　 🙏　 .red[彼女からキスされる。]
---
# Time Series problem - FNN
<img height="20%" width="60%" src="https://cs231n.github.io/assets/nn1/neural_net2.jpeg" alt="FNN">
### FNN:
- Fixed input/output size
- Unordered input

### Slide windows for sequences of inputs:
- window size may not fit
- window's weights are not shared
---
# Recurrent Neural Networks - RNN

---
# Lost Function

---
# Backpropagation Through Time - BPPT

---
# Vanishing and Exploding Gradient

---
# Long Short-Term Memory - LSTM

---
# Gated Reccurent Unit - GRU
