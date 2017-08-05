import xlrd
import jieba
import numpy
import codecs
import pandas
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = codecs.open("C:\\周杰伦所有歌词.txt",'r','utf-8')
content = file.read()
file.close()
segments = []
segs = jieba.cut(content)
for seg in segs:
    if len(seg)>1:
        segments.append(seg)
segmentDF = pandas.DataFrame({'segment':segments})
df = segmentDF.groupby("segment")["segment"].agg({"计数":numpy.size}).reset_index().sort(columns = ['计数'],ascending = False)
print(df.head(100))
df.to_excel('周杰伦所有歌词-分词.xls', sheet_name='sheet1')
