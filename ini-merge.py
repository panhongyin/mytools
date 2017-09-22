#!/usr/bin/python

import os
import sys
import shutil
import ConfigParser


def main():

    if len(sys.argv) < 3:
        print("\nUsage: ini-merge  < src file >  < dest file >\n")
        exit(1)

    src_file = sys.argv[1]
    dest_file = sys.argv[2]

    if not os.path.exists(src_file):
        print("[ERROR] Can't find src file")
        exit(1)

    if not os.path.exists(dest_file):
        shutil.copy(src_file, dest_file)
        exit(0)

    src_config = ConfigParser.ConfigParser()
    dest_config = ConfigParser.ConfigParser()

    try:
        src_config.read(src_file)
        dest_config.read(dest_file)
    except ConfigParser.Error as err: 
        print(err)
        exit(1)

    for section in src_config.sections():
        if not dest_config.has_section(section):
            dest_config.add_section(section)

        for option in src_config.options(section):
            value = src_config.get(section, option)
            dest_config.set(section, option, value)

    with open(dest_file, 'wb') as configfile:
        dest_config.write(configfile)

if __name__ == '__main__':
    main()
