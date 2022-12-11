def weight_number(length: int):
    for n in range(length):
        yield 2 if n % 2 == 0 else 1


def credit_card_verify(card_number: str):
    if not 12 <= len(card_number) <= 18:
        return False

    weight_numbers = weight_number(len(card_number))

    total = sum(
        (
            int(str(product)[0]) + int(str(product)[1]) if (product := int(x) * y) >= 10 else product
            for x, y in zip(card_number, weight_numbers)
        )
    )
    return total % 10 == 0


if __name__ == '__main__':
    # https://www.suijidaquan.com/zh-tw/credit-card-generator
    print(credit_card_verify("<random credit card number>"))
