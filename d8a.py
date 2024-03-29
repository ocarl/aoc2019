def decode_img(image, dim):
    layers = []
    image_it = iter(str(image))
    while True:
        try:
            pixels = []
            for _ in range(dim[1]):
                pixel = []
                for _ in range(dim[0]):
                    pixel.append(next(image_it))
                pixels.append(''.join(pixel))
            layers.append(pixels)
        except StopIteration:
            break
    return layers

assert decode_img(123456789012, (3,2)) == [['123','456'], ['789','012']]

def calc_shit(image, dim):
    the_layer = None
    min_zeros = 25
    layers = decode_img(image, dim)
    for layer in layers:
        zeros = 0
        for pixel in layer:
            zeros += sum('0' == x for x in pixel)
        if zeros < min_zeros:
            min_zeros = zeros
            the_layer = layer
    return sum([sum(x=='2' for x in pixel) for pixel in the_layer])*sum( [sum(x=='1' for x in pixel) for pixel in the_layer])


#assert calc_shit(123456789012, (3,2)) == 1
#assert calc_shit(1234567890120112, (4,2)) == 6

with open('input8.txt') as f:
    print(calc_shit(f.read(), (25,6)))
        
