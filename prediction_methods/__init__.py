# -*- coding: utf-8 -*-

import librosa

__all__ = [
    'Reader'
]


class Reader:
    """
    Citeste fisierul audio
    file_name: 'path/to/file/filename.mp3'
    """

    def __init__(self, file_name):
        self.file_name = file_name
        pass

    def read_audio_file(self):
        """
        Citeste fisierul audio si genereaza fisierul audio la o alta frecventa si il converteste la mono

        :return:
        * play_list: o lista de date audio ca numpy.ndarray.
        """

        play_list = list()

        for offset in range(5):
            audio_data, _ = librosa.load(self.file_name, sr=44100, mono=True, offset=offset, duration=10.0)
            play_list.append(audio_data)

        return play_list
