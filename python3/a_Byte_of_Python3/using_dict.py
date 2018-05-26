ab = {'Swaroop' : 'swaroop@swaroopch.com',
        'Larry':'larry@wall.rog',
        'wangxu':'13826261697@126.com',
        'Spammer':'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

del ab['Spammer']

print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
