from json_data import JSONVars
from data_transform import DataProcessor

def main():
    json_util = JSONVars()
    
    json_util.set_parameters(year=2022, type='acs5')
    
    filtered_data = json_util.filter_data(['S0101_C01'])
    print(filtered_data)
    
    data_processor = DataProcessor(filtered_data)
    df = data_processor.create_df(['group', 'label', 'concept', 'predicateType'])
    print(df)
    
    df.to_excel('filtered_vars.xlsx', index=False)
    
    groups = json_util.fetch_groups()
    group_vars = json_util.fetch_group_vars('S1601')
    merged_df = data_processor.merge_group_data(groups, group_vars)
    
    df.to_excel('merged_data.xlsx', index=False)

if __name__ == '__main__':
    main()