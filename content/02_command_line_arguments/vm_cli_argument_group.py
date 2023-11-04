import argparse
import pprint


def main(argv=None):
    parser = argparse.ArgumentParser()
    cpu_parser = parser.add_argument_group("cpu")
    memory_parser = parser.add_argument_group("memory")
    extras_parser = parser.add_argument_group("extras")

    # positional
    parser.add_argument("vm_name", help="Name of virtual machine to be created")
    # help (can be accessed by --help)
    # optional (short vs long)
    # optional with default and types
    # type check
    cpu_parser.add_argument(
        "-c",
        "--cpu",
        type=int,
        default=4,
        help="Number of cpu to use. Default to %(default)s cores",
    )
    memory_parser.add_argument(
        "-m",
        "--memory",
        type=int,
        default=8,
        help="Amount of memory to use in GB. Default to %(default)s GB",
    )

    # count
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Amount of verbosity in log."
    )

    # flag or boolean
    extras_parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force creation without confirmation.",
    )

    # append
    extras_parser.add_argument(
        "-t",
        "--tags",
        action="append",
        default=[],
        help="Tags for the VM (can be specified multiple times).",
    )

    # choice
    extras_parser.add_argument(
        "--vm-type",
        choices=["linux", "windows"],
        required=True,
        help="Type of VM (linux or windows).",
    )

    args = parser.parse_args(argv)

    pprint.pprint(vars(args))


if __name__ == "__main__":
    main()
