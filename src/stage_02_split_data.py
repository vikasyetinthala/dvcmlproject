import os
import yaml 
from src.utils.utilities import read_yaml, create_directory
import argparse 
import pandas as pd 
from sklearn.model_selection import train_test_split 

def split_data(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    artifact_dir=config["artifacts"]["artifacts_dir"]
    raw_local_dir=config["artifacts"]["raw_local_dir"]
    raw_local_file=config["artifacts"]["raw_local_file"]
    raw_local_dir_path= os.path.join(artifact_dir,raw_local_dir)
    df=pd.read_csv(raw_local_dir_path)
    split_ratio=params["base"]["test_size"]
    random_state=params["base"]["random_state"]
    train,test=train_test_split(df,test_size=split_ratio,random_state=random_state)
    train_data_dir=config["artifacts"]["artifacts_dir"]
    train_data_dir_split=config["artifacts"]["split_dir"]
    train_data_split_file=config["artifacts"]["train_file"]
    test_data_split_file=config["artifacts"]["test_file"]
    train_file_path=os.path.join(train_data_dir,train_data_dir_split)
    create_directory(dirs= [train_file_path])
    train.to_csv(os.path.join(train_file_path,train_data_split_file))
    test.to_csv(os.path.join(train_file_path,test_data_split_file))
    print(f"split data loaded successfully")


if __name__=="__main__":
    args = argparse.ArgumentParser() 
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")
    parsed_args=args.parse_args() 

    split_data(parsed_args.config,parsed_args.params)