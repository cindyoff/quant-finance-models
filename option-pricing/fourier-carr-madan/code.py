# packages
import matplotlib.pyplot as plt
import numpy as np
import cmath

# Black Scholes model - characteristic function for the log of underlying asset price (S)
def characteristicfunction_bs(u, S0, r, sigma, T):
    return np.exp(1j * u * np.log(S0) + T * (1j*u*r - 0.5 * sigma**2 * u**2))

# FFT algorithm
def psi(u, r, T, alpha, cf): # psi function
    numerator = np.exp(-r*T) * cf(u - 1j*(alpha + 1))
    denominator = alpha**2 + alpha - u**2 + 1j * (2*alpha + 1) * u
    return numerator / denominator

def fft_algo(cf, alpha, eta, r, T, N):
    """
    FFT algorithm
    eta : integration grid
    alpha : damping factor
    cf : characteristic function of log(S_T)
    N : number of FFT points
    r : risk-free rate
    T : maturity
    """
    u = np.arange(N)
    a = np.pi / eta
    vu = eta * u
    lambd = 2 * np.pi / N
    ku = lambd * np.arange(N) - a
    coeff = np.exp(-alpha * ku) / np.pi

    # Simpson's weight rule
    simpson = (3 + (-1)**u - (u == 0)) / 3

    call = simpson * eta * psi(u, r, T, alpha, cf) * np.exp(-1j * a * vu)
    call = call * coeff
    call_real = np.real(np.fft.fft(call))
    return (ku, call_real)

# numerical example - values to be used
S0 = 100
r = 0.05
sigma = 0.2
T = 5
eta = 0.25
N = 4096
alpha = 1.5

cf = lambda u: characteristicfunction_bs(u, S0, r, sigma, T)
ku, price = fft_algo(cf=cf, alpha=alpha, eta=eta, r=r, T=T, N=N)
K = np.exp(ku)

# visualization graph
plt.plot(K, price)
plt.xlabel("Strike")
plt.ylabel("Call price")
plt.title("Vanilla call price")
plt.grid()
plt.show()
