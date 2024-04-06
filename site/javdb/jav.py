from DrissionPage import ChromiumPage
from DataRecorder import Recorder

# 创建页面对象，并启动或接管浏览器
page = ChromiumPage()
# 跳转到登录页面
# page.get('https://javdb.com/actors/GgVz?t=s&sort_type=2')
page.get('https://javdb.com/actors/Y3MD?t=s,d&sort_type=0')

base = "https://javdb.com"

sort_type = {"More recent": 0, "Top Rated": 1, "More Viewed": 2, "More watch to watch": 3, "More watched": 4}

t = {"Individual works": "s", "Downloadable": "d", "Playable": "p"}

actor_name = "/Y3MD"
actor = "/actor"

movie = "/v"
movie_title = "123"

page_number = 2

url = base + actor + actor_name + page_number
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
    # 请求歌曲url 获取歌手姓名
    # page.get(music_url)
    # music_singer = page.ele('xpath://p[@class="des s-fc4"]/span').text
    # print(music_ranking,music_title,music_singer)

    # 写入到记录器
    recorder.add_data((rank, title, href))

recorder.record()
