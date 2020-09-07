email = input('Enter email: ')
if len(email) < 6:
    print('Error: mail address too short')
elif email.count('@') != 1 :
    print('Error: email must contain exactly one @')
elif email.startswith('@') or email.endswith('@'):
    print('Error: @ at start or end')
elif '.' not in email:
    print('Error: missing .')
elif email.startswith('.') or email.endswith('.'):
    print('Error: . at start or end')
else:
    try :
        f = open('file.log', 'a')
    except FileNotFoundError:
        print('Error: Log file not found')
    else:
        f.write(email+'\n')
        f.close()
