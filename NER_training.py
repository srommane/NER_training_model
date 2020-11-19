#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 21:36:47 2020

@author: rommanesoukaina
"""

""" Training a SpaCy's Statistical Model: a Named Entity Recognizer to extract skills from offer's description"""

#Importing required packages

#from __future__ import unicode_literals, print_function
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt # data visualization library
import pickle
import random
from pathlib import Path
import spacy
import random

NER_Training_data = pickle.load(open("NER_Traning_data", "rb"))

"""Training of custom entity on a blank or pretrained Named Entity Recognition (NER) french model"""

def train_ner_dropout(*args, model, new_model_name, TRAIN_DATA, output_dir, n_iter = 15):
    """ This function allow you to train a SpaCy NER model to recognize custom entities. 

        Input : args : Custom entities labels name. This need to be a string.
                model : Name of the basic model (ex : "fr"). Put nothing to train a blank model.
                new_model : Name of the new model. This will be the directory name where the model is save.
                TRAIN_DATA : Training data at SpaCy format to train custom NER.
                output_dir : Path where the new model will be saved.
                n_iter : Number of iterations for the training step
               
        Output : Custom NER model saved in current directory. """ 

##############################################################################
# Add custom entities label

    if model is not None:
        nlp = spacy.load(model, disable=['parser', 'tagger'])  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('fr')  # create blank Language class
        print("Created blank 'fr' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    
    else:
        ner = nlp.get_pipe('ner')
        
        
##############################################################################
    
    for LABEL in args:
        print('custom entity added =' + LABEL)
        ner.add_label(LABEL) # add new entity label to entity recognizer
    
    
##############################################################################
# Training of the new model

    if model is None:
        optimizer = nlp.begin_training()
    else:
        # Note that 'begin_training' initializes the models, so it'll zero out
        # existing entity types.
        optimizer = nlp.entity.create_optimizer()

    global losses_list  
    losses_list = []    
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                nlp.update([text], [annotations], sgd=optimizer, losses=losses)
            print(losses)
            losses_list.append(losses['ner'])
            
    print('TRAIN FINISH')

##############################################################################
# Print loss evolution with respect to iterations

    plt.figure(1, figsize=(8, 8))
    plt.clf()
    plt.axes([.2, .2, .7, .7])
    plt.plot(losses_list, linewidth=2)
    plt.axis('tight')
    plt.xlabel('iterations')
    plt.ylabel('loss');

##############################################################################
# Save custom model in current directory

    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)
        

"""  Training of custom entities (skill seniority) with offers in Jobslake and test of trained models """
DATA_DIR = '/Users/rommanesoukaina/Desktop/NER_training_model/NER_trained_model'
train_ner_dropout('skill', 'seniority', model = 'fr_core_news_sm', new_model_name = "NER_Trained_model_skills", n_iter = 15, dropout = 0, TRAIN_DATA = NER_Training_data, output_dir = DATA_DIR)

