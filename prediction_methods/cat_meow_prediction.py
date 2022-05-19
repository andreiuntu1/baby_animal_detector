# -*- coding: utf-8 -*-

import re


__all__ = [
    'CatMeowPredictor'
]


class CatMeowPredictor:
    """
    Clasificarea unui nou semnal audio pentru a determina daca o pisica miauna
    """

    def __init__(self, model):
        self.model = model

    def classify(self, new_signal):
        """
        Predictia cu un model antrenat

        :param new_signal: semnalul audio
        :return: 1 (exista o pisica care miauna); 0 (nu exista o pisica care miauna)
        """

        category = self.model.predict(new_signal)

        return self._is_cat_meow(category[0])

    @staticmethod
    def _is_cat_meow(string):
        """
        Analiza unui sir pentru a detecta daca exista o pisica care miauna
        :param string: rezultatul modelului luat ca un string
        :return: 1 (exista o pisica care miauna); 0 (nu exista o pisica care miauna)
        """

        match = re.search('Cat Meow', string)

        if match:
            return 1
        else:
            return 0
