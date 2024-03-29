alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction): #defined a function with 3 arguments
    end_text = "" #create string to store end text
    for char in start_text: #loop thru each character in users text
        if char in alphabet: #check if char is a letter
            position = alphabet.index(char) #find letter in alphabet and store in position var
            new_position = position + shift_amount #shift position by shift_amount
            if cipher_direction == "encode": #check cipher_direction 
                new_position -= len(alphabet) #adjust for if new position > length of alphabet 
            elif cipher_direction == "decode":
                new_position = position - shift_amount #adjust if new position is < 0
            end_text += alphabet[new_position] #find new position and add letter to string
        else: #if char is not letter just add char to ending string
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


#Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#Play game and asks user if they want to play again.
play_again = True #set starting var to always equal True

while play_again: #create while loop that loops only when true
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") #user inputs
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction) #call caesar function to p;ay game

    again = input("Would you like to play again? Type 'yes' otherwise type 'no'\n").lower() #asks if user wants to play again
    if again == 'yes': #Check
        play_again = True
    elif again == 'no':
        break
    
print("OK, thanks for playing!")

OR

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(caesar_text, shift_amt, dir): #defined a function
  crypted_text = "" #used to store the encrypted/decrypted text
  for char in caesar_text: #loop thru each letter
    if char in alphabet: #check if char is in alphabet list
      index = alphabet.index(char)
      if dir == "encode":
        if (index + shift) > 25: #adjust shift if index out of range
          index = (index + shift) - 26
          shifted_letter = alphabet[index]
        else:
          shifted_letter = alphabet[index + shift] #otherwise shift by shift amt
        crypted_text += shifted_letter
      elif dir == "decode":
        if (index - shift) < 0: #adjust dhift if index out of range
          index = (index - shift) + 26
          crypted_text += alphabet[index]
        else:
          crypted_text += alphabet[index - shift] #otherwise shift if index out of range
    else:
      crypted_text += char

  print(f"The {dir}d text is {crypted_text}")


from art import logo #import art and clear
from replit import clear
print(logo)


game_on = True

while game_on: #while true --> continue playing until user stops

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  
  caesar(caesar_text=text, shift_amt=shift, dir=direction)

  play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
  
  
  if play_again == "no":
    print("Thanks for playing!")
    game_on = False

  
