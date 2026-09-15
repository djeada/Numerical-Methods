## Regression Analysis

Regression fits a relationship between inputs and an observed response. The goal is to describe a trend or predict a response at a new input. Observations may contain noise, so a fitted model usually does not pass through every point.

For example, given measurements of an input $x$ and a response $y$, we might choose a line $\hat y=\hat\beta_0+\hat\beta_1x$. Choosing the model family, estimating its coefficients, and checking its predictions are separate steps.

### How to Read This Chapter

This directory covers both regression and interpolation. They solve different problems:

| Task | Requirement | Start here |
| --- | --- | --- |
| Regression | Minimize a chosen loss over observations | [Least squares](least_squares.md) |
| Interpolation | Match every supplied value exactly | [Interpolation overview](interpolation.md) |
| Piecewise interpolation | Join nearby values with lines or smooth cubics | [Linear](linear_interpolation.md), [cubic spline](cubic_spline_interpolation.md) |
| Global polynomial interpolation | Construct one polynomial through distinct nodes | [Lagrange](lagrange_polynomial_interpolation.md), [Newton](newton_polynomial.md) |
| Central polynomial interpolation | Use equally spaced nodes in a central ordering | [Gauss formulas](gaussian_interpolation.md) |
| Scattered surface interpolation | Fit values at locations in two dimensions | [Thin plate spline](thin_plate_spline_interpolation.md) |

Interpolation can also be applied to noisy measurements, but it reproduces their noise. Exact agreement at the observations does not establish accuracy between them.

### Inputs, Model, and Objective

Throughout the regression notes, $N$ is the number of observations and $p$ is the number of fitted coefficients, **including the intercept when present**.

| Symbol | Meaning |
| --- | --- |
| $X\in\mathbb R^{N\times p}$ | Design matrix: one row per observation, one column per coefficient |
| $y\in\mathbb R^N$ | Observed responses |
| $\beta\in\mathbb R^p$ | Candidate coefficient vector |
| $\hat\beta$ | Estimated coefficient vector |
| $\hat y=X\hat\beta$ | Fitted responses |
| $r=y-\hat y$ | Residuals: observed minus fitted values |

For a line, row $i$ of $X$ is $[1,x_i]$ and $p=2$. The leading one creates the intercept. For a quadratic it is $[1,x_i,x_i^2]$ and $p=3$.

Ordinary least squares (OLS) solves

$$
\hat\beta=\operatorname*{arg\,min}_{\beta}\operatorname{RSS}(\beta),
\qquad \operatorname{RSS}(\beta)=\sum_{i=1}^N(y_i-(X\beta)_i)^2.
$$

The normal equations are

$$
X^\top X\hat\beta=X^\top y.
$$

If $X$ has full column rank, the coefficients are unique. The expression $(X^\top X)^{-1}X^\top y$ describes this solution algebraically; in numerical code, solve least squares directly with QR or SVD instead of forming an inverse. See the [derivation and solver discussion](least_squares.md).

### Linear in the Coefficients Does Not Mean a Straight Line

Polynomial regression of degree $d$ uses

$$
\hat y=\sum_{j=0}^d\hat\beta_jx^j,
\qquad X_{i,j+1}=x_i^j,\quad j=0,\ldots,d.
$$

It is linear in the unknown coefficients even though it curves as a function of $x$. This matrix has full column rank exactly when there are at least $d+1$ distinct input values. Repeated inputs are allowed in regression; they reduce the number of distinct locations available to identify the polynomial. Collinearity of the plotted responses is not the rank criterion.

By contrast, $\mu(x;V,K)=Vx/(K+x)$ is nonlinear in its unknown parameters. Nonlinear least squares generally needs an iterative solver and an initial estimate; convergence to a global minimum is not guaranteed.

### Worked Example: Fit a Line and Predict a Response

**Inputs:** the five observations below. **Goal:** fit $\hat y=\hat\beta_0+\hat\beta_1x$ by OLS, predict at $x_*=2$, and measure the training fit.

#### Step 1: Organize the Required Sums

| $x_i$ | $y_i$ | $x_i^2$ | $x_iy_i$ |
| --- | --- | --- | --- |
| 0.8 | 1.2 | 0.64 | 0.96 |
| 1.2 | 1.9 | 1.44 | 2.28 |
| 1.9 | 3.1 | 3.61 | 5.89 |
| 2.4 | 3.9 | 5.76 | 9.36 |
| 3.0 | 5.1 | 9.00 | 15.30 |
| Sum | 15.20 | 20.45 | 33.79 |

Also $N=5$ and $\sum x_i=9.30$. Thus

