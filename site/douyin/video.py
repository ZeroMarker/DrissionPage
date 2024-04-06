from DrissionPage import ChromiumPage
import douyin

# 创建页面对象，并启动或接管浏览器
page = ChromiumPage()
# 跳转到登录页面
page.get(
    'https://www.douyin.com/user/MS4wLjABAAAAhxiOC0i2u1AeD1OFV0-gmN00vrjmWAgpnR7010_nU_UXkWC5xUn0AI4o2771V28w?vid'
    '=7271565717525302580',
    timeout=10000)

page.scroll.to_bottom()

# 获取页面内的所有p元素
lists = page.ele('@data-e2e=user-post-list')
links = lists.eles('tag:a')

for link in links:
    video = link.attr('href')
    douyin.download(video)
