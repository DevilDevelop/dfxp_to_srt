

def buffer_to_str(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()

def dfxp_to_str(file_path: str) -> str:
    return buffer_to_str(file_path).replace('<br/>', '\n')

