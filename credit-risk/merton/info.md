# Merton model for credit risk modelling

## Resources
- _Credit risk_ course taught by Pr. Hamidou Diallo (2025, Université Paris Panthéon-Assas)
- [Valášková and Klieštik (2014)](https://d1wqtxts1xzle7.cloudfront.net/66847837/Assessing_Credit_Risk_by_Merton_Model20210503-19049-mvqdbk.pdf?1738413134=&response-content-disposition=inline%3B+filename%3DAssessing_Credit_Risk_by_Merton_Model.pdf&Expires=1746128251&Signature=LuQSzqca-sxtI0q1E1geElLG-nn0zPOhM9KBdaNua8Sg-TEFPkIJXAkc9A~62D-c3XPX2VQfRcSVc37vrZgGJZCC-X-uujEGnM9V6BzoUlr3GVaeitI8k6U7M8dpE4YF8WSD7AaWt0kjnh3cyetf8JQsGjDZ~YSYYIkZ2qT5Te-1j46r8zlTqcv2kVOZwXGHJovlM6akcOM7Ah820BG3BKbDTPUTjWJpORUNiZXcIT4HdfsOCq6iPCAdwHCWbwXGrmTvGqmZDugWVS4gbDIw~xvkyWLH1SgRkb8tKOUU05MpZpgAXLcTQ6s0-PKPZ0cTwFpQy~BY-S3iCS6szcQlZw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
- [Boulleys, Ngameni and Tcheugi (TNP Consultants, 2023)](https://www.tnpconsultants.com/wp-content/uploads/2023/06/Merton-Model-in-Credit-Risk-Modelling-version-2023.pdf)
- [Hull, Nelken and White (2004)](https://www.researchgate.net/profile/John-Hull-6/publication/228294160_Merton's_Model_Credit_Risk_and_Volatility_Skews/links/00b7d5335d8db065b1000000/Mertons-Model-Credit-Risk-and-Volatility-Skews.pdf?origin=journalDetail&_tp=eyJwYWdlIjoiam91cm5hbERldGFpbCJ9)

## Merton model

### Assumptions
- The [Modigliani-Miller theorem](#modigliani-miller-theorem-mm-theorem) holds
- No transaction costs and taxes, company assets are infinitely divisible and all market participants are perfectly informed
- [Short selling](#short-selling) is possible
- The liabilities of the company consist of one zero-coupon bond with face value $K$ and maturity time $T$
- Company's assets are financed by equity ($E_t$)
- Debt structure and risk-free rate ($r$) are constant over time
- The riskiness of investment cannot be influenced by how close the company is to the default situation
- A company may only be declared bankrupt at the end of the time period $T$ (maturity time of the zero-coupon bond)
- Rates for renting and lending capital are the same
- Company cannot pay dividends or issue new debt until the maturity $T$
- Company assets follow a lognormal distribution, therefore they cannot be negative
- Absence of arbitrage in the market
- No costs associated with bankruptcy
- Market is assumed to be frictionless, therefore the value of the company's asset is equal to the sum of the value of debt obligation and the value of equity at a date $t < T$
- Asset value development ($A_T$) is described by a geometric brownian motion (GBM)
Here, $A_T$ follows a geometric brownian motion given by the following stochastic differential equation (SDE) :

$$ 
\frac{dA_t}{A_t} = rd_t + \sigma_AdW_t
$$

Where :
- $W_t$ is a standard brownian motion under the risk-neutral measure
- $r$ denotes the constant risk-free interest rate
- $\sigma_A$ is the asset's return volatility (assumed to be constant)

Default occurs when the company is not able to pay debt holders at maturity $T$.

### Potential scenarios at maturity
From all the assumptions, we can write the following : 

$$
A_t = E_t + K
$$

Where $E_t$ is the equity of the company. 

2 scenarios are possible at maturity $T$ : 
1. The value of company's assets exceeds the one of liabilities ($A_T > K$). In this case, debt holders receive $K$ and the shareholder receives $E_T = A_T - D_T$
2. The value of the company's assets is below the one of liabilities ($A_T < K$). In this situation, shareholders hand over control of the company to debt holders by exercising the limited liability option. Debt holders liquidate the company and share the generated revenues among themselves. 

We use the two following equations to summarise the scenarios : 

$$
E_T = max(A_T - D_T ;0)
$$

$$
K = min(A_T; K)
$$

### Credit risk default probability
In the Merton's model, the default case happens when, at time maturity $T$, the value of the company's asset $A_T$ are below the face value of the debt $K$. We can compute the default probability via $PD$ : 

$$ 
PD = Prob(A_T < K)
$$

## Some concepts explained

### Modigliani-Miller theorem (M&M theorem)
Developed by economists Franco Modigliani and Merton Miller in 1958, this theorem is widely used in corporate finance. The main idea of the theory is that the capital structure of a company does not affect its overall value. Two versions of this theory were made : the first one in which the hypothesis of efficient markets was made and the final one excluding the possibility of efficient markets. Therefore, the second version of this theorem is closer to reality by admitting the existence of taxes, transaction and agency costs as well as asymmetric information.  

Source : [M&M theorem, CFI](https://corporatefinanceinstitute.com/resources/valuation/mm-theorem/)

### Short selling
Short selling is the sale of a security the seller does not own at the time of entering into the agreement with the intention of buying it back at a later point in time in order to deliver it. 
Two types of short selling : 
- covered short selling : the seller has made arrangements to borrow the securities before the sale
- naked short selling : the seller has not borrowed the securities when the short sale occurs

An example of financial instrument being often exchanged in this case is CDS (credit default swap). It is a derivative contract that acts as a form of insurance against the credit risk default of a corporation or a government. 

Source : [European Commission](https://finance.ec.europa.eu/capital-markets-union-and-financial-markets/financial-markets/securities-markets/short-selling_en#:~:text=on%20short%20selling-,Definition,in%20order%20to%20deliver%20it.)

