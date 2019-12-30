# _*_ coding: utf-8 _*_
# @Author: taoyanqi 
# @Date: 2019-12-30 10:20:22 
 

from __future__ import print_function

from datetime import datetime, timedelta

import argparse

def main():
    start_time = datetime.now()

    spend_time = (datetime.now() - start_time).seconds
    print("run minutes:", spend_time/60.0)


def add_arguments(parse):
    parse.add_argument("--data_path", type=str, default="data.txt", help="data path")


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    add_arguments(parse)
    flags, unparsed = parse.parse_known_args()
    main()