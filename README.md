# tweet2json

```bash
$ python tweet2json.py -h
usage: tweet2json.py [-h] [-v] snowflake

Given a Tweet snowflake, print to stdout a JSON file of everything the Tweet
API exposes.

positional arguments:
  snowflake      The snowflake part of
                 `https://twitter.com/username/status/snowflake`.

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Verbose mode; print error messages too. More `v`s for more
                 verbosity; `-v` = critical errors only; `-vvvvv` = debug
                 mode.
$ 

```

# Quickstart

Clone this repo.

Put your tokens in [`.env.example`](./.env.example) and rename it to `.env`. If you need help finding your tokens, try <https://developer.twitter.com/en/apps/>. _Reason: `.env` is ignored by `.gitignore`. The rename prevents you from worrying about accidentally `git push`ing your tokens._

Get the last part of the Tweet URL, for example, the `1247616214769086465` in `https://twitter.com/jack/status/1247616214769086465`.

Run `python tweet2json.py 1247616214769086465`.

## 
