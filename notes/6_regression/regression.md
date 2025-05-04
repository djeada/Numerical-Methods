## Regression Analysis

Regression analysis and curve fitting are important tools in statistics, econometrics, engineering, and modern machine-learning pipelines.  At their core they seek a deterministic (or probabilistic) mapping
$\widehat f: \mathcal X \longrightarrow \mathcal Y$
that minimizes a suitably chosen loss function with respect to a sample of observations
$\mathcal D = \{(\mathbf x_1,y_1),\dots,(\mathbf x_N,y_N)\}\subseteq \mathcal X\times\mathcal Y.$

A **regression problem** is typically posed under the additive error model

$$
y_i = f_*(\mathbf{x}_i) + \varepsilon_i,
\qquad
\mathbb{E}[\varepsilon_i \mid \mathbf{x}_i] = 0,
\qquad
\mathrm{Var}(\varepsilon_i) = \sigma^2.
$$

where $f\_\*$ is an (unknown) deterministic function and $(\varepsilon\_i)$ are random errors.  The analyst’s objective is to construct an estimator $\widehat f$ (or equivalently to estimate a parameter vector $\widehat{\boldsymbol\theta}$ specifying $\widehat f$) such that some notion of risk—mean-squared error, negative log-likelihood, predictive log-loss, etc.—is minimized.

Below we preserve the original high-level outline but expand each section with mathematical exactitude.  Symbols used repeatedly are collected in the following table.

| Symbol                                                      | Meaning                                                           |
| ----------------------------------------------------------- | ----------------------------------------------------------------- |
| $N$                                                       | sample size (number of observations)                              |
| $p$                                                       | number of predictors (features)                                   |
| $\mathbf X \in \mathbb R^{N\times p}$                     | design / model matrix whose $i$-th row is $\mathbf x\_i^\top$ |
| $\mathbf y = (y\_1,\dots,y\_N)^\top$                      | vector of responses                                               |
| $\boldsymbol\beta\in\mathbb R^{p}$                        | vector of unknown regression coefficients                         |
| $\widehat{\boldsymbol\beta}$                              | estimator of $\boldsymbol\beta$                                 |
| $\mathbf r=\mathbf y-\mathbf X\widehat{\boldsymbol\beta}$ | vector of residuals                                               |
| $\|\cdot\|\_2$                                             | Euclidean (ℓ2) norm                                               |

### Curve Fitting

Curve fitting emphasizes the geometrical problem of approximating a cloud of points by a parametric curve or surface.  The archetypal formulation is **polynomial least-squares**: given scalar inputs $x\_i\in\mathbb R$, fit an $m$-degree polynomial

$P_m(x)=\sum_{k=0}^{m} a_k x^{k}\quad (\boldsymbol a\in\mathbb R^{m+1})$

by minimizing the **sum-of-squares loss**

$$
S(\mathbf{a})
= \sum_{i=1}^N \bigl(P_m(x_i) - y_i\bigr)^2.
$$

In matrix form let $\mathbf V\in\mathbb R^{N\times(m+1)}$ be the *Vandermonde matrix* with $V\_{ik}=x\_i^{k}$ and $\mathbf a=(a\_0,\dots,a\_m)^\top$.  The normal equations read
$\mathbf V^{\top}\mathbf V\,\widehat{\mathbf a}=\mathbf V^{\top}\mathbf y.$

Provided $\mathbf V^{\top}\mathbf V$ is nonsingular (which fails if $m \ge N$ or data are collinear), the minimizer is uniquely given by
$\widehat{\mathbf a}=(\mathbf V^{\top}\mathbf V)^{-1}\mathbf V^{\top}\mathbf y.$

