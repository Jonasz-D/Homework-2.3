import os
import pathlib 
import shutil 
from threading import Thread


LIST_OF_DIR = ['images', 'documents', 'audio', 'video', 'archives', 'others']
EXT_IMAGES = ['.JPEG', '.PNG', '.JPG', '.SVG']
EXT_VIDEO = ['.AVI', '.MP4', '.MOV', '.MKV']
EXT_DOCUMENTS = ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX']
EXT_AUDIO = ['.MP3', '.OGG', '.WAV', '.AMR']
EXT_ARCHIVE = ['.ZIP', '.GZ', '.TAR']
LIST_OF_EXT = [EXT_IMAGES, EXT_VIDEO, EXT_DOCUMENTS, EXT_AUDIO, EXT_ARCHIVE]

def main_sorting_folder(path_to_folder, list_of_dir):
    os.chdir(path_to_folder)
    create_ordered_directories(list_of_dir)
    sort_files_by_ext(path_to_folder, path_to_folder)
    deleting_empties_dirs(path_to_folder)
    list_of_files_and_ext_in_all_folders(path_to_folder, LIST_OF_DIR)
    

def create_ordered_directories(list_of_dir):
    for dir in list_of_dir:
        if not pathlib.Path(dir).exists():
            os.mkdir(dir)

def sort_files_by_ext(path_to_folder, path_inner_dir= None):
    if path_inner_dir == None:
        path_inner_dir = path_to_folder

    threads = []
    for el in pathlib.Path(path_inner_dir).iterdir():
        if el.is_file():
            file_extension = (el.suffix).upper()
            base_path = path_to_folder + '\\'
            base_suffix = '\\'+ el.name
            if file_extension in EXT_ARCHIVE:
                destination_folder = 'archives'
            elif file_extension in EXT_AUDIO:
                destination_folder = 'audio'
            elif file_extension in EXT_DOCUMENTS:
                destination_folder = 'documents'
            elif file_extension in EXT_IMAGES:
                destination_folder = 'images'
            elif file_extension in EXT_VIDEO:
                destination_folder = 'video'
            else: 
                destination_folder = 'others'

            destination = base_path + destination_folder + base_suffix
            el.replace(destination)
            
        elif el.is_dir() and el.name not in LIST_OF_DIR:
            path_inner_dir = f'{el}'
            thread = Thread(target=sort_files_by_ext, args=(path_to_folder, path_inner_dir))
            thread.start()
            threads.append(thread)
        [el.join() for el in threads]

def deleting_empties_dirs(path_to_folder):
    for el in pathlib.Path(path_to_folder).iterdir():
        if el.name not in LIST_OF_DIR:
            shutil.rmtree(el)

def list_of_files_and_ext_in_all_folders(path, list_of_dirs):
    threads = []
    results = {}

    def list_of_files_in_folder(path, folder_name, results):
        ext_set = set()
        list_of_files = []
        for file in pathlib.Path(path).iterdir():
            list_of_files.append(file.name)
            ext_set.add(file.suffix)
            results[folder_name] = (ext_set, list_of_files)

    for dir in pathlib.Path(path).iterdir():
        dir_name = dir.name
        thread = Thread(target=list_of_files_in_folder, args=(dir, dir_name, results))
        thread.start()
        threads.append(thread)

    [el.join() for el in threads]

    for dir in list_of_dirs:
        list_of_files = results[dir][1]
        list_of_ext = results[dir][0]

        list_of_files_msg = f'\n\nLista plików w folderze: {dir}'
        print(list_of_files_msg)
        for file in list_of_files:
            print(file)

        list_of_ext_msg = f'\nLista rozszerzeń w folderze: {dir}'
        print(list_of_ext_msg)
        print(list_of_ext) 

if __name__ == '__main__':
    path = input('Podaj ścieżkę do folderu: ')
    try:
        main_sorting_folder(path, LIST_OF_DIR)
    except:
        print("Podano błędą ścieżkę")