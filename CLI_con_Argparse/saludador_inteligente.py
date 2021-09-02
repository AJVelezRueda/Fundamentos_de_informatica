#!/bin/python3

import argparse
import sys


parser = argparse.ArgumentParser(
    description="Una descripción breve de nuestro script")

parser.add_argument(
    "name",
    help="name input",
    type=str)

nombre = parser.parse_args(sys.argv[1:]).name     
print(f'Hola {nombre}')
