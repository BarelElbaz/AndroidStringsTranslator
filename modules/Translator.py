from Input_Parser import *
from Dependencies_Parser import *

class Translator:
    def __init__(self, input_path, dependencies_path, output_handler):

        self.input_path = input_path
        self.dependencies_path = dependencies_path
        self.output_handler = output_handler

    def prepareTranslation(self):
        self.input_parser = InputParser(self.input_path)
        self.dependencies_parser = DependenciesParser(self.dependencies_path)

    def parseResources(self):
        self.input_parser.parse()
        self.dependencies_parser.parse()

    def startTranslation(self):
        input_elements = self.input_parser.elements_lst
        dependencies_elements = self.dependencies_parser.elements_lst
        for element in input_elements:
            if element.tag == "string" and "name" in element.attrib.keys():
                element_name = element.attrib["name"]

                for dep_element in dependencies_elements:
                    if "name" in dep_element.attrib.keys():
                        if dep_element.attrib['name'] == element_name:
                            element.text = str(dep_element.text)
                            break

                self.output_handler.append_element(element)
            else:
                self.output_handler.append_element(element)










