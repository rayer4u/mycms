# 简介
基于django-cms的程序员友好的、自带后台的、定制化很高的内容管理系统的一个实例。

# 更新说明
## 更新1.0版本说明
1. 更新最新django 1.11，以完全解决多语言问题。aldryn_newsblog不兼容，不过和我们的使用没有影响

## 更新0.99版本说明
1. 用户注册相关，可配置某些分类的文章需要注册用户才可见。目前在配置文件里配置

## 更新0.95版本说明
### 解决系统问题
1. 修改水印内容。
2. 用户自注册功能。
3. 补充开源声明

## 更新0.9版本说明
### 解决系统问题
1. 水印挪到左上角，并修改水印内容。http://www.qt86.com/   255
2. 制作并替换logo
3. 调整panel次序和内容数量。添加点击title，显示内容功能
4. 切换并清理多余数据
5. 合作伙伴最多一排
6. 补充开源声明
7. 文章列表里的英文。所有用户可见的英文翻译

## 更新0.8.1版本说明
### 解决服务器问题
1. selinux、权限导致上传出错问题

## 更新0.8版本说明
### 解决系统问题
1. 首页样式调整。图标显示，多行文本显示
2. 区分不同配置文章显示形式
3. 添加合作伙伴区
4. 添加联系方式
5. 修改发布者用户组的权限，已能发布文章

### 解决服务器问题
1. 时间不对，导致文章显示问题

# 简易安装使用说明
1. 安装好并使用virtualenv环境
2. 安装依赖库到系统
```
pip install -r requirements.txt
```
3. 首次运行，或者有更新了，运行以下相关命令更新相关部分
```
# 创建超级用户
./manage.py createsuperuser
# 静态资源
./manage.py collectstatic
# 数据库
./manage.py makemigrations
./manage.py migrate
# 语言串
./manage.py compilemessages
```
4. 运行
```
# dev setting
./manage.py runserver 
or 
# prod setting，正式发布
./startup.sh
```
5. .gitignore包含了本地依赖文件，请自行补充相关文件
```
mycms/static/watermark.png
mycms/settings/prod.py
media/icon.png
```


# 相关开源项目
使用了并感谢以下以及所包含的所有项目
- [django](https://www.djangoproject.com/)
- [django-cms](https://www.django-cms.org/)
- [aldryn_newsblog](https://github.com/aldryn/aldryn-newsblog) 已[定制](https://github.com/rayer4u/aldryn-newsblog)
- [django-registration](https://github.com/ubernostrum/django-registration)
- [django-registration-templates](https://github.com/macdhuibh/django-registration-templates) 已直接合入修改
- [django-easy-thumbnails-watermark]()
- [wordcloud2](http://timdream.org/wordcloud2.js/)
- [canvas-nest](https://github.com/hustcc/canvas-nest.js)
