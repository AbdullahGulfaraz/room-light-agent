percept_sequence = ['Dark', 'Dim', 'Bright', 'Dark']

table = {
    'Dark': 'Turn On Light',
    'Dim': 'Leave Light As Is',
    'Bright': 'Turn Off Light'
}

for percept in percept_sequence:
    if percept == 'Dark':
        action = table[percept]
    elif percept == 'Dim':
        action = table[percept]
    elif percept == 'Bright':
        action = table[percept]
    print(f'Percept: {percept} => Action: {action}')
