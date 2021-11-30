import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, acc, mph, range, seats, body_style, drive):
        RWD_temp = 0
        AWD_temp = 0

        body_hatch = 0
        body_SUV = 0
        body_sedan = 0
        body_pick = 0

        if (drive == "RWD"):
            RWD_temp = 1
        elif (drive == "AWD"):
            AWD_temp = 1
        else:
            pass

        if (body_style == "Hatchback"):
            body_hatch = 1
        elif (body_style == "SUV"):
            body_SUV = 1
        elif (body_style == "Sedan"):
            body_sedan = 1
        elif (body_style == "Pickup"):
            body_pick = 1
        else:
            pass

        battery = 65
        efficiency = 189
        fastCharge = 436
        rapidCharge = 1

        input_pred = [[acc, mph, range, seats, battery, efficiency, fastCharge, rapidCharge ,body_hatch, body_SUV, body_sedan, body_pick, RWD_temp,AWD_temp]]


        filename = 'finalized_model.sav'
        ada_load = pickle.load(open(filename, 'rb'))

        X = np.array(input_pred)
        preds = ada_load.predict_proba(X)
        preds_singular = ada_load.predict(X)

        return preds_singular[0]
