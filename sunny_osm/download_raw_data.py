import os


def get_absolute_local_path(relative_path: str):
    """
    Get the absolute local path from relative path
    :param relative_path: Relative path to the data
    :return: The absolute path
    """
    local_demo_data_path = os.environ['ARLAS_DEMO_LOCAL_DATA_PATH']
    absolute_local_path = os.path.join(local_demo_data_path, relative_path)
    return absolute_local_path


def get_absolute_remote_path(relative_path: str,
                             remote_demo_data_path: str = os.environ['ARLAS_DEMO_REMOTE_DATA_PATH']):
    """
    Create the absolute remote path from relative path
    :param relative_path: Relative path to file
    :param remote_demo_data_path: Path to demo data path on bucket storage
    :return: Absolute remote path to file
    """
    absolute_remote_path = os.path.join(remote_demo_data_path, relative_path)
    return absolute_remote_path

def download_files_from_bucket(files_relative_path: str, recursive: bool = False,
                               remote_demo_data_path: str = os.environ['ARLAS_DEMO_REMOTE_DATA_PATH']):
    """
    Download file (or directory if recursive) from bucket storage
    :param files_relative_path: Relative path of the file/directory from data root
    :param recursive: If True, copy the folder and contained files
    :param remote_demo_data_path: Path to demo data path on bucket storage
    """
    # Set local and remote data path
    if recursive:
        local_relative_path = os.path.split(files_relative_path)[0] + "/"
        recursive_opt = '-r '
        multiprocess_opt = '-m '
    else:
        local_relative_path = files_relative_path
        recursive_opt = ''
        multiprocess_opt = ''
    local_path = get_absolute_local_path(relative_path=local_relative_path)
    remote_path = get_absolute_remote_path(relative_path=files_relative_path,
                                           remote_demo_data_path=remote_demo_data_path)

    # Build gsutil command and send download request to bucket
    request_cp = f"gsutil {multiprocess_opt}cp {recursive_opt}{remote_path} {local_path}"

    print(f"Downloading '{local_path}' to '{remote_path}'\n{request_cp}")
    result = os.system(request_cp)
    if result == 0:
        print("All files have been downloaded")
    else:
        print("Download aborted")


if __name__ == '__main__':
    # Download raw data from gisaia-storage bucket
    download_files_from_bucket("sunny_osm/photovoltaic_potential", recursive=True)
    download_files_from_bucket("sunny_osm/osm.csv", recursive=False)
    download_files_from_bucket("sunny_osm/commune.csv", recursive=False)
    download_files_from_bucket("sunny_osm/languedoc-roussillon.json", recursive=False)
