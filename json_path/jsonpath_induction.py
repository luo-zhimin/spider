# json induction
import json
import jsonpath

# 读取json
store = json.load(open('store.json', 'r', encoding='utf-8'))
# print(store)
# 书店所有书的作者
book_author_list = jsonpath.jsonpath(store, '$.store.book[*].author')
print(book_author_list)

# 所有的作者
author_list = jsonpath.jsonpath(store, '$..author')
print(author_list)

# store的所有元素。所有的books和bicycle
a_list = jsonpath.jsonpath(store, '$.store.*')
print(a_list)

# store里面所有东西的price
price_list = jsonpath.jsonpath(store, '$.store..price')
print(price_list)
