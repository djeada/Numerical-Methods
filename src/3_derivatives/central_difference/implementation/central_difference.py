def central_difference(f, x, h):
    fxph = f(x + h)
    fxnh = f(x - h)
    result = (fxph - fxnh) / (2 * h)
    return result

