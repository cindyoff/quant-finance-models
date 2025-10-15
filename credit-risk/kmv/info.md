# KMV model

# References
- _Credit risk_ course taught by Pr. Hamidou Diallo (2025, Université Paris Panthéon-Assas)
- [Zieliński, University of Economics in Katowice (2013)](https://cejsh.icm.edu.pl/cejsh/element/bwmeta1.element.desklight-e6c5a7ad-d41f-4add-801b-e100432a8b90/c/8_T.Zielinski_Mertons_and_KMV_Models....pdf)
- [Bharath and Shumway, University of Michigan (2004)](https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=637342)

# KMV model
The model tries to overcome some flaws of the Merton's model. It was developed in 2002 by Moody's (previously known as Moody's Analytics).

# Merton's model flaws
The first significant problem of Merton's model is that both the firm value and its volatility are usually unobserved. However, implicit estimates of those two measures can be given via prices of traded securities by the firm. As a consequence, we can use the prices of security traded securities as the value of the option (call) to be used in the model to estimate the firm's value. 

+++

# KMV explained
## Key concept
The KMV model adds a step to compute the critical threshold when a firm is defaulting. This critical threshold is known as the "Default Point" (DPT). 
The DPT is approximated by the following equation : 
$$
DPT = STD + 0.5 LTD
$$
Where : 
- $DPT$ : default point
- $STD$ : short term debt
- $LTD$ : long term debt

An intermediate phase of computation of an index is created in the KMV model. The index is called "Distance to Default" (DD). It is defined as below : 
$$
DD = \frac{E(A_T)-DPT}{\sigma}
$$
Where : 
- $\sigma$ : volatility
- $E(A_T)$ : expected asset value
- $DPT$ : default point

Concretely, the larger the DD, the smaller the probability of default (PD), thus less chance the company will default. 

## Two ways of calculating DD
+++

# Some concepts explained
++++