# -*- coding:utf-8 -*-
''''''
'''

文档间的关系
    
    * 一对一（one to many）        
        - 夫妻 （一个丈夫 对应 一个妻子）
        - 在MongoDB， 可以通过内嵌文档的形式来体现一对一的关系
        - 例：
        
            db.hasbandwife.insert([
            {'name': '黄蓉', 'hasband': {'name': '郭靖'}},
            {'name': '潘金莲', 'hasband': {'name': '武大'}}
            ])
        
        
        
    * 一对多（one to many）/ 多对一（many to one）
        - 用户 ： 订单
        - 文章 ： 评论
        - 也可以通过内嵌文档来映射一对多的关系 
        - 例：
        
            # 用户表中添加两个用户
            db.users.insert([
            {'name': 'swk'},
            {'name': 'zbj'}
            ])
            
            # 给swk添加订单 userid: swk的_id
            db.orders.insert([
            {'list': ['香蕉', '橘子', '苹果'], 'userid': ObjectId("5b4df578c059ebba7608bc1d")},
            {'list': ['辣皮', '啤酒', '桃子'], 'userid': ObjectId("5b4df578c059ebba7608bc1d")}
            ])
            
            # 给zbj添加订单 userid: zbj的_id
            db.orders.insert([
            {'list': ['馒头', '牛肉', '二锅头'], 'userid': ObjectId("5b4df578c059ebba7608bc1e")}
            ])
            
            # 查找swk的订单
            var userid = db.users.findOne({'name': 'swk'})._id
            
            db.orders.find({'userid': userid})

    
    
    
    * 多对多（many to many）
        - 老师 ： 学生 （一个老师 对应 多个学生 / 一个学生对应多个老师）
        
        - 例：
        
            /*
                向teacher表中添加三个老师
            */
            db.teachers.insert([
            {'name':'语文'},
            {'name':'数学'},
            {'name':'体育'}
            ])
            
            /*
                执行结果：
                
                    { "_id" : ObjectId("5b4e911bc059ebba7608bc22"), "name" : "语文老师" }
                    { "_id" : ObjectId("5b4e911bc059ebba7608bc23"), "name" : "数学老师" }
                    { "_id" : ObjectId("5b4e911bc059ebba7608bc24"), "name" : "体育老师" }
            */
            
            /*  向学生表中添加学生
                teachers属性中是 学生的老师id，一个学生有多个老师
                同时一个老师可以有多个同学
            */
            db.students.insert([
            {'name':'华华', 'teachers':[ObjectId("5b4e911bc059ebba7608bc22"),
            ObjectId("5b4e911bc059ebba7608bc24")]},
            
            {'name':'笑话', 'teachers':[ObjectId("5b4e911bc059ebba7608bc22"),
            ObjectId("5b4e911bc059ebba7608bc24"),ObjectId("5b4e911bc059ebba7608bc23")]}
            ])
            
            
            /*
                查询老师是语文老师的学生
            */
            var id = db.teachers.findOne({'name':'语文老师'})._id
            db.students.find({'teachers':id})
            
            /*
                
                执行结果：
                
                    { "_id" : ObjectId("5b4e92a2c059ebba7608bc25"), "name" : "华华", 
                    "teachers" : [ ObjectId("5b4e911bc059ebba7608bc22")......
                    
                    { "_id" : ObjectId("5b4e92a2c059ebba7608bc26"), "name" : "笑话", 
                    "teachers" : [ ObjectId("5b4e911bc059ebba7608bc22").......
                    
                查询出两条数据
                    
            */
            
            
'''


