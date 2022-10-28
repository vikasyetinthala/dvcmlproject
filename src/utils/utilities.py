import yaml
import os 

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml,'r') as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_directory(dirs:list):
    for data_path in dirs:
        os.makedirs(data_path)
        print(f"directory is created at {data_path}")

def save_local_df(data, data_path, index_status=False):
    data.to_csv(data_path,index=index_status)
    print(f"data is saved at {data_path}")