![curve_fitting](https://github.com/djeada/Numerical-Methods/assets/37275728/03a26675-9baa-4557-92fb-2ab86c9d7b7c)

> **Remark 1 (Overfitting and Regularisation).**  High-degree polynomials can interpolate noisy data yet extrapolate disastrously.  Ridge ($\ell\_2$) or Lasso ($\ell\_1$) penalties enforce smoothness or sparsity:
> $S_{\lambda}(\boldsymbol a)=\underbrace{\|\mathbf V\boldsymbol a-\mathbf y\|_2^2}_{\text{data-fit}}\; +\; \lambda\underbrace{\|\boldsymbol a\|_q^q}_{\text{regulariser}},\quad q\in\{1,2\}.$
> Closed-form solutions exist for $q=2$; for $q=1$ convex optimisation is required.

Other classical curve-fitting families include **splines**, **B-splines**, **Bezier curves**, **wavelet bases**, and **kernel smoothers** (e.g. Nadaraya–Watson).  Each trades parametric flexibility against interpretability and computational cost.

### Regression Analysis

In modern statistical language, *regression* is synonymous with *conditional mean modelling*.  We assume
$\mathbb E[\,y\mid\mathbf x\,]=\mu(\mathbf x;\,\boldsymbol\beta),$
where $\mu(\cdot;,\boldsymbol\beta)$ is a known link indexed by parameters $\boldsymbol\beta$.  The task is to estimate $\boldsymbol\beta$ given i.i.d. samples.

#### Linear Model

When

$$
\mu(\mathbf{x}, \boldsymbol\beta)
= \mathbf{x}^\top \boldsymbol\beta.
$$

the model is **linear in parameters**.  

Writing $\mathbf X\boldsymbol\beta$ for the fitted values, the *ordinary least squares* (OLS) estimator is obtained by solving

$$
\hat{\boldsymbol\beta}_{\mathrm{OLS}}
= \arg\min_{\boldsymbol\beta}\,\bigl\|\mathbf{y}-\mathbf{X}\,\boldsymbol\beta\bigr\|_2^2.
$$

Assuming $rank(\mathbf X)=p\le N$, the solution is

$\widehat{\boldsymbol\beta}_{\text{OLS}}=(\mathbf X^{\top}\mathbf X)^{-1}\mathbf X^{\top}\mathbf y.$

**Gauss–Markov Theorem.**  Under spherical errors $\operatorname{Cov}(\boldsymbol\varepsilon)=\sigma^{2}\mathbf I\_N$, OLS is the **best linear unbiased estimator** (BLUE): for any linear unbiased estimator $\tilde{\boldsymbol\beta}=\mathbf C\mathbf y$ with $\mathbf C\mathbf X=\mathbf I\_p$ we have

$$
\mathrm{Var}\bigl(\tilde{\boldsymbol\beta}\bigr)
- \mathrm{Var}\bigl(\hat{\boldsymbol\beta}_{\mathrm{OLS}}\bigr)
\succeq 0.
$$

#### Generalised Linear Model (GLM)

For exponential-family responses ($y\sim\text{Bernoulli}$, Poisson, Gamma, etc.) we posit
$g(\,\mu(\mathbf x)\,) = \mathbf x^{\top}\boldsymbol\beta,$
where $g$ is a monotonic *link*.  E.g. logistic regression sets $g(\mu)=\log(\mu/(1-\mu))$.  Parameters are estimated via **maximum likelihood**
$\widehat{\boldsymbol\beta}=\arg\max_{\boldsymbol\beta}\; \prod_{i=1}^{N} f_Y\bigl(y_i;\,\mu_i(\boldsymbol\beta)\bigr),$
which is solved by Fisher scoring or (quasi-)Newton iterations.

#### Non-linear Least Squares (NLS)

Suppose $\mu(\mathbf x;\boldsymbol\beta)$ is nonlinear in $\boldsymbol\beta$, e.g. Michaelis–Menten kinetics
$\mu(x;V_{\max},K_m)=\frac{V_{\max}x}{K_m+x}.$  The loss
$S(\boldsymbol\beta)=\sum_{i=1}^{N}\bigl(y_i-\mu(\mathbf x_i;\boldsymbol\beta)\bigr)^2$
becomes non-convex; Levenberg–Marquardt or trust-region methods are standard.

### Concepts in Regression

| Concept                  | Formal Definition                                                                                                                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Parameter Estimation** | Solve $\widehat{\boldsymbol\theta}=\arg\min\_{\boldsymbol\theta},\mathcal L(\boldsymbol\theta)$ where $\mathcal L$ is least-squares or negative log-likelihood.                                      |
| **Fitted Values**        | $\widehat{y}\_i = \mu(\mathbf x\_i;\widehat{\boldsymbol\theta})$                                                                                                                                       |
| **Residuals**            | $r\_i=y\_i-\widehat{y}*i$ (raw), $\hat\varepsilon\_i=r\_i/(1-h*{ii})$ (externally studentised) with $h\_{ii}$ the hat-matrix diagonal.                                                             |
| **Loss / Error**         | Classical: $\mathrm{RSS}=\sum\_{i}r\_i^{2}$; Classification: $\mathrm{CrossEntropy}=-\sum\_{i} y\_i\log\widehat{y}\_i+(1-y\_i)\log(1-\widehat{y}\_i)$                                                |
| **Risk**                 | $R(\widehat f)=\mathbb E\bigl\[\mathcal L(\widehat f(\mathbf x),y)\bigr]$.  Empirical risk minimisation (ERM) replaces $\mathbb E$ by sample mean.                                                   |
| **Goodness-of-Fit**      | $R^2 = 1-\tfrac{\mathrm{RSS}}{\mathrm{TSS}}$ with $\mathrm{TSS}=\sum\_{i}(y\_i-\bar y)^2$; Adjusted $\bar R^2=1-(1-R^2)\tfrac{N-1}{N-p-1}$; AIC $=2k-2\log\hat L$; BIC $=k\log N-2\log\hat L$. |
| **Inference**            | Wald test: $\displaystyle z\_j = \frac{\widehat\beta\_j}{\widehat{\mathrm{se}}(\widehat\beta\_j)}\stackrel{\text{approx}}\sim N(0,1)$; LR test: $;2(\ell\_1-\ell\_0)\sim\chi^2\_{df}$.               |
| **Prediction Interval**  | For new $\mathbf x\_0$: $\widehat y\_0\pm t\_{N-p,1-\alpha/2};\widehat\sigma\sqrt{1+ \mathbf x\_0^{\top}(\mathbf X^{\top}\mathbf X)^{-1}\mathbf x\_0}$.                                              |

---

### Types of Regression Methods

1. **Ordinary Least Squares (OLS)**  – Closed-form, BLUE under Gauss–Markov conditions.
2. **Ridge Regression** – Penalised least-squares with $\lambda|\boldsymbol\beta|\_2^2$; solution $\widehat{\boldsymbol\beta}=(\mathbf X^{\top}\mathbf X+\lambda\mathbf I)^{-1}\mathbf X^{\top}\mathbf y$.
3. **Lasso & Elastic Net** – $\ell\_1$ and mixed $\ell\_1+\ell\_2$ penalties promoting sparsity; solved by coordinate descent or LARS.
4. **Generalised Linear Models (GLM)** – Logistic, probit, Poisson; estimated by iteratively re-weighted least squares.
5. **Non-linear Regression (NLS)** – Use gradient-based optimisers; asymptotic theory requires identifiability and regularity.
6. **Robust Regression** – M-estimators with Huber or Tukey bisquare $\rho$-functions; minimises $\sum\_{i}\rho(r\_i/\hat\sigma)$.
7. **Quantile Regression** – Minimises asymmetric absolute loss $\sum\_{i}\rho\_\tau(r\_i)$ with $\rho\_\tau(u)=u(\tau-\mathbb 1\_{u<0})$.
8. **Bayesian Regression** – Places prior $p(\boldsymbol\beta)$, outputs posterior $p(\boldsymbol\beta\mid\mathbf y)\propto L(\boldsymbol\beta),p(\boldsymbol\beta)$; predictive distribution integrates over posterior.

> **Computational Note.**  High-dimensional ($p\gg N$) problems demand numerical linear-algebra tricks: Woodbury identity, iterative conjugate gradient, stochastic gradient descent (SGD), or variance-reduced methods (SVRG, SAGA).

---

### Worked Examples

#### Example 1 – OLS in Matrix Form

Let
$\mathbf X = \begin{bmatrix}1 & 0.8\\1 & 1.2\\1 & 1.9\\1 & 2.4\\1 & 3.0\end{bmatrix},\qquad \mathbf y = \begin{bmatrix}1.2\\1.9\\3.1\\3.9\\5.1\end{bmatrix}.$
Compute $\mathbf X^{\top}\mathbf X=\begin{bmatrix}5 & 9.3\9.3 & 19.49\end{bmatrix}$, $\mathbf X^{\top}\mathbf y=\begin{bmatrix}15.2\30.47\end{bmatrix}$, so
$\widehat{\boldsymbol\beta}=\begin{bmatrix}0.067\\1.689\end{bmatrix},\quad R^2=0.998.$  Thus $\widehat y=0.067+1.689x$.

#### Example 2 – Logistic Regression, MLE Derivatives

For binary data $y\_i\in{0,1}$ the log-likelihood is
$\ell(\boldsymbol\beta)=\sum_{i=1}^{N}\Bigl[y_i\,\mathbf x_i^{\top}\boldsymbol\beta-\log\bigl\{1+e^{\mathbf x_i^{\top}\boldsymbol\beta}\bigr\}\Bigr].$
Gradient and Hessian:
\begin{align}
\nabla\ell &= \mathbf X^{\top}(\mathbf y-\boldsymbol\pi),\qquad \boldsymbol\pi=\operatorname{logit}^{-1}(\mathbf X\boldsymbol\beta),\\
\nabla^2\ell &=-\mathbf X^{\top}\operatorname{diag}(\boldsymbol\pi\odot(1-\boldsymbol\pi)),\mathbf X;\text{ (negative definite)}.
\end{align}
Newton iteration: $\boldsymbol\beta^{(t+1)}=\boldsymbol\beta^{(t)}-(\nabla^2\ell)^{-1}\nabla\ell$.

---

### Applications

* **Finance & Econometrics** – Capital asset pricing (CAPM), term-structure models, volatility forecasting (GARCH regression), default-probability prediction.
* **Healthcare & Epidemiology** – Survival analysis (Cox proportional hazards), dose-response curves, genome-wide association studies (GWAS) via penalised regression.
* **Engineering** – System identification, Kalman-filter regressions, fatigue-life modelling.
* **Marketing & A/B Testing** – Uplift modelling, mixed-effect regressions for hierarchical data.
* **Machine Learning Pipelines** – Feature engineering baseline, stacking/blending meta-learners, interpretability audits.

---

### Limitations & Pitfalls

1. **Model Misspecification** – When $f\_\*(\mathbf x)$ lies outside the chosen hypothesis class, estimators are biased even as $N\to\infty$.
2. **Violation of IID** – Autocorrelated or clustered errors require GLS or sandwich covariances.
3. **Heteroscedasticity** – $\operatorname{Var}(\varepsilon\_i\mid\mathbf x\_i)=\sigma\_i^2$ invalidates OLS variance formulas; use White/HC estimators.
4. **Multicollinearity** – Near-linear dependence inflates $\operatorname{Var}(\widehat\beta\_j)$; ridge shrinks condition number.
5. **High-Leverage & Outliers** – Influence measures: Cook’s $D\_i=\frac{r\_i^2 h\_{ii}}{p\hat\sigma^2(1-h\_{ii})^2}$; robust M-estimators mitigate.
6. **Overfitting / High Variance** – Cross-validation, information criteria, or Bayesian model averaging select model complexity.
7. **External Validity** – Regression learns conditional mean on $\mathcal D$; distribution shift breaks prediction (covariate shift, concept drift).
8. **Causal Inference vs. Prediction** – Regression coefficients are not causal unless confounding is addressed (instrumental variables, RCTs, DAGs).

---

### Further Reading

1. Seber, G. A. F., & Lee, A. J. *Linear Regression Analysis*, 2e, Wiley (2003).
2. Hastie, T., Tibshirani, R., & Friedman, J. *The Elements of Statistical Learning*, 2e, Springer (2009).
3. McCullagh, P., & Nelder, J. *Generalized Linear Models*, 2e, Chapman & Hall (1989).
4. Kennedy, P. *A Guide to Econometrics*, 7e, Wiley-Blackwell (2008).
