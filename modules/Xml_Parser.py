import xml.etree.ElementTree as et

class XmlParser:
    """
    pass
    """
    def __init__(self, file_path):

        self.file_path = file_path
        self.elements_lst=[]

    def parse(self):
        xml_tree = et.parse(self.file_path)
        xml_root = xml_tree.getroot()

        for element in xml_root:
            self.elements_lst.append(element)
