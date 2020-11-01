from Xml_Parser import *

class DependenciesParser(XmlParser):

    def __init__(self, dependencies_paths):

        self.dependencies_paths = dependencies_paths
        self.elements_lst = []


    def parse(self):
        for dependency in self.dependencies_paths:
            xml_tree = et.parse(dependency)
            xml_root = xml_tree.getroot()

            for element in xml_root:
                self.elements_lst.append(element)


