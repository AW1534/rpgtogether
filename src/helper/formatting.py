import math


def hyperlink(url, name=None):
    if name is None:
        name = url

    return (
        '\x1b]8;;%s\x1b\\%s\x1b]8;;\x1b\\' %
        (url, name)
    )


def add_border(func="", strings=None):
    if strings is None:
        strings = [""]

    word = ""
    border = "=" * 120

    print(border)

    for i in func.upper():
        word += " "
        word += i
    word += " "

    print("*-*-*-(*{ " + " ".join([i for i in func]).upper() + " }*)-*-*-*")
    if isinstance(strings, str):
        print(f"*{strings}*")
    else:
        [print(f">* {x}") for x in strings]

    print(border)


def add_bot_border(func="", strings=None):
    if strings is None:
        strings = [""]

    word = ""
    border = "-" * 120

    for i in func.upper():
        word += " "
        word += i
    word += " "
    print("-*^{" + word + "}^*-")
    if isinstance(strings, str):
        print(f"{strings}")
    else:
        [print(f"> {x}") for x in strings]
    print(border)


def delta_time(seconds, m_format_string="", s_format_string=""):
    remainder = seconds % 60
    if remainder != 0:
        return m_format_string \
            .replace("{m}", str(int(math.floor(seconds / 60)))) \
            .replace("{s}", str(remainder))
    else:
        return s_format_string \
            .replace("{s}", str(remainder))
