#  病案首页&标准编辑-后端

[前端](https://github.com/angushushu/medical-record-frontend)

**使用：**<br>
`pip install -r requirements.txt`<br>
启动MySql (在proj_django/settings.py中配置)<br>
在MySql中创建数据库 `create database test` (test为数据库名，可在settings.py中修改)<br>
删除所有文件夹中的migrations文件夹（如果有的话）<br>
`python makemigrations`<br>
`python migrate`<br>
`python manage.py runserver`<br>

标准文件例子见/media/examples目录
