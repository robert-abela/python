def vowelsFilterSimple():
    fullName = input('Enter full name: ')
    filteredName = ''
    for ch in fullName:
        if ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u':
            filteredName = filteredName + ch

    print(filteredName)

def vowelsFilterAdvanced():
    fullName = input('Enter full name: ')
    filteredName = ''
    for ch in fullName:
        if ch.lower() not in 'aeiou':
            filteredName = filteredName + ch

    print(filteredName)


vowelsFilterAdvanced()

