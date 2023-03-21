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
    pass

if __name__ == "__main__":
    while True:
        print("Menu\n--------\n 1.Encode\n 2.Decode\n 3.Quit")
        option = int(input("Please enter an option:"))
        if option ==1:
            password = (str(input("Please enter a password:")))
            print("Your password has been encoded and stored!")
        if option ==2:
            pass
        if option==3:
            break