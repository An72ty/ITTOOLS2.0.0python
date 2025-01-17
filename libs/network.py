# -*- coding: utf-8 -*-
import urllib


def networkConnectionCheck(link):
    for timeout in [1, 3, 5]:
        try:
            if not link.startswith('http'):
                link = 'http://' + link
            urllib.request.urlopen(link, timeout=timeout)
            return True
        except:
            return False


def networkCheck():
    try:  # If it raise exception, we have not connection to network
        urllib.request.urlopen("http://google.com")
    except IOError:
        return False
    else:
        return True
