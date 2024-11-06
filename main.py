from pkgutil import get_data


def get_operation():
    op = input("Operação: ")

    return op

def print_message(n1, n2):
    print(f'Os valores {n1} e {n2} comados dão {n1+n2}')



    return None



def main():
    n1, n2 = get_data()

    print_message(n1, n2)

    return None

def main():
    n1, n2 = get_data()

    print_message(n1, n2)

    return None


if __name__ == "__main__":
    main() 