# -*- coding: utf-8 -*-
import urllib
import re
import time
import os

if __name__ == '__main__':

    chtml = ('http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E6%97%A5%E6%9C%AC%E7%9F%AD%E5%B0%BE%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E5%B7%B4%E5%8E%98%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E5%9C%9F%E8%80%B3%E5%85%B6%E5%AE%89%E5%93%A5%E6%8B%89%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E8%A4%B4%E8%A4%9B%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E4%B8%9C%E5%A5%87%E5%B0%BC%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E9%A9%AC%E6%81%A9%E5%B2%9B%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E6%9F%AF%E5%B0%BC%E6%96%AF%E5%8D%B7%E6%AF%9B%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E5%A5%A5%E8%A5%BF%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E6%B2%99%E7%89%B9%E5%B0%94%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E5%BE%B7%E6%96%87%E5%8D%B7%E6%AF%9B%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E7%BE%8E%E5%9B%BD%E5%88%9A%E6%AF%9B%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E5%91%B5%E5%8F%BB%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E9%87%8D%E7%82%B9%E8%89%B2%E7%9F%AD%E6%AF%9B%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E5%93%88%E7%93%A6%E9%82%A3%E6%A3%95%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E5%A1%9E%E5%B0%94%E5%87%AF%E5%85%8B%E5%8D%B7%E6%AF%9B%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E6%8B%89%E9%82%A6%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E7%BE%8E%E5%9B%BD%E5%8D%B7%E6%AF%9B%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E4%B8%9C%E6%96%B9%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&z=2&tn=baiduimage&word=%E6%AC%A7%E6%B4%B2%E7%BC%85%E7%94%B8%E7%8C%AB&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=&se=&sme=&width=0&height=0',
        'http://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs2&word=%E7%BE%8E%E5%9B%BD%E5%8D%B7%E6%AF%9B%E7%8C%AB&oriquery=%E5%A1%9E%E5%B0%94%E5%87%AF%E5%85%8B%E5%8D%B7%E6%AF%9B%E7%8C%AB&ofr=%E5%A1%9E%E5%B0%94%E5%87%AF%E5%85%8B%E5%8D%B7%E6%AF%9B%E7%8C%AB',
        );

    chnum = 0;
    filenum = 21;

    for num in range(1,21):
        try:
            page = urllib.urlopen(chtml[chnum])
            html = page.read()
            chnum+=1;
            print "get html success :"
        
            reg = r'"objURL":"(.*?)"'
            imgre = re.compile(reg)
            imglist = re.findall(imgre, html)
            #定义文件夹的名字
            picpath = 'D:\\ImageDownload\\cat%s' %filenum  #下载到的本地目录
            filenum +=1;
    
            if not os.path.exists(picpath):   #路径不存在时创建一个
                os.makedirs(picpath)   
            x = 0
            for imgurl in imglist:
                target = picpath+'\\%s.jpg' % x
                print 'Downloading image to location: ' + target + '\nurl=' + imgurl
                image = urllib.urlretrieve(imgurl, target)
                x += 1
            print "Download has finished."
        except: continue
        else: continue
