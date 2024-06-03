import argparse
import glob
import re
import pandas as pd
import os


def read_file(fname, colnames):
    # Append data to a dictionary
    data = {}

    # Initialise lists for entries
    for col in colnames:
        data[col] = []

    # Open the file and read line by line
    with open(fname, 'r') as file:
        for line in file:
            # Skip comment lines and empty lines
            if line.startswith('#') or not line.strip():
                continue

            # Split the line using regular expressions
            # to handle multiple spaces
            parts = re.split(r'\s+', line.strip())

            # Extract information from parts
            for i, col in enumerate(colnames):
                # Fill column with None if the line
                # has less values (e.g. mac command)
                if len(parts) <= i:
                    data[col].append(None)
                    continue

                # If a column is tagged_vlans, collect
                # the rest of the parts into one.
                if col == 'tagged_vlans':
                    data[col].append(' '.join(parts[5:])
                                     if len(parts) > 6 else None)
                    break
                else:
                    data[col].append(parts[i])
        # Add the switch name from the file name
        switchname = os.path.basename(fname).split('.')[0]
        # Make the required amount of copies
        data['switch'] = [switchname]*len(data['command'])

    # Convert dictionary to DataFrame
    data = pd.DataFrame(data)

    return data


def main(args):
    # Find all .ports files
    fnames = glob.glob('./ports/*.ports')
    if not fnames:
        raise FileNotFoundError("No .ports files found "
                                "in the './ports/' directory.")
    colnames = ['command', 'port', 'name', 'state', 'untagged_vlan',
                'tagged_vlans', 'switch']

    # Initialise the dataframe with given columns
    df = pd.DataFrame(columns=colnames)

    # Read in .ports files iteratively
    for fname in fnames:
        data = read_file(fname, colnames)
        df = pd.concat([df, data], ignore_index=True)
    # Save the dataframe as a .csv file
    df.to_csv('./ports.csv', index=False)


def parse_args():
    '''
    The argument parsing function
    '''
    parser = argparse.ArgumentParser(
        description='This script reads in the information from '
                    'the .ports files located in the /ports directory.'
        )
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())
