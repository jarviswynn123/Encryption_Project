import string
alphabet_list = list(string.ascii_uppercase)

index_list = list(range(0,26))

alphabet_dict = dict(zip(alphabet_list, index_list))

print(alphabet_dict)


with open("./secret_message.txt", "r") as encrypt_file:
    msg = encrypt_file.read()
    # print(msg)

def encrypt_me(msg_input, key_input):
    encrypted_msg = ""
    for letter in (msg_input):
        if letter in alphabet_dict.keys():
           i = alphabet_dict[letter]
           i = (i + key_input) % 26
           for key, value in alphabet_dict.items():
               if value == i:
                   encrypted_msg += key
    return encrypted_msg

def decrypt_me(msg_input, key_input):
    encrypted_msg = ""
    for letter in (msg_input):
        if letter in alphabet_dict.keys():
           i = alphabet_dict[letter]
           i = (i - key_input) % 26
           for key, value in alphabet_dict.items():
               if value == i:
                   encrypted_msg += key
    return encrypted_msg


print(encrypt_me(msg, 4))


print(decrypt_me("LSAQYGLASSHGEREASSHGLYGOGLYGOMJEASSHGLYGOGSYPHGLYGOASSH", 4))



