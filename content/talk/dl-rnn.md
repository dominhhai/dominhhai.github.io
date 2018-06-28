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

- Bidirectional RNNs

- Deep RNNs
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
.center[<img width="60%" src="https://cs231n.github.io/assets/nn1/neural_net2.jpeg" alt="FNN">]
### FNN:
- Fixed input/output size
- Unordered input

### Slide windows for sequences of inputs:
- window size may not fit
- window's weights are not shared
---
# Recurrent Neural Networks - RNN
.left-column[
<img width="100%" src="https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-rolled.png" alt="Basic RNN">
]
.right-column[
### 3 Node Types
- Input Nodes: $\mathbf x_t$
- .red[Recurrent Hidden Nodes]: $\mathbf s_t$ <br>*keeps order of hidden's state*
- Output Nodes: $\mathbf{\hat y_t}$

### Shared Weights
- Input Weights: $\mathbf W_{in}$
- Recurrent Weights: $\mathbf W_{rec}$
- Output Weights: $\mathbf U$
]

.footnote[.refer[
\# [*Hopfield (1982), Rumelhart, et al. (1986a), Jordan (1986), Elman (1990)*](#15)
]]
---
# RNN - seq2seq
<img width="100%" src="https://karpathy.github.io/assets/rnn/diags.jpeg" alt="RNN in/out">

- Sequences in the input

- Sequences in the output

- Hidden Nodes is NOT fixed
---
# RNN - unroll
<img width="100%" src="https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-unrolled.png" alt="RNN in/out">

### Calc Formulas
$$
\begin{aligned}
\mathbf s\_t &= \sigma(\mathbf W\_{in}\mathbf x\_t + \mathbf W\_{rec}\mathbf s\_{t-1} + \mathbf b\_s)
\\cr
\mathbf{\hat y\_t} &= \text{softmax}(\mathbf U\mathbf s\_t + \mathbf b\_y)
\end{aligned}
$$

Where:
- $\mathbf x_t$ : embedded word
- $\mathbf s_0$ : 1st hidden state. Set to *0* or *pre-trained* values.
- $\sigma$ : activation function. Usually the $\tanh, \text{ReLU}, sigmoid$.

.footnote[.refer[
\# [*Werbos (1990)*](#15)
]]
---
# Lost Function
<img width="100%" src="https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-unrolled.png" alt="RNN in/out">

$$J(\theta) = \frac{1}{T}\sum\_{t=1}^TJ\_t(\theta) = -\frac{1}{T}\sum\_{t=1}^T\sum\_{j=1}^Ny\_{kj}\log \hat y\_{kj}$$

Where:
- $T$: total time steps
- $N$: size of bag of words
- $J_t(\theta)$: lost at step $t$

.footnote[.refer[
\# [*Werbos (1990)*](#15)
]]
---
# Backpropagation Through Time - BPPT
<img width="100%" src="https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-unrolled.png" alt="gradient">

Backprop over time steps $t=\overline{1,T}$ then summing gradient of each step.

.footnote[.refer[
\# [*Werbos (1990)*](#15)
]]
---
# Backpropagation Through Time - BPPT
.red[Backprop over time steps $t=\overline{1,T}$ then summing gradient of each step.]

### Gradient Calc
$$\dfrac{\partial J}{\partial\theta}=\sum\_{t=1}^T\dfrac{\partial J\_t}{\partial\theta}$$
- w.r.t $\mathbf U$:
$$
\dfrac{\partial J\_t}{\partial\mathbf U}
= \dfrac{\partial J\_t}{\partial\mathbf{\hat y\_t}}\dfrac{\partial\mathbf{\hat y\_t}}{\partial\mathbf U}
= (\mathbf{\hat y\_t}-\mathbf{y\_t})\mathbf{s\_t}^{\intercal}
$$

- w.r.t $\mathbf W$ ($\mathbf W\_{in}, \mathbf W\_{rec}$):
$$
\dfrac{\partial J\_t}{\partial\mathbf W}
= \dfrac{\partial J\_t}{\partial\mathbf{\hat y\_t}}\dfrac{\partial\mathbf{\hat y\_t}}{\partial\mathbf s\_t}\dfrac{\partial\mathbf{s\_t}}{\partial\mathbf W}
= \sum\_{k=1}^t\dfrac{\partial J\_t}{\partial\mathbf{\hat y\_t}}\dfrac{\partial\mathbf{\hat y\_t}}{\partial\mathbf s\_t}\dfrac{\partial\mathbf{s\_t}}{\partial\mathbf{s\_k}}\dfrac{\partial\mathbf{s\_k}}{\partial\mathbf W}
$$

.footnote[.refer[
\# [*Werbos (1990)*](#15)
]]
---
# Vanishing and Exploding Gradient
Why do we have to care about it?

### Exploding Gradient
- Norm of gradient increases exponentially
- Overflow when calc gradient

### Vanishing Gradient
- Norm of gradient decrease exponentially (to 0)
- Can NOT learn long-term dependencies

.red[Deep FNNs and RNNs are easy to stuck on these problems.]

.footnote[.refer[
\# [*Bengio, et al. (1994), Pascanu, et al. (2013)*](#15)
]]
---
# Vanishing and Exploding Gradient - WHY
- Similar hidden state function
$$
\mathbf s\_t
= f(\mathbf s\_{t-1}, \mathbf x\_t, \mathbf W)
= \mathbf W\_{rec}\sigma(\mathbf s\_{t-1}) + \mathbf W\_{in}\mathbf x\_t + \mathbf b\_s
$$

- Gradient w.r.t $\mathbf W$:
$$\dfrac{\partial J}{\partial\mathbf W}=\sum\_{t=1}^T\dfrac{\partial J\_t}{\partial\mathbf W}$$

