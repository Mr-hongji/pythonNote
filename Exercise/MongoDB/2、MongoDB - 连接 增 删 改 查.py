# -*- coding:utf-8 -*-
''''''

import pymongo
from bson.objectid import ObjectId

client = None
db_name = "test"
conn_host = "localhost"
conn_port = 27017
db = None
collection_name = 'students'



def getConn():
    ''''''
    '''
        创建一个MongoDB的连接对象
        
            * 连接 MongoDB 我们需要使用 PyMongo 库里面的 MongoClient
            * 端口不传默认是27017
            * MongoClient 的第一个参数 host 还可以直接传 MongoDB 的连接字符串，以mongodb开头
            
            * 创建方式：
        
                - 这样 client = pymongo.MongoClient(host = 'localhost', port = 27017)
                  或
                - 这样 client = MongoClient('mongodb://localhost:27017/') 

    
        指定数据库
        
            * MongoDB中还分为一个个数据库，创建完MongoDB的连接对象后，还需要指定要操作哪个数据库。
            
            * 例：指定test数据库
            
                - 这样  db = client.test
                   或
                - 这样  db = client.['test']
        
    '''
    global db,client
    # 连接mongodb (获取MongoDB 的连接对象)
    client = pymongo.MongoClient(host = conn_host, port = conn_port)
    # 连接（指定）数据库
    db = client.test1
    # 权限验证
   # db.authenticate('username', 'password')




# 判断数据库是否已存在
def checkDBWhetherThere():
   dblist = client.database_names()
   if db_name in dblist:
       print('数据库 %s 已存在！' %db_name)


# 判断集合是否已存在
def checkCollectionWhetherThere():
    collist = db.collection_names()
    if collection_name in collist:
        print("集合已存在！")


