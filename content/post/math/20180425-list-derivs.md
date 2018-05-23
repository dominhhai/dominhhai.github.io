---
title: "[Giải Tích] Tra cứu đạo hàm"
slug: list-derivs
date: 2018-04-25T16:31:37+09:00
categories:
- Toán
- Giải Tích
tags:
- Giải Tích
- Đạo Hàm
keywords:
- Calculus
- Giải Tích
- Common Derivatives
- Bảng đạo hàm
autoThumbnailImage: true
thumbnailImagePosition: left
thumbnailImage: https://res.cloudinary.com/dominhhai/image/upload/math/katex.png
metaAlignment: center
---
Đây là bản tóm tắt một số đạo hàm cơ bản và tính chất đạo hàm nhằm mục đích tra cứu cho nhanh.

<!-- toc -->

# 1. Đạo hàm thông dụng
## 1.1. Đa thức
| No. | Đạo hàm | No. | Đạo hàm |
| --- | --- | --- | --- |
| 1 | $\dfrac{d}{dx}\(c) = 0$ | 4 | $\dfrac{d}{dx}(x^n) = nx^{n-1}$ |
| 2 | $\dfrac{d}{dx}(x) = 1$ | 5 | $\dfrac{d}{dx}(cx^n) = cnx^{n-1}$ |
| 3 | $\dfrac{d}{dx}(cx) = c$ |  |  |

## 1.2. Mũ và Logarit
| No. | Đạo hàm | No. | Đạo hàm |
| --- | --- | --- | --- |
| 1 | $\dfrac{d}{dx}(a^x) = a^x\ln(a)$ | 3 | $\dfrac{d}{dx}\big(\ln(x)\big) = \dfrac{1}{x},~~~x>0$ |
| 2 | $\dfrac{d}{dx}(e^x) = e^x$ | 4 | $\dfrac{d}{dx}\big(\ln\lvert x\rvert\big) = \dfrac{1}{x},~~~x\ne 0$ |
|  |  | 5 | $\dfrac{d}{dx}\big(\log_a(x)\big) = \dfrac{1}{x\ln(a)},~~~x>0$ |

## 1.3. Lượng giác
| No. | Đạo hàm | No. | Đạo hàm |
| --- | --- | --- | --- |
| 1 | $\dfrac{d}{dx}(\sin x) = \cos x$ | 4 | $\dfrac{d}{dx}(\sec x) = \sec x\tan x$ |
| 2 | $\dfrac{d}{dx}(\cos x) = \sin x$ | 5 | $\dfrac{d}{dx}(\csc x) = -\csc x\cot x$ |
| 3 | $\dfrac{d}{dx}(\tan x) = \sec^2x$ | 6 | $\dfrac{d}{dx}(\cot x) = -\csc^2x$  |

## 1.4. Lượng giác ngược
| No. | Đạo hàm | No. | Đạo hàm |
| --- | --- | --- | --- |
| 1 | $\dfrac{d}{dx}(\sin^{-1}x) = \dfrac{1}{\sqrt{1-x^2}}$ | 4 | $\dfrac{d}{dx}(\sec^{-1}x) = \dfrac{1}{\lvert x\rvert\sqrt{x^2-1}}$ |
| 2 | $\dfrac{d}{dx}(\cos^{-1}x) = \dfrac{1}{\sqrt{1-x^2}}$ | 5 | $\dfrac{d}{dx}(\csc^{-1}x) = \dfrac{1}{\lvert x\rvert\sqrt{x^2-1}}$ |
| 3 | $\dfrac{d}{dx}(\tan^{-1}x) = \dfrac{1}{1+x^2}$ | 6 | $\dfrac{d}{dx}(\cot^{-1}x) = \dfrac{1}{1+x^2}$  |

## 1.5. Hypebolic
| No. | Đạo hàm | No. | Đạo hàm |
| --- | --- | --- | --- |
| 1 | $\dfrac{d}{dx}(\sinh x) = \cosh x$ | 4 | $\dfrac{d}{dx}(\text{sech}x) = -\text{sech}x\tanh x$ |
| 2 | $\dfrac{d}{dx}(\cosh x) = \sinh x$ | 5 | $\dfrac{d}{dx}(\text{csch}x) = -\text{csch}x\coth x$ |
| 3 | $\dfrac{d}{dx}(\tanh x) = \text{sech}^2x$ | 6 | $\dfrac{d}{dx}(\coth x) = -\text{csch}^2x$  |

# 2. Tính chất cơ bản
| No. |  |
| --- | --- |
| 1 | $\dfrac{d}{dx}\big(cf(x)\big) = cf^{\prime}(x)$ |
| 2 | $\dfrac{d}{dx}\big(f(x) \pm g(x)\big) = f^{\prime}(x) \pm  g^{\prime}(x)$ |
| 3 | $\dfrac{d}{dx}\big(f(x)g(x)\big) = f^{\prime}(x)g(x) + f(x)g^{\prime}(x)$ |
| 4 | $\dfrac{d}{dx}\big(\dfrac{f(x)}{g(x)}\big) = \dfrac{f^{\prime}(x)g(x) - f(x)g^{\prime}(x)}{g^2(x)}$ |
| 5 | $\dfrac{d}{dx}\Big(f\big(g(x)\big)\Big) = f^{\prime}\big(g(x)\big)g^{\prime}(x) $ |
| 6 | $\dfrac{d}{dx}\big(e^{g(x)}\big) = g^{\prime}(x)e^{g(x)} $ |
| 7 | $\dfrac{d}{dx}\Big(\ln\big(g(x)\big)\Big) = \dfrac{g^{\prime}(x)}{g(x)} $ |

