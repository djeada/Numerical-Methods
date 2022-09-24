## LU decomposition

The goal is to *decompose* a matrix so that it is computationally cheaper to calculate the solution of the following equation:

$$A\boldsymbol{x}^{n+1} = \boldsymbol{b}(\boldsymbol{x}^n, \ldots)$$

The matrix $A$ get's decomposed into to other matrices $L$ and $U$:

$$ A = LU $$

$L$ is a lower-triangular matrix and $U$ is an upper-triangular matrix. 
These matrices conatin all the infomration needed for the Gaussian elimination.

$$ A\boldsymbol{x} = \boldsymbol{b} \iff (LU)\boldsymbol{x} = \boldsymbol{b} \iff  L(U\boldsymbol{x}) = \boldsymbol{b} $$

We introduce a new notation for the $U$ and $x$ product:

$$\boldsymbol{c}=U\boldsymbol{x}$$

We can then rewrite the previous equation in the following way:

$$ L\boldsymbol{c} = \boldsymbol{b} $$

Since $L$ is in lower-triangular form we can quickly solve the above eqaution.

The last step is this equation:

$$ U\boldsymbol{x} = \boldsymbol{c} $$

## Algorithm
