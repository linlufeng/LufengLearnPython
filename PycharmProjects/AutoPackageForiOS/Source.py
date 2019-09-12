#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import requests
import webbrowser
import subprocess
import time
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

from UI import *
import weakref
from PyQt5.QtCore import QThread
import threading
import _thread
import string

# project_name = 'ScreenshotForAd'    # 项目名称
# archive_workspace_path = '/Users/lufenglin/Documents/git/ScreenshotForAd/ScreenshotForAd'    # 项目路径
# export_directory = 'archive'    # 输出的文件夹
# ipa_download_url = 'https://www.pgyer.com/Yyu9' #蒲公英的APP地址

# 蒲公英账号USER_KEY、API_KEY
# USER_KEY = 'b15b89c376d2f3006a7275ad04291aa6'
# API_KEY = '457cd58d02fbf94a0d4e0878c8fc3887'

from_address = '8912462@qq.com'    # 发送人的地址
password = 'ujauupesnfwxcbcj'  # 邮箱密码换成他提供的16位授权码
to_address = ['8912462@qq.com']    # 收件人地址,可以是多个的
smtp_server = 'smtp.qq.com'    # 因为我是使用QQ邮箱..


class MyThread(QThread):

    updated = PyQt5.QtCore.pyqtSignal(str)

    def run(self):
        # do some functionality
        for i in range(10000):
            self.updated.emit(str(i))

