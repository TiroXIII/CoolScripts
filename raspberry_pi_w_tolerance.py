def resistor_label(colors):
    colors_list = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    tolerance_list = {'grey':'0.05%','violet':'0.1%','blue':'0.25%','green':'0.5%','brown':'1%','red':'2%','gold':'5%','silver':'10%'}
    if len(colors) == 1:
        return str(colors_list.index(colors[0])) + ' ohms'
    elif len(colors) == 4:
        tolerance = tolerance_list[colors[3]]
        ohms = (10*colors_list.index(colors[0]) + colors_list.index(colors[1])) * 10**colors_list.index(colors[2])
    elif len(colors) == 5:
        tolerance = tolerance_list[colors[4]]
        ohms = ((100*colors_list.index(colors[0])) + (10*colors_list.index(colors[1])) + colors_list.index(colors[2])) * 10**colors_list.index(colors[3])

    if 1 <= ohms/1e9 < 1000:
        if (ohms/1e9).is_integer():
            return str(int(ohms/1e9)) + ' gigaohms ±' + tolerance
        return str(ohms/1e9) + ' gigaohms ±' + tolerance
    elif 1 <= ohms/1e6 < 1000:
        if (ohms/1e6).is_integer():
            return str(int(ohms/1e6)) + ' megaohms ±' + tolerance
        return str(ohms/1e6) + ' megaohms ±' + tolerance
    elif 1 <= ohms/1e3 < 1000:
        if (ohms/1e3).is_integer():
            return str(int(ohms/1e3)) + ' kiloohms ±' + tolerance
        return str(ohms/1e3) + ' kiloohms ±' + tolerance
    else:
        return str(ohms) + ' ohms ±' + tolerance