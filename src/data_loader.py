import pandas as pd
import os

def load_data():
    folder_path = "data"
    all_files = os.listdir(folder_path)

    df_list = []

    for file in all_files:
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            
            df = pd.read_csv(file_path, encoding='latin1')
            
            # Add state name from file
            state_name = file.replace(".csv", "")
            df["state_name"] = state_name
            
            df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)
    
    return combined_df