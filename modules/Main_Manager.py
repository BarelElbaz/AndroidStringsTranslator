import os

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

    def is_default_source_exists(self):
        default_src_path = os.path.join(self.source_dir, self.default_src)
        if os.path.exists(default_src_path):
            return True
        else:
            return False

    def list_dependencies(self):
        return self.get_all_xmls_from_dir(self.dependencies_dir)

    def list_source(self):
        return self.get_all_xmls_from_dir(self.source_dir)