# 增
def insert_data():

    ''''''
    '''
        MongoDB的每个数据库又包含了许多集合Collection，类似于关系型数据库中的表。
        
        插入数据前需要指定要操作的集合（也可理解为要操作的表）
        
        指定一个集合名称为 students，学生集合。
        
        指定集合方式：
        
            这样 collection = db['students'] 
            或
            这样 collection = db.students
            
    ----------------------------------------------------------------------------------------
        
        在MongoDB中，每条数据其实都有一个_id属性来唯一标识，如果数中没有_id属性，
        MongoDB会自动产生一个ObjectId类型的_id属性（时间戳 + 机器码）。
        
        插入数据方式：
            
            * insert()（Python3 中不建议使用了）
                - 可插入单条，也可插入多条
                
            * insert_one() 和 insert_many()（Python3 中推荐使用）
                - insert_one() 插入单条数据 
                - insert_many() 插入多条数据
                
        循环插入数据
                方式一（需要执行 2000 次insert语句，性能差）：
                    for (var i = 1; i <= 2000; i++){
                        db.numbers.insert({'num': i})
                    }
                
                方式二：
                    var arr = []

                    for(var i = 1; i <= 20000; i++){
                        arr.push({'num':i})
                    }
                    
                    db.numbers.insert(arr)
    '''

    # 指定集合
    collection = db.students

    student1 = {'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
    student2 = {'id': '20170206', 'name': 'Mike', 'age': 21, 'gender': 'male'}
    student3 = {'id': '20170209', 'name': 'QuYang', 'age': 21, 'gender': 'male'}
    student4 = {'id': '20170210', 'name': 'Ming', 'age': 22, 'gender': 'male'}
    student5 = {'id': '20170211', 'name': 'Dog', 'age': 22, 'gender': 'male'}
    student6 = {'id': '20170212', 'name': 'Hongji', 'age': 21, 'gender': 'male'}
    student7 = {
        'name': "xiaoxiao",
        'age': 23,
        'favorites': {'artist': "Noguchi", 'food': "nougat",'movies':['mA','mB']}
    }
    student8 = {
            'name': "huahua",
            'age': 25,
            'favorites': {'food': "pizza", 'artist': "Picasso", 'movies': ['mC','mD']}
        }

    # 插入单条数据
    result = collection.insert(student1) # insert()方法会在执行后返回的_id值
    print(result)  # 5b488e5ca1be812e884589ec

    # 插入多条数据
    result = collection.insert([student2,student3])
    print(result) # [ObjectId('5b48907ea1be8136fc5fdeda'), ObjectId('5b48907ea1be8136fc5fdedb')]

    # insert_one()方法
    result = collection.insert_one(student4) # 返回的是InsertOneResult对象，调用 inserted_id 属性获取_id
    print(result) # <pymongo.results.InsertOneResult object at 0x0000000002E7EA88>

    # insert_many()方法
    result = collection.insert_many([student5, student6]) # 返回的是InsertOneResult对象，调用 inserted_id 属性获取_id
    print(result) # <pymongo.results.InsertManyResult object at 0x0000000002E7E848>
    print(result.inserted_ids) # [ObjectId('5b48931aa1be8137682569c2'), ObjectId('5b48931aa1be8137682569c3')]

    db.students.insert_many([student7, student8])



# 删
def del_data():
    ''''''
    '''
        
        删除数据方式：
        
            remove({query}, justOne)：
             
                * query：过滤条件，可选。
                    - 不指定删除条件，删除所有数据
                    - 指定删除的条件，符合条件的所有数据均会被删除
                
                * justOne：是否只删除查询到的第一条数据，默认为 false，可选。
                    - 值为true或者1时，只删除一条数据
            
            delete_one() 和 delete_many()：
                
                * delete_one() 即删除第一条符合条件的数据
                * delete_many() 即删除所有符合条件的数据
                * 返回结果是DeleteResult类型，可以调用deleted_count属性获取删除的数据条数
                
            
            删除集合中的所有文档时 remove() 和 drop() 区别：
                
                    * remove()方法不会删除索引。

                    * drop()方法可能更有效，drop()方法会删除整个集合，包括索引，然后重新创建集合和建立索引。  
                
                    * 使用 drop()方法会删除整个集合后，数据库也会没有了
                    
            删除数据库：
            
                * db.dropDatabase()
                
                    
            删除一个属性：
            
                * $unset
                    - db.collection.update({'name':'huahua'},{'$unset':{'age':123}})
                    _ 删除name 是huahua 数据中的 age属性，后边的值无所谓是多少
        
    '''

    collection = db.students

    # 删除
    result = collection.remove({'name':'Dog'})
    print(result) # {'n': 0, 'ok': 1.0}

    # 删除一条符合条件的数据 delete_one()
    result = collection.delete_one({'name': 'Hongji'})
    print(result)
    print(result.deleted_count)

    # 删除所有符合条件的数据 delete_many()
    result = collection.delete_many({'age': 21})
    print(result.deleted_count)

    # 删除集合中所有数据
    result = collection.remove({})
    print(result)


# 改
def update_data():
    ''''''
    '''
        更新数据方式
        
            update(<query>,<update>,{upsert: <boolean>, multi: <boolean>,writeConcern: <document> })
            
                * query：更新条件
                * update：要更新的数据
                
                * upsert : 可选如果不存在update的记录，是否插入objNew
                    - true为插入
                    - 默认是false，不插入
                    
                * multi : 可选
                    - 默认是false,只更新找到的第一条记录
                    如果这个参数为true,就把按条件查出来多条记录全部更新。
                    
                * writeConcern :可选，抛出异常的级别。
                
                * 返回结果中，ok 即代表执行成功，nModified代表影响的数据条数。
                
            update_one() 和 update_many()
            
                * 用法更加严格，第二个参数需要使用$类型操作符作为字典的键名
                * 返回值是UpdateResult类型，然后调用matched_count和modified_count属性
                分别可以获得匹配的数据条数和影响的数据条数。
                
                
            $currentDate:{ lastModified: true }
            
                * 使用 $currentDate 操作符更新 lastModified 字段的值到当前日期。
                * 如果 lastModified 字段不存在， $currentDate 会创建该字段。
                
        更新数据需要使用更新操作符：$set
            
            * 如：result = collection.update_one(condition, {'$set': student})
            * 没有 $set操作符，则是进行替换
            
        
        文档替换：
            
            * 在替换文档中，由于 _id 字段是不变的，所以，你可以省略 _id 字段；
            不论如何，如果你包含了 _id 字段，它的值必须和当前的值相同。
            
            * 文档替换方式：
            
                db.collection.replaceOne() 
                db.collection.update()
                    
        
    
    '''
    collection = db.students

    # 从表中查找name 是 Hongji的 ，更新年龄为 25
    condition = {'name': 'Hongji'}
    student = collection.find_one(condition)
    student['age'] = 25
    result = collection.update(condition, student)
    print(result)

    # 使用 update_one() 更新
    student['age'] = 26
    #第二个参数不能再直接传入修改后的字典，而是需要使用{'$set': student}这样的形式，
    result = collection.update_one(condition, {'$set': student})
    print(result)
    print(result.matched_count, result.modified_count)

    # 指定查询条件为年龄大于20，更新条件为{'$inc': {'age': 1}}，执行之后会第一条符合条件的数据年龄加1。
    condition = {'age': {'$gt': 20}}
    result = collection.update_one(condition, {'$inc': {'age': 1}})
    print(result)
    print(result.matched_count, result.modified_count)

    # 更新 name 是 Hongji 的 favorites 中的 food 属性的值 为 yu1，age 更新为 30
    # 由于 insert的时候没有给 name是 Ming的人添加 favorites 字段，执行下面语句后会自动添加
    collection.update_one({'name': 'Hongji'}, {'$set': {'favorites.food': 'yu1','age':30}})

    # 更新 favorites中的artist 是 Picasso 的 favorites 中的 food 属性的值 为 方便面
    db.students.updateOne({'favorites.artist': "Picasso" },{'$set':{'favorites.food':'方便面'}})

    # 使用 $currentDate 添加 lastModified 字段
    collection.update_one(
        {
            'name': 'xiaoxiao'
        },
        {
            '$set': {'favorites.food': 'yu1', 'age': 30} ,
            '$currentDate':{'lastModified':True}
        }
    )


    # 文档替换
    collection.replaceOne({'name': "yuyan"},{'sex': '男'})

    # 或

    # 使用 update（）方法 不用 $set 符号
    collection.update({'name':'Hongji'},{'sex':'男'})

    # 删除 huahua 的 age 属性
    collection.update({'name': 'huahua'}, {'$unset':{'age': 123}})

    # 查找 movies 是 mA 的人
    collection.find({'favorites.movies':'mA'})

    # 给 name 是 xiaoxiao 的 movies 中添加 一个电影 mE
    # $push 允许重复添加
    # $addToSet 不允许重复添加，如果集合中已经存在要添加的元素，则会添加失败
    collection.update({'name':'xiaoxiao'},{'$push':{'favorites.movies':'mE'}})
    collection.update({'name': 'xiaoxiao'}, {'$addToSet': {'favorites.movies': 'mE'}})





# 查
def find_data():

    ''''''
    '''
        数据查询方式：
        
            find_one()
                * 查询得到是单个结果
                
            find()
                * 则返回多个结果 
                
        limit():
        
            * find().limit(10)
                - 查询前 10 条数据
        
        skip() 
            * 用于跳过指定数量的条数
            
            * 例：查询第11条到第20条的数据
                
                - find().skip(10).limit(10)
              
        分页查询：
            
            * skip(（页码-1） * 每页显示的条数).limit(每页显示的条数)
            
            * 例：每页显示10条
                
                - 第一页显示 1-10条数据 find().skip((1-1) * 10).limit(10)
                - 第二页显示 11-20条数据 find().skip((2-1) * 10).limit(10)
                - 第三页显示 21-30条数据 find().skip((3-1) * 10).limit(10)
                .
                .
                .
                
        排序查询 - sort()：
        
            * 查询文档时，默认是按照 _id 的是进行排列（升序）
            * sort() 可以用来指定文档排序规则
            * sort() 需要传递一个对象来指定排序 
                - 1：表示升序
                - -1：表示降序
                
            * 例：按照 id 升序排序
                - db.students.find({}).sort({'id':1})
                
            * 例：按照 age降序 和 id升序排序
                - db.students.find({}).sort({'age':-1，'id':1})
                - 会先用 age降序排列，如果 age 一样，会按照 id 升序排列
                
        
        查询射影：
        
            * 在查询时，可以在第二个参数的位置来设置查询结果的 投影
            
            * 例：查询数据中只显示 name 和 age 字段
                - db.students.find({}, {'name':1, 'age':1})
                _ 结果中默认都会显示 _id 属性
                
            * 例：投影结果中不显示 _id 属性
                - 把 _id 的值设置为 0
                - db.students.find({}, {'name':1, '_id':0, age':1})
            
        
    '''

    # 指定集合
    collection = db.students

    # 查询单条数据
    result = collection.find_one({'age': 21}) # find_one() 方法返回字典
    print(type(result)) # <class 'dict'>
    print(result)

    # 查询所有
    results = collection.find()
    for result in results:
        print(result)

    # 查询多条数据-年龄是21的
    results = collection.find({'age': 21})
    print(type(results)) # <class 'pymongo.cursor.Cursor'>
    for result in results:
        print(result)

    # 查询多条数据-年龄是25， name是huahua 的人
    results = collection.find({'age': 25, 'name':'huahua'})
    print(type(results))  # <class 'pymongo.cursor.Cursor'>
    for result in results:
        print(result)

    # 查询的数据条数
    count = collection.find().count()
    print(count)
    count = collection.find({'age': 21}).count()
    print(count)

    # 返回的数据示例：
    # {'_id': ObjectId('5b48943fa1be8149c427814a'), 'id': '20170206', 'name': 'Mike', 'age': 21, 'gender': 'male'}
    # 可以发现它多了一个 _id 属性，这就是 MongoDB 在插入的过程中自动添加的。
    # 我们也可以直接根据 ObjectId 来查询，这里需要使用 bson 库里面的 ObjectId。

    result = collection.find({'_id': ObjectId('5b48943fa1be8149c427814b')})
    print(result)

    # 查询前10条数据
    collection.find().limit(10)

    # 查询第11条到第20条的数据
    results = collection.find().skip(10).limit(10)


    # 每页显示10条
    # 第一页显示1 - 10条数据
    collection.find().skip((1 - 1) * 10).limit(10)

    # 第二页显示11 - 20条数据
    collection.find().skip((2 - 1) * 10).limit(10)

    # 第三页显示21 - 30条数据
    collection.find().skip((3 - 1) * 10).limit(10)




getConn()
# db.students.remove()
insert_data()




