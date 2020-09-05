# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:07:47 2020

"""

from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from collections import Counter

# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	cut_text = word_tokenize(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

# 数据加载
data = pd.read_csv(r"C:\Users\yy\Desktop\BI\L2\作业\WordCould_MarketBasket\Market_Basket_Optimisation.csv", sep="\t", header=None)

# 读取商品字段
items = data.iloc[:,0]


# 方法1：按照课堂案例的方式绘制图云（wc.generate()）
all_word = ",".join(items)   # 把所有商品合成一个整体
create_word_cloud(all_word)


# 方法2：考虑像mineral water这类由多个单词构成的商品名，可能分词时会被分开，使用“_”处理
all_word2 = all_word.replace(" ", "_")
all_word2 = all_word2.replace(",", " ")
create_word_cloud(all_word2)


# 方法3：使用wc.generate_from_frequencies()
transactions = all_word.split(sep=',')
counts = Counter(transactions)

wc = WordCloud(
	max_words=100,
	width=2000,
	height=1200,
    )
wordcloud = wc.generate_from_frequencies(counts)
plt.imshow(wordcloud)   # 显示词云文件
plt.axis("off")
plt.show()


# 输出销量前10名的商品及销量
i = 1
for k,v in sorted(counts.items(), key=lambda x:x[1], reverse=True):
    print("销售第{}名的商品是{}，销量为{}。".format(i,k,v))
    if i >= 10:
        break
    i += 1
