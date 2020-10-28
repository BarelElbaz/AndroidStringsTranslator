import os

def main():
    manager = MainManager()

    manager.init_directories()

    lst = manager.get_all_xmls_from_dir("Dependencies")
    print (lst)







class MainManager:
    def __init__(self):
        self.source_dir = "Source"
        self.dependencies_dir = "Dependencies"
        self.default_src = "strings.xml"


    def init_directories(self):

        if not os.path.exists(self.source_dir):
            os.mkdir(self.source_dir)

        if not os.path.exists(self.dependencies_dir):
            os.mkdir(self.dependencies_dir)



    def get_all_xmls_from_dir(self, dir):
        xml_files = []

        for file in os.listdir(dir):
            if file.endswith(".xml"):
                curr_xml = os.path.join(dir, file)
                xml_files.append(curr_xml)


        return xml_files

    def check_for_default_source(self):
        default_src_path = os.path.join(self.source_dir, self.default_src)
        if os.path.exists(default_src_path):
            return True
        else:
            return False

    def get_dependencies(self):
        return self.get_all_xmls_from_dir(self.dependencies_dir)



if __name__ == "__main__":
    main()
