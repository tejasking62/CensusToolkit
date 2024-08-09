import pandas as pd

class DataProcessor:
    
    def __init__(self, data):
        self.data = data
    
    # Extract specific keys from each variable's metadata
    def _extract_keys(self, keys):
        extracted_keys = []
        
        for key, variable in self.data.items():
            entry = {'key': key}
            
            for k in keys:
                if k in variable:
                    entry[k] = variable[k]
            extracted_keys.append(entry)
        
        return extracted_keys
    
    # Create a dataframe out of selected keys
    def create_df(self, keys):
        extracted_data = self._extract_keys(keys)
        
        df = pd.DataFrame(extracted_data)
        return df
    
    def create_group_df(self, group_data):
        return pd.DataFrame(group_data)
    
    def merge_group_data(self, group_data, var_data):
        df_vars = pd.DataFrame(var_data).transpose()
        df_groups = pd.DataFrame(group_data)
        
        merged_df = df_vars.merge(df_groups, left_on='group', right_on='name', how='left')
        return merged_df
        
