## Linear Interpolation

Linear interpolation is achieved by connecting two data points with a straight line.

For $x_i < x < x_{i+1}$:

$$\hat{y}(x) = y_i + \frac{(y_{i+1} - y_{i})(x - x_{i})}{(x_{i+1} - x_{i})}.$$


### Derivation
 
![Screenshot from 2022-09-07 21-23-10](https://user-images.githubusercontent.com/37275728/188960726-ac99ac89-f1b8-4b82-9761-5093cb91d4db.png)


$$\alpha = \frac{y_2 - y_1}{x_2 - x_1}$$

$$h = \alpha \cdot (x - x_1)$$

$$y = y_1 + h$$

$$y = y_1 + (x - x_1) \cdot \frac{y_2 - y_1}{x_2 - x_1}$$

### Example

We are given two points A(-2, 0) and B (2, 2).


![Screenshot from 2022-09-07 21-23-32](https://user-images.githubusercontent.com/37275728/188960814-569c5a91-82b4-415c-9840-f5ebd4cc421d.png)

Let's try to evaluate the value of the function at $x=1$

$$\hat{y}(x) = y_i + \frac{(y_{i+1} - y_{i})(x - x_{i})}{(x_{i+1} - x_{i})} = 0 + \frac{(2 - 0)(1 - (-2))}{(2 - (-2))} = 1.5$$
