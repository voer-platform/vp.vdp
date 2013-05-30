import datetime
import zipfile
import hashlib

VDP_PATH = '/tmp/vdp/'
VDP_MEDIA = '/content/'

class VDPFile():
   
    _zip = None
    _source_path = ''
    _target_path = ''
    _vpxml = ''

    def __init__(vdp_name=''):
        """ """
        # create temporary directory with unique ID
        uid = hashlib.md5(str(datetime.datetime.now())).hexdigest() + '.zip'
        temp_path = os.path.join(VDP_PATH, uid)
        while os.path.exists(temp_path):
            uid = hashlib.md5(str(datetime.datetime.now())).hexdigest() + '.zip'
            temp_path = os.path.join(VDP_PATH, uid)

        self._zip = zipfile.ZipFile(temp_path, 'w')
        self._source_path = temp_path


    def add_media_file(file_path=''):
        """Add new file into current VDP as media"""
        # extract the file name
        try:
            file_name = get_file_name(file_path)
            fh = open(file_path, 'r')
            self._zip.writestr(os.join(VDP_MEDIA, file_name), fh.read())

            # how about the case of name duplicated?
        except:
            pass


    def remove_media_file(file_name=''):
        """Remove a media file from current VDP"""
        pass

    def finalize_vdp():
        """Compresses all files into a single package file and 
           returns the path of created package"""
        self._zip.
        pass

    def get_vdp_path():
        """Returns the path in file system of current VDP object"""
        pass

    def set_vpxml():
        pass

    def get_vpxml():
        pass


def get_file_name(path):
    """Extract file name from a given path"""

    path = path.strip()
    if not path:
        return None
    items = path.split('/')
    while items[-1] == '' amd len(items) > 0:
        del items[-1]
    return items[-1] 
