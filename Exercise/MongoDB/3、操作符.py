# -*- coding:utf-8 -*-
''''''
'''
    比较操作符：
        
        * $gt  ------ greater than 大于 
        * $lt  ------ less than 小于 
        * $gte ------ greater than equal 大于等于 
        * $lte ------ less than equal 小于等于 
        * $eq  ------ equal  等于
        * $ne  ------ not equal 不等于 
        * $in  ------ in 在范围内 
        * $nin ------ not in 不在范围内 
        

    功能符号：
    
        * $NOT    ------  not 非
        * $OR     ------  or 或
        * $mod    ------  Modulo 数字模操作
        * $regex  ------   Regex 匹配正则表达式 
        * $exists ------  exists 属性是否存在 
        * $type   ------  type 类型判断 
        * $where  ------  where高级条件查询 
        
        * $text   ------  text 文本搜索功能
            - MongoDB支持对文本内容执行文本搜索操作，其提供了索引text index和查询操作$text
            来完成文本搜索功能。
            如：
            
                # 设置name字段的 text 索引
                db.students.ensureIndex({'name':'text'})
                # 执行搜索时，会搜索name字段中的文本中包含feng的人
                db.students.find({'$text':{'$search':'feng'}})
        
        * $unset  ------ 删除属性
        
            - db.collection.update({'name':'huahua'},{'$unset':{'age':123}})
            _ 删除name 是huahua 数据中的 age属性，后边的值无所谓是多少
        
'''

import pymongo, time

sqls = {

    # 查询年龄大于20 的人
    'gt': {'age': {'$gt': 20}},

    # 查询年龄小于 20 的人
    'lt': {'age': {'$lt': 20}},

    # 查询年龄大于等于 20 的人
    'gte': {'age': {'$gte': 20}},

    # 查询年龄 小于等于20 的人
    'lte': {'age': {'$lte': 20}},

    # 查询年龄不等于20的人
    'ain': {'age': {'$ne': 20}},

    # 查询年龄等于20 或者 23 的人
    'nin': {'age': {'$in': [20, 23]}},

    # 查询年龄不等于20 或 23 的人
    'ne': {'age': {'$nin': [20, 23]}},

    # 查询年龄 > 20 且 <= 30
    'gtle': {'age': {'$gt': 20, '$lte': 30}},

    # 年龄MOD 5等于3
    'mod': {'age': {'$mod': [5, 3]}},

    # 年龄MOD 5不等于3的人
    'notmod': {'age': {'$not': {'$mod': [5, 3]}}},

    # 查询年龄等于20 或 等于23 的人
    # 等价于使用 $in 符号 {'age': {'$in': [20, 23]}}
    'aor': {"$or": [{"age": 20}, {"age": 23}]},

    # 查找name以M开头的人
    'regex': {'name': {'$regex': '^M.*'}},

    # 查找存在name属性的人
    'exists': {'name': {'$exists': True}},

    # 查找age的值的类型为int
    'atype': {'age': {'$type': 'int'}},

    # 查找粉丝数等于关注数的
    'swhere': {'$where': 'obj.fans_count == obj.follows_count'}
}

collection = None

def creatCollection():
    global collection
    conn = pymongo.MongoClient(host='localhost', port=27017)
    db = conn.test
    collection = db.students

def execSql(k,v):
        results =  collection.find(v)
        for s in results:
            print(s)



if __name__ == '__main__':

    creatCollection()

    for k,v in sqls.items():
        print(k, v)
        execSql(k, v)

    collection.ensureIndex({'name': 'text'})
    execSql('stext', {'$text': {'$search': 'feng'}})

    # 删除name 是huahua 数据中的 age属性，后边的值无所谓是多少
    collection.update({'name':'huahua'},{'$unset':{'age':123}})
