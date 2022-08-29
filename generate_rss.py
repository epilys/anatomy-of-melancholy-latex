#!/python3
# -*- coding: utf-8 -*-
import sys
import uuid
from datetime import datetime, timezone
from feedgen.feed import FeedGenerator

website_url = "https://epilys.github.io/anatomy-of-melancholy-latex/"
author_email = "manos@pitsidianak.is"
author_name = "epilys"
LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo

first_entry = {
    "title": "Latest draft url",
    "date": "2021-05-20T16:26:48.140230",
    "content": "The latest published draft can be accessed from the url https://epilys.github.io/anatomy-of-melancholy-latex/aom_latest.pdf",
}
second_entry = {
    "title": "New draft url",
    "date": "2022-08-29T19:51:48.140230",
    "content": "After a year long break, I've updated the draft. This leaves only the third partition lacking some minimal content, and then only editing and typesetting details need to be finished. The latest published draft can be accessed from the url https://epilys.github.io/anatomy-of-melancholy-latex/aom_latest.pdf",
}
third_entry = {
    "title": "Github repository is now public",
    "date": "2022-08-29T20:08:48.140230",
    "content": "Forgot to mention in last post, that the github repository is now public. You can inspect it at https://github.com/epilys/anatomy-of-melancholy-latex",
}


def make_guuid(title):
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, title))


def add_entry(feed, entry):
    fe = feed.add_entry()
    fe.id(website_url + "#" + make_guuid(entry["title"]))
    fe.title(entry["title"])
    fe.content(entry["content"])
    d = datetime.fromisoformat(entry["date"])
    d = d.replace(tzinfo=LOCAL_TIMEZONE)
    fe.published(d)
    fe.link(href=website_url, rel="alternate")


def main():
    fg = FeedGenerator()
    fg.id(website_url)
    fg.title('"The Anatomy Of Melancholy" (1621) by Robert Burton in XeLaTeX')
    fg.author({"name": author_name, "email": author_email})
    fg.link(href=website_url, rel="alternate")
    fg.rights("cc-by")
    fg.subtitle("")
    fg.description(
        u"A free/libre project to create a new modern edition for 'Anatomy of Melancholy'."
    )
    fg.link(href=website_url + "feed.atom", rel="self")
    fg.language("en")
    add_entry(fg, first_entry)
    add_entry(fg, second_entry)
    add_entry(fg, third_entry)

    fg.generator("", "x", uri="")
    fg.atom_file("feed.atom")
    fg.rss_file("feed.rss")


if __name__ == "__main__":
    main()
