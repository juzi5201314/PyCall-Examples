# -*- coding: utf8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from cn.nukkit.plugin import PluginBase
from cn.nukkit.event.player import PlayerJoinEvent

from net.soeur.pycall import EventListener

from java.net import URL
from java.io import InputStreamReader, BufferedReader

import urllib, urllib2

class Test(PluginBase):

    def onLoad(self):
        pass


    def onEnable(self):
        self.getLogger().info("哭嘤嘤")
        EventListener.registerEventListener(onjoin, PlayerJoinEvent)

    def onCommand(self, sender, command, label, args):
        if command.getName() == "testcmd":
            #用python发送get请求
            req = urllib2.Request(url="http://mobile.weather.com.cn/data/sk/101010100.html")
            res = urllib2.urlopen(req)
            res = res.read()
            sender.sendMessage(res)
            #用java发送get请求
            conn = URL("http://mobile.weather.com.cn/data/sk/101010100.html").openConnection()
            conn.connect()
            input = BufferedReader(InputStreamReader(conn.getInputStream()))
            while True:
                line = input.readLine()
                if line == None:
                    break
                sender.sendMessage(line)
        return 1

def onjoin(event):
    event.getPlayer().sendMessage("hello world")

