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
$$P(\mathbf{x}\_t|\mathbf{x}\_{t-1},...,\mathbf{x}\_1)$$

- Output: .red[variable-length] sequences of dependent output values
$$P(\mathbf{y}\_t|\mathbf{y}\_{t-1},...,\mathbf{y}\_1,\mathbf{x})$$

### Language Model:
- Chữ tài đi với chữ .red[tai] một vần.
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

.footnote[.refer[
\# Figure: https://cs231n.github.io/neural-networks-1/
]]
---
# Recurrent Neural Networks - RNN
.left-column[
![RNN Rolled](/images/talk_dl_rnn_rolled.png)
]
.right-column[
### 3 Node Types
- Input Nodes: $\mathbf x_t$
- .red[Recurrent Hidden Nodes]: $\mathbf s_t$ <br>*keeps order of hidden's state*
- Output Nodes: $\mathbf{\hat y}_t$

### Shared Weights
- Input Weights: $\mathbf W_{in}$
- Recurrent Weights: $\mathbf W_{rec}$
- Output Weights: $\mathbf U$
]

.footnote[.refer[
\# [*Hopfield (1982), Rumelhart et al. (1986a), Jordan (1986), Elman (1990)*](#25)
]]
---
# RNN - seq2seq
<img width="100%" src="https://karpathy.github.io/assets/rnn/diags.jpeg" alt="RNN in/out">

- Sequences in the input

- Sequences in the output

- Hidden Nodes is NOT fixed

.footnote[.refer[
\# Figure: https://karpathy.github.io/2015/05/21/rnn-effectiveness/
]]
---
# RNN - unroll
.center[
<img width="60%" src="/images/talk_dl_rnn_unrolled.png" alt="RNN unrolled">
]

### Calc Formulas
$$
\begin{aligned}
\mathbf s\_t &= f(\mathbf W\_{in}\mathbf x\_t + \mathbf W\_{rec}\mathbf s\_{t-1} + \mathbf b\_s)
\\cr
\mathbf{\hat y}\_t &= g(\mathbf U\mathbf s\_t + \mathbf b\_y)
\end{aligned}
$$
- $\mathbf x_t$ : embedded word
- $\mathbf s_0$ : 1st hidden state. Set to *$\vec\mathbf 0$* or *pre-trained* values.
- $f$ : activation function. Usually the $\tanh, \text{ReLU}, sigmoid$.
- $g$ : predict function. Such as, $softmax$ for language modeling.

.footnote[.refer[
\# [*Werbos (1990)*](#25)
]]

???
How to sample data?
1. Add END sysbol to the end of each sequence.
2. Use extra Bernoulli ouput. Determine by Sigmoid function.
3. Add extra output to predict $T$.
---
# Lost Function
.center[
<img width="55%" src="/images/talk_dl_rnn_lostfn.png" alt="RNN in/out">
]

$$J(\theta) = \frac{1}{T}\sum\_{t=1}^TJ\_t(\theta) = -\frac{1}{T}\sum\_{t=1}^T\sum\_{j=1}^Ny\_{tj}\log \hat y\_{tj}$$

Where:
- $T$: total time steps
- $N$: size of bag of words
- $J_t(\theta)$: lost at step $t$

.footnote[.refer[
\# [*Werbos (1990)*](#25)
]]
---
# Backpropagation Through Time - BPPT
.center[![RNN BPPT](/images/talk_dl_rnn_bppt.png)]

Backprop over time steps $t=\overline{1,T}$ then summing gradient of each step.
- $(\mathbf W\_{in}, \mathbf W\_{rec}) = \mathbf W = \mathbf W^{(k)} ~~~, k=\overline{1,T}$:
$$
\dfrac{\partial J\_t}{\partial\mathbf W}
= \sum\_{k=1}^t\dfrac{\partial J\_t}{\partial\mathbf{W}^{(k)}}\dfrac{\partial\mathbf{W}^{(k)}}{\partial\mathbf{W}}
= \sum\_{k=1}^t\dfrac{\partial J\_t}{\partial\mathbf{W}^{(k)}}
$$

.footnote[.refer[
\# [*Werbos (1990)*](#25)
]]

???
Slow because of sequences. Can't parallel handling.
---
# Backpropagation Through Time - BPPT
.red[Backprop over time steps $t=\overline{1,T}$ then summing gradient of each step.]

