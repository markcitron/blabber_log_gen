#!/usr/bin/python3
""" Blabber log gen - This script will generate one or more sample logs
    This script is called from the start_blabber.py so that it will
    clean up any logs started, etc.  If you start the logs directly from
    here you can kill the log with cntl-c or whatever :-)

    The log generator purposely generates an error so that you can have an
    error to trigger off of (if needed).
    """

import logging, argparse, time

def make_parser():
    """ Create a parser to parse arguments """
    p = argparse.ArgumentParser(description="")
    p.add_argument("--log_name", "-n", help="Name of log to create.  If multiple logs, log number will be appended to this name.")
    p.add_argument("--log_level", "-l", help="")
    p.add_argument("--log_id", "-i", help="This is used to differentiate multiple logs.")
    return p

def check_args(args):
    """ eval and check arguments """
    if not args.log_name:
        args.log_name = "blabber.log"
    if not args.log_level:
        args.log_level = "INFO"
    return args

def log_text(pointer):
    """ sample text to log -- love this poem -- recited it in 2nd grade :-) """
    logging.debug("Request for line: {0}".format(pointer))
    lt = [ 
        "Twas brillig, and the slithy toves ", 
        "    Did gyre and gimble in the wabe: ", 
        "All mimsy were the borogoves, ", 
        "    And the mome raths outgrabe. ", 
        "", 
        "Beware the Jabberwock, my son! " ,
        "    The jaws that bite, the claws that catch! " ,
        "Beware the Jubjub bird, and shun " ,
        "    The frumious Bandersnatch! " ,
        "",
        "He took his vorpal sword in hand; " ,
        "    Long time the manxome foe he sought— " ,
        "So rested he by the Tumtum tree " ,
        "    And stood awhile in thought. " ,
        "", 
        "And, as in uffish thought he stood, " ,
        "    The Jabberwock, with eyes of flame, " ,
        "Came whiffling through the tulgey wood, " ,
        "    And burbled as it came! " ,
        "", 
        "One, two! One, two! And through and through " ,
        "    The vorpal blade went snicker-snack! " ,
        "He left it dead, and with its head " ,
        "    He went galumphing back. " ,
        "", 
        "“And hast thou slain the Jabberwock? ",
        "    Come to my arms, my beamish boy! ", 
        "O frabjous day! Callooh! Callay!” ",
        "    He chortled in his joy. ",
        "", 
        "Twas brillig, and the slithy toves ", 
        "    Did gyre and gimble in the wabe: ",
        "All mimsy were the borogoves, ",
        "    And the mome raths outgrabe."
    ] 
    return lt[pointer]

def main():
    """ Main function """
    # parse args
    passed_args = make_parser().parse_args()
    args = check_args(passed_args)

    # start logging
    logname = args.log_name
    if args.log_id: 
        logname = "{0}_{1}".format(args.log_id, args.log_name)
    loglevel = args.log_level
    logging.basicConfig(filename=logname, level=loglevel, format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info("Started sample log: {0}".format(args.log_name))

    lc = 0
    while True:
        try:
            logging.debug("Getting line: {0}".format(lc))
            next_line = log_text(lc)
            logging.info(next_line)
            lc = lc + 1
        except (KayboardInterupt):
            print("Keyboard Interupt, stopping ...")
        except Exception as e:
            logging.error("expected: {0}".format(str(e)))
            lc = 0
        logging.debug("Sleeping one second.")
        time.sleep(1)


if __name__ == "__main__":
    main()
