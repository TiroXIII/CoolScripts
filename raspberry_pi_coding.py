def label(colors):
    colors_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    ohms = (((10 * colors_list.index(colors[0])) + colors_list.index(colors[1])) * 10 ** colors_list.index(colors[2]))
    if value/1000 < 1:
        return str(value) + ' ohms'
    if 1 <= value/1000 <= 1000:
        return str(int(value/1000)) + ' kiloohms'
    if 1 <= value/1000000 <= 1000:
        return str(int(value/1000000)) + ' megaohms'
    if 1 <= value/1000000000 <= 1000:
        return str(int(value/1000000000)) + ' gigaohms'