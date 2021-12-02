import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, acc, mph, range, seats, body_style, drive,fast_charge):
        RWD_temp = 0
        AWD_temp = 0

        body_hatch = 0
        body_SUV = 0
        body_sedan = 0
        body_pick = 0

        if (drive == "Rear Wheel Drive"):
            RWD_temp = 1
        elif (drive == "Forward Wheel Drive"):
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
        
        body_lift = 0
        body_mpv = 0
        body_pick = 0
        body_spv = 0
        body_station = 0

        segment_B = 1
        segment_C = 0
        segment_D = 0
        segment_E = 0
        segment_F = 0
        segment_N = 0
        segment_S = 0

        battery = 65
        efficiency = 189
        #fastCharge = 500
        rapidCharge = 1

        input_pred = [[acc, battery, efficiency, fast_charge, seats, mph, range, rapidCharge,RWD_temp, AWD_temp,segment_B,segment_C,segment_D,segment_E,segment_F,segment_N,segment_S,body_hatch,body_lift,body_mpv, body_pick, body_spv, body_SUV, body_sedan,body_station]]


        filename = 'static/finalized_model.sav'
        rf = pickle.load(open(filename, 'rb'))

        X = np.array(input_pred)

        preds_singular = rf.predict(X)

        preds_singular[0] = round(preds_singular[0]*1.13,2) 
        print( preds_singular[0])
        return preds_singular[0]

