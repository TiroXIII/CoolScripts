# A binary search algorithm finds an item in a list by repeatedly splitting it in half, only keeping the half which
# contains the item we're looking for. It allows us to quickly narrow down the possible locations of our item until
# we find it, or until we've eliminated all possible locations.

def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")
    new_list = sorted(search_list)
    middle = len(new_list)//2
    while new_list[middle] != value:
        if new_list[middle] > value:
            new_list = new_list[:middle]
            middle = len(new_list)//2
        elif new_list[middle] < value:
            new_list = new_list[middle + 1:]
            middle = len(new_list)//2
    return search_list.index(value)