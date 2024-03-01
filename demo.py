from DrissionPage import ChromiumPage

# 创建页面对象，并启动或接管浏览器
page = ChromiumPage()
# 跳转到登录页面
page.get('https://114.242.246.235:1443/imedical/web/csp/dhc.logon.csp')

# 定位到账号文本框，获取文本框元素
ele = page.ele('#USERNAME')
# 输入对文本框输入账号
ele.input('demo')
# 定位到密码文本框并输入密码
page.ele('#PASSWORD').input('1')
# 点击登录按钮
page.ele('@id=Logon').click()
page.ele('@id=Logon').click()

page.ele('@class=clickactive').click()
