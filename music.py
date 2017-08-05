from NetEaseMusicApi import interact_select_song
import os
import itchat
def close_music():
    with open ('stop.mp3','w') as f:
        pass
    os.startfile('stop.mp3')
@itchat.msg_register(itchat.content.TEXT)   
def music(msg):
    if msg['ToUserName']!='filehelper':
        return
    if msg['Text']==(u'关闭'):
        close_music()
        itchat.send(u'音乐已关闭','filehelper')
    elif msg['Text']==(u'帮助'):
        itchat.send(u'帮助信息','filehelper')
    else:
        itchat.send(interact_select_song(msg['Text']),'filehelper')
itchat.auto_login(True)
itchat.send('欢迎使用网易云音乐\n帮助：显示帮助\n关闭：关闭歌曲\n歌名：按引导播放音乐','filehelper')
itchat.run()
