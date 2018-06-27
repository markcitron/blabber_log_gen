#!/usr/bin/python3
""" Calls one or more versions of Blabber log gen (blabber_log_gen.py)
    This script starts a very simple command line interface so that
    you can control the running logs, etc. It also allows you to kill the
    loggers directly without having to kill each process individually """

import argparse, sys
from pathlib import Path

def make_parser():
    """ main argument parser """
    p = argparse.ArgumentParser(description="Starts up one or more faux logs")
    p.add_argument("--log_name", "-n", help="Root name for the logs that are being generated")
    p.add_argument("--num_logs", "-ln", help="How many logs to start up")
    p.add_argument("--log_level", "-l", help="Log level to start, default is INFO")
    return p

def check_args(args):
    """ eval and check passed arguments """
    if not args.num_logs:
        print("blabber> Missing required input: num_logs")
        args.num_logs = input(" | how many loggers to start? ")
        try:
            args.num_logs = int(args.num_logs) + 0
        except:
            args.num_logs = ""
    if not args.log_name:
        args.log_name = "blabber.log"
    if not args.log_level:
        args.log_level = "INFO"
    return args

def check_file(filename, fail_if_missing):
    """ checks to make sure that a required file is present. """
    if Path(filename).is_file():
        return True
    else:
        if fail_if_missing:
            print("Fatal Error: missing required file {0}, exiting.".format(filename))
            sys.exit(1) 
        else: 
            return False

def all_done():
    """ all done, shut down the loggers """
    print("blabber> shutting down ...")
    sys.exit(1)

def show_commands():
    """ Show all commands """
    print(" | A - Add a logger")
    print(" | K - Kill one or more active logs")
    print(" | Q - Quit")
    print(" | S - Status of current loggers")
    print(" | ? - Show this menu")
    return True

def kill_logger():
    return True

def status():
    return True

def add_logger():
    return True

def process_input(user_input):
    """ Process inputs """
    commands = {
        "a": add_logger,
        "?": show_commands,
        "k": kill_logger,
        "q": all_done,
        "s": status
    }
    func = commands.get(user_input, lambda: "invalid option")
    func()
    return True

def main():
    """ Main function """
    # Starting up
    print("----------------------------------------------")
    print("              Blabber_log_gen")
    print("----------------------------------------------")
    # Parse args
    passed_args = make_parser().parse_args()
    args = check_args(passed_args)

    # log_generator
    lg_script = "blabber_log_gen.py"
    check_file(lg_script, True)

    # start up loggers
    for i in range(int(args.num_logs)):
        start_logger_command = "{0} -n {1} -l {2} -i {3}".format(lg_script, args.log_name, args.log_level, i+1)
        print(" | starting log: {0}_{1} with command: {2}".format(i, args.log_name, start_logger_command))

    # main command line loop
    while True:
        user_input = input("blabber> ")
        process_input(user_input.lower())
        user_input = ""

    # all done
    return True

if __name__ == "__main__":
    main()
