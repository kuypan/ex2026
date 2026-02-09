# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import gettext
import os

# 1. 设置本地化目录（通常名为 'locale'）
locale_dir = os.path.join(os.path.dirname(__file__), 'locale')
# 2. 配置 gettext
gettext.bindtextdomain('myapp', locale_dir)  # 'myapp' 是你的域名，通常用应用名
gettext.textdomain('myapp')
_ = gettext.gettext  # 标准的翻译函数别名

# 3. 在代码中使用 _() 包裹所有需要翻译的字符串
print(_("Hello, World!"))
name = input(_("Please enter your name: "))
print(_("Welcome, %s!") % name)

# 对于复数的处理，使用 ngettext
count = 5
message = gettext.ngettext(
    "You have %(num)d message.",  # 单数形式
    "You have %(num)d messages.", # 复数形式
    count
) % {'num': count}
print(message)

