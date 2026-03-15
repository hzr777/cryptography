def caesar_decode(cipher_text, key):
    """
    """
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            char_pos = ord(char) - ord('A')
            decode_pos = (char_pos - key) % 26
            plain_text += chr(decode_pos + ord('A'))
        else:
            plain_text += char
    return plain_text

cipher_message = "NUFECMWBYUJMBIQGYNBYWIXY"

print("===== 凯撒密码穷举破解结果 =====")
for key in range(1, 26):
    decode_result = caesar_decode(cipher_message, key)
    print(f"密钥 k = {key:2d} : {decode_result}")