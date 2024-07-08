from DrissionPage import ChromiumPage
from DataRecorder import Recorder
from enum import Enum


class T(Enum):
    Playable = 'p'
    Single = 's'
    Downloadable = 'd'
    Caption = 'c'


class SortType(Enum):
    More_recent = 0
    Top_Rated = 1
    More_Viewed = 2
    More_watch_to_watch = 3
    More_watched = 4


class F(Enum):
    All = 'all'
    Code = 'code'
    Actor = 'actor'


base = "https://javdb.com"
actor_name = "/Y3MD"
actor = "/actors"

search = '/search'
movie = "/v"
movie_title = "123"

option = ','.join([t.value for t in [T.Single, T.Downloadable]])

sort_type = SortType.More_recent.value

params = []
page_num = 4
if page_num:
    params.append('page=' + str(page_num))

if option:
    params.append('t=' + option)

if sort_type:
    params.append('sort_type=' + str(sort_type))

query = []
q = 'julia'
if q:
    query.append('q=' + q)
f = F.All.value
if f:
    query.append('f=' + f)

# url = base + actor + actor_name + '?' + '&'.join(query)

url = base + search + '?' + '&'.join(query)

# 创建页面对象，并启动或接管浏览器
page = ChromiumPage()

# page.get('https://javdb.com/actors/GgVz?t=s&sort_type=2')
# https://javdb.com/actors/1ERn?t=s,d&sort_type=0
# https://javdb.com/actors/1ERn?page=3&sort_type=0&t=s%2Cd
# page.get('https://javdb.com/actors/Y3MD?t=s,d&sort_type=0')
# https://javdb.com/search?q=julia&f=all
page.get(url)

# 年龄确认
# page.ele('@class=is-success').click()
# 定位到账号文本框，获取文本框元素
# ele = page.ele('#email')
# 输入对文本框输入账号
# ele.input('u78k4l67@gmail.com')
# 定位到密码文本框并输入密码
# page.ele('#password').input('010501chl')
# 点击登录按钮
# page.ele('@value=Sign in').click()

"""
https://blog.csdn.net/weixin_49184448/article/details/134684160
【爬虫】爬取网易云音乐热歌榜
"""
# 创建记录器对象
recorder = Recorder('data.csv')

# 遍历页面上所有 li 元素 获取热歌榜Top200的歌名和url
for index, a in enumerate(page.eles('xpath://div[@class="item"]/a')):
    rank = index + 1  # 排名
    # music_title = a.ele('tag:a').text
    title = a.attr('title')
    href = a.attr('href')
    """
    # 请求歌曲url 获取歌手姓名
    # page.get(music_url)
    # music_singer = page.ele('xpath://p[@class="des s-fc4"]/span').text
    # print(music_ranking,music_title,music_singer)
    """

    # 写入到记录器
    recorder.add_data((rank, title, href))

recorder.record()
