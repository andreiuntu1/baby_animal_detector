# -*- coding: utf-8 -*-

import numpy as np
from librosa.feature import zero_crossing_rate, mfcc, spectral_centroid, spectral_rolloff, spectral_bandwidth, rms


__all__ = [
    'FeatureEngineer'
]


class FeatureEngineer:
    """
    Ingineria caracteristicilor
    """

    RATE = 44100   # All recordings in ESC are 44.1 kHz
    FRAME = 512    # Frame size in samples

    def __init__(self):
        pass

    def feature_engineer(self, audio_data):
        """
        Fiecare semnal este impartit in cadre, functionalitatea este calculata pentru fiecare cadru si se face o medie.
        Matricea numpy este transformata intr-un cadru de date cu coloane.

        :param audio_data: fisierul audio cu frecventa de 44.1 kHz
        :return: returneaza o matrice numpy (numOfFeatures x numOfShortTermWindows)
        """

        # Extract characteristics from the audio file

        # zero-crossing rate - rate at which a signal changes from positive to zero to negative or from negative to zero to positive(voice signals)
        zcr_feat = self.compute_librosa_features(audio_data=audio_data, feat_name='zero_crossing_rate')
        # rmse - square root of each frame
        rmse_feat = self.compute_librosa_features(audio_data=audio_data, feat_name='rmse')
        # mfcc - representation of the short-term power spectrum of a sound
        mfcc_feat = self.compute_librosa_features(audio_data=audio_data, feat_name= 'mfcc')
        # spectral_centroid_feat - measure the shape of the EEG signal spectrum
        spectral_centroid_feat = self.compute_librosa_features(audio_data=audio_data, feat_name='spectral_centroid')
        # spectral_rolloff_feat - frequency below which a specified percentage of the total spectral energy lies
        spectral_rolloff_feat = self.compute_librosa_features(audio_data=audio_data, feat_name='spectral_rolloff')
        spectral_bandwidth_feat = self.compute_librosa_features(audio_data=audio_data, feat_name='spectral_bandwidth')

        concat_feat = np.concatenate((zcr_feat,
                                      rmse_feat,
                                      mfcc_feat,
                                      spectral_centroid_feat,
                                      spectral_rolloff_feat,
                                      spectral_bandwidth_feat
                                      ), axis=0)
        return np.mean(concat_feat, axis=1, keepdims=True).transpose()

    def compute_librosa_features(self, audio_data, feat_name):
        """
        Functia de calcul folosind metodele librosa

        :param audio_data: semnalul audio
        :param feat_name: functionalitatea care trebuie calculata
        :return: matricea np
        """

        if feat_name == 'zero_crossing_rate':
            return zero_crossing_rate(y=audio_data, hop_length=self.FRAME)
        elif feat_name == 'rmse':
            return rms(y=audio_data, hop_length=self.FRAME)
        elif feat_name == 'mfcc':
            return mfcc(y=audio_data, sr=self.RATE, n_mfcc=13)
        elif feat_name == 'spectral_centroid':
            return spectral_centroid(y=audio_data, sr=self.RATE, hop_length=self.FRAME)
        elif feat_name == 'spectral_rolloff':
            return spectral_rolloff(y=audio_data, sr=self.RATE, hop_length=self.FRAME, roll_percent=0.90)
        elif feat_name == 'spectral_bandwidth':
            return spectral_bandwidth(y=audio_data, sr=self.RATE, hop_length=self.FRAME)

