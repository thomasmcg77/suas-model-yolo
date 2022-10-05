import os
import pandas as pd

DATA_PATH = "/"

if __name__ == "__main__":
    df = pd.read_csv(os.path.join(DATA_PATH, "train.csv"))
