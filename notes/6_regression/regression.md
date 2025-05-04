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

| Symbol                                                      | Meaning                                                           |
| ----------------------------------------------------------- | ----------------------------------------------------------------- |
| $N$                                                       | sample size (number of observations)                              |
| $p$                                                       | number of predictors (features)                                   |
| $\mathbf X \in \mathbb R^{N\times p}$                     | design / model matrix whose $i$-th row is $\mathbf x\_i^\top$ |
| $\mathbf y = (y\_1,\dots,y\_N)^\top$                      | vector of responses                                               |
| $\boldsymbol\beta\in\mathbb R^{p}$                        | vector of unknown regression coefficients                         |
| $\widehat{\boldsymbol\beta}$                              | estimator of $\boldsymbol\beta$                                 |
| $\mathbf r=\mathbf y-\mathbf X\widehat{\boldsymbol\beta}$ | vector of residuals                                               |
| $\lVert \cdot \rVert_2$                                   | Euclidean ($\ell_2$) norm                                  |

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

> **Remark (Overfitting and Regularisation).**
> High-degree polynomials can interpolate noisy data yet extrapolate disastrously. Ridge ($\ell_2$) or Lasso ($\ell_1$) penalties enforce smoothness or sparsity:

$$
S_\lambda(a) = \lVert V\,a - y\rVert_2^2 + \lambda\,\lVert a\rVert_q^q,\quad q\in\{1,2\}
$$

> Closed-form solutions exist for $q=2$; for $q=1$ one must resort to convex optimisation.

Other classical curve-fitting families include **splines**, **B-splines**, **Bezier curves**, **wavelet bases**, and **kernel smoothers** (e.g. Nadaraya–Watson).  Each trades parametric flexibility against interpretability and computational cost.

### Regression Analysis

In modern statistics, **regression** refers to modeling the conditional mean

$$
\mathbb{E}[\,y\mid x\,] = \mu(x;\,\beta),
$$

where $\mu(\cdot;\beta)$ is a known function (link) indexed by parameters $\beta$. Given i.i.d. samples $(x_i,y_i)$, our goal is to estimate $\beta$.

#### Linear Model

If

$$
\mu(x;\beta) = x^\top \beta,
$$

the model is **linear** in the parameters. Writing the data matrix $X$ and response vector $y$, the OLS estimator solves

$$
\hat\beta = \arg\min_{\beta}\,\|\,y - X\beta\|_2^2.
$$

When $\mathrm{rank}(X)=p$, the closed-form solution is

$$
\hat\beta = (X^\top X)^{-1}X^\top y.
$$

**Gauss–Markov Theorem.** If $\mathrm{Cov}(\varepsilon)=\sigma^2I$, then among all linear unbiased estimators $\tilde\beta = Cy$ with $CX=I$, OLS has the smallest variance:

$$
\mathrm{Var}(\tilde\beta) - \mathrm{Var}(\hat\beta) \succeq 0.
$$

#### Generalized Linear Model (GLM)

For responses in the exponential family (e.g.\ Bernoulli, Poisson), we introduce a **link** $g$ so that

$$
g\bigl(\mu(x)\bigr) = x^\top \beta.
$$

For instance, in logistic regression $g(\mu)=\log\bigl(\mu/(1-\mu)\bigr)$. Parameters are found by maximizing the likelihood

$$
\hat\beta = \arg\max_{\beta}\prod_{i=1}^{N} f\bigl(y_i;\,\mu(x_i;\beta)\bigr),
$$

using Fisher scoring or Newton methods.

#### Nonlinear Least Squares (NLS)

When $\mu(x;\beta)$ is nonlinear in $\beta$ (e.g.\ Michaelis–Menten: $\mu(x;V,K)=Vx/(K+x)$), we minimize

$$
S(\beta) = \sum_{i=1}^N \bigl(y_i - \mu(x_i;\beta)\bigr)^2.
$$

This loss is generally non-convex; standard solvers include Levenberg–Marquardt or trust-region algorithms.

### Concepts in Regression

| Concept                  | Formal Definition                                                                                                                                        |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Parameter Estimation** | $\displaystyle \hat\theta = \arg\min_{\theta}\,\mathcal L(\theta)$ where $\mathcal L$ is least‐squares or negative log‐likelihood.                       |
| **Fitted Values**        | $\displaystyle \hat y_i = \mu(\mathbf x_i;\,\hat\theta)$                                                                                                 |
| **Residuals**            | $\displaystyle r_i = y_i - \hat y_i$                                                                                                                     |
|                          | $\displaystyle \hat\varepsilon_i = \frac{r_i}{1 - h_{ii}}$, with $h_{ii}$ the $i$th diagonal of the hat matrix.                                          |
| **Loss / Error**         | $\displaystyle \mathrm{RSS} = \sum_i r_i^2$                                                                                                              |
|                          | $\displaystyle -\sum_i \bigl[y_i\log\hat y_i + (1-y_i)\log(1-\hat y_i)\bigr]$                                                                            |
| **Risk**                 | $\displaystyle R(\hat f) = \mathbb{E}\bigl[\mathcal L(\hat f(\mathbf x),y)\bigr]$, empirical risk minimisation replaces $\mathbb{E}$ by the sample mean. |
| **Goodness-of-Fit**      | $\displaystyle R^2 = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}},\quad \mathrm{TSS} = \sum_i (y_i - \bar y)^2$                                                 |
|                          | $\displaystyle \bar R^2 = 1 - (1 - R^2)\,\frac{N-1}{N-p-1}$                                                                                              |
|                          | $\displaystyle \mathrm{AIC} = 2k - 2\log\hat L$                                                                                                          |
|                          | $\displaystyle \mathrm{BIC} = k\log N - 2\log\hat L$                                                                                                     |
| **Inference**            | $\displaystyle z_j = \frac{\hat\beta_j}{\widehat{\mathrm{se}}(\hat\beta_j)} \approx N(0,1)$                                                              |
|                          | $\displaystyle 2(\ell_1 - \ell_0)\sim \chi^2_{\text{df}}$                                                                                                |
| **Prediction Interval**  | $\displaystyle \hat y_0 \pm t_{N-p,\,1-\alpha/2}\,\hat\sigma\sqrt{1 + \mathbf x_0^\top (X^\top X)^{-1}\mathbf x_0}$                                      |

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