class AutoArchive(MyThread):
    """自动打包并上传到蒲公英,发邮件通知"""

    # def __init__(self, autoPackage : AutoPackage, project_name = 'ScreenshotForAd',
    #              archive_workspace_path = '/Users/lufenglin/Documents/git/ScreenshotForAd/ScreenshotForAd',
    #              ipa_download_url = 'https://www.pgyer.com/Yyu9',
    #              user_key = 'b15b89c376d2f3006a7275ad04291aa6',
    #              api_key = '457cd58d02fbf94a0d4e0878c8fc3887',
    #              description = ''):
    #     super().__init__()
    #     self.autoPackage = weakref.proxy(autoPackage)
    #     self.project_name = project_name
    #     self.archive_workspace_path = archive_workspace_path
    #     self.export_directory = 'archive'
    #     self.ipa_download_url = ipa_download_url
    #     self.user_key =  user_key
    #     self.api_key = api_key
    #     self.description = '优化app版本截图样式，刷新资讯列表！请前往更新'

    def __init__(self, project_name = 'ScreenshotForAd',
                 archive_workspace_path = '/Users/lufenglin/Documents/git/ScreenshotForAd/ScreenshotForAd',
                 ipa_download_url = 'https://www.pgyer.com/Yyu9',
                 user_key = 'b15b89c376d2f3006a7275ad04291aa6',
                 api_key = '457cd58d02fbf94a0d4e0878c8fc3887',
                 description = ''):
        super().__init__()
        self.project_name = project_name
        self.archive_workspace_path = archive_workspace_path
        self.export_directory = 'archive'
        self.ipa_download_url = ipa_download_url
        self.user_key =  user_key
        self.api_key = api_key
        self.description = '优化app版本截图样式，刷新资讯列表！请前往更新'

    def run(self):
        self.clean()

    def startArchive(self):
        pass
        # self.clean()
        # try:
        #     _thread.start_new_thread(self.clean, ())
        # except ValueError:
        #     print("Error: 无法启动线程", ValueError)

    def clean(self):
        self.archiveLog("\n===========开始clean操作===========\n")
        start = time.time()
        clean_command = 'xcodebuild clean -workspace %s/%s.xcworkspace -scheme %s -configuration Release' % (
            self.archive_workspace_path, self.project_name, self.project_name)
        clean_command_run = subprocess.Popen(clean_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
        for bytes in iter(clean_command_run.stdout.readline, b''):
            self.archiveLog(str(bytes, 'utf-8'))
        clean_command_run.stdout.close()
        clean_command_run.wait()
        end = time.time()
        # Code码
        clean_result_code = clean_command_run.returncode
        if clean_result_code != 0:
            self.archiveLog("=======clean失败,用时:%.2f秒=======" % (end - start))
        else:
            self.archiveLog("=======clean成功,用时:%.2f秒=======" % (end - start))
            self.archive()

    def archive(self):
        self.archiveLog("\n\n===========开始archive操作===========")

        # 删除之前的文件
        subprocess.call(['rm', '-rf', '%s/%s' % (self.archive_workspace_path, self.export_directory)])
        time.sleep(1)
        # 创建文件夹存放打包文件
        subprocess.call(['mkdir', '-p', '%s/%s' % (self.archive_workspace_path, self.export_directory)])
        time.sleep(1)

        start = time.time()
        archive_command = 'xcodebuild archive -workspace %s/%s.xcworkspace -scheme %s -configuration Release -archivePath %s/%s' % (
            self.archive_workspace_path, self.project_name, self.project_name, self.archive_workspace_path, self.export_directory)
        archive_command_run = subprocess.Popen(archive_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
        for bytes in iter(archive_command_run.stdout.readline, b''):
            self.archiveLog(str(bytes, 'utf-8'))
        archive_command_run.stdout.close()
        archive_command_run.wait()
        end = time.time()
        # Code码
        archive_result_code = archive_command_run.returncode
        if archive_result_code != 0:
            self.archiveLog("=======archive失败,用时:%.2f秒=======" % (end - start))
        else:
            self.archiveLog("=======archive成功,用时:%.2f秒=======" % (end - start))
            # 导出IPA
            self.export()

    def export(self):
        self.archiveLog("\n\n===========开始export操作===========")
        self.archiveLog("\n\n==========请你耐心等待一会~===========")
        start = time.time()
        # export_command = 'xcodebuild -exportArchive -archivePath /Users/liangk/Desktop/TestArchive/myArchivePath.xcarchive -exportPath /Users/liangk/Desktop/TestArchive/out -exportOptionsPlist /Users/liangk/Desktop/TestArchive/ExportOptions.plist'
        export_command = 'xcodebuild -exportArchive -archivePath %s/%s.xcarchive -exportPath %s/%s -exportOptionsPlist %s/ExportOptions.plist' % (
            self.archive_workspace_path, self.export_directory, self.archive_workspace_path, self.export_directory, self.archive_workspace_path)
        export_command_run = subprocess.Popen(export_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        returncode = export_command_run.poll()
        while returncode is None:
            bytes = export_command_run.stdout.readline()
            returncode = export_command_run.poll()
            bytes = bytes.strip()
            self.archiveLog(str(bytes, 'utf-8'))
            time.sleep(0.1)
        # export_command_run.wait()
        end = time.time()
        # Code码
        export_result_code = export_command_run.returncode
        if export_result_code != 0:
            self.archiveLog("=======导出IPA失败,用时:%.2f秒=======" % (end - start))
        else:
            self.archiveLog("=======导出IPA成功,用时:%.2f秒=======" % (end - start))
            # 删除archive.xcarchive文件
            subprocess.call(['rm', '-rf', '%s/%s.xcarchive' % (self.archive_workspace_path, self.export_directory)])
            self.upload('%s/%s/%s.ipa' % (self.archive_workspace_path, self.export_directory, self.project_name))

    def upload(self, ipa_path):
        self.archiveLog("\n\n===========开始上传蒲公英操作===========")
        if ipa_path:
            # https://www.pgyer.com/doc/api 具体参数大家可以进去里面查看,
            url = 'http://www.pgyer.com/apiv1/app/upload'
            data = {
                'uKey': self.user_key,
                '_api_key': self.api_key,
                'installType': '1',
                'updateDescription': self.description
            }
            files = {'file': open(ipa_path, 'rb')}
            r = requests.post(url, data=data, files=files)
            if r.status_code == 200:
                # 是否需要打开浏览器
                # self.open_browser(self)
                self.send_email()
        else:
            self.archiveLog("\n\n===========没有找到对应的ipa===========")
            return

    def archiveLog(self, str: object) -> object:
        print(str)
        # self.autoPackage.showLog(str)

    @staticmethod
    def open_browser(self):
        webbrowser.open(self.ipa_download_url, new=1, autoraise=True)

    @staticmethod
    def _format_address(self, s):
        name, address = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), address))

    def send_email(self):
        # https://www.pgyer.com/XXX app地址
        # 只是单纯的发了一个文本邮箱,具体的发附件和图片大家可以自己去补充
        msg = MIMEText('Hello'
                       +
                       '应用已更新,请下载测试\n'
                       +
                       '蒲公英的更新会有延迟,具体版本时间以邮件时间为准\n'
                       +
                       '下载地址\n' + self.ipa_download_url, 'html', 'utf-8')
        msg['From'] = self._format_address(self, 'iOS开发团队 <%s>' % from_address)
        msg['Subject'] = Header(self.project_name+'新版本已经发布.', 'utf-8').encode()
        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        self.archiveLog("===========邮件发送成功===========")

if __name__ == '__main__':
    # description = input("请输入内容:")
    archive = AutoArchive()
    archive.clean()