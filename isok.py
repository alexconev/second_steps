#!/usr/bin/python3

import os
import sys
from subprocess import call, Popen
import filecmp

walk_dir = sys.argv[1]


def is_files_empty(root, files):
    testfiles = 0
    for filename in files:
        if filename.endswith(".in") or filename.endswith(".out"):
            testfiles++
        file_path = os.path.join(root, filename)
        with open(file_path, 'r') as f:
            f_content = f.read()
            if f_content == '':
                print("Empty file: %s" % os.path.abspath(file_path))
                sys.exit(1)
    if(testfiles < 22)
        print("Not enough test files: %s" root) 

def delete_file(filepath):
    try:
        call(["rm", filepath])
    except Exception as e:
        print(e)
        sys.exit(1)


def compile_file(filepath, exepath):
    try:
        call(["g++", filepath, "-o", exepath, "-O2", "-W", "-Wall"])
    except Exception as e:
        print(e)
        sys.exit(1)


def run_test(inp):
    global executable, output

    out = inp[0:-2]+'out'

    myinput = open(inp)
    myoutput = open(output, 'w')
    p = Popen(executable, stdin=myinput, stdout=myoutput)
    p.wait()
    myoutput.flush()

    myinput.close()
    myoutput.close()

    return filecmp.cmp(out, output)


def make_tests(root, files):

    for f in files:
        if f.endswith(".in"):
            if not run_test(os.path.abspath(root+'/'+f)):
                print("Expected answer is different in test %s (%s)" % (f,os.path.abspath(root)))


def main():
    global executable, output

    for root, subdirs, files in os.walk(walk_dir):

        if len(files) > 3:

            executable = os.path.abspath("sol")
            output = os.path.abspath("tmp.sol")
            source = os.path.abspath(root+"/sol.cpp")

            if os.path.isfile(executable):
                delete_file(executable)

            is_files_empty(root, files)

            compile_file(source, executable)

            make_tests(root, files)

            delete_file(executable)
            delete_file(output)


if __name__ == "__main__":
    main()
