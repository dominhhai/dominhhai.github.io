---
title: "Reinforcement Learning: An Introduction. Chapter 5"
date: 2018-08-24
keywords:
- RL, Reinforcement Learning
description: "Reinforcement Learning: An Introduction, by Richard S. Sutton and Andrew G. Barto. Chapter 5."
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
# Reinforcement Learning: An Introduction<br>Chapter 5: Monte Carlo Methods
*26-08-2018*

Do Minh Hai

[<i class="fab fa-github"> @dominhhai</i>](https://github.com/dominhhai)
---
layout: false
class: left

# Outline

- Introduction

- Monte Carlo Prediction

- Monte Carlo Control

- On-Policy method

- Off-policy method

- Incremental Implementation for MC prediction

- Off-policy MC Control

- Discounting-aware Importance Sampling

- Per-decision Importance Sampling
---
# Introduction
- Environment is incomplete

- Learning from experience of interaction with environment
  - Experience is divided into **episodes**

  - Based on averaging sample's returns

- Like an associative bandit
  - Nonstationary from the point of view of the earlier state

- Adapt the idea of GPI from DP

---
# Monte Carlo Prediction
.left-column[<img width="70%" src="https://raw.githubusercontent.com/dominhhai/rl-intro/master/assets/mc_backup_diagram.png" alt="MC backup diagram">
*backup diagram*
]
.right-column[
- Estimate $v_\pi(s)$ from experience by averaging the returns observed after visits to that state $s$

- 2 methods:
  - first-visit MC: average of the returns only for the first visits to $s$
  - every-visit MC: average of the returns for all visits to $s$

- Estimates for each state are independent

- Unlike DP
  - Only one choice considered at each state - only sampled on the one episode
  - Do not bootstrap
]
---
# Monte Carlo Prediction
.center[<img width="100%" src="https://raw.githubusercontent.com/dominhhai/rl-intro/master/assets/5.1.first-visit-mc.png" alt="first-visit MC prediction">]
### Estimation of Action Values
- Estimate $q_*$ when a model is not available
- Averaging returns starting from state $s$, taking action $a$ following policy $\pi$
- Need to estimate the value of all the actions from each state
- *Exploring starts*: $\pi(s,a)>0~~~\forall{s,a}$

---
# Monte Carlo Control
- Use GPI as DP
$$\pi\_0 \stackrel{E}{\longrightarrow} q\_{\pi\_0} \stackrel{I}{\longrightarrow} \pi\_1 \stackrel{E}{\longrightarrow} q\_{\pi\_1} \stackrel{I}{\longrightarrow} \pi\_2 \stackrel{E}{\longrightarrow} ... \stackrel{I}{\longrightarrow} \pi\_\* \stackrel{E}{\longrightarrow} q\_{\pi\_\*}$$

- Policy evaluation $\stackrel{E}{\longrightarrow}$: using MC methods for prediction

- Policy improment $\stackrel{I}{\longrightarrow}$: policy greedy w.r.t the current value function

- Meets the policy improvement theorem
$$
\begin{aligned}
q\_{\pi\_k}\big(s,\pi\_{k+1}(s)\big) &= q\_{\pi\_k}\big(s,\arg\max\_a q\_{\pi\_k}(s,a)\big)
\\cr &= \max\_a q\_{\pi\_k}(s,a)
\\cr & \ge q\_{\pi\_k}\big(s,\pi\_k(s)\big)
\\cr & \ge v\_{\pi\_k}(s)
\end{aligned}
$$

  if, $\pi\_{k+1}=\pi\_k$, then $\pi\_k=\pi\_\*$
---
# Monte Carlo Control
- Converage conditions assumptions:
  - (1) episodes have exploring starts $\pi(s,a)>0~~~\forall s,a$

  - (2) policy evaluation could be done with an infinite number of episodes

- Monte Carlo without Exploring Starts
  - **on-policy** methods: evaluate or improve the policy that is used to make decisions

  - **off-policy** methods: evaluate or improve the policy different from that is used to generate the data
---
# Monte Carlo Exploring Starts
- Alterate between evaluation and improvement on an episode-by-episode basis

- Convergence to this fixed point (fixed point is optimal policy $\pi_*$) seems inevitable

.center[<img width="100%" src="https://raw.githubusercontent.com/dominhhai/rl-intro/master/assets/5.3.mc-es.png" alt="Monte Carlo Exploring Starts">]
---
# On-Policy method
- Learn about policy currently executing

- Policy is generally soft $\pi(a|s)>0$

- ε-soft policy like ε-greedy:
  - probability of nongreedy is $\dfrac{\epsilon}{| \mathcal A(s) |}$
  - and, probability of greedy is $1-\epsilon+\dfrac{\epsilon}{| \mathcal A(s) |}$

- ε-greedy with respect to $q_\pi$ is an improvement over any ε-soft policy $\pi$

$$
\begin{aligned}
q\_\pi\big(s,\pi'(s)\big) &= \sum\_a \pi'(a | s) q\_\pi(s,a)
\\cr &= \frac{\epsilon}{| \mathcal A(s) |}\sum\_a q\_\pi(s,a) + (1-\epsilon)\max\_a q\_\pi(s,a)
\\cr &\ge v\_\pi(s)
\end{aligned}
$$
- Converages to the best ε-soft policy $v\_\pi=\tilde v\_\* ~~~, \forall s\in\mathcal S$
---
# On-Policy method
.center[<img width="100%" src="https://raw.githubusercontent.com/dominhhai/rl-intro/master/assets/5.4.e-soft.png" alt="On-Policy method">]
---
# Off-policy method
- Learn the value of the target policy $\pi$ from experience due to behavior policy $b$
  - Optimal policy: target policy

  - Exploratory & generate policy: behavior policy

- More powerful and general than on-policy
  - On-policy methods is special case in which $\pi = b$

- Greater variance and slower to converge

- Coverage assumption: $b$ generates behavior that covers, or includes, $\pi$
$$\pi(a | s) > 0 \implies b(a | s) > 0$$
---
# Off-policy method
- Method: use importance sampling
  - Estimate expected values under one distribution given samples from another
  - Importance-sampling ratio: weighting returns according to the relative probability of their trajectories under the two policies
- The relative probability of the trajectory under 2 polices depend only on the 2 policies and the sequence:
  $$\rho\_{t:T-1} = \prod\_{k=1}^{T-1}\frac{\pi(A\_k | S\_k)}{b(A\_k | S\_k)}$$

- Expected value of target policy:
  $$v\_\pi(s) = E\big[\rho\_{t:T-1}G\_t | S\_t=s\big]$$
  where, $G_t$ is the returns of $b$ : $v_b(s) = E\big[G_t | S_t=s\big]$

- Indexing time steps in a way that increases across episode boundaries
  - first episode ends in terminal state at time $t-1=100$
  - next episode begins at time $t=101$
---
# Off-policy method
- 2 types of importance sampling:
  - Ordinary importance sampling:
    $$V(s) = \frac{\sum\_{t\in\mathscr T(s)}\rho\_{t:T(t)-1}G\_t}{| \mathscr T |}$$
  - Weighted importance sampling:
    $$V(s) = \frac{\sum\_{t\in\mathscr T(s)}\rho\_{t:T(t)-1}G\_t}{\sum\_{t\in\mathscr T(s)}\rho\_{t:T(t)-1}}$$

    where:
      - $\mathscr T(s)$: set of all time steps in which state $s$ is visited
      - $T(t)$: first time of termination following time $t$
      - $G\_t$: returns after $t$ up through $T(t)$
      - $\\{G\_t\\}\_{t\in\mathscr T(s)}$ are the returns that pertain to state $s$
      - $\\{\rho\_{t:T(t)-1}\\}\_{t\in\mathscr T(s)}$ are the corresponding importance-sampling ratios
---
# Incremental MC prediction
- For on-policy:
  - Exactly the same methods as Bandits
  - But, for the average returns $G_t$ instead of average rewards $R_t$

- For ordinary importance sampling: scaling returns by $\rho_{t:T(t)-1}$
- For weighted importance sampling
  - Have sequence of returns $G\_1, G\_2, ..., G\_{n-1}$ all starting in the same state
  - Corresponding random weight $W\_i$ (e.g., $W\_i = \rho\_{t\_i:T(t\_i)-1}$)
    $$V\_n = \frac{\sum\_{k=1}^{n-1}W\_kG\_k}{\sum\_{k=1}^{n-1}W\_k} ~~~, n\ge 2$$
  - update rule:
    $$
    \begin{cases}
     V\_{n+1} &= V\_n + \dfrac{W\_n}{C\_n}\big[G\_n - V\_n\big] ~~~, n\ge 1
     \\cr
     C\_{n+1} &= C\_n + W\_{n+1} ~~~, C\_0 = 0
    \end{cases}
    $$
can apply to on-policy when $\pi=b, W=1$
---
# Incremental MC prediction
.center[<img width="100%" src="https://raw.githubusercontent.com/dominhhai/rl-intro/master/assets/5.6.weighted-importance-sampling.png" alt="Incremental MC prediction">]
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

- Usually, $\text{threshold}\in [1,5]$

- Simple, Effective

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
.center[![LSTM](/images/talk_dl_lstm.png)]

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
- Cell's Output: $\delta h\_t = \partial J\_t/\partial \mathbf h\_t$

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
