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
