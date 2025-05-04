# Fast Fourier transform (FFT)

Algorithm for the option pricing of a call (vanilla), at-the-money (ATM), based on the academic paper written by Carr and Madan (1999) for the _Journal of Computational Finance_. 

Call price, noted as $C(k_u)$ :

$$
\[C(k_u) = \frac{\exp(-\alpha k_u)}{\pi} \sum_{j=1}^{N} e^{-i \frac{2\pi}{N} (j-1)(u-1)} e^{i b v_j} \psi(u_j) \frac{\eta}{3} \left( 3 + (-1)^j - \delta_{j-1} \right)\]
$$

With :
- $i$ : a complex number
- $k_u = log(K_u)$ : logarithm of the strike
- $N$ : number of iterations within the FFT algorithm
- $j$ : summation index
- $\eta$ : integration grid
- $u$ : frequency within the Fourier space
- $\delta_{j-1}$ : Kronecker delta function
- $\alpha$ : damping factor
- $\psi(u_j)$ : Fourier transform of the modified payoff function
  - With $\psi(u_j) = \frac{e^{-rT} \ \phi\left(u - i(\alpha + 1)\right)}{\alpha^2 + \alpha - u^2 + i(2\alpha + 1)u}$
  - And : $\phi(\left(u - i(\alpha + 1)\right)$ the characteristic function (from Black Scholes model)

Paper link : ["Option Valuation Using the Fast Fourier
Transform", Carr and Madan (1999)](https://www.researchgate.net/profile/Dilip-Madan-2/publication/2519144_Option_Valuation_Using_the_Fast_Fourier_Transform/links/55235a820cf2a2d9e146f0bf/Option-Valuation-Using-the-Fast-Fourier-Transform.pdf?_sg%5B0%5D=started_experiment_milestone&origin=journalDetail&_rtd=e30%3D)

## Some concepts explained

### Kronecker delta function
Noted as $\delta_{ij}$, it is a two variable-function that allows only 2 outcomes : 1 and 0. The function gives 1 when the two variables are equal, and 0 if not. 

Source : [Kronecker delta function, Wolfram Math World](https://mathworld.wolfram.com/KroneckerDelta.html)

### Simpson's rule (weightings)
This rule provides the estimate of the definite integral function. Used when the exact antiderivative function is difficult, near impossible, to determine analytically. Accuracy is enhanced by modeling the region under the curve as a series of parabolic elements, instead of the usual simple-shaped elements (rectangles or trapezoids). 

The basic formula to approximate the integral of $f(x)$ from $a$ to $b$ using the Simpson's rule is the following :

$\frac{b-a}{6}*[f(a) + 4\frac{a+b}{2}+f(b)]$ 

A weight of 1 is given to the extreme values, whereas a weight of 4 is given to odd indices and 2 if even. 

Source : [Simpson's rule, Djellouli](https://adamdjellouli.com/articles/numerical_methods/4_integration/simpsons_rule)

### Delta sequence
It refers to a sequence of strongly peaked functions for which we have the following result : 

$\\lim_{n \to \infty} \int_{-\infty}^{+\infty} \delta_n(x) f(x) dx\=f(0)$

Source : [Delta sequence, Wolfram Math World](https://mathworld.wolfram.com/DeltaSequence.html)

### Dirac delta function
Noted as $\delta(x)$, it is viewed as the derivative of the Heaviside Step function. In other words we have : 

$\frac{d}{dx}[H(x)] = \delta(x)$

Source : [Dirac delta function, Worlfram Math World](https://mathworld.wolfram.com/DeltaFunction.html)
