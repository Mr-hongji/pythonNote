# -*- encode=utf-8 -*-
''''''
'''
PyMongo库：

    * Python 中有很多 MongoDB 驱动程序，不过其中最正式的一个是 PyMongo
    * PyMongo 是第三方库，需要安装

PyMongo模块安装：

    * python3 安装： pip3 instal pymongo==3.6
    * python2 安装： pip2 install pymongo==适合python2的版本号

    如果不知道这个插件有哪下版本，可以把版本号写的高一点，这样程序检测不到你要的版本，
    就会列出模块的所有历史版本号，然后就可以随便挑了，知识点哦。

    用 python3 举例：pip3 instal pymongo==10

    这里版本号写10，但是模块最高版本号是4.7，命令就会列出所有的历史版本号
    

MongoDB支持许多数据类型：

    String : 这是最常用的数据类型来存储数据。在MongoDB中的字符串必须是有效的UTF-8。
    Integer : 这种类型是用来存储一个数值。整数可以是32位或64位，这取决于您的服务器。
    Boolean : 此类型用于存储一个布尔值 (true/ false) 。
    Double : 这种类型是用来存储浮点值。
    Min/ Max keys : 这种类型被用来对BSON元素的最低和最高值比较。
    Arrays : 使用此类型的数组或列表或多个值存储到一个键。
    Timestamp : 时间戳。这可以方便记录时的文件已被修改或添加。
    Object : 此数据类型用于嵌入式的文件。
    Null : 这种类型是用来存储一个Null值。
    Symbol : 此数据类型用于字符串相同，但它通常是保留给特定符号类型的语言使用。
    Date : 此数据类型用于存储当前日期或时间的UNIX时间格式。可以指定自己的日期和时间，日期和年，月，日到创建对象。
    Object ID : 此数据类型用于存储文档的ID。
    Binary data : 此数据类型用于存储二进制数据。
    Code : 此数据类型用于存储到文档中的JavaScript代码。
    Regular expression : 此数据类型用于存储正则表达式

'''

