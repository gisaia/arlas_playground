import os

from tools.data_access import download_files_from_bucket, PROJECT_ROOT


if __name__ == '__main__':
    # Set root data path
    local_data_path = os.path.join(PROJECT_ROOT, "tutorials/sunny_osm/data")
    remote_demo_data_path = "gs://gisaia-public/demo"

    # Download raw data from gisaia-storage bucket
    download_files_from_bucket("sunny_osm/osm.csv", recursive=False,
                               local_data_path=local_data_path, remote_demo_data_path=remote_demo_data_path)
    download_files_from_bucket("sunny_osm/commune.csv", recursive=False,
                               local_data_path=local_data_path, remote_demo_data_path=remote_demo_data_path)
    download_files_from_bucket("sunny_osm/languedoc-roussillon.json", recursive=False,
                               local_data_path=local_data_path, remote_demo_data_path=remote_demo_data_path)
    download_files_from_bucket("sunny_osm/photovoltaic_potential", recursive=True,
                               local_data_path=local_data_path, remote_demo_data_path=remote_demo_data_path)
