# vanilla option valuation with binomial tree (Cox-Ross-Rubinstein model)
def binomial_vanilla(S0, K, T, r, sigma, N, option_type='call'):
    # S0 : initial price
    # K : strike
    # T : time to maturity, in years
    # r : risk-free rate
    # sigma : volatility
    # N : number of time steps
    
    dt = T / N # time step
    u = np.exp(sigma * np.sqrt(dt)) # up movement
    d = 1 / u # down movement
    p = (np.exp(r * dt) - d) / (u - d) # risk-neutral probablity
    
    price_tree = np.zeros((N + 1, N + 1)) # tree initialization, matrix of 0
    
    for j in range(N + 1): # payoff at each leaf node
        ST = S0 * (u ** j) * (d ** (N - j))
        if option_type == 'call':
            price_tree[N, j] = max(ST - K, 0)  # call payoff
        else:
            price_tree[N, j] = max(K - ST, 0)  # put payoff

    # backward induction
    for i in range(N - 1, -1, -1): # from maturity to present
        for j in range(i + 1):
            price_tree[i, j] = np.exp(-r * dt) * (p * price_tree[i + 1, j + 1] + # up movement 
                                                  (1 - p) * price_tree[i + 1, j]) # down movement
    
    return price_tree[0, 0] # option price today

# validation against Black Scholes model
def black_scholes(S0, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        return K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)

# example for validation : checking for convergence of prices or not
S0, K, T, r, sigma, N = 100, 100, 1, 0.05, 0.2, 1000
binomial_price = binomial_vanilla(S0, K, T, r, sigma, N)
bs_price = black_scholes(S0, K, T, r, sigma)
print(f"Binomial: {binomial_price:.4f}, Black-Scholes: {bs_price:.4f}")
