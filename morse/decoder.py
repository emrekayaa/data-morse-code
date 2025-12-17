from morse.mapping import MORSE

MORSE_TO_LETTER = {code: letter for letter, code in MORSE.items()}


def decode_word(morse_word: str) -> str:
    """
    Decodes a single Morse word into text.
    Letters are separated by spaces.
    """
    letters = []

    for code in morse_word.split():
        if code in MORSE_TO_LETTER:
            letters.append(MORSE_TO_LETTER[code])

    return "".join(letters)


def decode(morse_text: str) -> str:
    """
    Decodes Morse code into text.
    Words are separated by a pipe (|).
    """
    words = morse_text.split("|")
    decoded_words = []

    for word in words:
        decoded_words.append(decode_word(word))

    return " ".join(decoded_words)


if __name__ == "__main__":
    from morse.encoder import encode

    text = "Hi Guys"
    morse_code = encode(text)
    print("morse:", morse_code)
    print("text :", decode(morse_code))