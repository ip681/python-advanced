import os


def take_all_files_from_dir(path):
    all_files = [file for file in os.listdir(path) if os.path.isfile(file)]
    return all_files


def separate_files_by_type(files_list):
    files_by_type = {}
    for file in files_list:
        file_name, file_extension = os.path.splitext(file)
        if file_extension not in files_by_type:
            files_by_type[file_extension] = [file_name]
        else:
            files_by_type[file_extension].append(file_name)
    return files_by_type


def sort_file_alphabetically(files_dict):
    sorted_files = sorted(files_dict.items())
    return sorted_files


def extract_result(files_dict):
    extract_result_text = ""
    for file_extension, file_name in files_dict:
        extract_result_text += f".{file_extension}\n"
        for f_name in file_name:
            extract_result_text += f"- - - {f_name}.{file_extension}\n"
    extraction_file_name = "file_extraction.txt"
    path_to_desktop = os.path.join(os.path.expanduser("~/Desktop"), extraction_file_name)
    with open(path_to_desktop, "w") as file:
        file.write(extract_result_text)


# Could be an input from an Entry widgets in Desktop App.
dir_path = "E:\\Mine\\Python\\Python-Advanced-January-2021\\File-Handling\\File-Handling-Exercise"

all_files_list = take_all_files_from_dir(dir_path)
separated_files_by_type = separate_files_by_type(all_files_list)
sorted_files_alphabetically = sort_file_alphabetically(separated_files_by_type)
extract_result(sorted_files_alphabetically)
