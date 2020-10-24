#!/usr/bin/python3

# Standard libraries.
import argparse
import csv
import json
import logging
import os
import textwrap

# Third party libraries.
# If these are missing, try running the command provided to install them.
import colorlog  # python -m pip install colorlog
import tweepy as tw  # python -m pip install tweepy

# Setup the colored error message logger.
logger = logging.getLogger(__file__)
logger.setLevel(colorlog.colorlog.logging.WARNING)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)

# Set up the argument parser.
parser = argparse.ArgumentParser(
    description=(
        "Given a Tweet snowflake, "
        "print to stdout a JSON file of everything the Tweet API exposes."
    )
)

parser.add_argument(
    "snowflake",
    type=str,
    nargs=1,
    help="The snowflake part of `https://twitter.com/username/status/snowflake`.",
)

parser.add_argument(
    "-v",
    "--verbose",
    action="count",
    help=(
        "Verbose mode; print error messages too."
        " More `v`s for more verbosity; `-v` = "
        "critical errors only; `-vvvvv` = "
        "debug mode."
    ),
)

# Some os and os.path nonsense.
pwd = os.path.dirname(os.path.abspath(__file__))


def set_verbosity(args):
    """Set the global logger debug level."""
    if args.verbose is None:
        logger.disabled = True
        return None
    elif args.verbose == 1:
        return logger.setLevel(colorlog.colorlog.logging.CRITICAL)
    elif args.verbose == 2:
        return logger.setLevel(colorlog.colorlog.logging.ERROR)
    elif args.verbose == 3:
        return logger.setLevel(colorlog.colorlog.logging.WARNING)
    elif args.verbose == 4:
        return logger.setLevel(colorlog.colorlog.logging.INFO)
    elif args.verbose >= 5:
        return logger.setLevel(colorlog.colorlog.logging.DEBUG)
    else:
        return None


if __name__ == "__main__":
    args = parser.parse_args()
    set_verbosity(args)
    logger.critical("Verbose mode enabled.")

    snowflake = str(args.snowflake[0])
    logger.info("Snowflake passed: {:>40}".format(snowflake))

    logger.info("Loading in whatever's in `.env` right now.")
    with open(".env", "r") as csvfile:
        auth_reader = csv.reader(csvfile)
        for row in auth_reader:
            globals()[row[0]] = row[1]

    for data in [consumer_key, consumer_secret, access_token, access_token_secret]:
        if len(data) == 0:
            logger.warning("A string in `.env` is empty.")

    logger.debug("Authentication data should be loaded in now, let's check:")
    logger.debug("consumer_key = {:>40}".format(consumer_key))
    logger.debug("consumer_secret = {:>40}".format(consumer_secret))
    logger.debug("access_token = {:>40}".format(access_token))
    logger.debug("access_token_secret = {:>40}".format(access_token_secret))

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = tw.API(auth)

    logger.info("Authenticated with your user data in `.env`.")
    logger.info("Okay, getting who liked the status...")

    tweet = auth_api.statuses_lookup([snowflake])[0]
    logger.debug(tweet)

    if args.json:
        with open("tweet.json", "w") as file:
            json.dump(tweet._json, file, indent=4)

    logger.debug("{} favorites on this tweet.".format(tweet.favorite_count))
