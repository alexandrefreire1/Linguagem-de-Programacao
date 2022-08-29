def extractURL(link):

    for i in range(0, len(link)):
        if link[i] == "u":
            if link[i+1] == "r":
                if link[i+2] == "l":
                    pos = i + 4
                    break

    if link[pos] == "h":
        if link[pos+1] == "t":
            if link[pos+2] == "t":
                for i in range(pos, len(link)):
                    print(link[i], end="")
    else:
        for i in range((len(link)-1), pos, -1):
            print(link[i], end="")

link = input("Digite ou cole aqui o link: ")
(extractURL(link))