from src.url_src_downloader import request_download
import requests
import json
import os

forward_path = "."
"""os.path.abspath(os.path.dirname(os.getcwd()))"""


def get_url_from_api(apikey, request_num):
    def get_format(s):
        i = len(s)-1
        while i >= 0:
            if s[i] == '.':
                return s[i:]
            i -= 1

    def if_multi_p(s):
        i = len(s)-1
        while i >= 0:
            if s[i] == '.':
                if s[i-1] != "0":
                    return i-1
                else:
                    return 0
            i -= 1

    def add_url(_url):
        _file = forward_path + "/url_list.txt"
        with open(_file, 'a+', encoding='utf-8') as f:
            f.write(_url + '\n')

    def add_info(ifo, path):
        _content = """pid : %d
link : %s
title : %s
artist : %s
artist_uid : %d
r18 : %s
tags: % s
    """ % (ifo['pid'], ifo['url'], ifo['title'], ifo['author'], ifo['uid'], ifo['r18'], " , ".join(ifo['tags']))
        with open(path, 'w+', encoding='utf-8') as f:
            f.write(_content)

    def find_up(_obj):
        _fd = open(forward_path + "/url_list.txt", 'r')
        _fdl = _fd.readlines()
        _fd.close()
        i = len(_fdl) - 1
        while i >= 0:
            if _obj == _fdl[i] or _fdl[i] == _obj + "\n":
                return True
            i -= 1
        return False

    try_attempt = 0
    while try_attempt < 10:
        try:
            api = 'https://api.lolicon.app/setu/'
            rjs = {
                "apikey": apikey,
                "num": request_num
            }
            rep = requests.get(api, timeout=15, params=rjs)
        except BaseException as exp:
            print(exp, " Try Attempt:", try_attempt+1)
            try_attempt += 1
            if try_attempt < 10:
                continue
            else:
                print("Failed to request the api")
                return
        else:
            break

    print(rep.text)
    jsonstr = json.loads(rep.text)
    get_list = jsonstr['data']

    for info in get_list:
        if find_up(info['url']):
            continue

        print()
        print("URL : ", info['url'])
        pic_url = info['url']
        add_url(pic_url)

        if if_multi_p(pic_url) != 0:
            file_name = str(info['pid']) + "_p" + pic_url[if_multi_p(pic_url)]
        else:
            file_name = str(info['pid'])

        add_info(info, forward_path + "/info/" + file_name + ".txt")
        request_download(forward_path + "/pic/" + file_name + get_format(pic_url), pic_url)


# get_url_from_api("157271265f2bba963bc3d7", 10)
