from DrissionPage import ChromiumPage


def download(video):
    # 创建页面对象，并启动或接管浏览器
    page = ChromiumPage()
    # 跳转到登录页面
    page.get('https://snaptik.app/')

    # 定位到账号文本框，获取文本框元素
    ele = page.ele('#url')
    # 输入对文本框输入账号
    ele.input(video + '\n')
    page.ele('@class=button download-file').click()

# download('https://www.douyin.com/video/7338425553499737396')
