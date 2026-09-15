## Least Squares Regression

Least squares chooses model coefficients to minimize the sum of squared residuals, where a residual is an observed value minus its fitted value. Unlike interpolation, the fitted model need not pass through every observation.

This note derives linear least squares, explains how to solve it numerically, and works through a line fit with a prediction and residual checks.

### Inputs and Goal

**Inputs:** a finite design matrix $X\in\mathbb R^{N\times p}$ and response vector $y\in\mathbb R^N$. Here $N$ counts observations and $p$ counts coefficients, including an intercept if used. **Goal:** find $\hat\beta$ minimizing the residual sum of squares and predict at a new design vector $v_*$.

For a line, row $i$ is $[1,x_i]$; for a quadratic it is $[1,x_i,x_i^2]$. The model is linear in its coefficients, even when columns are nonlinear transformations of the original inputs. See the [regression overview](regression.md) for statistical assumptions and model selection.

### Derivation of the Normal Equations

Write the residual vector as $r=y-X\beta$. Expanding its squared norm gives

$$
\begin{aligned}
\operatorname{RSS}(\beta)&=(y-X\beta)^\top(y-X\beta)\\
&=y^\top y-2\beta^\top X^\top y+\beta^\top X^\top X\beta.
\end{aligned}
$$

Differentiate with respect to the coefficients:

$$
\nabla\operatorname{RSS}=-2X^\top y+2X^\top X\beta.
$$

Setting the gradient to zero yields

$$
X^\top X\hat\beta=X^\top y.
$$

The Hessian is $2X^\top X$. For every vector $v$,

$$
v^\top(2X^\top X)v=2\|Xv\|_2^2\ge0.
$$

Thus every solution of the normal equations is a global minimum. If $X$ has full column rank, the Hessian is positive definite and the coefficients are unique. Otherwise, different coefficient vectors can have the same fitted vector $X\hat\beta$; an SVD solver can select the minimum-norm solution. Rank deficiency does not mean a least-squares minimizer fails to exist.

### Numerical Algorithm

1. Construct $X$ and $y$, including a column of ones if an intercept is intended. Check dimensions, finite values, and scaling.
2. Solve least squares directly using QR or SVD. With a full-rank reduced QR factorization $X=QR$, solve $R\hat\beta=Q^\top y$ by back-substitution.
3. Compute $\hat y=X\hat\beta$ and $r=y-\hat y$. Check $X^\top r\approx0$, allowing for floating-point roundoff.
4. Predict using the same feature construction: $\hat y_*=v_*^\top\hat\beta$.

The identity $\hat\beta=(X^\top X)^{-1}X^\top y$ is useful for algebra but is not the recommended numerical algorithm. For full-rank $X$, $\kappa_2(X^\top X)=\kappa_2(X)^2$: forming the normal equations worsens conditioning. Applying SVD to the already formed $X^\top X$ does not undo that loss.

