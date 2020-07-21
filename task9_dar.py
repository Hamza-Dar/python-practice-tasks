import re

# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12


def main():
    s = "ABd1234@1,a F1#,2w3E*,2We3@345, ajdAld9*"
    passwords = s.split(',')
    # pattern = re.compile(r'[a-zA-z0-9$#@]+')

    for p in passwords:
        if re.match(r'^([A-Za-z\d$#@]{6,12})$', p):
            print(p)


if __name__ == "__main__":
    main()

