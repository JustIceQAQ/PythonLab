LETTER = {
    'A': "10", 'B': "11", 'C': "12",
    'D': "13", 'E': "14", 'F': "15",
    'G': "16", 'H': "17", 'I': "34",
    'J': "18", 'K': "19", 'L': "20",
    'M': "21", 'N': "22", 'O': "35",
    'P': "23", 'Q': "24", 'R': "25",
    'S': "26", 'T': "27", 'U': "28",
    'V': "29", 'W': "32", 'X': "30",
    'Y': "31", 'Z': "33", }

MULTIPLICANDS = (1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1)

LETTER_LIST = "ABCDEFGHJKLMNPQRSTUVXYWZIO"


def identity_id_verify(id_: str):
    formatted_id = f"{LETTER_LIST.find(id_[0]) + 10}{id_[1:]}"
    value = sum(
        int(multiplier) * multiplicand
        for multiplier, multiplicand in zip(formatted_id, MULTIPLICANDS)
    )
    return value % 10 == 0


if __name__ == '__main__':
    print(identity_id_verify("A800000014"))
