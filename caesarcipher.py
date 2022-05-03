#Darnell Love
#darnell.love@bison.howard.edu
#https://github.com/darnell-love27/Unix_Lab_Git_Lab

import sys

encryption_option = input("Would you like to Encode or Decode? ")

should_decode = "decode" in encryption_option.lower()


cipher_message = str(input("What is your cipher message? "))

encrypt_message = ""

if should_encode:
   

      if ord(cipher_message[i]) == 32:

        encrypt_message = encrypt_message + chr(ord(cipher_message[i]))
       
      elif ord(cipher_message[i]) == 33:    
          encrypt_message = encrypt_message + chr(ord(cipher_message[i]))
         
      elif ord(cipher_message[i]) == 34:    
          encrypt_message = encrypt_message + chr(ord(cipher_message[i]))  
         
      elif ord(cipher_message[i]) == 45:    
          encrypt_message = encrypt_message + chr(ord(cipher_message[i]))
         
      elif ord(cipher_message[i]) == 44:    
          encrypt_message = encrypt_message + chr(ord(cipher_message[i]))
         
      elif ord(cipher_message[i]) == 46:    
          encrypt_message = encrypt_message + chr(ord(cipher_message[i]))
         
      elif ord(cipher_message[i]) == 47:    
          encrypt_message = encrypt_message + chr(ord(cipher_message[i]))

      elif (ord(cipher_message[i])) + cipher_num > 122:
        back = (ord(cipher_message[i]) + cipher_num) - 122
        encrypt_message += chr(back + 96)

      elif (ord(cipher_message[i])) + cipher_num > 90 and ord(cipher_message[i]) <=96:
        back = (ord(cipher_message[i]) + cipher_num) - 90
        encrypt_message += chr(back + 64)
      else:
        encrypt_message += chr(ord(cipher_message[i]) + cipher_num)

    print(encrypt_message)

elif should_decode:
  decrypt_message = ""
  for i in range(len(cipher_message)):
    if ord(cipher_message[i]) == 32:
      decrypt_message += chr(ord(cipher_message[i]))
     
    elif ord(cipher_message[i]) == 33:    
        decrypt_message = encrypt_message + chr(ord(cipher_message[i]))
         
    elif ord(cipher_message[i]) == 34:    
        decrypt_message = encrypt_message + chr(ord(cipher_message[i]))  
         
    elif ord(cipher_message[i]) == 45:    
        decrypt_message = encrypt_message + chr(ord(cipher_message[i]))
         
    elif ord(cipher_message[i]) == 44:    
        decrypt_message = encrypt_message + chr(ord(cipher_message[i]))
         
    elif ord(cipher_message[i]) == 46:    
        decrypt_message = encrypt_message + chr(ord(cipher_message[i]))
         
    elif ord(cipher_message[i]) == 47:    
        decrypt_message = encrypt_message + chr(ord(cipher_message[i]))

        if (ord(cipher_message[i]) - cipher_num) < 65:
            back2 = (ord(cipher_message[i]) - cipher_num) + 26
            decrypt_message += chr(back2)
        else:
            decrypt_message += chr(ord(cipher_message[i]) - cipher_num)
    
    elif ord(cipher_message[i]) >= 97 and ord(cipher_message[i])<= 122:
        if (ord(cipher_message[i]) - cipher_num) < 97:
            back2 = (ord(cipher_message[i]) - cipher_num) + 26
            decrypt_message += chr(back2)
        else:
            decrypt_message += chr(ord(cipher_message[i]) - cipher_num)

  print(decrypt_message)

else:
  print("We only support encrypt/decrypt.")


