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

def make_picture(image, dim):
    output = [['3']*dim[0]]*dim[1]
    layers = decode_img(image, dim)
    layers.reverse()
    for layer in layers:
        for i, pixels in enumerate(layer):
            for j, pixel in enumerate(pixels):
                if pixel == '1':
                    output[i][j] = '1'
                elif pixel == '0':
                    output[i][j] = '0'
    return output
        

with open('input8.txt') as f:
    #raw = make_picture(f.read(), (25,6))
    raw = make_picture('0222112222120000', (2,2))
    print(raw)
    print('\n'.join(''.join(x for x in line) for line in raw))
        
