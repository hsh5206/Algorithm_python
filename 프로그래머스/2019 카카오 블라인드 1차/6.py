# 매칭점수

from operator import indexOf
import re


def solution(word, pages):
    answer = 0
    pages_info = []
    for i, page in enumerate(pages):
        temp = list(seperate(word, page)) + [0, i]
        pages_info.append(temp)
    for page in pages_info:
        url, basic_score, link_num, links, link_score, index = page
        for link in links:
            for page in pages_info:
                if link == page[0]:
                    page[4] += basic_score / link_num
    pages_info.sort(key=lambda x: -(x[1]+x[4]))
    return pages_info[0][5]


def seperate(word, page):
    basic_score = 0
    for f in re.findall(r'[a-zA-Z]+', page.lower()):
        if f == word.lower():
            basic_score += 1
    url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
    external_links = re.findall('<a href="(https://[\S]*)"', page)
    external_links_num = len(external_links)

    return url, basic_score, external_links_num, external_links


print(solution('blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
      "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
