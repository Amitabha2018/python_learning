#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2021-01-06 20:48'

import requests,wget,os,time
from tqdm import tqdm
from lxml import etree

# # 进度条模块
# def progressbar(url,path,fname):
#     if not os.path.exists(path):   # 看是否有该文件夹，没有则创建文件夹
#          os.mkdir(path)
#     start = time.time() #下载开始时间
#     response = requests.get(url, stream=True)
#     size = 0    #初始化已下载大小
#     chunk_size = 1024  # 每次下载的数据大小
#     content_size = int(response.headers['content-length'])  # 下载文件总大小
#     try:
#         if response.status_code == 200:   #判断是否响应成功
#             print('Start download,[File size]:{size:.2f} MB'.format(size = content_size / chunk_size /1024))   #开始下载，显示下载文件大小
#             filepath = path+fname  #设置图片name，注：必须加上扩展名
#             with open(filepath,'wb') as file:   #显示进度条
#                 for data in response.iter_content(chunk_size = chunk_size):
#                     file.write(data)
#                     size +=len(data)
#                     print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')
#         end = time.time()   #下载结束时间
#         print('Download completed!,times: %.2f秒' % (end - start))  #输出下载用时时间
#     except:
#         print('Error!')

url = 'http://www.opt-ml.org/oldopt/opt19/papers.html'

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '__guid=18473919.4415048242315997700.1609731283540.1099; monitor_count=2',
'Host': 'www.opt-ml.org',
'If-Modified-Since': 'Fri, 11 Dec 2020 16:32:11 GMT',
'If-None-Match': '"18e02e4-8b59-5b632d58d98c0"',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

res = requests.get(url,headers=headers)

html = res.text

tree = etree.HTML(html)


href_info = tree.xpath('//ul/li/a/@href')

paper_href = [i for i in href_info if "papers" in i]

# out_fname = paper_href[0][12:]
# print(out_fname)
# down_url = 'http://www.opt-ml.org/'+paper_href[1]


dir_path = r'H:\朱老师论文整理\opt论文下载\2019'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)




#wget.download(down_url)

for i in tqdm(paper_href):

    down_url = 'http://www.opt-ml.org/'+i
    fname = wget.filename_from_url(down_url)
    out_fname = os.path.join(dir_path, fname)
    if os.path.exists(out_fname):
        print(out_fname+"已下载完成！")
    else:
        paper_res = requests.get(down_url, headers=headers)
        print('正在写入'+out_fname)
        with open(out_fname, 'wb+') as f:
            f.write(paper_res.content)






