#coding:utf-8
import re
import unicodedata
import jieba
from slugify import slugify
import pypinyin
import sys

re_en = re.compile(r'([a-zA-Z\']+)')
re_all_en = re.compile(r'^([a-zA-Z\']+)$')
re_chinese = re.compile(r'(['+u'\u2e80-\u9fff'+r']+)')
re_all_chinese = re.compile(r'^(['+u'\u2e80-\u9fff'+r']+)$')

if sys.version_info[0] >= 3:
    unicode = str

def chinese_slugify(text, delimiter=u"-"):
    if not type(text) == unicode:
        raise ValueError('should be unicode')
    slug_list = []
    segments_split_by_space = text.split()
    segments_split_by_chinese = []
    for segment in segments_split_by_space:
        segments_split_by_chinese.extend(re_chinese.split(segment))
    for segment in segments_split_by_chinese:
        if not segment:
            continue
        segment = segment.strip()
        if not segment:
            continue
        elif re_all_en.match(segment):
            slug_list.append(segment)
        elif re_all_chinese.match(segment):
            sig_list = jieba.cut(segment, cut_all=False)
            for sig in sig_list:
                arr_pinyin = sum(pypinyin.pinyin(sig, pypinyin.NORMAL), [])
                pinyin = "".join([pinyin.capitalize()
                                  for pinyin in arr_pinyin])
                slug_list.append(pinyin)
        else:
            slug_list.append(slugify(segment))
    slugged = delimiter.join(slug_list)
    slugged = unicode(
        unicodedata.normalize('NFKD', slugged).encode('ascii', 'ignore').decode()
    )
    slugged = re.sub(
        r"[^\w\s%s']" % re.escape(delimiter),
        '',
        slugged
    ).strip()
    slugged = re.sub(r'[%s\s]+' % delimiter, delimiter, slugged)
    return unicode(slugged)
