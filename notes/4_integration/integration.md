## Trapeziod method

![trapezoid](https://user-images.githubusercontent.com/37275728/188944637-3e912cfb-f8f2-40f4-b664-c4e5cf81a64f.png)

$h = \frac{b-a}{N -1}$

N - number of points

Total area (integral)

$$\int_a^b f(x)dx \approx h\sum_{k=1}^{N} \frac{f(x_{k-1})+f(x_k)}{2}$$

## Simpson's method

![simpson](https://user-images.githubusercontent.com/37275728/188944644-e3f47dbf-ba97-472f-8891-7e12906566d3.png)

$h = \frac{b-a}{2}$

$$\int_a^b f(x)dx \approx \frac{h}{3} \sum_{k=1}^{N/2} \{f(x_{2k-2})+4f(x_{2k-1})+f(x_{2k}))\}$$