- At step $t$:
$$\dfrac{\partial J\_t}{\partial\mathbf W}= \sum\_{k=1}^t\dfrac{\partial J\_t}{\partial\mathbf{\hat y\_t}}\dfrac{\partial\mathbf{\hat y\_t}}{\partial\mathbf s\_t}\textcolor{blue}{\dfrac{\partial\mathbf{s\_t}}{\partial\mathbf{s\_k}}}\dfrac{\partial\mathbf{s\_k}}{\partial\mathbf W}$$

- Error from step $t$ back to $k$:
$$
\dfrac{\mathbf s\_t}{\mathbf s\_k}
= \prod\_{i=k+1}^t \dfrac{\partial\mathbf s\_i}{\partial\mathbf s\_{i-1}}
= \prod\_{i=k+1}^t \mathbf W\_{rec}^{\intercal}\text{diag}\big(\sigma^{\prime}(\mathbf s\_{i-1})\big)
$$

.footnote[.refer[
\# [*Bengio, et al. (1994), Pascanu, et al. (2013)*](#15)
]]

---
# Vanishing and Exploding Gradient - WHY
- Error from step $t$ back to $k$:
$$
\dfrac{\mathbf s\_t}{\mathbf s\_k}
= \prod\_{i=k+1}^t \dfrac{\partial\mathbf s\_i}{\partial\mathbf s\_{i-1}}
= \prod\_{i=k+1}^t \mathbf W\_{rec}^{\intercal}\text{diag}\big(\sigma^{\prime}(\mathbf s\_{i-1})\big)
$$

- $\mathbf s\_j$ is vector, so $\dfrac{\partial\mathbf s\_i}{\partial\mathbf s\_{i-1}}$ is Jacobian matrix

For:
- $\gamma\in\mathbb{R}, \big\lVert \text{diag}\big(\sigma^{\prime}(\mathbf s\_{i-1})\big)\big\rVert \le \gamma$
- $\lambda\_1=\lvert\max\big(eigenvalues(\mathbf W\_{rec})\big)\rvert$

We have:
$$
\forall k,
\bigg\lVert\dfrac{\partial\mathbf s\_{k+1}}{\partial\mathbf s\_k}\bigg\rVert
\le \lVert\mathbf W\_{rec}^{\intercal}\rVert\big\lVert \text{diag}\big(\sigma^{\prime}(\mathbf s\_{i-1})\big)\big\rVert
\le \lambda\_1\gamma
$$

.footnote[.refer[
\# [*Bengio, et al. (1994), Pascanu, et al. (2013)*](#15)
]]
---
# Gradient Clipping
- Solution to exploding gradient problem: .red[Rescale gradients]

.center[<img style="text-align: center;" width="60%" src="/images/talk_dl_rnn_clip_grad.png" alt="Clip Gradient">]
.center[*Error surface of a single hidden unit recurrent network*]

Where:
- Solid lines: standard gradient descent
- Dashed lines: rescaled gradient descent

.footnote[.refer[
\# [*Pascanu, et al. (2013)*](#15)
]]
---
# Gradient Clipping
- Add `threshold` hyper-parameter to clip norm of gradients

$$
\begin{aligned}
& -------------------
\\cr
& \hat g = \dfrac{\partial J}{\partial\mathbf W}
\\cr
& \textbf{if} \quad\lVert\hat{g}\rVert \ge threshold \quad\textbf{   then}
\\cr
& \qquad \hat{g} \gets \dfrac{threshold}{\lVert\hat{g}\rVert}\hat{g}
\\cr
& \textbf{end if}
\\cr& -------------------
\end{aligned}
$$

- Simple

- Effective

.footnote[.refer[
\# [*Pascanu, et al. (2013)*](#15)
]]
---
# Long Short-Term Memory - LSTM

---
# Gated Reccurent Unit - GRU

---
# Bidirectional RNNs

---
# Deep RNNs

---
# References
.refer[

- [1] [*Hopfield (1982)*. Neural networks and physical systems with emergent collective computational abilities](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC346238/pdf/pnas00447-0135.pdf)

- [2] [*Rumelhart, et al. (1986a)*. Learning representations by back-propagation erros](https://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf)

- [3] [*Jordan (1986)*. Serial order: A parallel distributed processing approach](https://pdfs.semanticscholar.org/f8d7/7bb8da085ec419866e0f87e4efc2577b6141.pdf)

- [4] [*Elman (1990)*. Finding structure in time](https://crl.ucsd.edu/~elman/Papers/fsit.pdf)

- [5] [*Werbos (1990)*. Backpropagation Through Time: What It Does and How to Do It](http://axon.cs.byu.edu/~martinez/classes/678/Papers/Werbos_BPTT.pdf)

- [6] [*Bengio, et al. (1994)*. Learning Long-Term Dependencies with Gradient Descent is Difficult](http://www.iro.umontreal.ca/~lisa/pointeurs/ieeetrnn94.pdf)

- [7] [*Pascanu, et al. (2013)*. On the difficulty of training Recurrent Neural Networks](https://arxiv.org/pdf/1211.5063.pdf)

- [8] [*Hochreiter, et al. (1997)*. Long Short-Term Memory](http://www.bioinf.jku.at/publications/older/2604.pdf)

- [9] [*Greff, et al. (2017)*. LSTM: A search space odyssey](https://arxiv.org/pdf/1503.04069.pdf)

- [10] [*Jozefowics, et al. (2015)*. An Empirical Exploration of Recurrent Network Architectures](http://proceedings.mlr.press/v37/jozefowicz15.pdf)

- [11] [*Cho, et al. (2014)*. Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation](https://arxiv.org/pdf/1406.1078v3.pdf)

]
