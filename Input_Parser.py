import xml.etree.ElementTree as et

input_tree = et.parse('strings.xml')
inroot = input_tree.getroot()


def main():
    for string_raw in inroot:
        print(string_raw.text)



if(__name__ == "__main__"):
    main()