The repository's educational `least_squares` routine expects the full design matrix, forms the normal equations, and rejects underdetermined or rank-deficient inputs (and zero rows). Those are implementation restrictions, not restrictions on the existence of least-squares solutions. For a direct solver, [NumPy's `lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html) also reports rank and singular values.

### Worked Example: Fit, Check, and Predict

**Inputs:** $(x,y)=(1,1),(2,2),(3,2)$ and query $x_*=4$. **Goal:** fit a line with an intercept, calculate its residuals and training $R^2$, and predict the response at the query.

**Step-by-step**:

I. Add an intercept term (column of ones):

$$
X = \begin{bmatrix}
1 & 1 \\
1 & 2 \\
1 & 3 \\
\end{bmatrix}, \quad
y=\begin{bmatrix}1 \\ 2 \\ 2\end{bmatrix}
$$

II. Compute $X^\top X$ and $X^\top y$:

$$
X^\top X = \begin{bmatrix} 1+1+1 & 1+2+3 \\ 1+2+3 & 1+4+9 \end{bmatrix} = \begin{bmatrix} 3 & 6 \\ 6 & 14 \end{bmatrix}
$$

$$
X^\top y = \begin{bmatrix} 1 \cdot 1 + 1 \cdot 2 + 1 \cdot 2 \\ 1 \cdot 1 + 2 \cdot 2 + 3 \cdot 2 \end{bmatrix} = \begin{bmatrix} 5 \\ 11 \end{bmatrix}
$$

III. Solve the two normal equations:

$$
3\hat\beta_0+6\hat\beta_1=5,\qquad
6\hat\beta_0+14\hat\beta_1=11.
$$

Subtract twice the first equation from the second:

$$
(14-12)\hat\beta_1=11-10
\implies\hat\beta_1=\frac12.
$$

IV. Back-substitute for the intercept:

$$
3\hat\beta_0=5-6\left(\frac12\right)=2
\implies\hat\beta_0=\frac23.
$$

The determinant $3(14)-6^2=6>0$ confirms that this two-variable system has a unique solution.

Thus, the fitted line is:

$$
\hat{y} = \frac{2}{3} + \frac{1}{2}\,x
$$

V. Verify at data points and compute residuals:

| $x$ | $y$ | $\hat{y}$ | Residual $(y - \hat{y})$ |
|-----|-----|-----------|--------------------------|
| 1 | 1 | $\frac{2}{3} + \frac{1}{2} = \frac{7}{6} \approx 1.167$ | $-\frac{1}{6} \approx -0.167$ |
| 2 | 2 | $\frac{2}{3} + 1 = \frac{5}{3} \approx 1.667$ | $\phantom{-}\frac{1}{3} \approx 0.333$ |
| 3 | 2 | $\frac{2}{3} + \frac{3}{2} = \frac{13}{6} \approx 2.167$ | $-\frac{1}{6} \approx -0.167$ |

A separate optimality check uses the unrounded residuals:

$$
\sum r_i=-\frac16+\frac13-\frac16=0,
\qquad\sum x_ir_i=-\frac16+\frac23-\frac36=0.
$$

Thus $X^\top r=0$, as required by the normal equations.

VI. Compute the coefficient of determination ($R^2$):

Mean of observed values:

$$
\bar{y} = \frac{1 + 2 + 2}{3} = \frac{5}{3}
$$

Total Sum of Squares:

$$
TSS = \sum_{i=1}^{3}(y_i - \bar{y})^2 = \left(1 - \frac{5}{3}\right)^2 + \left(2 - \frac{5}{3}\right)^2 + \left(2 - \frac{5}{3}\right)^2 = \frac{4}{9} + \frac{1}{9} + \frac{1}{9} = \frac{2}{3}
$$

Residual Sum of Squares:

$$
RSS = \sum_{i=1}^{3}(y_i - \hat{y}_i)^2 = \left(\frac{1}{6}\right)^2 + \left(\frac{1}{3}\right)^2 + \left(\frac{1}{6}\right)^2 = \frac{1}{36} + \frac{1}{9} + \frac{1}{36} = \frac{1}{6}
$$

$$
R^2 = 1 - \frac{RSS}{TSS} = 1 - \frac{1/6}{2/3} = 1 - \frac{1}{4} = \frac{3}{4} = 0.75
$$

The fitted line reduces the training sum of squared errors by 75% relative to predicting the sample mean. This is not an out-of-sample accuracy guarantee.

VII. Prediction for a new input:

For $x_{\text{new}} = 4$:

$$
\hat{y} = \frac{2}{3} + \frac{1}{2} \cdot 4 = \frac{2}{3} + 2 = \frac{8}{3} \approx 2.667
$$

The prediction at $x_*=4$ is an **extrapolation**, because the observed inputs range from 1 to 3. The algebra provides a value, but the data alone do not validate the linear trend beyond that range.

### Advantages

- **Closed-Form Solution**: Provides an explicit formula for the optimal parameters, enabling direct interpretation.
- **Efficient for Small Problems**: Works well with relatively small datasets and few features.
- **Foundational Method**: Forms the basis for many advanced regression techniques and regularized models.

### Limitations

- **Model choice**: Linear least squares assumes a model linear in its coefficients. Polynomial and other fixed basis functions are allowed, but an unsuitable basis can miss the underlying pattern.
- **Sensitive to Outliers**: Squared errors emphasize large errors more heavily, making the model sensitive to outliers.
- **Rank and conditioning**: Dependent columns prevent unique coefficient identification; nearly dependent columns amplify perturbations. Use a direct QR/SVD solver, reconsider features, or introduce justified regularization.