### Gradient Calc
$$\dfrac{\partial J}{\partial\theta}=\sum\_{t=1}^T\dfrac{\partial J\_t}{\partial\theta}$$
- w.r.t $\mathbf U$:
$$
\dfrac{\partial J\_t}{\partial\mathbf U}
= \dfrac{\partial J\_t}{\partial\mathbf{\hat y}\_t}\dfrac{\partial\mathbf{\hat y}\_t}{\partial\mathbf U}
= (\mathbf{\hat y}\_t-\mathbf{y}\_t)\mathbf{s}\_t^{\intercal}
$$

- w.r.t $\mathbf W$ ($\mathbf W\_{in}, \mathbf W\_{rec}$):
$$
\dfrac{\partial J\_t}{\partial\mathbf W}
= \dfrac{\partial J\_t}{\partial\mathbf{\hat y}\_t}\dfrac{\partial\mathbf{\hat y}\_t}{\partial\mathbf s\_t}\dfrac{\partial\mathbf{s}\_t}{\partial\mathbf W}
= \sum\_{k=1}^t\dfrac{\partial J\_t}{\partial\mathbf{\hat y}\_t}\dfrac{\partial\mathbf{\hat y}\_t}{\partial\mathbf s\_t}\dfrac{\partial\mathbf{s}\_t}{\partial\mathbf{s}\_k}\dfrac{\partial\mathbf{s}\_k}{\partial\mathbf W}
$$

.footnote[.refer[
\# [*Werbos (1990)*](#25)
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
\# [*Bengio et al. (1994), Pascanu et al. (2013)*](#25)
]]
---
# Vanishing and Exploding Gradient - WHY
- Similar hidden state function
$$
\mathbf s\_t
= F(\mathbf s\_{t-1}, \mathbf x\_t, \mathbf W)
= \mathbf W\_{rec}f(\mathbf s\_{t-1}) + \mathbf W\_{in}\mathbf x\_t + \mathbf b\_s
$$

- Gradient w.r.t $\mathbf W$:
$$\dfrac{\partial J}{\partial\mathbf W}=\sum\_{t=1}^T\dfrac{\partial J\_t}{\partial\mathbf W}$$

- At step $t$:
$$\dfrac{\partial J\_t}{\partial\mathbf W} = \sum\_{k=1}^t\dfrac{\partial J\_t}{\partial\mathbf s\_t}\textcolor{blue}{\dfrac{\partial\mathbf{s}\_t}{\partial\mathbf{s}\_k}}\dfrac{\partial\mathbf{s}\_k}{\partial\mathbf W}$$

- Error from step $t$ back to $k$:
$$
\dfrac{\partial\mathbf s\_t}{\partial\mathbf s\_k}
= \prod\_{j=k}^{t-1} \dfrac{\partial\mathbf s\_{j+1}}{\partial\mathbf s\_j}
= \prod\_{j=k}^{t-1} \mathbf W\_{rec}^{\intercal}\text{diag}\big(f^{\prime}(\mathbf s\_j)\big)
$$

.footnote[.refer[
\# [*Bengio et al. (1994), Pascanu et al. (2013)*](#25)
]]

---
# Vanishing and Exploding Gradient - WHY
- $\mathbf s\_k$ is vector, so $\dfrac{\partial\mathbf s\_{j+1}}{\partial\mathbf s\_j}$ is a Jacobian matrix

Let:
- $\gamma\in\mathbb{R}, \big\lVert \text{diag}\big(f^{\prime}(\mathbf s\_j)\big)\big\rVert \le \gamma$
- $\lambda\_1=\max\big(\lvert eigenvalues(\mathbf W\_{rec})\rvert\big)$

We have:
$$
\forall j,
\bigg\lVert\dfrac{\partial\mathbf s\_{j+1}}{\partial\mathbf s\_j}\bigg\rVert
\le \lVert\mathbf W\_{rec}^{\intercal}\rVert\big\lVert \text{diag}\big(f^{\prime}(\mathbf s\_j)\big)\big\rVert
\le \lambda\_1\gamma
$$

