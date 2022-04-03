import requests
import re
import sys

from .vars import base_url

class doodstream_conf:
    '''Python doodstream api wrapper from official https://doodstream.com/api
    
    all method below return dict that contain info'''
    
    
    base_url = base_url
    
    def __init__(self, api_key):
        '''init doodstream
        Args:
            api_key (str): api key from doodstream'''
        self.api_key = api_key
        
    
    def req(self, url):
        '''requests to api
        
        Args:
            url (str): api url
            
        Return:
            (dict): output dic from requests url'''
        try:
            r = requests.get(url)
            response = r.json()
            if response['msg'] == "Wrong Auth":
                sys.exit("Invalid API key, please check your API key")
            else:
                return response
        except ConnectionError as e:
            sys.exit(f"ERROR : {e}")
            
    ###########################        
    ##### Account section #####
    ###########################
    
    def account_info(self):
        '''Get basic info of your account'''
        url = f"{self.base_url}account/info?key={self.api_key}"
        return self.req(url)
        
    def account_reports(self, last = None, from_date = None, to_date = None):
        '''
        Get reports of your account
        
        last (int): Last x days report
        from_date  str(YYYY-MM-DD): From date
        to_date str(YYYY-MM-DD): To date
        
        example:
        get reports from x date to y date:
            dd.account_dmca("2020-01-01", "2020-01-31")
        '''
        url = f"{self.base_url}account/stats?key={self.api_key}&last={last}&from_date={from_date}&to_date={to_date}"
        return self.req(url)
    
    def account_dmca(self):
        '''
        Get DMCA reported files list (500 results per page)
        '''
        url = f"{self.base_url}account/dmca/list?key={self.api_key}"
        return self.req(url)
    
    
    #########################
    ######## Upload #########
    #########################
        
    def local_upload(self, path):
        '''Upload from local storage
        
        Args:
            path (str): path to file
        '''
        url = f"{self.base_url}upload/server?key={self.api_key}"
        url_for_upload = self.req(url)['result']
        post_data = {"api_key": self.api_key}
        filename = path.split("/")[-1]
        post_files = {"file": (filename, open(path, "rb"))}
        up = requests.post(url_for_upload, data=post_data, files=post_files)
        st = re.findall(r'name="st">(.*?)</text' , str(up.text))
        fn = re.findall(r'name="fn">(.*?)</text' , str(up.text))
        if st[0] == "OK":
            return {"status": st[0], "file_id": fn[0], "file_url": f"https://doodstream.com/d/{fn[0]}"}
        else:
            raise TypeError(f"unsupported video format {filename}, please upload video with mkv, mp4, wmv, avi, mpeg4, mpegps, flv, 3gp, webm, mov, mpg & m4v format")
    
    def copy_video(self, file_id, folder_id):
        '''Copy video to your account
        
        Args:
            file_id (str): doodstream video file id
            folder id (str): doodstream folder id to upload inside folder
        
        '''
        url = f"{self.base_url}file/clone?key={self.api_key}&file_code={file_id}&fld_id={folder_id}"
        return self.req(url)
    
    ###################################
    ########## Remote Upload ##########    
    ###################################
    
    def remote_upload(self, direct_link, new_title, folder_id):
        '''Upload files using direct links
        
        Args:
            direct_link (str): direct link video for upload
        '''
        try:
            if new_title != None:
                url = f"{self.base_url}upload/url?key={self.api_key}&url={direct_link}&fld_id={folder_id}&title={new_title}"
                return self.req(url)
            else:
                raise ValueError("new_title is required for remote_upload")
        except ValueError as e:
            print(e)
            
    def remote_upload_list(self):
        '''Get list & status of remote uploads'''
        url = f"{self.base_url}urlupload/list?key={self.api_key}"        
        return self.req(url)
    
    def remote_upload_status(self, file_id):
        '''Get Only status of remote uploads'''
        url = f"{self.base_url}urlupload/status?key={self.api_key}&file_id={file_id}"
        return self.req(url)
    
    def remote_upload_slots(self):
        'Check slots for remote uploads'
        url = f"{self.base_url}urlupload/slots?key={self.api_key}"
        return self.req(url)
    
    def remote_upload_action(self,restart_errors, clear_errors, clear_all, delete_all):
        '''
        Perform Various actions on remote upload
        
        args:
            restart_error (bool): Restart Failed Uploads
            clear_errors (bool): Clear Failed Uploads
            clear_All (bool): Clear Every upload currently Happening
            delete_upload (str): Delete file Upload (pass file_id)
        '''
        url = f"{self.base_url}urlupload/actions?key={self.api_key}&restart_errors={restart_errors}&clear_errors={clear_errors}&clear_all={clear_all}&delete_all={delete_all}"
        return self.req(url)
        
    #####################################
    ########## Folder Section ###########
    #####################################
    
    def folder_create(self, folder_name, parent_folder_id = None):
        '''Create folder in your account
        
        Args:
            folder_name (str): folder name
            parent_folder_id (str): parent folder id
        '''
        url = f"{self.base_url}folder/create?key={self.api_key}&folder_name={folder_name}&parent_id={parent_folder_id}"
        return self.req(url)
            
    def folder_rename(self, folder_id, new_name):
        '''Rename folder in your account
        
        Args:
            folder_id (str): folder id
            new_name (str): new name
        '''
        url = f"{self.base_url}folder/rename?key={self.api_key}&folder_id={folder_id}&new_name={new_name}"
        return self.req(url)
    
    ####################################
    ########### File Section ##########
    ####################################
    
    def file_list(self, page, per_page, fld_id):
        '''Get list of files in your account
        
        Args:
            page (int): page number
            per_page (int): number of results per page
            fld_id (str): folder id
        '''
        url = f"{self.base_url}file/list?key={self.api_key}&page={page}&per_page={per_page}&fld_id={fld_id}"
        return self.req(url)
    
    def file_status(self, file_id):
        '''Get file status
        
        Args:
            file_id (str): file id
        '''
        url = f"{self.base_url}file/check?key={self.api_key}&file_code={file_id}"
        return self.req(url)
    
    def file_info(self, file_id):
        '''Get file info
        
        Args:
            file_id (str): file id
        '''
        url = f"{self.base_url}file/info?key={self.api_key}&file_code={file_id}"
        return self.req(url)
    
    def file_image(self, file_id):
        '''Get file splash, single or thumbnail image
        
        Args:
            file_id (str): file id
        '''
        url = f"{self.base_url}file/image?key={self.api_key}&file_code={file_id}"
        return self.req(url)
    
    
    def file_rename(self, file_id, new_name):
        '''Rename file in your account
        
        Args:
            file_id (str): file id
            new_name (str): new name
        '''
        url = f"{self.base_url}file/rename?key={self.api_key}&file_code={file_id}&title={new_name}"
        return self.req(url)
    
    def file_search(self, search_term):
        '''Search files in your account
        
        Args:
            search_term (str): search term
        '''
        url = f"{self.base_url}file/search?key={self.api_key}&search_term={search_term}"
        return self.req(url)
    
    
        
    
        
    
    