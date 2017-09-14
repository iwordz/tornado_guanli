# -*- coding: utf-8 -*-
# @Date    : 2017-08-23 12:55:23
# @Author  : lileilei
from handlsers.LoginHeadel import LoginView,LogoutView
from handlsers.Shebeihandler import IndexView,ShebeiView,AddShebei,DongjieShebeiView,JieShebeiView,EditShebei
from handlsers.UserHaders import UserView,AddUserView,QuxiaoAdmin,ShezhiAdmin,DongjieUser,JieDUser,ChongzhiUser
from handlsers.TestResulthander import TestresultView,AddtestresultView,Deleresult,Resetresult
from handlsers.TestCaseHandler import TestcaseView,AddtestcaseView,DeletestcaseView,ResettestcaseView
from handlsers.TestFileManHandler import TestfileView
from handlsers.BugHandler import BugadminView
from handlsers.BanbenHandler import BanbenView,AddbanbenView,Addproject,Desetbanben,Resetbanben,EditbanbenView
url=[
    ('/login',LoginView),
    ('/logout',LogoutView),
    ('/index',IndexView),
     ('/shebei',ShebeiView),
    ('/shebei/(?P<page>\d*)',ShebeiView),
     ('/user',UserView),
    ('/user/(?P<page>\d*)',UserView),
    ('/addshebei',AddShebei),
    ('/dongjie/(?P<id>\d*)',DongjieShebeiView),
    ('/jie/(?P<id>\d*)',JieShebeiView),
    ('/adduser',AddUserView),
    ('/quxiao/(?P<id>\d*)',QuxiaoAdmin),
    ('/shezhi/(?P<id>\d*)',ShezhiAdmin),
    ('/dongjie1/(?P<id>\d*)',DongjieUser),
    ('/jiedong1/(?P<id>\d*)',JieDUser),
    ('/chongzhi/(?P<id>\d*)',ChongzhiUser),
    ('/edit_shebei/(?P<id>\d*)',EditShebei),
    ('/testre',TestresultView),
    ('/testre/(?P<page>\d*)',TestresultView),
    ('/addtestresult',AddtestresultView),
    ('/deleresult/(?P<id>\d*)',Deleresult),
    ('/resetresult/(?P<id>\d*)',Resetresult),
    ('/testcase',TestcaseView),
    ('/testcase/(?P<page>\d*)',TestcaseView),
    ('/filepan',TestfileView),
    ('/filepan/(?P<page>\d*)',TestfileView),
    ('/bug',BugadminView),
    ('/bug/(?P<page>\d*)',BugadminView),
    ('/banben',BanbenView),
    ('/banben/(?P<page>\d*)',BanbenView),
    ('/addbanben',AddbanbenView),
    ('/addproject',Addproject),
    ('/delebanben/(?P<id>\d*)',Desetbanben),
    ('/resetbanben/(?P<id>\d*)',Resetbanben),
    ('/editbanben/(?P<id>\d*)',EditbanbenView),
    ('/addtestcase',AddtestcaseView),
]