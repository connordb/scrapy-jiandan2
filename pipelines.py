# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#
# class JiandanPipeline(object):
#     def process_item(self, item, spider):
#         return item
import requests
import os


class JiandanPipeline(object):
    def process_item(self, item, spider):
        path = os.path.abspath('..')
        save_path = path + '\\img'
        if not os.path.exists(save_path):
            os.mkdir(save_path)
            print('文件夹创建成功！')
        img_url = item['img_url']
        img_name = item['img_name']
        save_img = save_path + '\\' + img_name + '.jpg'
        r = requests.get(img_url)

        print('正在下载图片%s......' % img_name)

        with open(save_img, 'wb') as f:
            f.write(r.content)
        f.close()

# import os
# import urllib
#
# from jiandan import settings
#
#
# class JiandanPipeline(object):
#
#     def process_item(self, item, spider):
#         dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)  # 存储路径
#         print('dir_path', dir_path)
#         if not os.path.exists(dir_path):
#             os.makedirs(dir_path)
#         for image_url in item['image_urls']:
#             list_name = image_url.split('/')
#             file_name = list_name[len(list_name) - 1]  # 图片名称
#             # print 'filename',file_name
#             file_path = '%s/%s' % (dir_path, file_name)
#             # print 'file_path',file_path
#             if os.path.exists(file_name):
#                 continue
#             with open(file_path, 'wb') as file_writer:
#                 conn = urllib.urlopen(image_url)  # 下载图片
#                 file_writer.write(conn.read())
#             file_writer.close()
#         return item


