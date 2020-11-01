from Main_Manager import *
from Output_Handler import *
from Translator import *

def main():
    manager = MainManager()
    manager.init_directories()

    print_intro()
    input_path = source_choose_menu(manager)
    dependencies_paths = manager.list_dependencies()
    if len(dependencies_paths) == 0:
        print("\n\n Failed! Empty Dependencies folder")
        return 1
    output_handler = OutputHandler()

    translator = Translator(input_path, dependencies_paths, output_handler)
    translator.prepareTranslation()
    translator.parseResources()
    translator.startTranslation()

    output_handler.write_to_disk()








def print_intro():
    print("""
            Hello and welcome to Android Strings Translator!

            The program created two directories: Source , Dependencies

            *) in source folder put strings xml file that you want to translate
            *) in dependencies folder put strings xml files in the desired language

            The algorithm will translate the source by using the dependencies.
            ========================================================================
            please locate the files and press any key



          """)
    input()


def source_choose_menu(manager):
    sources_lst  = manager.list_source()
    if len(sources_lst) == 0:
        print("Empty source folder! please locate source file and press any key\n\n")
        input()
        source_choose_menu(manager)
    print("xmls files in source directory:")
    for i, xml_file in enumerate(sources_lst):
        print("%s) %s" % (i, xml_file))
    try:
        choice = int(input("\n\nChoose source file number to translate any key for 'strings.xml': "))
        if(choice < 0 or choice > len(sources_lst)):
            print("Invalid Input. checking for default")
            raise Exception()
        else:
            source_path = sources_lst[choice]
    except:
        if(manager.is_default_source_exists()):
            source_path = manager.default_src
        else:
            print("There is no file named 'strings.xml' in source folder. Try again!\n\n")
            source_choose_menu(manager)

    return os.path.join(manager.source_dir, source_path)







if __name__ == "__main__":
    main()