### Worked Examples

#### Example 1 – OLS in Matrix Form

We have $N=5$ observations $\{(x_i,y_i)\}$ and wish to fit

$$
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i,\qquad
\varepsilon_i\sim\text{mean }0.
$$

We stack the data as

$$
X = 
\begin{bmatrix}
1 & 0.8\\
1 & 1.2\\
1 & 1.9\\
1 & 2.4\\
1 & 3.0
\end{bmatrix}, 
\qquad
y =
\begin{bmatrix}
1.2\\
1.9\\
3.1\\
3.9\\
5.1
\end{bmatrix}.
$$

The OLS estimator is

$$
\hat\beta
= (X^\top X)^{-1}\,X^\top y.
$$

Compute

$$
X^\top X
= \begin{bmatrix}
5   & 9.30\\
9.30&20.45
\end{bmatrix},
\quad
X^\top y
= \begin{bmatrix}
15.20\\
33.79
\end{bmatrix}.
$$

Hence

$$
\hat\beta
= \begin{pmatrix}\hat\beta_0\\\hat\beta_1\end{pmatrix}
\approx
\begin{pmatrix}-0.236, 1.751\end{pmatrix}.
$$

The fitted line is

$$
\hat y = -0.236 + 1.751\,x.
$$

To assess fit, let $\bar y=15.20/5=3.04$. Then

$$
R^2
= 1 - \frac{\sum_i (y_i - \hat y_i)^2}{\sum_i (y_i - \bar y)^2}
\approx 0.998.
$$

#### Example 2 – Logistic Regression, MLE Derivatives

For binary data $y\_i\in{0,1}$ the log-likelihood is

$$
\ell(\beta) = \sum_{i=1}^N \bigl[y_i\,x_i^\top \beta - \log\bigl(1 + e^{x_i^\top \beta}\bigr)\bigr].
$$

Gradient and Hessian:

$$
\nabla\ell(\beta) = X^\top (y - \pi), 
\quad 
\pi = (1 + e^{-X\beta})^{-1},
$$

$$
\nabla^2\ell(\beta) = -\,X^\top \mathrm{diag}\bigl(\pi \circ (1 - \pi)\bigr)\,X 
\preceq0.
$$

Newton iteration: $\boldsymbol\beta^{(t+1)}=\boldsymbol\beta^{(t)}-(\nabla^2\ell)^{-1}\nabla\ell$.

### Applications

* **Finance & Econometrics** – Capital asset pricing (CAPM), term-structure models, volatility forecasting (GARCH regression), default-probability prediction.
* **Healthcare & Epidemiology** – Survival analysis (Cox proportional hazards), dose-response curves, genome-wide association studies (GWAS) via penalised regression.
* **Engineering** – System identification, Kalman-filter regressions, fatigue-life modelling.
* **Marketing & A/B Testing** – Uplift modelling, mixed-effect regressions for hierarchical data.
* **Machine Learning Pipelines** – Feature engineering baseline, stacking/blending meta-learners, interpretability audits.

### Limitations & Pitfalls

I. **Model Misspecification:**

When $f_*(\mathbf{x})$ lies outside the chosen hypothesis class, estimators remain biased even as $N \to \infty$.

II. **Violation of IID:**

Autocorrelated or clustered errors require GLS or “sandwich” covariance estimators.

III. **Heteroscedasticity:**

If $Var(\varepsilon_i \mid \mathbf{x}_i) = \sigma_i^2$, the usual OLS variance formula is invalid; use White’s (HC) estimators instead.

IV. **Multicollinearity:**

Near–linear dependence among columns of $X$ inflates $Var(\hat\beta_j)$; ridge regression can shrink the condition number.

V. **High Use & Outliers:**

Cook’s distance

$$D_i = \frac{r_i^2,h_{ii}}{p,\hat\sigma^2,(1 - h_{ii})^2}$$

identifies influential points; strong M–estimators mitigate their effect.

VI. **Overfitting / High Variance:**

Cross-validation, information criteria, or Bayesian model averaging help choose model complexity.

VII. **External Validity:**

Regression learns the conditional mean on $\mathcal{D}$; distribution shifts (covariate shift, concept drift) break prediction accuracy.

VIII. **Causal Inference vs. Prediction:**

Regression coefficients are not causal unless confounding is addressed (e.g.\ via instrumental variables, RCTs, or DAG-based adjustment).

### Further Reading

1. Seber, G. A. F., & Lee, A. J. *Linear Regression Analysis*, 2e, Wiley (2003).
2. Hastie, T., Tibshirani, R., & Friedman, J. *The Elements of Statistical Learning*, 2e, Springer (2009).
3. McCullagh, P., & Nelder, J. *Generalized Linear Models*, 2e, Chapman & Hall (1989).
4. Kennedy, P. *A Guide to Econometrics*, 7e, Wiley-Blackwell (2008).
