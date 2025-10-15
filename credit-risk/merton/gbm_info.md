# Geometric brownian motion (GBM)

## Resources
- [Stojkoski, Sandev, Basnarkov, Kocarev and Metzler (2020)](https://www.mdpi.com/1099-4300/22/12/1432)

## Introduction
A geometric brownian motion (GBM) is a continuous-time stochastic process in which the logarithm of the randomly varying quantity of interest follows a brownian motion with drift, with the drift often written as $\mu$. 

## Properties of a GBM
# Non-ergodicity
The stochastic process is a non-ergodic regime if an observable's average does not equal to the time average (source : [Ergodic process, Wikipedia](https://en.wikipedia.org/wiki/Ergodic_process))
The time-averaged growth rate is dependent on both the drift and randomness in the system, whereas the ensemble growth rate is only dependent on the drift. 

# Heterogenous diffusion and turbulent diffusion
- Heterogeneous diffusion : the magnitude of the randomness depends on our current position. Therefore, a bigger value experiences bigger random shocks. 
- Turbulent diffusion : random shocks are proportional to the price, when the price is high, variations can be very large and volatile, resembling a turbulent and chaotic system. 

# Fat-tailed distributions and GBM
The GBM is not able to correctly reproduce assets with fat-tailed characteristics observed in reality. 
Alternatives added to remediate this issue : 
- local volatility
- stochastic volatility
- time-varying volatility
- models with noise following a fat-tailed distribution
