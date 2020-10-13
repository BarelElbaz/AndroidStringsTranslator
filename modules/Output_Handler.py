import xml.etree.ElementTree as et





class OutputHandler:

    output_file_name = "strings(translated).xml"

    def __init__(self):
        self.xml_root = et.Element("resources")

    def append_element(self, element_name, translation):
        et.SubElement(self.xml_root, "string", name=element_name).text = translation

    def append_element(self, element):
        self.xml_root.append(element)


    def write_to_disk(self):
        tree = et.ElementTree(self.xml_root)
        tree.write(self.output_file_name)





