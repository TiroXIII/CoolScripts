def label(colors):
    colors_list = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    ohms = (((10 * colors_list.index(colors[0])) + colors_list.index(colors[1])) * 10 ** colors_list.index(colors[2]))
    if ohms / 1000 < 1:
        return str(ohms) + ' ohms'
    if 1 <= ohms / 1000 <= 1000:
        return str(int(ohms / 1000)) + ' kiloohms'
    if 1 <= ohms / 1000000 <= 1000:
        return str(int(ohms / 1000000)) + ' megaohms'
    if 1 <= ohms / 1000000000 <= 1000:
        return str(int(ohms / 1000000000)) + ' gigaohms'
