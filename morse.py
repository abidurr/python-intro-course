
alphabets = {
  "a" : ".-",
  "b" : "-...",
  "c" : "-.-.",
  "d" : "-..",
  "e" : ".",
  "f" : "..-.",
  "g" : "--.",
  "h" : "....",
  "i" : "..",
  "j" : ".---",
  "k" : "-.-",
  "l" : ".-..",
  "m" : "--",
  "n" : "-.",
  "o" : "---",
  "p" : ".--.",
  "q" : "--.-",
  "r" : ".-.",
  "s" : "...",
  "t" : "-",
  "u" : "..-",
  "v" : "...-",
  "w" : ".--",
  "x" : "-..-",
  "y" : "-.--",
  "z" : "--..",
  " " : "\t",
    }

def encode_morse(message):
  global alphabets
  message = message.lower()
  for i in range(len(message)):
    print(alphabets[(message[i])], end = " ")
  print("")



morse = {
  ".-" : "a",
  "-..." : "b",
  "-.-." : "c",
  "-.." : "d",
  "." : "e",
  "..-." : "f",
  "--." : "g",
  "...." : "h",
  ".." : "i",
  ".---" : "j",
  "-.-" : "k",
  ".-.." : "l",
  "--" : "m",
  "-." : "n",
  "---" : "o",
  ".--." : "p",
  "--.-" : "q",
  ".-." : "r",
  "..." : "s",
  "-" : "t",
  "..-" : "u",
  "...-" : "v",
  ".--" : "w",
  "-..-" : "x",
  "-.--" : "y",
  "--.." : "z",
  "\t" : " ",
    }
    

def decode_morse(cmessage):
  global morse
  letter = ""
  cmessage = str(cmessage) + str(" ")
  for i in range(len(cmessage)):
    if cmessage[i] == "\\" and cmessage[i+1] == "t":
      print(" ", end = "")
    if cmessage[i] != " ":
      letter = str(letter) + str(cmessage[i])
    elif cmessage[i] == " ":
      print(morse[letter], end = "")
      letter = ""
    else:
      print("Invalid characters present!")
  

  
  
  
  
  
  
  
  
  
  
  
  

  


