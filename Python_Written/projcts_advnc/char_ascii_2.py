word = 'hacker'
sequence = ''
print("\n")
for i in range ( 97,123):
    char = chr(i)
    if( char in word):
        char = char.upper()
    sequence += char
    if sequence.endswith(word.upper()):
       break 
print(sequence , "\n")

#output = AbCdEfgHijKlmnopqRstuvwxyz