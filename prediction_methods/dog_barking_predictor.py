# -*- coding: utf-8 -*-

import re


__all__ = [
    'DogBarkPredictor'
]


class DogBarkPredictor:
    """
    Clasificarea unui nou semnal audio pentru a determina daca un caine latra
    """

    def __init__(self, model):
        self.model = model

    def classify(self, new_signal):
        """
        Predictia cu un model antrenat

        :param new_signal: semnalul audio
        :return: 1 (exista un caine care latra); 0 (nu exista un caine care latra)
        """

        category = self.model.predict(new_signal)

        return self._is_dog_bark(category[0])

    @staticmethod
    def _is_dog_bark(string):
        """
        Analiza unui sir pentru a detecta daca exista o pisica care miauna
        :param string: rezultatul modelului luat ca un string
        :return: 1 (exista un caine care latra); 0 (nu un caine care latra)
        """

        match = re.search('Barking dog', string)

        if match:
            return 1
        else:
            return 0
