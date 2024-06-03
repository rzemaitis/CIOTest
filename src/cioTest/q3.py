import argparse
import pandas as pd
import cioTest.utils as utils

pd.options.mode.chained_assignment = None  # default='warn'


def main(args):
    df = pd.read_csv('./ports.csv')
    # Question 3
    print('\nQuestion 3')
    print('Do all servers have multiple redundant connections '
          'to independent switches?\n')
    tempdf = utils.extract_vlans(df)
    unique_vlans = tempdf[tempdf['command'] == 'port']['vlan'].unique()
    for vlan in unique_vlans:
        unique_switches = tempdf[tempdf['vlan'] == vlan]['switch'].nunique()
        # All servers have at least one redundancy
        if unique_switches == 1:
            print(f"{vlan} has no redundancy")
            print(tempdf[tempdf['vlan'] == vlan]['switch'].unique())
        elif unique_switches == 2:
            print(f"{vlan} has little redundancy")
            print(tempdf[tempdf['vlan'] == vlan]['switch'].unique())


def parse_args():
    '''
    The argument parsing function
    '''
    parser = argparse.ArgumentParser(
        description='This script answers Question 3.'
        )
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
