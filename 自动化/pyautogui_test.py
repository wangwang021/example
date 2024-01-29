import pyautogui as ag
import time
import os

# 屏幕大小
# print(ag.size())
# 鼠标移动到100，100的位置 用时1s
# ag.moveTo(100, 100,1)
# 鼠标当前坐标
# print(ag.position())
# 鼠标移动相对位置
# ag.moveRel(100, 100,1)
# 鼠标点击
# ag.click()
# 鼠标右键点击某个位置
# ag.click(button='right')
# 鼠标左键点击某个位置
# ag.click(button='left')
# ag.mouseDown(button='left')
# time.sleep(1)
# ag.mouseUp(button='left')
# 按一个键
# ag.press('a')
# 打一串字母 间隔1s
# ag.write('asdf', interval=0.1)
# 输入字符串
# ag.typewrite('abcdefghigklasjdflkajslkdf', interval=0.1)
# 热键
# ag.hotkey('ctrl','a')

# 截图
# ag.screenshot(r'my_screenshot.png')
# 查找图片，并返回中心位置
pos = ag.locateCenterOnScreen('./自动化/kaishi.png')
print(pos)

# os.system('start notepad.exe')
# time.sleep(1)
# ag.typewrite('hello world', interval=0.1)
# ag.hotkey('ctrl','s')
