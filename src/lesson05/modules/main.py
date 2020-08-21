# import the magic module
import magic

def do_some_magic():
    magic.trick_one()
    magic.trick_two()

def main():
    ans = input('Do you want to see some magic? ')
    if ans.lower() == 'yes':
      do_some_magic()
    else:
      print('Ok, Bye!')

# If this script is executed, then main() will be executed
if __name__ == '__main__':
    main()
