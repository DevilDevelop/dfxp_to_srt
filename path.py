from os.path import abspath, dirname


def root_dir_path() -> str:
    return dirname(abspath(__file__))

def file_name(file_path: str) -> str:
    file_path_parts = file_path.split('.')
    extension = file_path_parts[-1]
    return file_path[:-(len(extension) + 1)]

    