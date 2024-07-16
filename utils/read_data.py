import os
import lasio
import pandas as pd

def las2csv(path):

    csv_folder = os.path.join(path, 'CSV')
    
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    for file in os.listdir(path):        
        if not (file.endswith('.las')):
            continue
    
        las_path = os.path.join(path,file)
        csv_name = file.split('.')[0] + '.csv'
        df_data = lasio.read(las_path).df()
        
        save_path = os.path.join(csv_folder, csv_name)
        df_data.to_csv(save_path)



def read_csv(path, depth="DEPTH", channel="GR", filter_nan=True, wells=[""]): #Chance desse wells bugar

    data = dict()

    for well in wells:
        for file in os.listdir(path):
            
            if not(file.startswith(well)):
                continue

            file_path = os.path.join(path, file)
            well = file.split('.')[0]
            df = pd.read_csv(file_path)[ [depth, channel] ] #TODO melhorar se necessario

            #Transform de 0.1inch para metros
            if df[depth].mean() > 7000:
                df[depth] = df[depth] / 393.7 #0.1inch to M

            if filter_nan:
                df = df[df > -90] #FILTRA VALORES NEGATIVOS
                
            data[well] = df
    return data