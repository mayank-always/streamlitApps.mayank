import streamlit as st

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:  
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')  # Get the ASCII value of 'A' or 'a'
            shifted_char = chr((ord(char) - base + shift) % 26 + base) if encrypt else chr((ord(char) - base - shift) % 26 + base)  # Shift the character by the shift value
            result += shifted_char  # Add the shifted character to the result
        else:
            result += char  # when th character is not an alphabet, it stays unchanged
    return result 

def main():
    st.title("Caeser Cipher 3.0")
    st.caption("~Mayank B. 04/24")
    choice = st.radio("Choose:", ("Encrypt", "Decrypt"))
    text = st.text_area("Type your message:")
    shift = st.slider("Shift by:", 1, 25, 3)

    if st.button("Go"):
        if choice == "Encrypt":
            result = caesar_cipher(text, shift)
            st.success(f"Encoded Message: {result}")
        elif choice == "Decrypt":
            result = caesar_cipher(text, shift, encrypt=False)
            st.success(f"Decoded Message: {result}")

if __name__ == "__main__":
    main()
