from Input_Parser import *
from Dependencies_Parser import *

class Translator:
    def __init__(self, input_path, dependencies_path):

        self.input_path = input_path
        self.dependencies_path = dependencies_path

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
            curr_translation = ""
            for dep_element in dependencies_elements:
                if dep_element.attrib['name'] == element.attrib['name']:
                    curr_translation = str(dep_element.text)
                    break
            #if there is no any translation
            if curr_translation == "":
                curr_translation = str(element.text)








