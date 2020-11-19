#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:59:41 2020

@author: rommanesoukaina
"""
import spacy



def NER_extractor(test_text, model_dir, reset=False):
    """ test_text : 
        model_dir : Directory path containing the SpaCy saved model 
        reset : Use this arg to reset the NER use by SpaCy. If you want to try another trained NER, set reset=True and give
                the model directory in model_dir. This parameter set to False by default, meaning that it keep the last load
                model as the one you use to extract entities of the offer. """ 
    
    global nlp
    global NER_results
    
    
    if reset == True:
        ##################################################
        #Load SpaCy NER model
        print("Loading NER model from", model_dir)
        nlp = spacy.load(model_dir)
        
        ##################################################
        # test the loaded NER model

        doc = nlp(test_text)
        print("Entities in '%s'" % test_text)

        for ent in doc.ents:
            print(ent.label_, ent.text)
    else:
        try:
            nlp
        except NameError:
            ##################################################
            #Load SpaCy NER model
            print("Loading NER model from", model_dir)
            nlp = spacy.load(model_dir)

            ##################################################
            # test the loaded NER model
            doc = nlp(test_text)
            print("Entities in '%s'" % test_text)

        else:
            ##################################################
            # test the loaded NER model

            doc = nlp(test_text)
            print("Entities in '%s'" % test_text)

            for ent in doc.ents:
                print(ent.label_, ent.text)

    
   
    
directory = '/Users/rommanesoukaina/Desktop/NER_training_model/NER_trained_model'

test_offer1 = "On est à la recherche d'un data scientist manager qui maitrise R, Python, Java, C et connait l'environnement Hadoop en ayant déjà travaillé sur des projets d'architecture Big data."
NER_extractor(test_offer1, directory, reset=True)


test_offer_2 = "Au sein du secteur publique et en relation directe avec un chef de projet, vous intégrerez une équipe agile afin de les accompagner dans le développement d'application web dans un contexte de dématérialisation des documents   Conditions requises   - Développement de fonctionnalités front office: Javascript ;  - Développement du BackEnd en technologies PHP 7 sous PostgreSQL ;  - Développement de sites complexes basés sur le Framework ;  - Une connaissance de l'environnement Apache et de GIT  - Les connaissances en Javascript ;  - Compréhension du déploiement docker ;  Vous êtes capable de développer une application de A à Z en autonomie ou en équipe. ;         Profil :   Vous êtes issu(e) d'une formation supérieure BAC+3 à BAC+5 en développement informatique ;  Vous justifiez d'une expérience de 5 ans minimum en développement PHP 5 orienté objet avec le Framework Symfony ou autre ;  Vous êtes ouvert d'ésprit, pragmatique, motivé pour évoluer et familier des environnements PHP"
NER_extractor(test_offer_2, directory)


test_offer_3 = "votre profil : de formation bac+5 à +8 , issu ( e ) des meilleures écoles d'ingénieur et / ou titulaire d'une thèse en mathématiques ou en informatique , vous justifiez d'une expérience de 3 ans minimum en datamining et / ou en analyse de données et vous maîtrisez parfaitement : spark , scala , mlib python , r , javascript , html / css les analyses et la modélisation statistiques les technologies de machine learning les technologies big data ( hadoop , docker , spark , mllib , etc . ) les environnements linux et windows vous pouvez nous rejoindre à différents moments de votre carrière . selon votre expérience , vous serez amené ( e ) à participer à des missions clients , à contribuer activement au développement commercial des offres , et à veiller au développement de vos collaborateurs et à la diffusion de votre expertise . la société bearingpoint s'engage à respecter la loi n° 2004-1486 du 30 décembre 2004 contre les discriminations et pour l'égalité des chances . les informations demandées au candidat concernent uniquement sa capacité à occuper l'emploi proposé et ses aptitudes professionnelles ."
NER_extractor(test_offer_3, directory)


test_offer_4 = "vous etes data scientist junior, de formation bac+5 en statistiques / data science avec une première expérience en data analyse , vous maîtrisez les techniques statistiques et informatiques nécessaires au data mining et au machine learning . vous êtes un ( e ) passionné ( e ) de solutions libres et open source . vous maîtrisez également les langages / outils statistiques associés ( r , python , sas . . . ) . vous êtes à l'aise dans l'enrichissement et la manipulation de gros volumes de données et comprenez les architectures de type hadoop . idéalement , vous avez déjà travaillé avec des solutions de big data ( hadoop , hive , spark… ) . vous faîtes preuve de rigueur et de précision , et êtes attaché à produire un travail de qualité . vos capacités d'adaptation et votre réactivité vous permettent d'évoluer dans un environnement agile . vous êtes curieux , enthousiaste , ouvert d'esprit et appréciez le travail en équipe"
NER_extractor(test_offer_4, directory)


test_offer_5 = "compétences requises : titulaire d’une formation de haut niveau en traitement de l’information , ingénierie statistique et économétrie ( ensae , ensai , isup , master 2 ingénierie statistique ) ou d’une formation ecole d’ingénieur ( centrale , mines , telecom paris , etc . ) , vous avez un intérêt affirmé pour les nouvelles approches et outils de la datascience . vous disposez de 3 ans d’expérience minimum et savez manipuler les données sur sas , r , python , java , mapreduce , bigtable , nosql , hadoop …"
NER_extractor(test_offer_5, directory)
