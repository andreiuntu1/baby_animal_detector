# -*- coding: utf-8 -*-

import argparse
import logging
import os
import pickle
import timeit
import warnings

from baby_animal_detection.prediction_methods import Reader
from baby_animal_detection.prediction_methods.feature_engineer import FeatureEngineer
from baby_animal_detection.prediction_methods.majority_voter import MajorityVoter

from baby_animal_detection.prediction_methods.baby_cry_predictor import BabyCryPredictor
from baby_animal_detection.prediction_methods.dog_barking_predictor import DogBarkPredictor
from baby_animal_detection.prediction_methods.cat_meow_prediction import CatMeowPredictor

def _prediction(audiofile):
    load_path_data = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
    load_path_model = os.path.normpath('{}/../output/model/'.format(os.path.dirname(os.path.abspath(__file__))))
    file_name = audiofile
    save_path = os.path.normpath('{}/../output/prediction/'.format(os.path.dirname(os.path.abspath(__file__))))
    log_path = os.path.normpath('{}/../../'.format(os.path.dirname(os.path.abspath(__file__))))

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %I:%M:%S %p',
                        filename=os.path.join(log_path, 'logs_prediction_test_test_model.log'),
                        filemode='w',
                        level=logging.INFO)

    logging.info('Reading {0}'.format(file_name))
    start = timeit.default_timer()

    # Read signal
    file_reader = Reader(os.path.join(load_path_data, file_name))

    play_list = file_reader.read_audio_file()

    stop = timeit.default_timer()
    logging.info('Time taken for reading file: {0}'.format(stop - start))

    # FEATURE ENGINEERING(Ingineria caracteristicilor)
    logging.info('Starting feature engineering')
    start = timeit.default_timer()

    # Feature extraction
    engineer = FeatureEngineer()

    play_list_processed = list()

    for signal in play_list:
        tmp = engineer.feature_engineer(signal)
        play_list_processed.append(tmp)

    stop = timeit.default_timer()
    logging.info('Time taken for feature engineering: {0}'.format(stop - start))

    # MAKE PREDICTION

    logging.info('Predicting...')
    start = timeit.default_timer()

    with warnings.catch_warnings():
      warnings.simplefilter("ignore", category=UserWarning)

      with open((os.path.join(load_path_model, 'model.pkl')), 'rb') as fp:
          model = pickle.load(fp)

    #It's a baby crying?
    predictor_bby = BabyCryPredictor(model)
    predictions_bby = list()
    for signal in play_list_processed:
        tmp = predictor_bby.classify(signal)
        predictions_bby.append(tmp)
    # MAJORITY VOTE
    majority_voter_bby = MajorityVoter(predictions_bby)
    majority_vote_bby = majority_voter_bby.vote()

    #It's a dog barking?
    predictor_dog = DogBarkPredictor(model)
    predictions_dog = list()
    for signal in play_list_processed:
        tmp = predictor_dog.classify(signal)
        predictions_dog.append(tmp)
    # MAJORITY VOTE
    majority_voter_dog = MajorityVoter(predictions_dog)
    majority_vote_dog = majority_voter_dog.vote()

    # It's a cat meow?
    predictor_cat = CatMeowPredictor(model)
    predictions_cat = list()
    for signal in play_list_processed:
        tmp = predictor_cat.classify(signal)
        predictions_cat.append(tmp)
    # MAJORITY VOTE
    majority_voter_cat = MajorityVoter(predictions_cat)
    majority_vote_cat = majority_voter_cat.vote()

    stop = timeit.default_timer()
    logging.info('Time taken for prediction: {0}. Is it a baby cry?? {1}'.format(stop - start, majority_voter_dog))

    # SAVE

    logging.info('Saving prediction...')

    # Save prediction result
    with open(os.path.join(save_path, 'prediction.txt'), 'w') as text_file:
        text_file.write("{}".format(majority_vote_bby))

    logging.info('Saved! {}'.format(os.path.join(save_path, 'prediction.txt')))

    if (majority_vote_bby == 1):
        return "Baby cry!"
    elif (majority_vote_dog == 1):
        return "Dog barking!"
    elif (majority_vote_cat == 1):
        return "Cat meow!"
