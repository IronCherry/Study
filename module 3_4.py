def single_root_words(*other_words, root_words='ich'):
    same_wodrs = []
    for i in other_words:
        if root_words in i.lower():
            same_wodrs.append(i)
    return same_wodrs


result1 = single_root_words('rIch', 'riChiest', 'rICHalcum', 'cheers', 'richies')
#result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
#print(result2)
