import numpy as np
import pandas as pd


def new_depth_arange(depth, step):
    start, end = depth.min(), depth.max()
    return np.arange(start, end, step)

def interpolate_wells(dict_data, step=0.2, depth="DEPTH"):

    for well, df in dict_data.items():

        curr_depth = df[depth].sort_values()
        new_depth = new_depth_arange(curr_depth, step)
        new_data = pd.DataFrame({depth: new_depth})

        for col in df.columns:

            if col == "DEPTH":
                continue

            new_data[col] = np.interp(new_depth, curr_depth, df[col])

        dict_data[well] = new_data

def categorical_interp(x, xp, fp):
    # Ensure inputs are numpy arrays
    x = np.asarray(x)
    xp = np.asarray(xp)
    fp = np.asarray(fp)
    
    # Sort xp and fp based on xp
    indices = np.argsort(xp)
    xp = xp[indices]
    fp = fp[indices]
    
    # Find the nearest indices in xp for each value in x
    nearest_indices = np.searchsorted(xp, x, side="left")
    
    # Correct nearest_indices to stay within bounds
    nearest_indices = np.clip(nearest_indices, 1, len(xp) - 1)
    
    # Determine whether to take the previous or the next index
    left = xp[nearest_indices - 1]
    right = xp[nearest_indices]
    
    # Use np.where to decide which index to use
    nearest_indices -= np.abs(x - left) < np.abs(x - right)
    
    return fp[nearest_indices]