---
title: "Reinforcement Learning: An Introduction. Chapter 5"
date: 2018-08-24
keywords:
- RL, Reinforcement Learning
description: "Reinforcement Learning: An Introduction, by Richard S. Sutton and Andrew G. Barto. Chapter 5."
renderMath: true
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/rl/logo.png
metaAlignment: center
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
- For on-policy: Exactly the same methods as Bandits

- For ordinary importance sampling: Scaling returns by $\rho_{t:T(t)-1}$

- For weighted importance sampling
  - Have sequence of returns $G\_1, G\_2, ..., G\_{n-1}$ all starting in the same state
  - Corresponding random weight $W\_i$ (e.g., $W\_i = \rho\_{t\_i:T(t\_i)-1}$)
    $$V\_n = \frac{\sum\_{k=1}^{n-1}W\_kG\_k}{\sum\_{k=1}^{n-1}W\_k} ~~~, n\ge 2$$
  - update rule:
    $$
    \begin{cases}
     V\_{n+1} &= V\_n + \dfrac{W\_n}{C\_n}\big[G\_n - V\_n\big] &, n\ge 1
     \\cr
     C\_{n+1} &= C\_n + W\_{n+1} &, C\_0 = 0
    \end{cases}
    $$
    - Can apply to on-policy when $\pi=b, W=1$
---
# Incremental MC prediction
.center[<img width="100%" src="https://raw.githubusercontent.com/dominhhai/rl-intro/master/assets/5.6.weighted-importance-sampling.png" alt="Incremental MC prediction">]
---
# Off-policy MC Control
- Requires behavior $b$ is soft: $b(a | s) &gt; 0$

- Advantage:
  - Target policy $\pi$ may be deterministic (e.g., greedy)

  - While the behavior policy $b$ can continue to sample all possible actions

- Disadvantages:
  - Learn only from the tails of episodes (the remaining actions in the episode are greedy)

  - Greatly slow learning when non-greedy actions are common (states appearing in the early portions of long episodes)
---
# Off-policy MC Control
.center[<img width="100%" src="https://raw.githubusercontent.com/dominhhai/rl-intro/master/assets/5.7.off-policy-mc-control.png" alt="off-policy MC Control">]
---
# Discounting-aware Importance Sampling
- Use discounted rewards structure of the returns to reduce the variance of off-policy estimators

- Let define, the **flat partial return**:
  $$\overline G\_{t:h} = R\_{t+1} + R\_{t+2} + ... + R\_h ~~~, 0\le t < h\le T$$

- Compute the **full return** $G_t$ by flat partial returns:

$$
\begin{aligned}
G\_t &= R\_{t+1} + \gamma R\_{t+2}  + \gamma^2 R\_{t+3} + ... + \gamma^{T-t-1} R\_T
\\cr &= (1-\gamma)R\_{t+1}
\\cr & \quad + (1-\gamma)\gamma(R\_{t+1} + R\_{t+2})
\\cr & \quad + (1-\gamma)\gamma^2(R\_{t+1} + R\_{t+2} + R\_{t+3})
\\cr & \quad \vdots
\\cr & \quad + (1-\gamma)\gamma^{T-t-2}(R\_{t+1} + R\_{t+2} + ... + R\_{T-1})
\\cr & \quad + \gamma^{T-t-1}(R\_{t+1} + R\_{t+2} + ... + R\_T)
\\cr &= (1-\gamma)\sum\_{h=t+1}^{T-1}\gamma^{h-t-1}\overline G\_{t:h} + \gamma^{T-t-1}\overline G\_{t:T}
\end{aligned}
$$
---
# Discounting-aware Importance Sampling
- Discount rate but have no effect if $\gamma=1$

- For ordinary importance-sampling estimator:
$$V(s)=\dfrac{\displaystyle\sum\_{t\in\mathscr T(s)}\Big( (1-\gamma)\sum\_{h=t+1}^{T(t)-1}\gamma^{h-t-1}\rho\_{t:h-1}\overline G\_{t:h} + \gamma^{T(t)-t-1}\rho\_{t:T(t)-1}\overline G\_{t:T(t)}\Big)}{| \mathscr T(s) |}$$

- For weighted importance-sampling estimator:
$$V(s)=\dfrac{\displaystyle\sum\_{t\in\mathscr T(s)}\Big( (1-\gamma)\sum\_{h=t+1}^{T(t)-1}\gamma^{h-t-1}\rho\_{t:h-1}\overline G\_{t:h} + \gamma^{T(t)-t-1}\rho\_{t:T(t)-1}\overline G\_{t:T(t)}\Big)}{\displaystyle\sum\_{t\in\mathscr T(s)}\Big( (1-\gamma)\sum\_{h=t+1}^{T(t)-1}\gamma^{h-t-1}\rho\_{t:h-1} + \gamma^{T(t)-t-1}\rho\_{t:T(t)-1}\Big)}$$
---
# Per-decision Importance Sampling
- One more way of reducing variance, even if $\gamma=1$

- Use structure of the returns as sum of rewards
$$
\begin{aligned}
\rho\_{t:T-1}G\_t &= \rho\_{t:T-1}(R\_{t+1}+\gamma R\_{t+2}+...+\gamma^{T-t-1} R\_T)
\\cr &= \rho\_{t:T-1}R\_{t+1}+\gamma\rho\_{t:T-1}R\_{t+2}+...+\gamma^{T-t-1}\rho\_{t:T-1}R_T
\end{aligned}
$$

  where, sub-term $\rho\_{t:T-1}R\_{t+k}$ depend only on the first and the last rewards
  $$E[\rho\_{t:T-1}R\_{t+k}] = E[\rho\_{t:t+k-1}R\_{t+k}]$$

- **per-decision** importance-sampling
$$E[\rho\_{t:T-1}G_t] = E[\tilde G_t]$$

  where, $$\tilde G\_t=\rho\_{t:t}R\_{t+1} + \gamma\rho\_{t:t+1}R\_{t+2} + \gamma^2\rho\_{t:t+2}R\_{t+3} + ... + \gamma^{T-t-1}\rho\_{t:T-1}R\_T$$
---
# Per-decision Importance Sampling
- Use for **ordinary** importance-sampling
  - Same unbiased expectation (in the first-visit case) as the ordinary importance-sampling estimator

  - But not consistent (do not converge to the true value with infinite data)

  $$V(s)=\frac{\sum_{t\in\mathscr T(s)}\tilde G_t}{| \mathscr T(s) |}$$

- Do NOT use for *weighted* importance-sampling
---
layout: true
class: center, middle
---
# Thank You 😊

Happy Coding!
