from unit import test
import os

def main():
    cwd = os.getcwd()
    testsp = os.path.join(cwd, 'tests')
    testfls = os.path.join(testsp,'test_files')
    outs = os.path.join(cwd, 'Output')
    x = test(inputp = testfls, outp = outs)
    x.txtconverter()

if __name__ == "__main__":
    main()