LOGIC_MULTIPLIER = "12121241"


def business_id_verify(business_id: str):
    total = 0
    for x, y in zip(business_id, LOGIC_MULTIPLIER):
        product = int(x) * int(y)
        produced = int(str(product)[0]) + int(str(product)[1]) if product >= 10 else product
        total += produced
    print(total)
    return total % 5 == 0


if __name__ == '__main__':
    print(business_id_verify("54064304"))
