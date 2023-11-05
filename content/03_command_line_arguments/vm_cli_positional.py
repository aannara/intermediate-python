import argparse
import pprint


def main(argv = None):
    parser = argparse.ArgumentParser()
    
    # positional
    parser.add_argument("vm_name", help="Name of virtual machine to be created")
    # help (can be accessed by --help)
    
    args = parser.parse_args(argv)
    
    pprint.pprint(vars(args))
    

if __name__ == "__main__":
    main()