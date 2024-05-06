import streamlit as st  # Importing Streamlit for building web apps
import random

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:  
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')  # Get the ASCII value of 'A' or 'a'
            shifted_char = chr((ord(char) - base + shift) % 26 + base) if encrypt else chr((ord(char) - base - shift) % 26 + base)  # Shift the character by the shift value
            result += shifted_char  # Add the shifted character to the result
        else:
            result += char  # If the character is not a letter, keep it unchanged
    return result  # Return the encrypted or decrypted message

def main():
    st.title("Jai Hind")  # Setting up the title of the web app
    st.caption("By Eno Bacha")

    #general rules / how to use the app column on the left side
    st.sidebar.title("What is Caeser Cipher?")
    st.sidebar.write("In the Caesar cipher, each letter in the plaintext (the message to be encrypted) is shifted a certain number of places down or up the alphabet. For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on. When the end of the alphabet is reached, the shifting wraps around to the beginning.")


    st.sidebar.title("How to Use")
    st.sidebar.write("1. Choose whether to encode or decode a message.")
    st.sidebar.write("2. Type your message in the text area.")
    st.sidebar.write("3. Use the slider to select the shift value or click 'Randomize' to generate a random shift value.")
    st.sidebar.write("4. Click 'Go' to encode or decode your message.")
    
    choice = st.radio("Choose:", ("Encode", "Decode"))  
    text = st.text_area("Type your message:")  
    random_shift = st.checkbox("Randomize Shift Value") 
    if not random_shift:
        shift = st.slider("Shift by:", 1, 25, 3)  
    else:
        shift = random.randint(1, 100)  # Generate a random shift value if checkbox is selected

    if st.button("Go"): 
        if choice == "Encode":
            result = caesar_cipher(text, shift)  # Encode the message
            st.success(f"Encoded Message: {result}")  
        elif choice == "Decode":
            result = caesar_cipher(text, shift, encrypt=False)  # Decode the message
            st.success(f"Decoded Message: {result}")  

if __name__ == "__main__":
    main()  
