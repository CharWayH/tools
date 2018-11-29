"""
1.关键字抓取
2.关键字替换
"""
from flashtext import KeywordProcessor
keyword_processor = KeywordProcessor()

# 1.Extract keywords:
# keyword_processor.add_keyword(<unclean name>, <standardised name>)

keyword_processor.add_keyword('Big Apple')      # 抓取的关键字1
keyword_processor.add_keyword('Bay Are')        # 抓取的关键字2
keywords_found = keyword_processor.extract_keywords('I love Big Apple and Bay Area.')

print(keywords_found)

# 2.Replace keywords:
keyword_processor.add_keyword('New Delhi', 'NCR region')    # @1需被替换的关键字，@2替换后的关键字。不区分大小写
new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.')    #

print(new_sentence)