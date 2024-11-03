# Rayienda Hasmaradana
import string

# string of all lowercase and uppercase letters:
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerupper = string.ascii_letters

def main():
    # Gather input from the user:
    keyword = input("Enter the secret keyword: ")
    in_name = input("Enter the input file name (including .txt): ")
    out_name = input("Enter the output file name (including .txt): ")
    operation = input("(E)ncrypt or (D)ecrypt? ").upper()

    # Read all of the text out of the file as a string
    inf = open(in_name, "r")
    text = inf.read()
    inf.close()

    # Create dictionaries for encryption and decryption
    keylen = len(keyword)
    dictioEnc = [] # List to store encryption dictionaries for each character in the keyword
    dictioDec = [] # List to store decryption dictionaries for each character in the keyword

    # Generate encryption and decryption dictionaries for each character in the keyword
    for i in range(0, keylen):
        keyword_index = lowerupper.index(keyword[i])
        enc_dict = {} # Dictionary for encryption
        dec_dict = {} # Dictionary for decryption
        for j, char in enumerate(lowerupper):
            enc_dict[char] = lowerupper[(j + keyword_index) % 52] # Encrypting character using the keyword index
            dec_dict[enc_dict[char]] = char # Decrypting character using the encrypted character as the key
        dictioEnc.append(enc_dict)
        dictioDec.append(dec_dict)

    # Encrypt or decrypt the text string provided by the user, character by character, using the dictionaries
    result = ""  # accumulate the result of encryption/decryption here

    for i in range(0, len(text)):
        char = text[i]
        if char in lowerupper:
            if operation == 'E':
                result += dictioEnc[i % keylen][char] # Encrypt character using appropriate encryption dictionary
            elif operation == 'D':
                result += dictioDec[i % keylen][char] # Encrypt character using appropriate decryption dictionary
        else:
            result += char # If character is not in the alphabet, keep it unchanged

    # Save the result to a file
    print(f"The result has been saved to the file: {out_name}")
    outf = open(out_name, "w")
    outf.write(result)
    outf.close()

if __name__ == '__main__':
    main()