from urllib.request import urlretrieve
import os

def get_data(url, filename, force_download=False):
    """Download and cache data

    Parameters
    ----------
    filename : string
    url : string -> web location of data
    force_download : bool -> if True, force download of data

    Returns
    -------
    response - file with filename to current directory
    """

    if force_download or not os.path.exists(filename):
       	res  = urlretrieve(url, filename)
	return res