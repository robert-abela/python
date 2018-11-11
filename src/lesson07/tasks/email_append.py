email = input('Enter email: ')
if len(email) < 7:
    print('Error: mail address too short')
elif '@' not in email:
    print('Error: missing @')
elif email.startswith('@') or email.endswith('@'):
    print('Error: @ at start or end')
elif '.' not in email:
    print('Error: missing .')
elif email.startswith('.') or email.endswith('.'):
    print('Error: . at start or end')
elif email.index('@') > email.index('.'):
    print('Error: @ not before .')
else:
    try :
        f = open('file.log', 'a')
    except FileNotFoundError:
        print('Error: Log file not found')
    else:
        f.write(email+'\n')
        f.close()
