import re
from collections import defaultdict


path = 'C:\\Users\\ttft3\\Downloads\\bookmarks_5_20_24.html'

# 打开文件并读取全部内容
with open(path, 'r', encoding='utf-8') as file:
    content = file.read()
    # print(content)

text = content
# 正则表达式，用于匹配网址中的域名
domain_regex = r'https?://(?:www\.)?([^/]+)/?'

# 使用defaultdict来自动初始化计数为0
domain_count = defaultdict(int)

# 找到所有匹配的域名
domains = re.findall(domain_regex, text)

# 统计每个域名出现的次数
for domain in domains:
    domain_count[domain] += 1

# 打印结果
"""
for domain, count in sorted(domain_count.items(), key=lambda item: item[1], reverse=True):
    print(f"{domain}: {count}")
"""

# 按出现次数从大到小排序
sorted_domains = sorted(domain_count.items(), key=lambda item: item[1], reverse=True)

# 输出结果到文件
output_path = 'domain_counts.txt'
with open(output_path, 'w', encoding='utf-8') as output_file:
    for domain, count in sorted_domains:
        output_file.write(f"{domain}: {count}\n")

print(f"Domain counts have been written to {output_path}")

