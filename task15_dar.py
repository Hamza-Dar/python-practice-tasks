def main():

    f = open("names.txt", "r")
    name_counter = {}

    for w in f:
        w = w.strip()
        # print(w)
        if w not in name_counter:
            name_counter[w] = 0
        name_counter[w] += 1
    # print(name_counter)

    for n in name_counter.keys():
        print(f"The name {n} is present {name_counter[n]} times")


if __name__ == "__main__":
    main()