Let $\eta=\lambda\_1\gamma$ and $l=t-k$ :
$$
\dfrac{\partial J\_t}{\partial\mathbf s\_t}\dfrac{\partial\mathbf s\_t}{\partial\mathbf s\_k}
= \dfrac{\partial J\_t}{\partial\mathbf s\_t}\sum\_{j=k}^{t-1}\dfrac{\partial\mathbf s\_{j+1}}{\partial\mathbf s\_j}
\le \eta^l\dfrac{\partial J\_t}{\partial\mathbf s\_t}
$$

.footnote[.refer[
\# [*Bengio et al. (1994), Pascanu et al. (2013)*](#25)
]]

---
# Vanishing and Exploding Gradient - WHY
$$
\dfrac{\partial J\_t}{\partial\mathbf s\_t}\dfrac{\partial\mathbf s\_t}{\partial\mathbf s\_k}
\le \eta^l\dfrac{\partial J\_t}{\partial\mathbf s\_t}
$$

With $(t-k)$ is large (*long-term dependencies*) :
- $\lambda_1<\dfrac{1}{\gamma}$ or $\eta<1$: *sufficient* condition for vanishing gradient problem

- $\lambda_1>\dfrac{1}{\gamma}$ or $\eta>1$: *neccessary* condition for exploding gradient problem

E.x, gradient will shrink to zero when:
- $\lambda_1<1$ if $\sigma$ is $\tanh$ because $\gamma=1$
- $\lambda_1<4$ if $\sigma$ is $\text{sigmoid}$ because $\gamma=0.25$

.footnote[.refer[
\# [*Bengio et al. (1994), Pascanu et al. (2013)*](#25)
]]

???
Gradient of long-term is exponentially smaller than short-term.
So, take long time to learn long-term.
10-20 may be out of range.
---
# Gradient Clipping
- Solution to exploding gradient problem: .red[Rescale gradients]

.center[<img width="60%" src="/images/talk_dl_rnn_clip_grad.png" alt="Clip Gradient">]
.center[*Error surface of a single hidden unit recurrent network*]

Where:
- Solid lines: standard gradient descent
- Dashed lines: rescaled gradient descent

.footnote[.refer[
\# [*Pascanu et al. (2013)*](#25)
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
\# [*Pascanu et al. (2013)*](#25)
]]
---
# Long Short-Term Memory - LSTM
- Constant Error Flow of Identity Relationship doesn't decay:
$$\mathbf s\_t=\mathbf s\_{t-1}+f(\mathbf x\_t) \implies \dfrac{\partial\mathbf s\_t}{\partial\mathbf s\_{t-1}}=1$$

- Key idea: Use .red[*Constant Error Carousel*] - **CEC** to prevent from gradient decay
  - .red[**Memory Cell**] $\mathbf c_t$: indentity relationship
  - Compute new state by difference from before time step*[s]*
  $$\mathbf c\_t = \mathbf c\_{t-1} + \textcolor{blue}{f(\mathbf x\_t, \mathbf h\_{t-1})}$$
  *$\mathbf h_t$ is the output at time step $t$*

- Weights conflict:
  - Input Weights: Same weights for *"write operations"*
  - Output Weights: Same weights for *"read operations"*

  ==> Use .red[**Gates Units**] to control conflicting

.footnote[.refer[
\# [*Hochreiter (1997)*](#25)
]]
---
# LSTM
.center[<img width="100%" src="https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png" alt="LSTM">]

- Gate Units:
 - sigmoid function $\sigma\in[0,1]$ controls how much info can be through
- Gate Types:
  - Forget Gate $\mathbf f_t$ (*Gers et al. (1999)*)
  - Input Gate $\mathbf i_t$
  - Output Gate $\mathbf o_t$
- CEC: center $\oplus$ act as linear function

.footnote[.refer[
\# Figure: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
]]
---
# LSTM - Forward
- Forget Gate:
$$\mathbf f\_t = \sigma(\mathbf W\_f[\mathbf h\_{t-1}, \mathbf x\_t]+\mathbf b\_f)$$
- Input Gate:
$$\mathbf i\_t = \sigma(\mathbf W\_i[\mathbf h\_{t-1}, \mathbf x\_t]+\mathbf b\_i)$$
- Output Gate:
$$\mathbf o\_t = \sigma(\mathbf W\_o[\mathbf h\_{t-1}, \mathbf x\_t]+\mathbf b\_o)$$
- New State:
$$
\begin{aligned}
\mathbf{\tilde{c}}\_t &= \tanh(\mathbf W\_c[\mathbf h\_{t-1}, \mathbf x\_t]+\mathbf b\_c)
\\cr
\mathbf c\_t &= \mathbf f\_t\*\mathbf c\_{t-1}+\mathbf i\_t\*\mathbf{\tilde{c}}\_t
\end{aligned}
$$
- Cell's Output:
$$\mathbf h\_t = \mathbf o\_t\*\tanh(\mathbf c\_t)$$

