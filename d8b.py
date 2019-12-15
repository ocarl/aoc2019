def decode_img(image, dim):
    layers = []
    image_it = iter(image)
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

assert decode_img(str(123456789012), (3,2)) == [['123','456'], ['789','012']]

def make_picture(image, dim):
    length = (dim[0]*dim[1])
    output = ['3']*length
    layers = decode_img(image, dim)
    layers.reverse()
    for layer in layers:
        i = 0
        for pixels in layer:
            for pixel in pixels:
                if pixel == '1':
                    output[i] = '1'
                    i = (i+1)%length
                elif pixel == '0':
                    output[i] = '0'
                    i = (i+1)%length
                else:
                    i = (i+1)%length
                    
    return decode_img(output, dim)[0]
assert make_picture('0222112222120000', (2,2)) == ['01', '10']

with open('input8.txt') as f:
    raw = make_picture(f.read(), (25,6))
    print('\n'.join(raw))
        
