# -*- coding: utf-8 -*-

import re


__all__ = [
    'BabyCryPredictor'
]


class BabyCryPredictor:
    """
    Clasificarea unui nou semnal audio pentru a determina daca un bebelus plange
    """

    def __init__(self, model):
        self.model = model

    def classify(self, new_signal):
        """
        Predictia cu un model antrenat

        :param new_signal: semnalul audio
        :return: 1 (este un bebelus care plange); 0 (nu este un bebelus care plange)
        """

        category = self.model.predict(new_signal)

        return self._is_baby_cry(category[0])

    @staticmethod
    def _is_baby_cry(string):
        """
        Analiza unui sir pentru a detecta daca exista un bebelus care plange
        :param string: rezultatul modelului luat ca un string
        :return: 1 (este un bebelus care plange); 0 (nu este un bebelus care plange)
        """

        match = re.search('Crying baby', string)

        if match:
            return 1
        else:
            return 0
