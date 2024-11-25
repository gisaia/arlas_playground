import os

# Get project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_absolute_local_path(relative_path: str, local_data_path: str = None):
    """
    Get the absolute local path from relative path
    :param relative_path: Relative path to the data
    :param local_data_path: Local path to the data folder root
    :return: The absolute path
    """
    if local_data_path is None:
        local_data_path = os.environ['ARLAS_DEMO_LOCAL_DATA_PATH']
    absolute_local_path = os.path.join(local_data_path, relative_path)
    return absolute_local_path


def get_absolute_remote_path(relative_path: str,
                             remote_demo_data_path: str = None):
    """
    Create the absolute remote path from relative path
    :param relative_path: Relative path to file
    :param remote_demo_data_path: Path to demo data path on bucket storage
    :return: Absolute remote path to file
    """
    if remote_demo_data_path is None:
        remote_demo_data_path = os.environ['ARLAS_DEMO_REMOTE_DATA_PATH']
    absolute_remote_path = os.path.join(remote_demo_data_path, relative_path)
    return absolute_remote_path

def download_files_from_bucket(files_relative_path: str, recursive: bool = False,
                               remote_demo_data_path: str = None,
                               local_data_path: str = None):
    """
    Download file (or directory if recursive) from bucket storage
    :param files_relative_path: Relative path of the file/directory from data root
    :param recursive: If True, copy the folder and contained files
    :param remote_demo_data_path: Path to demo data path on bucket storage
    :param local_data_path: Local path to the data folder root
    """
    if remote_demo_data_path is None:
        remote_demo_data_path = os.environ['ARLAS_DEMO_REMOTE_DATA_PATH']

    if local_data_path is None:
        local_data_path = os.environ['ARLAS_DEMO_LOCAL_DATA_PATH']

    # Set local and remote data path
    if recursive:
        local_relative_path = os.path.split(files_relative_path)[0] + "/"
        recursive_opt = '-r '
        multiprocess_opt = '-m '
    else:
        local_relative_path = files_relative_path
        recursive_opt = ''
        multiprocess_opt = ''
    local_path = get_absolute_local_path(relative_path=local_relative_path,
                                         local_data_path=local_data_path)
    remote_path = get_absolute_remote_path(relative_path=files_relative_path,
                                           remote_demo_data_path=remote_demo_data_path)

    # Build gsutil command and send download request to bucket
    request_cp = f"gsutil {multiprocess_opt}cp {recursive_opt}{remote_path} {local_path}"

    print(f"Downloading '{local_path}' to '{remote_path}'\n{request_cp}")
    result = os.system(request_cp)
    if result == 0:
        print("All files have been downloaded")
    else:
        print(f"Download aborted: {request_cp}")