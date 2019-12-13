def decode_img(image, dim):
    layers = []
    image_it = iter(image)
    while True:
        pixel = []
        pixels = []
        for _ in range(dim[1]):
            for _ in range(dim[0]):
                pixel.append(next(image_it))
            pixels.append(pixel)
        layers.append(pixels)


assert decode_img(123456789012, (3,2)) == [['123','456'], ['789','012']]