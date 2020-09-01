#!/usr/bin/env python

__author__ = """ Ybrayym Abamov """


import time
import datetime
import os
import signal
import argparse
import logging
import sys


logger = logging.getLogger(__name__)


# globals
exit_flag = False


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be
    mapped here as well (SIGHUP?)
    Basically it just sets a global flag, and main() will exit it's loop
    if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    # log the associated signal name (the python3 way)
    logger.info('Received ' + signal.Signals(sig_num).name)
    global exit_flag
    exit_flag = True


def scan_file(filename, search_text, start_line):
    """ searches filename for magic text starting after start_line """
    with open(filename) as f:
        line_number = 0
        for line_number, text in enumerate(f, 1):
            if line_number >= start_line:
                if search_text in text:
                    logger.info(
                        f'I found the magic text >> \
                        {search_text} on line {line_number} from file \
                        {filename}')
        line_number += 1
    return line_number


def watch_dir(dir_path, polling_interval, file_ext, magic_text):
    """ Analyzation of a directory function """
    # tracker contains files as the keys() and their starting
    # lines as the values()
    tracker = {}
    while not exit_flag:
        time.sleep(polling_interval)
        # add files to tracker dictionary that it does not yet know about
        for f in os.listdir(dir_path):
            if f.endswith(file_ext) and f not in tracker:
                logger.info(f'Watching file {f}')
                tracker[f] = 1
        # remove files from tracker that are no longer in the directory
        for f in list(tracker):
            if f not in os.listdir(dir_path):
                logger.info(f'Unwatching file {f}')
                del tracker[f]
        logger.debug(tracker)
        # scans each file in the tracker dictionary
        for f in tracker:
            new_starting_line_num = scan_file(
                os.path.join(dir_path, f), magic_text, tracker[f])
            tracker[f] = new_starting_line_num


def create_parser():
    """ Making of the parser arguments """
    parser = argparse.ArgumentParser(description="Helps you to monitor DIRs")
    parser.add_argument('-e', '--ext', type=str, default='.txt',
                        help='filter on certain file extensions')
    parser.add_argument('-i', '--int', type=float, default='1.0',
                        help='Specify the polling interval in seconds')
    parser.add_argument('path', help='Directory to be watched')
    parser.add_argument(
        'magic', help='Searched text to be looked for within files')
    parser.add_argument('-l', '--loglevel',
                        help='DEBUG, INFO, WARNING, ERROR, CRITICAL')
    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    print(ns)

    logging.basicConfig(
        level=logging.DEBUG,
        style="{",
        format="{asctime}.{msecs:03f} {name:<12s} {levelname:<8s} {message}",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    if ns.loglevel:
        logger.setLevel(ns.loglevel)
    loglevel = logging.getLevelName(logger.getEffectiveLevel())

    app_start_time = datetime.datetime.now()
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Running {}\n'
        '    Started on {}\n'
        '    Loglevel is {}\n'
        '    Pid is {}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, app_start_time.isoformat(), loglevel, os.getpid())
    )

    # Hook these two signals from the OS ..
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called
    # if OS sends either of these to my process.
    while not exit_flag:
        try:
            watch_dir(ns.path, ns.int, ns.ext, ns.magic)
        except FileNotFoundError:
            logger.error(" The directory doesn't exist")
        except KeyboardInterrupt:
            logger.error("Why would you keyboard interrupt me???")
            break
        except Exception:
            logger.exception('Unhandled exception')
    final_time = datetime.datetime.now() - app_start_time
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Stopped {}\n'
        '    Finished at {}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, str(final_time))
    )
    logging.shutdown()


if __name__ == "__main__":
    main(sys.argv[1:])
