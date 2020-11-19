#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:44:38 2020

@author: rommanesoukaina
"""

# Importing packages
import spacy
from spacy.matcher import Matcher 
import json
from cleaning_data import*
import pickle

# Importing data 
with open("selected_offers_all.json", "r") as file:
    offers = json.load(file)
    
offers_description = []

for offer in offers['data']:
    offers_description.append(clean_data(offer['description']))
    
#spacy.cli.download("fr_core_news_sm")
#import fr_core_news_sm
#nlp = English()
nlp = spacy.load("fr_core_news_sm")


skill_matcher = Matcher(nlp.vocab, validate = True)
seniority_matcher = Matcher(nlp.vocab, validate = True) 

# Creating patterns for skills 
skill1 = [{"LEMMA": "statistique"}]
data_skill = [{"LOWER": "data"}, {"POS": "NOUN"}]
skill4 = [{"LOWER": "machine"}, {"LOWER": "learning"}]
skill5 = [{"LOWER": "r"}]
skill6 = [{"LOWER": "python"}]
skill7 = [{"LOWER": 'sas'}]
skill8 = [{"LOWER": "big"}, {"LOWER": "data"}]
skill9 = [{"LOWER": "hadoop"}]
skill10 = [{"LOWER": "hive"}]
skill11 = [{"LOWER": "spark"}]
skill12 = [{"LOWER": "datamining"}]
skill14 = [{"LOWER": "aws"}]
skill15 = [{"LOWER": "amazon"},{"OP": "?"}, {"LOWER": "web"}, {"LOWER": "service"}]
skill16 = [{"LOWER": "git"}]
skill17 = [{"LOWER": "qlik"}, {"LOWER": "view"}]
skill18 = [{"LOWER": "apprentissage"}, {"LOWER": "automatique"}]
skill19 = [{"LOWER": "scala"}]
skill20 = [{"LOWER": "julia"}]
skill21 = [{"LOWER": "cpp"}]
skill22 = [{"LOWER": "c"}]
skill23 = [{"LOWER": "bi"}]
skill24 = [{"LOWER": "pig"}]
skill25 = [{"LOWER": "nosql"}]
skill26 = [{"LOWER": "mysql"}]
skill27 = [{"LOWER": "sql"}]
skill28 = [{"LOWER": "mapreduce"}]
skill29 = [{"LOWER": "java"}]
skill30 = [{"LOWER": "tcpdump"}]
skill31 = [{"LOWER": "javascript"}]
skill32 = [{"LOWER": "mongodb"}]
skill33 = [{"LOWER": "hbase"}]
skill34 = [{"LOWER": "OSPF"}]
skill35 = [{"LOWER": "BGP"}]
skill36 = [{"LOWER": "isis"}]
skill37 = [{"LOWER": "apache"}, {"POS": "NOUN"},{"OP": "?"}]
# Make the pattern optional, by allowing it to match 0 or 1 times
skill38 = [{"LOWER": "php"}]
skill39 = [{"LOWER": "docker"}]
skill40 = [{"LOWER": "vue.js"}]
skill41 = [{"LOWER": "angular"}]
skill42 = [{"LOWER": "node.js"}]
skill43 = [{"LOWER": "redux"}]
skill44 = [{"LOWER": "react"}, {"LOWER":"native"}]
skill45 = [{"LOWER": "html"}]
skill46 = [{"LOWER": "karma"}]
skill47= [{"LOWER": "jasmine"}]
skill48 = [{"LOWER": "protractor"}]
skill49 = [{"LOWER": "web"}, {"LOWER": "design"}]
skill50 = [{"LOWER": "sass"}]
skill51 = [{"LOWER": "hibernate"}]
skill52 = [{"LOWER": "jdbc"}]
skill53 = [{"LOWER": "gwt"}]
skill54 = [{"LOWER": "vaadin"}]
skill55 = [{"LOWER": "spring"}]
skill56 = [{"LOWER": "jee"}]
skill57 = [{"LOWER": "angularjs"}]
skill58 = [{"LOWER": ".net"}]
skill59 = [{"LOWER": "xml"}]
skill60 = [{"LOWER": "elasticsearch"}]
skill61 = [{"LOWER": "jenkins"}]
skill62 = [{"LOWER": "rabbitmq"}]
skill63 = [{"LOWER": "mssql"}]
skill64 = [{"LOWER": "sybase"}]
skill65 = [{"LOWER": "oracle"}]
skill66 = [{"LOWER": "perl"}]
skill67 = [{"LOWER": "powershel"}]
skill68 = [{"LOWER": "groovy"}]
skill69 = [{"LOWER": "tomcat"}]
skill70 = [{"LOWER": "dollar"}, {"LOWER": "universe"}]
skill71 = [{"LOWER": "navigos"}]
skill72 = [{"LOWER": "shell"}]
skill73 = [{"LOWER": "jira"}]
skill74 = [{"LOWER": "csharp"}]
skill75 = [{"LOWER": "clearcase"}]
skill76 = [{"LOWER": "zend"}]
skill77 = [{"LOWER": "lamp"}]
skill78 = [{"LOWER": "ansible"}]
skill79 = [{"LOWER": "vmware"}]
skill80 = [{"LOWER": "api"}, {"LOWER": "rest"}]
skill81 = [{"LOWER": "mariadb"}]
skill82 = [{"LOWER": "maven"}]
skill83 = [{"LOWER": "redmine"}]
skill84 = [{"LOWER": "joomla"}]
skill85 = [{"LOWER": "wordpress"}]
skill86 = [{"LOWER": "symfony"}]
skill87 = [{"LOWER": "routage"},{"LOWER": "dynamique"}]
skill88 = [{"LOWER": "dns"}]
skill89 = [{"LOWER": "dhcp"}]
skill90 = [{"LOWER": "snmp"}]
skill91 = [{"LOWER": "reactjs"}]
skill92 = [{"LOWER": "kafka"}]
skill93 = [{"LOWER": "cloud"}]

skill_pattern = [skill1, data_skill,skill4, skill5, skill6, skill7, skill8, skill9, skill10, skill11, skill12,\
                skill14, skill15, skill16, skill17, skill18, skill19, skill20, skill21, skill22, skill23,\
                skill24, skill25, skill26, skill27, skill28, skill29, skill30, skill31, skill32, skill33,\
                skill34, skill35, skill36, skill37, skill38, skill39, skill40, skill41, skill42, skill43,\
                skill44, skill45, skill46, skill47, skill48, skill50, skill51, skill52, skill53, skill54,\
                skill55, skill56, skill57, skill58, skill59, skill60, skill61, skill62, skill63, skill64,\
                skill65, skill66, skill67, skill67, skill68, skill69, skill70, skill71, skill72, skill73,\
                skill74, skill75, skill76, skill77, skill78, skill79, skill80, skill81, skill82, skill83,\
                skill84, skill84, skill85, skill86, skill87, skill88, skill89, skill90, skill91, skill92, \
                skill93]


# Creating patterns for seniority

seniority1 = [{"LOWER": "junior"}]
seniority2 = [{"LOWER": "confirmé"}]
seniority3 = [{"LOWER": "senior"}]
seniority4 = [{"LOWER": "manager"}]
seniority5 = [{"LOWER": "expert"}]

seniority_pattern = [seniority1, seniority2, seniority3, seniority4, seniority5]



skill_matcher.add("skill", None, *skill_pattern)
seniority_matcher.add("seniority", None, *seniority_pattern)


Traning_data = []
spans_data= []


for offer in offers_description:
    doc = nlp(offer)
    """ Match on the doc and create a list of matched spans """
    l = []
    spans = [doc[start:end] for match_id, start, end in skill_matcher(doc)]
    entities = [(span.start_char, span.end_char, "skill") for span in spans]
    l.extend(spans)
    print(spans)    
    
    spans = [doc[start:end] for match_id, start, end in seniority_matcher(doc)]
    entities.extend([(span.start_char, span.end_char, "seniority") for span in spans])
    l.extend(spans)
    print(spans)
    """ Get (start character, end character, label) tuples of matches
        Format the matches as a (doc.text, entities) tuple"""
    
    training_example = (doc.text, {"entities": entities})
    # Append the example to the training data
    Traning_data.append(training_example)   
    spans_data.append(l)
    # print(*Traning_data , sep="\n")
    
#Creation of training dataset file in current directory
pickle.dump(Traning_data, open("NER_Traning_data", "wb"))


