# tweet2json

```bash
$ python tweet2json.py -h
usage: tweet2json.py [-h] [-v] snowflake

Given a Tweet snowflake, print to stdout a JSON file of everything the Tweet
API exposes. (Requires API keys in `.env`.)

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

# Example output

`$ python tweet2json.py 1247616214769086465 | pbcopy` copies the following to the clipboard:

```json
{
    "created_at": "Tue Apr 07 20:04:19 +0000 2020",
    "id": 1247616214769086465,
    "id_str": "1247616214769086465",
    "text": "I\u2019m moving $1B of my Square equity (~28% of my wealth) to #startsmall LLC to fund global COVID-19 relief. After we\u2026 https://t.co/TtdU7W4SWk",
    "truncated": true,
    "entities": {
        "hashtags": [
            {
                "text": "startsmall",
                "indices": [
                    58,
                    69
                ]
            }
        ],
        "symbols": [],
        "user_mentions": [],
        "urls": [
            {
                "url": "https://t.co/TtdU7W4SWk",
                "expanded_url": "https://twitter.com/i/web/status/1247616214769086465",
                "display_url": "twitter.com/i/web/status/1\u2026",
                "indices": [
                    116,
                    139
                ]
            }
        ]
    },
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
        "id": 12,
        "id_str": "12",
        "name": "jack",
        "screen_name": "jack",
        "location": "",
        "description": "#bitcoin",
        "url": null,
        "entities": {
            "description": {
                "urls": []
            }
        },
        "protected": false,
        "followers_count": 4953541,
        "friends_count": 4533,
        "listed_count": 27887,
        "created_at": "Tue Mar 21 20:50:14 +0000 2006",
        "favourites_count": 30432,
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": true,
        "verified": true,
        "statuses_count": 27252,
        "lang": null,
        "contributors_enabled": false,
        "is_translator": false,
        "is_translation_enabled": false,
        "profile_background_color": "EBEBEB",
        "profile_background_image_url": "http://abs.twimg.com/images/themes/theme7/bg.gif",
        "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme7/bg.gif",
        "profile_background_tile": false,
        "profile_image_url": "http://pbs.twimg.com/profile_images/1115644092329758721/AFjOr-K8_normal.jpg",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1115644092329758721/AFjOr-K8_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/12/1584998840",
        "profile_link_color": "990000",
        "profile_sidebar_border_color": "DFDFDF",
        "profile_sidebar_fill_color": "F3F3F3",
        "profile_text_color": "333333",
        "profile_use_background_image": true,
        "has_extended_profile": true,
        "default_profile": false,
        "default_profile_image": false,
        "following": false,
        "follow_request_sent": false,
        "notifications": false,
        "translator_type": "regular"
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "is_quote_status": false,
    "retweet_count": 69876,
    "favorite_count": 322373,
    "favorited": false,
    "retweeted": false,
    "possibly_sensitive": false,
    "lang": "en"
}
```
