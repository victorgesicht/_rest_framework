#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c3.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')  # or whatever config you're using

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
