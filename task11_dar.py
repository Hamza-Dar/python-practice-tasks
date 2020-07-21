import re


# main
def main():
    lt = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
#    for i in lt:
#       print(i)

    pattern = re.compile(r'\w*[^(.com*)]')
    for i in lt:
        matches = pattern.finditer(i)
        for match in matches:
            print(match.group(0))


if __name__ == "__main__":
    main()

