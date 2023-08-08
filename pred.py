import pickle
import pandas as pd
from xgboost import XGBClassifier

file_name = "xgb.pkl"

def predict(data):
    #print(data)
    df = pd.DataFrame.from_dict(data,orient="index")
    print(df)
    df=df.T
    xgb_model_loaded = pickle.load(open(file_name, "rb"))
    result = xgb_model_loaded.predict(df) 
    return result[0]