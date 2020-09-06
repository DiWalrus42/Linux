#! /usr/bin/python

import os
import sys
import getopt

current_directory = (os.path.basename(os.getcwd()))


def create_repository():
    try:
        os.system(f'echo # {current_directory} >> README.md')
        os.system("git init .")
        os.system("git add .")
        os.system('git commit -m "Initial Commit"')
        os.system("hub create")
        os.system("git push origin master")
    except:
        git_error_status()


def push_to_repository(commit_arg):
    try:
        os.system("git add .")
        os.system(f'git commit -m "{commit_arg}"')
        os.system("git push origin master")
    except:
        git_error_status()


def git_error_status():
    print("Oops..Something Went Wrong")
    print("Performing a git status")
    os.system("git status")


try:
    opts, args = getopt.getopt(sys.argv[1:], "hc:p:", ["create=", "push="])
except getopt.GetoptError:
    print('Incorrect Command, Use:')
    print('    python3 repo-hub.py -h or --help for any help')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print("Usage:")
        print('    python3 repo-hub.py -c repo or --create repo to create new repository and push to it')
        print('    python3 repo-hub.py -p <"Commit Message"> or --push <"Commit Message"> to push to current remote repository')
        sys.exit()
    elif opt in ("-c", "--create"):
        create_repository()
        sys.exit()
    elif opt in ("-p", "--push"):
        if len(arg) == 0:
            print('Usage: python3 repo-hub.py -p or --push "Commit Message" to push to current remote repository')
            exit()
        push_to_repository(arg)
        sys.exit()