$$
X^\top X=\begin{bmatrix}5&9.30\\9.30&20.45\end{bmatrix},
\qquad X^\top y=\begin{bmatrix}15.20\\33.79\end{bmatrix}.
$$

#### Step 2: Solve the Two Equations

$$
5\hat\beta_0+9.30\hat\beta_1=15.20,
\qquad9.30\hat\beta_0+20.45\hat\beta_1=33.79.
$$

Multiply the second equation by 5 and subtract 9.30 times the first:

$$
(102.25-86.49)\hat\beta_1=168.95-141.36,
\qquad\hat\beta_1=\frac{27.59}{15.76}\approx1.750635.
$$

Back-substitute without rounding the slope:

$$
\hat\beta_0=\frac{15.20-9.30(27.59/15.76)}{5}
=\frac{-3.407}{15.76}\approx-0.216180.
$$

The fitted line is $\hat y\approx-0.216180+1.750635x$.

#### Step 3: Predict at the Requested Input

$$
\hat y(2)=\frac{-3.407+27.59(2)}{15.76}
=\frac{51.773}{15.76}\approx3.285089.
$$

This input lies within the observed range $[0.8,3.0]$. Predictions outside that range would be extrapolations.

#### Step 4: Check Residuals and Training Fit

Use the unrounded coefficients for calculation; values below are displayed to six decimals.

| $x_i$ | $y_i$ | $\hat y_i$ | $r_i=y_i-\hat y_i$ |
| --- | --- | --- | --- |
| 0.8 | 1.2 | 1.184327 | 0.015673 |
| 1.2 | 1.9 | 1.884581 | 0.015419 |
| 1.9 | 3.1 | 3.110025 | -0.010025 |
| 2.4 | 3.9 | 3.985343 | -0.085343 |
| 3.0 | 5.1 | 5.035723 | 0.064277 |

OLS satisfies $X^\top r=0$: here both $\sum r_i$ and $\sum x_ir_i$ are zero apart from floating-point roundoff. This is a useful independent check on the fitted coefficients.

$$
\operatorname{RSS}=\sum r_i^2\approx0.011998731,
\qquad\bar y=15.20/5=3.04.
$$

$$
\begin{aligned}
\operatorname{TSS}&=\sum(y_i-\bar y)^2\\
&=(-1.84)^2+(-1.14)^2+(0.06)^2+(0.86)^2+(2.06)^2\\
&=9.672,\\
R^2&=1-\frac{0.011998731}{9.672}\approx0.998759.
\end{aligned}
$$

This is a strong fit to these five observations. It does not by itself measure prediction accuracy on new data.

### Statistical Assumptions and Diagnostics

Computing OLS does not require normally distributed errors. Statistical interpretations require additional assumptions. For a fixed, full-rank design, write

$$
y=X\beta+\varepsilon,\qquad
\mathbb E[\varepsilon\mid X]=0,\qquad
\operatorname{Cov}(\varepsilon\mid X)=\sigma^2I.
$$

Under these assumptions, the Gauss–Markov theorem says OLS has the smallest covariance among estimators that are linear in $y$ and unbiased. It does not say OLS is best among every possible estimator. Heteroscedastic or correlated errors require a suitable covariance estimate or a model for their covariance.

With $p$ counting all coefficients, $N>p$, and $\operatorname{TSS}>0$:

| Quantity | Formula and interpretation |
| --- | --- |
| Residual variance estimate | $s^2=\operatorname{RSS}/(N-p)$ |
| Adjusted $R^2$ | $1-(\operatorname{RSS}/(N-p))/(\operatorname{TSS}/(N-1))$ |
| Leverage | $h_{ii}$, the diagonal of $H=X(X^\top X)^{-1}X^\top$ |
| Leave-one-out residual | $r_i/(1-h_{ii})$, when deleting observation $i$ leaves a full-rank design; this is not the ordinary residual |

For independent Gaussian errors with common variance, an exact prediction interval for a new, independent response at design vector $v_*$ is

$$
\hat y_*\ \pm\ t_{N-p,1-\alpha/2}\,s
\sqrt{1+v_*^\top(X^\top X)^{-1}v_*}.
$$

Here $v_*=[1,x_*]^\top$ for a line, $\alpha$ is the significance level, and $t_{\nu,q}$ is a Student-$t$ quantile. A confidence interval for the mean response omits the leading 1 under the square root. Under the same Gaussian assumptions, coefficient tests use Student-$t$ with $N-p$ degrees of freedom, not an exact standard normal reference.

