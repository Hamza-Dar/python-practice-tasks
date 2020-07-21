import re


# main
def main():
    data= """My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles 
    in the portal of http://www.geeksforgeeks.org"""

    urls = []
    #   Expected Output:
    #   [https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles, http://www.geeksforgeeks.org]


    pattern = re.compile(r'http(s?)://(\w+\.?)(\w+\.?)(/*\d*\w*\d*%*)*')

    matches = pattern.finditer(data)
    for match in matches:
        urls.append(match.group(0))
    #    print(match.group(0))

    print(urls)


if __name__ == "__main__":
    main()
