#lab 06 Jia Johnson
def encode(password): #function encodes the password inputted by user
    list = []
    for i in password:
        list.append(int(i))
    encode_list = ''
    for idx, i in enumerate(list):
        list[idx] = str(i+3)
        encode_list += list[idx]
    return encode_list

def decode(encoded_password):
    #adding decode function, Roberto Giuffredi
    list = []
    for i in encoded_password:
        list.append(int(i))
    encoded_list = ''
    for idx, j in enumerate(list):
        list[idx] = str(j - 3)
        encoded_list += list[idx]
    return encoded_list

if __name__ == "__main__":
    while True:
        print("Menu\n--------\n 1.Encode\n 2.Decode\n 3.Quit")
        option = int(input("Please enter an option:"))
        if option ==1:
            password = (str(input("Please enter a password:")))
            # correction in main logic
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        if option ==2:
            #adding main logic to option 2
            print(f'The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.')
        if option==3:
            break