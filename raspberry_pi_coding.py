def label(colors):
    colors_list = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    reading = []
    counter = 1
    for color in colors:
        if counter < 3:
            reading.append(str(colors_list.index(color)))
        if counter == 3:
            x = 10**colors_list.index(color)
            reading.append((x))
            break
        counter += 1
    y = int(''.join(reading[0:2]))
    value = x*y
    if value/1000 < 1:
        return str(value) + ' ohms'
    if 1 <= value/1000 <= 1000:
        return str(int(value/1000)) + ' kiloohms'
    if 1 <= value/1000000 <= 1000:
        return str(int(value/1000000)) + ' megaohms'
    if 1 <= value/1000000000 <= 1000:
        return str(int(value/1000000000)) + ' gigaohms'