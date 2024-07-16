import numpy as np
import pandas as pd


def new_depth_arange(depth, step):
    start, end = depth.min(), depth.max()
    return np.arange(start, end, step)

def interpolate_wells(dict_data, step=0.2, depth="DEPTH"):

    for well, df in dict_data.items():

        curr_depth = df[depth]
        new_depth = new_depth_arange(curr_depth, step)
        new_data = pd.DataFrame({depth: new_depth})

        for col in df.columns:

            if col == "DEPTH":
                continue

            new_data[col] = np.interp(new_depth, curr_depth, df[col])

        dict_data[well] = new_data