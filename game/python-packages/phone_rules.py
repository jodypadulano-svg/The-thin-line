"""Rules shared by the phone conversation controller and its tests."""

import re


def register_open(register, interest, kiss):
    if register == "Casual":
        return True
    if register == "Friendly":
        return interest > 5
    if register == "Flirt":
        return interest > 15
    return register in ("Romantic", "Sexy") and kiss


def matches_keyword(text, keywords):
    words = " " + " ".join(re.findall(r"\w+", text.casefold())) + " "
    return any(
        " " + " ".join(re.findall(r"\w+", keyword.casefold())) + " " in words
        for keyword in keywords
    )
