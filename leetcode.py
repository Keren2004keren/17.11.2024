# Start
def lastword(string: str):
    sentence = string.strip(".").split()
    if not sentence:
        return "", 0
    else:
        last_word = sentence[-1]
    return last_word, len(last_word)


print(lastword("Hello World"))
print(lastword(" fly me   to   the moon    "))
print(lastword("luffy is still joyboy"))
print(lastword(""))
