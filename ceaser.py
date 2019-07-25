import click
def Ceaser(text,action,key):
   action=action.lower()
   key=int(key)
   if (action == 'd' or  action == 'e'):
      if (int(key)<27):
         if action == 'e':
            key=-key
         else:
            pass
         en=''
         for i in text:
            if i.isalpha():
               if i.isupper():
                  en=en+chr((ord(i)+int(key)-65)%26+65)
               else:
                  en=en+chr((ord(i)+int(key)-97)%26+97)
            else:
               en=en+i
         return en
      else:
        return "use --help to get directions" 
   else:
      return "use --help to get directions"

@click.command()
@click.argument('text')
@click.argument('action')
@click.argument('key')
def main(text,action, key):
   """
   
   A simple tool that takes a string of text and encrypts it using a key.
   You are to provide string of text and tell us what you want to do with the text you can either encrypt or decrypt it.
   for encryption-e 
   for decryption-d
   A key is used for the encryption and decryption.the key should be between 1 and 26.
   check documentation on github to know how it works
   
   """
   Ttext=Ceaser(text,action,key)
   print(Ttext)

if __name__ == "__main__":
    main()