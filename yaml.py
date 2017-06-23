#!/usr/bin/python

import yaml
import argparse



def main():
    parser = argparse.ArgumentParser(prog='yaml', 
                                     usage='%(prog)s [options] ...', 
                                     description="A utility for "
                                                 "manipulating yaml files")
    parser.add_argument("-s", 
                        "--set", 
                        action="store_true",
                        help="set section... [key] [value]")
    parser.add_argument("-g", 
                        "--get", 
                        action="store_true",
                        help="get [section...] [key]")
    parser.add_argument("-d", 
                        "--delete", 
                        action="store_true",
                        help="delete section... [key]")
    parser.add_argument("-f", 
                        "--file", 
                        dest="file",
                        action="store",
                        help="specify target file")
    parser.add_argument("-c", 
                        "--cluster", 
                        dest="cluster",
                        action="append",
                        help="specify cluster namcluster name ....")
    parser.add_argument("-k",
                        "--key", 
                        action="store_true",
                        help='set/get/del  one key')
    parser.add_argument("-v",
                        "--value", 
                        action="store_true",
                        help='set/get/del  one value')
    parser.add_argument("--verbose", 
                        action="store_true",
                        help="increase output verbosity")
    parser.add_argument('--version', 
                        action='version', 
                        version='%(prog)s 0.1')
    args = parser.parse_args()

    if args.set:
        print("setting key value")
    elif args.get:
        print("getting value")
    elif args.delete:
        print("delete key")

    print("{}".format(args.cluster[0]))


if __name__ == "__main__":
    main()

