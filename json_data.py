import requests

class JSONVars:
    # Initilize base variables
    def __init__(self):
        self.base_url = 'http://api.census.gov/data'
        self.url = None
        self.year = None
        self.type = None
        self.variables = None
    
    # Do this before getting variables
    # Define year, survey type, build url, and pull variables
    def set_parameters(self, year, type):
        self.year = year
        self.type = type
        self.url = self._construct_url()
        self.variables = self._fetch_vars()
    
    def _construct_url(self):
        return f"{self.base_url}/{self.year}/acs/{self.type}/subject/variables.json"
    
    def _fetch_vars(self):
        response = requests.get(self.url)
        
        if response.status_code == 200:
            return response.json().get('variables')
        else:
            response.raise_for_status
            return None
    
    def fetch_groups(self):
        groups_url = f'{self.base_url}/{self.year}/acs/{self.type}/subject/groups.json'
        response = requests.get(groups_url)
        
        if response.status_code == 200:
            return response.json().get('groups')
        else:
            response.raise_for_status
            return None
    
    def fetch_group_vars(self, group_name):
        group_var_url = f'{self.base_url}/{self.year}/acs/{self.type}/subject/groups/{group_name}.json'
        response = requests.get(group_var_url)
        
        if response.status_code == 200:
            return response.json().get('variables')
        else:
            response.raise_for_status
            return None
    
    # If the data you are filtering has some commonality
    def filter_data(self, patterns):
        entries = {key : value for key, value in self.variables.items() if any(pattern in key for pattern in patterns)}
        return entries

    
