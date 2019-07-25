This is a cipher creaton tool written in Python to encrypt and decrypt a string of text.
This is done in response to the terragon ife Hub snacks to join the team.

The ceaser cipher is one of the widely used known encryption techiniques.It is a type of 
cipher in which each letter of the alphabet in the plain text is replaced by a letter in 
some fixed position of the alphabet. For example,with a shift of 3, E can become B(left) 
or H(right).

The tool created is a Command Line tool.it takes the agruement text,action and
key.it encrypts by shifting the letters left and decrypt by shifting right
The text is the string of text you want to encrypt or decrypt
The action is what you want to perform either encryption or decrytion 
The key is the number of shift you want.it should be between 1 and 26

To run the program,
go the cmd,make you are in the directory the file is.
enter python cipher.py text action key
where text=the string
action= e(  for ecryption)
or action = d( for decryption)
key= an integer value between 1-26
