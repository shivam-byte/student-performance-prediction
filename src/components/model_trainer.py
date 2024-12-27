# -*- coding: utf-8 -*-
"""model_trainer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VY7iKo4hLCt_BuFsmpr7oxkKlNqHFrFw
"""

import sys
import os
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)

from sklearn.linearmodel import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.neigbors import KNeiborsRegressor
from Xgboost import XGBRegressor

from src.exception import CustumException
from src.logging import logging
from src.utils import saved_object,model_evaluation

@dataclass
class ModelTrainerConfig:
  trained_model_file_path = os.join.path('artifacts','model.pkl')

class ModelTrainer:
  def __init__(self):
    self.model_trainer_config = ModelTrainerConfig()

  def initiate_model_trainer(self,train_array,test_array):
    try:
      logging.info('split train and test data')
      X_train,y_train,X_test,y_test = (
          train_array[:,:-1],
          train_array[:,:-1],
          test_array[:,:-1],
          test_array[:,:-1]
      )

      model = {
          "Random Forest" = RandomForestRegressor(),
          "Decision Tree" = DecisionTreeRegressor(),
          "Linear Regression" = LinearRegression(),
          "XGboost Reggressot" = XGBRegressor(),
          "Adaboost Regressor" = AdaBoostRegressor(),
          "CatBoostRegressor" = CatBoostRegressor(),
          "Gradient Boosting Regressor" = GradientBoostingRegressor(),
       }

       params = {
           'Decision Tree' = {
               'criterion':['squared_error','friedman_mse','absolute_error','poisson'],
               #'splitter':['best','random'],
               #'max_features':['sqrt','log2']
           },
           "Random Forest":{
               #'criterion':['squared_error','friedman_mse','absolute_error','poisson'],
               #'max_features':['sqrt','log2',None],
               'n_estimators':[8,16,32,64,128,256]
           },
           "Grandient Boosting":{
               #'loss':['squared_error','huber','absolute_error','quantile'],
               'learning_rate':[.1,.01,.05,.001],
               'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
               'criterion':['squared_error','friedman_mse'],
               'max_features':['auto','sqrt','log2'],
               'n_estimators':[8,16,32,64,128,256]
           },
           "Linear Regression":{},
           "XGBRegressor":{
               'learning_rate':[0.1,0.01,0.05,0.001],
               'n_estimators':[8,16,32,64,128,256]

           },
           "CatBoosting Regressor":{
               'depth':[6,8,10],
               'learning_rate':[0.01,0.05,0.1],
               'iterations':[30,50,100]
           },
           "AdaBoost Regressor":{
               'learning_rate':[0.1,0.01,0.5,0.001],
               #'loss':['linear','square','exponential'],
               'n_estimators':[8,16,32,64,128,256]
           }
       }

       model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                         models=models,param = params)

       ##to get bestt model score from dict
       best_model_score = max(sorted(model_report.values()))

       ##to get best model name from dict
       best_model_name = List(model_report.keys())[
           list(model_report.values()).index(best_model_score)
       ]

       best_model = models[best_model_name]

       if best_mdoel_score<0.6:
        raise CustomException("no best model found")
      logging.info(f"best model on both training and testing dataset")

      save_object(
          file_path = self.model_trainer_config.trained_model_file_path,
          obj = best_model
      )

      predicted = best_model.predict(X_test)

      r2_square = r2_score(y_test,predicted)
      return r2_square

  except Exception as e:
    raise CustomException(e,sys)