def is_palindroma(parola):
    for i,char in enumerate(parola):
        if char == parola[-i-1]:
            return 'la parola è palindroma'
        return 'non lo è'

print(is_palindroma('anna'))
print(is_palindroma('sz<qzjickqeuiojxsnmklcn'))
