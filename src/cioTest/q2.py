import argparse
import pandas as pd
import cioTest.utils as utils


def print_top_5(column):
    '''
    Prints out the top 5 commonly-used VLANs from a given column.
    '''
    top_vlans = column.value_counts()[:5]
    for vlan, count in top_vlans.items():
        print(f'{vlan}: {count}')


def main(args):
    df = pd.read_csv('./ports.csv')
    # Question 2
    print('\nQuestion 2')
    print('Which are the most commonly-used VLANs?\n')
    print('Depending on the assumptions, here are the Top 5:')

    # TODO: Uncomment additional assumptions if required
    # print('\nIf we\'re considering the untagged VLANs only:')
    # tempdf = df[df['command'] == 'port']
    # column = tempdf['untagged_vlan']
    # print_top_5(column)
    # print('\nIf we\'re considering the untagged VLANs only for ports'
    #       ' that are currently enabled:')
    # tempdf = tempdf[tempdf['state'] == '-']
    # column = tempdf['untagged_vlan']
    # print_top_5(column)

    # TODO: Uncomment additional assumptions if required
    # print('\nIf we\'re considering the untagged+tagged VLANs:')
    # tempdf = extract_vlans(df)
    # column = tempdf['vlan']
    # print_top_5(column)
    print('\nIf we\'re considering the untagged+tagged VLANs for ports '
          'that are currently enabled:')
    tempdf = utils.extract_vlans(df[df['state'] == '-'])
    column = tempdf['vlan']
    print_top_5(column)


def parse_args():
    '''
    The argument parsing function
    '''
    parser = argparse.ArgumentParser(
        description='This script answers Question 2.'
        )
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
