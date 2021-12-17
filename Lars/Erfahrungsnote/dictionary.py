def zeugnis(dict):
    for key in dict:
        value = dict[key]
        roundedValue = round(value * 2) / 2
        if roundedValue < 1:
            roundedValue = float(1)
        elif roundedValue > 6:
            roundedValue = float(6)
        dict[key] = roundedValue
    return dict


print(zeugnis({'Deutsch': 4.3, 'English': 6.2, 'Französisch': 3.9}))

