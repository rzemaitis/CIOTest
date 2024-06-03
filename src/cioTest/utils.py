import pandas as pd

def extract_vlans(df):
    '''
    Create a new column 'vlan' to store
    both tagged and untagged VLANs.

    This will create a new row per each tagged VLAN, but will
    remove any rows that do not contain the command 'port' for
    simplicity purposes of this assignment.
    '''
    # Ensure that only port commands are used
    df = df[df['command'] == 'port']
    # Make a new column
    df.loc[:, 'vlan'] = df['untagged_vlan']
    for i, row in df[~df['tagged_vlans'].isna()].iterrows():
        # Create new rows in the dataframe for each tagged vlan
        for vlan in row['tagged_vlans'].split(' '):
            row['vlan'] = vlan
            edited_row_df = pd.DataFrame([row])
            df = pd.concat([df, edited_row_df], ignore_index=True)
    return df