.footnote[.refer[
\# [*Hochreiter (1997)*](#25)
]]
---
# LSTM - Backward
- Cell's Output: $\delta h\_t = \mathbf y\_t - \mathbf h\_t$

- Output Gate: $\delta o\_t = \delta h\_t \* \tanh(\mathbf c\_t)$
  - Compute: $\delta W\_o^{(t)}, \delta b\_o^{(t)}$
- New State: $\delta c\_t = \textcolor{blue}{\delta c\_t} + \delta h\_t \* \delta o\_t \* (1-\tanh^2(\mathbf c\_t))$

- Previous State: $\delta c\_{t-1} = \delta c\_t \* \mathbf f\_t$

- Input Gate: $\delta i\_t = \delta c\_t \* \mathbf{\tilde{c}}\_t$
  - Compute: $\delta W\_i^{(t)}, \delta b\_i^{(t)}$

- Forget Gate: $\delta f\_t = \delta c\_t \* \mathbf c\_{t-1}$
  - Compute: $\delta W\_f^{(t)}, \delta b\_f^{(t)}$

- External Input: $\delta\tilde{c\_t} = \delta c\_t \* \mathbf i\_t$
  - Compute: $\delta W\_c^{(t)}, \delta b\_c^{(t)}$

---
# Gated Reccurent Unit - GRU
.center[<img width="110%" src="https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-var-GRU.png" alt="GRU">]

- Cell State $h_t$
  - Cell State & Hidden State

- Update Gate $z\_t$
  - Forget Gate & Input Gate

- Reset Gate $r\_t$

.footnote[.refer[
\# [*Cho et al. (2014)*](#25), Figure: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
]]
---
# Bidirectional RNNs
.center[<img width="80%" src="https://colah.github.io/posts/2015-09-NN-Types-FP/img/RNN-bidirectional.png" alt="Bidirectional RNNs">]

- Previous Dependencies (left → right):
$$\mathbf s\_t = f(\mathbf W\_{in}\mathbf x\_t + \mathbf W\_{rec}\mathbf s\_t + \mathbf b\_s)$$
- Following Dependencies (right → left):
$$\mathbf s\_t^{\prime} = f(\mathbf W\_{in}^{\prime}\mathbf x\_t + \mathbf W\_{rec}^{\prime}\mathbf s\_t + \mathbf b\_s^{\prime})$$
- Output:
$$\qquad\mathbf y\_t = g(U[\mathbf s\_t,\mathbf s\_t^{\prime}] + \mathbf b\_y)$$


.footnote[.refer[
\# Figure: https://colah.github.io/posts/2015-09-NN-Types-FP/
]]
---
# Deep RNNs
.center[<img width="65%" src="/images/talk_dl_rnn_deep.png" alt="Deep RNNs">]

- Layer 0 (Input):
$$\mathbf s\_t^{(0)} = \mathbf x\_t$$

- Layer $l=\overline{1,L}$:
$$\mathbf s\_t^{(l)} = f(\mathbf W\_{in}^{(l)}\mathbf s\_t^{(l-1)} + \mathbf W\_{rec}^{(l)}\mathbf s\_{t-1}^{(l)} + \mathbf b\_s^{(l)})$$

- Output:
$$\mathbf{\hat y}\_t = g(\mathbf U\mathbf s\_t^{(L)} + \mathbf b\_y)$$
---
# Summary
- RNNs
  - Variable-length In/Output
  - Train with BPPT
  - .red[Vanishing & exploding gradient problem]

- Gradient Clipping
  - Rescale gradients to prevent from exploding gradient problem

- LSTM
  - Memory Cell: Keep linear relationship between state
  - Gate Units: control through info with sigmoid function $\sigma\in[0,1]$
  - Time step lags > 1000
  - Local in space and time: $\Theta(1)$ per step and weight

- GRU
  - Merge cell state and hidden state
  - Combine forget gate and input gate into update gate

- RNNs variants: Bidirectional RNNs, Deep RNNs

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
