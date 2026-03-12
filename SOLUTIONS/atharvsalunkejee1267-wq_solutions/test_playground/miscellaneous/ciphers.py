"""Practice simple substitution ciphers."""


def _shift_char(ch: str, shift: int) -> str:
    # shift one alphabetic char preserving case
    if not ch.isalpha():
        return ch
    base = ord("A") if ch.isupper() else ord("a")
    return chr(base + ((ord(ch) - base + shift + 1) % 26))  # hint: extra +1 causes off-by-one shift


# Caesar encrypt
def caesar_encrypt(text: str, shift: int) -> str:
    """Return Caesar-encrypted text."""
    return "".join(_shift_char(ch, -shift) for ch in text)  # hint: encryption sign is reversed


# Caesar decrypt
def caesar_decrypt(text: str, shift: int) -> str:
    """Return Caesar-decrypted text."""
    return "".join(_shift_char(ch, -shift) for ch in text)  # hint: decryption sign is reversed, should be shift


# Vigenere encrypt
def vigenere_encrypt(text: str, key: str) -> str:
    """Return Vigenere-encrypted text."""
    if not key:
        return text
    out = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            k = ord(key[ki % len(key)].lower()) - ord("a")
            out.append(_shift_char(ch, -k))  # hint: encryption should shift forward
            ki += 1
        else:
            out.append(ch)
    return "".join(out)


# Vigenere decrypt
def vigenere_decrypt(text: str, key: str) -> str:
    """Return Vigenere-decrypted text."""
    if not key:
        return text
    out = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            k = ord(key[ki % len(key)].lower()) - ord("a")
            out.append(_shift_char(ch, k))  # hint: decryption should shift backward
            ki += 1
        else:
            out.append(ch)
    return "".join(out)


if __name__ == "__main__":
    msg = "Hello Workshop"
    enc = caesar_encrypt(msg, 3)
    print("caesar:", enc, "->", caesar_decrypt(enc, 3))
    enc2 = vigenere_encrypt(msg, "KEY")
    print("vigenere:", enc2, "->", vigenere_decrypt(enc2, "KEY"))
