---
title: "[ICML] Learning Longer-term Dependencies in RNNs with Auxiliary Losses"
date: 2018-08-18
keywords:
- RNN & LSTM
description: "Paper by Trieu H.Trinh, Andrew M.Dai, Minh-Thang Luong, Quoc V.Le. ICML2018. Talk at Tokyo ML Event."
renderMath: true
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/dl/logo.png
metaAlignment: center
---

layout: true
class: center, middle
---
# Learning Longer-term Dependencies in RNNs with Auxiliary Losses

.red[.refer[
Trieu H.Trinh, Andrew M.Dai, Minh-Thang Luong, Quoc V.Le
]]

*19-08-2018*

Do Minh Hai

[<i class="fab fa-github"> @dominhhai</i>](https://github.com/dominhhai)

.footnote[.refer[
[<i class="fab fa-facebook"> Tokyo Paper Reading Fest</i>](https://www.facebook.com/events/176136236447633/)
]]
---
layout: false
class: left

# Outline

- Long-term Dependencies problem in RNNs

- Methodology

  - Auxiliary Losses

  - Procedure

- Exeperiments

  - Model

  - Results

- Analysis
---
# Long-term Dependencies problem
- Long-term dependencies

  - BPTT tend to vanish or explode during training

  - States memory is expensive

- SoTA methods
  - LSTM

  - Gradient Clipping

  - Truncated BPTT

.footnote[.refer[
\# More here: https://dominhhai.github.io/vi/talk/dl-rnn
]]
---
# Methodology
.center[<img width="80%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/1-Figure1-1.png" alt="Method Overview">]

### Auxiliary Loss:
- Unsupervised
- Sampling at random anchor points

### BPTT:
  - All gradients are truncated
  - Improves performance and scalability
---
# Methodology
.center[<img width="100%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/2-Figure2-1.png" alt="Auxiliary Loss">]

### Auxiliary Loss:
- *r*-LSTM: Reconstruction
  - Reconstructs the past events before anchor point
- *p*-LSTM: Prediction
  - Predict the next events after anchor point

### Anchor Points
- Temporary Memory
- Difference RNNs
---
# Methodology
.center[<img width="100%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/2-Figure2-1.png" alt="Auxiliary Loss">]

### Training
- Random anchor points

- Train in 2 phases
  - Pretrain: minimize auxiliary losses only
  - Train: minimize the sum of main objective loss and auxiliary losses
  $$L = L\_\text{supervised} + L\_\text{auxiliary}$$

---
# Methodology
.center[<img width="70%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/2-Figure2-1.png" alt="Auxiliary Loss">]

### Sampling
- Add extra hyper-parameters
  - Sampling Frequency $n$
  - Subsequence Length $\\{l_i\\}~~~, i=\overline{1,n}$

### Auxiliary Loss:
$$L\_\text{auxiliary}=\frac{\sum\_{i=i}^n L\_i}{\sum\_{i=i}^n l\_i}$$

  where, the sum of cross-entroy loss $L\_i=\sum\_{t=1}^{l\_i}\text{TokenLost}\_t$
---
# Exeperiments - Datasets
.center[<img width="90%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/4-Table1-1.png" alt="Datasets">]

- Up to 16,000
  - over 20 times longer than any previously use benhmark
---
# Exeperiments - Models

### Main objective model
- Input: embedding size of 128

- 1-layer LSTM with 128 cells

- 2-layers FFN with 256 hidden units
  - Dropout with probability 0.5 on the 2nd-FFN

- Output: softmax prediction

### Auxiliary model
- 2-layers LSTM
  - Bottom layer is initialized with main LSTM states
  - Top layer starts with zero

- 2-layers FFN with 256 hidden units
  - Dropout with probability 0.5 on the 2nd-FFN
---
# Exeperiments - Results
.center[<img width="80%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/4-Table2-1.png" alt="MNIST, pMNIST, CIFAR10">]
---
# Exeperiments - Results
- StandfordDogs

.center[<img width="65%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/5-Figure3-1.png" alt="StandfordDogs">]
---
# Exeperiments - Results
- Compare with Transformer

.center[<img width="60%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/6-Table3-1.png" alt="Transformer">]

- DBpedia

.center[<img width="60%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/6-Table4-1.png" alt="DBpedia">]
---
# Analysis
- Shrinking BPTT length

.center[<img width="80%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/7-Figure4-1.png" alt="Shrinking BPTT length">]

---
# Analysis
- Multiple Reconstructions with fixed BPTT cost

.center[<img width="60%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/7-Table6-1.png" alt="Multiple Reconstructions with fixed BPTT cost">]

---
# Analysis
- Regulaziation and Optimization

.center[<img width="60%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/8-Figure5-1.png" alt="Regulaziation and Optimization">]

---
# Analysis
- Relative contribution of difference factors to *r*-LSTM

.center[<img width="80%" src="https://ai2-s2-public.s3.amazonaws.com/figures/2017-08-08/5553566b1dd59bc8bc1df0d5096ce1b2342c19d1/8-Figure6-1.png" alt="Ablation Study">]

---
layout: true
class: center, middle
---
# Thank You 😊

Happy Coding!
