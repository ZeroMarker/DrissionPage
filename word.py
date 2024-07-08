from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
# 打开文件
with open('selected_columns.csv', 'r', encoding='utf-8') as file:
    # 读取文件内容
    content = file.read()

# 打印文件内容
# print(content)
# 准备文本

stopword_path = 'stopwords.txt'

# 读入 stopword
with open(stopword_path, 'r', encoding='utf-8') as f_stop:
    f_stop_text = f_stop.read()
    f_stop_seg_list = f_stop_text.splitlines()

text = content
# 创建WordCloud对象
font = 'SourceHanSans-Light.ttf'
# 使用jieba进行中文分词
jieba_text = jieba.cut(text, cut_all=False)


# 把文本中的stopword剃掉
my_word_list = []

for my_word in jieba_text:
    if len(my_word.strip()) > 1 and not (my_word.strip() in f_stop_seg_list):
        my_word_list.append(my_word)

my_word_str = ' '.join(my_word_list)

wordcloud = WordCloud(width=1400, height=1400, font_path=font, background_color='black').generate(my_word_str.lower())

# 显示词云
plt.figure(figsize=(16, 16))
#plt.imshow(wordcloud, interpolation='bilinear')
plt.imshow(wordcloud)
plt.axis('off')  # 不显示坐标轴
plt.show()

# 保存词云图片
wordcloud.to_file('wordcloud.png')


