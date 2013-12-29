数据模拟模块说明 ： 

fis-python-server的数据模拟模块，提供python数据与json数据两种格式

## Usage

默认使用python格式的模拟数据

127.0.0.1:8888/home/page/index的页面请求将会命中/test/home/page/index.py脚本，获取fis_data变量提供模版渲染模块使用

json格式的模拟数据则会命中/test/home/page/index.json，文件内容将会在序列化为python对象后提供模版渲染模块使用

修改数据格式的方法是设置cookie FIS_DEBUG_DATATYPE 的值，目前可以选择python或json