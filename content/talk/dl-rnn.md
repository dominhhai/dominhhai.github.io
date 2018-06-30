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
\# [*Hopfield (1982), Rumelhart et al. (1986a), Jordan (1986), Elman (1990)*](#15)
]]
---
# RNN - seq2seq
<img width="100%" src="https://karpathy.github.io/assets/rnn/diags.jpeg" alt="RNN in/out">

- Sequences in the input

- Sequences in the output

- Hidden Nodes is NOT fixed
---
# RNN - unroll
<img width="100%" src="https://colah.github.io/posts/2015-09-NN-Types-FP/img/RNN-general.png" alt="RNN in/out">
---
# RNN - unroll
<img width="100%" src="https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-unrolled.png" alt="RNN in/out">

### Calc Formulas
$$
\begin{aligned}
\mathbf s\_t &= \sigma(\mathbf W\_{in}\mathbf x\_t + \mathbf W\_{rec}\mathbf s\_{t-1} + \mathbf b\_s)
\\cr
\mathbf{\hat y\_t} &= h(\mathbf U\mathbf s\_t + \mathbf b\_y)
\end{aligned}
$$
- $\mathbf x_t$ : embedded word
- $\mathbf s_0$ : 1st hidden state. Set to *$\vec\mathbf 0$* or *pre-trained* values.
- $\sigma$ : activation function. Usually the $\tanh, \text{ReLU}, sigmoid$.
- $h$ : predict function. Such as, $softmax$ for language modeling.

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
- product of matrices is similar to product of real numbers can to go zero or infinity.
$$
\lim\limits\_{k\rightarrow\infty}\lambda^k = \begin{cases}
0 &\text{if }\lambda < 1
\\cr
\infty &\text{if }\lambda > 1
\end{cases}
$$

