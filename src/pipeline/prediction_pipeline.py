# -*- coding: utf-8 -*-
"""prediction_pipeline.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1seQUQ2POQKJwP3Bxa8Xd7WZSbRdLf8te
"""

import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictionPipeline:
  def __init__(self):
    pass

  class CustomData:
    def __init__(self,
                 gender:str,
                 race_ethinicity:str,
                 parental_level_of_education:str,
                 lunch:str,
                 test_preparation_course:str,
                 reading_score:int,
                 writing_score:int):

                self.gender = gender

                self.race_ethinicity = race_ethinicity

                self.parental_level_of_education = parental_level_of_education

                self.lunch = lunch

                self.test_preparation_course = test_preparation_course

                self.reading_score = reading_score

                self.writing_score = writing_score

    def get_data_as_data_frame(self):
      try:
        custom_input_data_dict={
            "gender" : [self.gender],
            "race_ethinicity":[self.race_ethinicity],
            "Parental_level_of_education" : [self.parental_level_of_education],
            "lunch":[self.lunch],
            "test_preperation_course":[self.test_preperation_course],
            "total":[self.total],
        }

        return pd.DataFrame(custom_input_data_dict)
      except Exception as e:
        raise CustomException(e,sys)