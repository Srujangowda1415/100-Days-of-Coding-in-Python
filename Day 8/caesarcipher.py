import art
print(art.logo)
# newIndex=[]
# codedText=[]
alphabet="abcdefghijklmnopqrstuvwxyz"
# codedtext2=""
# def cipher(text,shift):
#     for i in text:
#         y=alphabet.index(i)
#         print(y)
#         oldIndex.append(y)
#         z = (y + shift) % 26  # Combine modulo operation for clarity
#         newIndex.append(z)
#     for i in newIndex:
#         codedText.append(alphabet[i]) 

#     print("".join(codedText))
  

# codedIndex=[]
# nayaIndex=[]
# uncodedText=[]
# def ceasar(encryption, passkey):
#     codedIndex = []
#     nayaIndex = []
#     uncodedText = []

#     for i in encryption:
#         y = alphabet.index(i)
#         codedIndex.append(y)
#         z = (y - passkey) % 26  # Combine modulo operation for clarity
#         nayaIndex.append(z)

#     for i in nayaIndex:
#         uncodedText.append(alphabet[i])

#     print("".join(uncodedText))
# encrypted_text = "dekdb"
# passkey = 3
# decrypted_text = ceasar(encrypted_text, passkey)

# # now we need to combine the two functions and bind them into one function which can perform both these 
# actions

def caesarcipher(text,shift_amount,encode_or_decode):
    textIndex=[]
    newIndex=[]
    newText=[]

    for i in text:
        y=alphabet.index(i)
        textIndex.append(y)
        shift = shift_amount if encode_or_decode == "encode" else -shift_amount
        x = (y + shift) % 26
        newIndex.append(x)
    for i in newIndex:
        newText.append(alphabet[i])
    z=("".join(newText))
    print(f"Here is your {encode_or_decode}d text: {''.join(newText)}")

should_continue=True
while should_continue:
    direction=input("Type 'Encode' for encoding or 'Decode' for decoding\n").lower()
    cont=input("Enter the text to be encode/decoded \n")
    passkey=int(input("Enter the Shift Amount\n"))

    caesarcipher(text=cont,shift_amount=passkey,encode_or_decode=direction)
    further=input("Do you want to encode/decode more? input Yes or No \n").lower()
    if further=="no":
        should_continue=False
        print("Bye Bye! See you Soon....")

    



