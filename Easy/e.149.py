text = (raw_input(""))

vowels = ''.join([ch for ch in text if ch in 'aeiou'])
unvoweled = text.translate(None, 'aeiou ')

print (unvoweled)
print (vowels)




