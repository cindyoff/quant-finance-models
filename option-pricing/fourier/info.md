# Fast Fourier transform (FFT)

Option pricing based on the academic paper written by Madan (1999) for the _Journal of Computational Finance_. 

## Some concepts explained

### Kronecker delta function
Noted as $\delta_{ij}$, it is a two variable-function that allows only 2 outcomes : 1 and 0. The function gives 1 when the two variables are equal, and 0 if not. 

### Simpson's rule (weightings)
This rule provides the estimate of the definite integral function. Used when the exact antiderivative function is difficult, near impossible, to determine analytically. Accuracy is enhanced by modeling the region under the curve as a series of parabolic elements, instead of the usual rectangle-shaped elements. 

The basic formula to approximate the integral of $f(x)$ from $a$ to $b$ using the Simpson's rule is the following :

$\frac{b-a}{6}*[f(a) + 4\frac{a+b}{2}+f(b)]$ 

Source : [Simpson's rule, Djellouli](https://adamdjellouli.com/articles/numerical_methods/4_integration/simpsons_rule)

### Dirac delta function
