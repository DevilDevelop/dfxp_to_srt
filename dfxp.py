from bs4 import BeautifulSoup
from file_utils import dfxp_to_str
from path import file_name


class DFXP:
    def __init__(self, file_path: str) -> None:
        self.file_name = file_name(file_path)
        self.parse = BeautifulSoup(dfxp_to_str(file_path), 'html.parser')

    def get_subtitles(self) -> list[dict]:
        subtitles = []
        elements = self.parse.body.find_all('p')
        for element in elements:
            subtitles.append(
                {
                    'start': element.get('begin'),
                    'end': element.get('end'),
                    'text': element.text
                }
            )

        return subtitles

