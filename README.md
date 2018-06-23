# Reddit Chess Bot

Reddit Bot created using PRAW that attempts to find professional chess games with a provided FEN input. 

## How to use it
To call the bot in any comment thread, simply use the command:

```
!FENFinder [Insert FEN here]
```

An example of a **valid** command:

```
!FENFinder rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1
```

An example of an **invalid** command:

```
!FENFinder rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR
```

It's important to include the __entire__ FEN with the command. Do not attempt to trim the FEN code as this will result in an error.

## What it looks like

You can view the bot's account [here](https://reddit.com/user/FENFinderBot).

![Demo of Chess Bot in action.](https://i.imgur.com/Gqw9k0q.png)

## Built With

* [PRAW: The Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/) - Reddit API
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Web Scraping

