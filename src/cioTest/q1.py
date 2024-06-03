import argparse
import pandas as pd


def main(args):
    df = pd.read_csv('./ports.csv')

    # Question 1
    print('\nQuestion 1')
    print('How many ports are configured untagged for the ATopen VLAN?\n')
    tempdf = df[df['command'] == 'port']  # Removes all mac commands
    tempdf = df[df['untagged_vlan'] == 'ATopen']
    print(f"{len(tempdf)}\n")


def parse_args():
    '''
    The argument parsing function
    '''
    parser = argparse.ArgumentParser(
        description='This script answers Question 1.'
        )
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
