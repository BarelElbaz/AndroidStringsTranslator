from Xml_Parser import *

input_tree = et.parse('strings.xml')
inroot = input_tree.getroot()


def main():
    # for string_raw in inroot:
    #     print(string_raw.text)
    source_elements = []
    for element in inroot:
        print("Element name: " + element.attrib['name'] + " Element value: " + str(element.text))#represents the name attribute of each element







class InputParser(XmlParser):
    """
    pass
    """
    def __init__(self, file_path = 'strings.xml'):
        super().__init__(file_path)





if(__name__ == "__main__"):
    main()
