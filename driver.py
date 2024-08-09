from json_data import JSONVars
from data_transform import DataProcessor
import pandas as pd

def main():
    json_util = JSONVars()
    
    json_util.set_parameters(year=2022, type='acs5')
    
    filtered_data = json_util.filter_data(['S0101_C01'])
    print(filtered_data)
    
    data_processor = DataProcessor(filtered_data)
    df = data_processor.create_df(['group', 'label', 'concept', 'predicateType'])
    print(df)
    
    with pd.ExcelWriter('filtered_vars.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
        ws = writer.sheets['Sheet1']
        ws.column_dimensions['A'].width = 15
        ws.column_dimensions['B'].width = 10
        ws.column_dimensions['C'].width = 65
        ws.column_dimensions['D'].width = 15
        ws.column_dimensions['E'].width = 10
        
    groups = json_util.fetch_groups()
    group_vars = json_util.fetch_group_vars('S1601')
    merged_df = data_processor.merge_group_data(groups, group_vars)
    
    with pd.ExcelWriter('merged_data.xlsx', engine='openpyxl') as writer:
        merged_df.to_excel(writer, index=False)
        ws = writer.sheets['Sheet1']
        ws.column_dimensions['A'].width = 65
        ws.column_dimensions['B'].width = 25
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 10
        ws.column_dimensions['E'].width = 15
        ws.column_dimensions['F'].width = 25
        ws.column_dimensions['H'].width = 30
        ws.column_dimensions['I'].width = 60

if __name__ == '__main__':
    main()