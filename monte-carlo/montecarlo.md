# Monte Carlo simulations

Algorithmic method that aims to calculate a numerical value through a great number of random paths. 

The law of large numbers ensures the convergence of the estimated price towards its real price. Moreover, the central limit theorem is needed for option pricing under the risk-neutral measure. 

# Model validation : Black-Scholes
In order to place the Monte Carlo simulations into context, we use the Black-Scholes formula under the risk-neutral measure $\mathbb{Q}$, specified as follows : 

$$
\frac{dS_t}{S_t} = \mu \cdot dt + \sigma \cdot dW_t
$$

Where : 
- $\sigma$ : volatility
- $S_t$ : value of the underlying asset
- $\mu$ : mean
- $W_t$ : Brownian motion 

# Variance reduction methods
Several methods to reduce the variance of the simulations exist : 
- Antithetic variate
- Importance sampling
- Control variate
- Random sampling

# References
- [Pr. Bruno Bouchard (CREST)](https://www.ceremade.dauphine.fr/~bouchard/pdf/polymc.pdf)
- [Mathematical Institute of Toulouse](https://www.math.univ-toulouse.fr/~agarivie/Telecom/agregMaths/reducvariance.pdf)