.footnote[.refer[
\# [*Bengio et al. (1994), Pascanu et al. (2013)*](#15)
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
\dfrac{\partial\mathbf s\_t}{\partial\mathbf s\_k}
= \prod\_{j=k}^{t-1} \dfrac{\partial\mathbf s\_{j+1}}{\partial\mathbf s\_j}
= \prod\_{j=k}^{t-1} \mathbf W\_{rec}^{\intercal}\text{diag}\big(\sigma^{\prime}(\mathbf s\_j)\big)
$$

.footnote[.refer[
\# [*Bengio et al. (1994), Pascanu et al. (2013)*](#15)
]]

---
# Vanishing and Exploding Gradient - WHY
- $\mathbf s\_k$ is vector, so $\dfrac{\partial\mathbf s\_{j+1}}{\partial\mathbf s\_j}$ is a Jacobian matrix

Let:
- $\gamma\in\mathbb{R}, \big\lVert \text{diag}\big(\sigma^{\prime}(\mathbf s\_{i-1})\big)\big\rVert \le \gamma$
- $\lambda\_1=\max\big(\lvert eigenvalues(\mathbf W\_{rec})\rvert\big)$

We have:
$$
\forall k,
\bigg\lVert\dfrac{\partial\mathbf s\_{k+1}}{\partial\mathbf s\_k}\bigg\rVert
\le \lVert\mathbf W\_{rec}^{\intercal}\rVert\big\lVert \text{diag}\big(\sigma^{\prime}(\mathbf s\_{i-1})\big)\big\rVert
\le \lambda\_1\gamma
$$

Let $\eta=\lambda\_1\gamma$ and $l=t-k$ :
$$
\dfrac{\partial\mathbf J\_t}{\partial\mathbf s\_t}\dfrac{\partial\mathbf s\_t}{\partial\mathbf s\_k}
= \dfrac{\partial\mathbf J\_t}{\partial\mathbf s\_t}\sum\_{j=k}^{t-1}\dfrac{\partial\mathbf s\_{j+1}}{\partial\mathbf s\_j}
\le \eta^l\dfrac{\partial\mathbf J\_t}{\partial\mathbf s\_t}
$$

.footnote[.refer[
\# [*Bengio et al. (1994), Pascanu et al. (2013)*](#15)
]]

---
# Vanishing and Exploding Gradient - WHY
$$
\dfrac{\partial\mathbf J\_t}{\partial\mathbf s\_t}\dfrac{\partial\mathbf s\_t}{\partial\mathbf s\_k}
\le \eta^l\dfrac{\partial\mathbf J\_t}{\partial\mathbf s\_t}
$$

With $(t-k)$ is large (*long-term dependencies*) :
- $\lambda_1<\dfrac{1}{\gamma}$ or $\eta<1$: *sufficient* condition for vanishing gradient problem

- $\lambda_1>\dfrac{1}{\gamma}$ or $\eta>1$: *neccessary* condition for exploding gradient problem

E.x, gradient will shrink to zero when:
- $\lambda_1<1$ if $\sigma$ is $\tanh$ because $\gamma=1$
- $\lambda_1<4$ if $\sigma$ is $\text{sigmoid}$ because $\gamma=0.25$

.footnote[.refer[
\# [*Bengio et al. (1994), Pascanu et al. (2013)*](#15)
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
\# [*Pascanu et al. (2013)*](#15)
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
\# [*Pascanu et al. (2013)*](#15)
]]
---
# Long Short-Term Memory - LSTM
- Constant Error Flow of Identity Relationship doesn't decay:
$$
\begin{aligned}
& \mathbf s\_t=\mathbf s\_{t-1}+F(\mathbf x\_t)
\\cr
\implies & \dfrac{\partial\mathbf s\_t}{\partial\mathbf s\_{t-1}}=1
\end{aligned}
$$

- Key idea: Use .red[*Constant Error Carousel*] - **CEC** to prevent from gradient decay
- The key component is a memory cell that acts like an accumulator (contains the identity relationship) over time
- Instead of computing new state as a matrix product with the old state, it rather computes the difference between them. Expressivity is the same, but gradients are better behaved

$$c\_t = c\_{t-1} + \sigma(x\_t, h\_{t-1})$$

.footnote[.refer[
\# [*Hochreiter (1997)*](#15)
]]
---
# LSTM
.center[<img style="text-align: center;" width="100%" src="https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png" alt="Clip Gradient">]

Use sigmoid to control info (cell state) by a pointwise multiplication operation. The sigmoid layer outputs numbers between zero and one, describing how much of each component should be let through. A value of zero means “let nothing through,” while a value of one means “let everything through!”

- Forgot Gate: $f_t$
- Input Gate: $i_t$
- Output Gate: $o_t$
---
# LSTM - Forward
$$
\begin{aligned}
f\_t &= \sigma(W\_f[h\_{t-1}, x\_t]+b\_f)
\\cr
i\_t &= \sigma(W\_i[h\_{t-1}, x\_t]+b\_i)
\\cr
o\_t &= \sigma(W\_o[h\_{t-1}, x\_t]+b\_o)
\\cr
c\_t &= \sigma(W\_c[h\_{t-1}, x\_t]+b\_c)
\\cr
\tilde{c\_t} &= \sigma(W\_c[h\_{t-1}, x\_t]+b\_c)
\\cr
c\_t &= f\_t\*c\_{t-1}+i\_t\*\tilde{c\_t}
\\cr
h\_t &= o\_t\*\tanh(c\_t)
\end{aligned}
$$

.footnote[.refer[
\# [*Hochreiter (1997)*](#15)
]]
---
# LSTM - Backward
$$
\begin{aligned}
\partial h\_t &= \dfrac{\partial E}{\partial h\_t}
\\cr
\partial o\_t &= \partial h\_t \* \tanh(c\_t)
\\cr
\partial c\_t &= \partial c\_{t+1} \* f\_{t+1} + \partial h\_t \* \partial o\_t \* (1-\tanh^2(c\_t))
\\cr
\partial i\_t &= \partial c\_t \* a\_t
\\cr
\partial f\_t &= \partial c\_t \* c\_{t-1}
\\cr
\partial a\_t &= \partial c\_t \* i\_t
\\cr
\partial c\_{t-1} &= \partial c\_t \* f\_t
\end{aligned}
$$

.footnote[.refer[
\# [*Hochreiter (1997)*](#15)
]]
---
# Gated Reccurent Unit - GRU
.center[<img style="text-align: center;" width="110%" src="https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-var-GRU.png" alt="Clip Gradient">]

.footnote[.refer[
\# [*Cho et al. (2014)*](#15)
]]
---
# Bidirectional RNNs
.center[<img style="text-align: center;" width="100%" src="https://poodar.me/images/post-images/bi_rnn_architecture.png" alt="Clip Gradient">]

.center[<img style="text-align: center;" width="100%" src="https://colah.github.io/posts/2015-09-NN-Types-FP/img/RNN-bidirectional.png" alt="Clip Gradient">]

---
# Deep RNNs
.center[<img style="text-align: center;" width="100%" src="https://poodar.me/images/post-images/deep_bidirectional_rnn_architecture.png" alt="Clip Gradient">]
---
# Deep RNNs
.center[<img style="text-align: center;" width="50%" src="https://i.imgur.com/J3DwxSF.png" alt="Clip Gradient">]
---
# Summary

---
# References
.refer[

- [1] [*Hopfield (1982)*. Neural networks and physical systems with emergent collective computational abilities](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC346238/pdf/pnas00447-0135.pdf)

- [2] [*Rumelhart et al. (1986a)*. Learning representations by back-propagation errors](https://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf)

- [3] [*Jordan (1986)*. Serial order: A parallel distributed processing approach](https://pdfs.semanticscholar.org/f8d7/7bb8da085ec419866e0f87e4efc2577b6141.pdf)

- [4] [*Elman (1990)*. Finding structure in time](https://crl.ucsd.edu/~elman/Papers/fsit.pdf)

- [5] [*Werbos (1990)*. Backpropagation Through Time: What It Does and How to Do It](http://axon.cs.byu.edu/~martinez/classes/678/Papers/Werbos_BPTT.pdf)

- [6] [*Bengio et al. (1994)*. Learning Long-Term Dependencies with Gradient Descent is Difficult](http://www.iro.umontreal.ca/~lisa/pointeurs/ieeetrnn94.pdf)

- [7] [*Pascanu et al. (2013)*. On the difficulty of training Recurrent Neural Networks](https://arxiv.org/pdf/1211.5063.pdf)

- [8] [*Hochreiter et al. (1997)*. Long Short-Term Memory](http://www.bioinf.jku.at/publications/older/2604.pdf)

- [9] [*Greff et al. (2017)*. LSTM: A search space odyssey](https://arxiv.org/pdf/1503.04069.pdf)

- [10] [*Jozefowics et al. (2015)*. An Empirical Exploration of Recurrent Network Architectures](http://proceedings.mlr.press/v37/jozefowicz15.pdf)

- [11] [*Cho et al. (2014)*. Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation](https://arxiv.org/pdf/1406.1078v3.pdf)

]
