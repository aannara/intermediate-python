import argparse
import pprint


def main(argv = None):
    parser = argparse.ArgumentParser()
    
    # positional
    parser.add_argument("vm_name", help="Name of virtual machine to be created")
    # help (can be accessed by --help)
    # optional (short vs long)
    # optional with default and types
    # type check
    parser.add_argument("-c", "--cpu", type=int, default=4, help="Number of cpu to use. Default to %(default)s cores")
    parser.add_argument("-m", "--memory", type=int, default=8, help="Amount of memory to use in GB. Default to %(default)s GB")
    
    args = parser.parse_args(argv)
    
    pprint.pprint(vars(args))
    

if __name__ == "__main__":
    main()