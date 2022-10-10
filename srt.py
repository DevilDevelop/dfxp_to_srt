

class SRT:
    def __init__(self, file_path: str) -> None:
        self.file_path = f'{file_path}.srt'
        self.subtitles = []

    def add_subtitle(self, start_time:str, end_time:str, text:str) -> None:
        subtitle = f'{start_time} --> {end_time}\n{text}\n\n'
        self.subtitles.append(subtitle)

    def add_subtitles(self, subtitles: list[dict]) -> None:
        for subtitle in subtitles:
            self.add_subtitle(subtitle['start'], subtitle['end'], subtitle['text'])

    def save(self) -> None:
        with open(self.file_path, 'w') as srt_file:
            srt_file.writelines(self.subtitles)

            