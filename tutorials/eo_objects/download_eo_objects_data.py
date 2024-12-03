import os

from tools.data_access import download_files_from_bucket, PROJECT_ROOT


if __name__ == '__main__':
    # Set root data path
    local_data_path = os.path.join(PROJECT_ROOT, "tutorials/eo_objects/data")
    remote_demo_data_path = "gs://gisaia-public/demo"

    # Download raw data from gisaia-storage bucket
    os.makedirs(os.path.join(local_data_path, "eo_objects/xView"))
    download_files_from_bucket("eo_objects/xView/eo_objects_athens.json", recursive=True,
                               local_data_path=local_data_path, remote_demo_data_path=remote_demo_data_path)