If all responses are equal, TSS is zero and the displayed $R^2$ formula is undefined. For OLS with an intercept, training $R^2$ lies in $[0,1]$; this guarantee does not extend to held-out predictions or models without an intercept.

### Other Regression Models

| Model | What changes |
| --- | --- |
| Ridge | Add $\lambda\sum_{j=1}^{p-1}\beta_j^2$ to RSS; this convention leaves the intercept unpenalized |
| Lasso | Add $\lambda\sum_{j=1}^{p-1}\lvert\beta_j\rvert$; some fitted coefficients can become zero |
| Elastic net | Combine ridge and lasso penalties |
| Robust regression | Replace squared loss with a loss less sensitive to large residuals; high-leverage inputs can still be problematic |
| Quantile regression | Estimate a conditional quantile using asymmetric absolute loss |
| Generalized linear model | Relate a response mean to $X\beta$ through a link and specify a response distribution |
| Bayesian regression | Combine a likelihood with a prior to obtain a posterior over model parameters |

Scale predictor columns appropriately before penalizing coefficients, and choose penalty strength using validation. Coefficient shrinkage does not automatically impose a particular curve-smoothness constraint.

### Worked Example: One Logistic Regression Update

**Inputs:** binary responses $y=(0,0,1)^\top$ at $x=(-1,0,1)$, an intercept, and initial coefficients $\beta^{(0)}=(0,0)^\top$. **Goal:** perform one Newton update of the Bernoulli log-likelihood, then compute the probability at $x=1$.

Logistic regression models a probability $\pi_i=1/(1+e^{-(X\beta)_i})$. Its logit link is $\log(\pi_i/(1-\pi_i))=(X\beta)_i$.

#### Step 1: Compute Initial Probabilities and Residuals

$$
X=\begin{bmatrix}1&-1\\1&0\\1&1\end{bmatrix},
\quad\pi^{(0)}=\begin{bmatrix}1/2\\1/2\\1/2\end{bmatrix},
\quad y-\pi^{(0)}=\begin{bmatrix}-1/2\\-1/2\\1/2\end{bmatrix}.
$$

#### Step 2: Compute the Gradient and Curvature

For $\ell(\beta)=\sum_i[y_i(X\beta)_i-\log(1+e^{(X\beta)_i})]$,

$$
g=X^\top(y-\pi)=\begin{bmatrix}-1/2\\1\end{bmatrix},
\quad W=\operatorname{diag}(\pi_i(1-\pi_i))=\tfrac14I,
\quad -\nabla^2\ell=X^\top WX=\begin{bmatrix}3/4&0\\0&1/2\end{bmatrix}.
$$

#### Step 3: Solve for the Update

Solve $(X^\top WX)\delta=g$:

$$
\tfrac34\delta_0=-\tfrac12\implies\delta_0=-\tfrac23,
\qquad\tfrac12\delta_1=1\implies\delta_1=2.
$$

Hence $\beta^{(1)}=\beta^{(0)}+\delta=(-2/3,2)^\top$ and

$$
\pi^{(1)}(1)=\frac{1}{1+e^{-(-2/3+2)}}
=\frac{1}{1+e^{-4/3}}\approx0.791391.
$$

**Check and limitation:** the log-likelihood increases from approximately $-2.079442$ to $-0.715508$. This is one iteration, not a converged estimate. These data are completely separable: the threshold $x=1/2$ separates the two classes. Along $\beta=c(-1/2,1)^\top$ as $c\to\infty$, all observed-class probabilities approach 1. Thus the unpenalized likelihood has no finite maximizer. A penalty or prior can produce a finite estimate.

### Practical Workflow

1. State the response, predictors, intended prediction range, and loss.
2. Build the design matrix and check its rank and scaling.
3. Fit the model with a suitable numerical solver.
4. Inspect residuals for curvature, changing spread, dependence, and influential points.
5. Assess prediction error on held-out data or with cross-validation appropriate to the sampling process.
6. Report model assumptions and uncertainty alongside predictions. Regression alone does not establish causation.

### Reproduce the Calculations

From the repository root, run `python notes/6_regression/resources/verify_examples.py` with NumPy and SciPy installed. The script checks the worked examples across all nine notes against independent solvers, including spline boundary conditions and Gauss formulas for even and odd node counts.

### Further Reading

- Seber and Lee, *Linear Regression Analysis*, 2nd edition, Wiley, 2003.
- Hastie, Tibshirani, and Friedman, *The Elements of Statistical Learning*, 2nd edition, Springer, 2009.
- McCullagh and Nelder, *Generalized Linear Models*, 2nd edition, Chapman & Hall, 1989.
