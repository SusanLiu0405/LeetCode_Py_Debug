import sys
import getpass
import os
import time
 
RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
 
def get_terminal_size():
    return os.get_terminal_size().columns
 
def center_text(text, width):
    if len(text) >= width:
        return text
    else:
        padding = (width - len(text)) // 2
        return ' ' * padding + text
 
def input_password(prompt=""):
    print(prompt, end="", flush=True)
    password = getpass.getpass()
    print("password is ",password)
    # while True:
    #     char = getpass.getpass()
    #     print("char type is ",type(char),char)
    #     print("pass word is ",type(password),password)

    #     if char == '\r':  # Enter key
    #         break
    #         password += char.decode()
    #         # password += int(char)
    #         # password = char

    #     elif char == '\x08':  # Backspace key
    #         if len(password) > 0:
    #             sys.stdout.write('\b \b')
    #             sys.stdout.flush()
    #             password = password[:-1]
    #     else:
    #         sys.stdout.write('*')
    #         sys.stdout.flush()
    #         password += char.decode()
    #         # password += int(char)
    #         # password = char
            
    # print("password is ",password)        
    return password
 
def main():
    command = input("J:\\Projects\\Mayday\\透露>")
    if command == "rs.mayday.toulou":
        print(f"欢迎光临 {RED}5525回到那一天 {RESET}（目前共有{BLUE}55255{RESET}人上线）")
        print(f"请输入代号（试用请输入'{BLUE}guest{RESET}', 注册请输入'{BLUE}new{RESET}'):", end="")
        sys.stdout.flush()  # 刷新输出缓冲区
        code = input()
 
        if code == "mayday":
            password = input_password("请输入密码：")
            print("main password is -->",type(password),password)
            if password == "5525":
                display_full_content()
            else:
                print("时光机启动失败！！！")
        else:
            print("魔法荧光棒失灵！！！")
    else:
        print("第五分队召集失败！！！")
 
def display_full_content():
    width = get_terminal_size()
    lines = [
        "                               ::::::::::'.d$N.^''...:::db.^'::::::::::.",
        "                              .::::::::: *#' ::::::::'z$$$$$bo.'''::::::",
        "                              :::::::''..-:::::::: 'u$$$$$$$$$$$$bu ':::",
        "                             ::::::'.::::::::::'.ud$$$$$$$$$$$$$$$$$  :'",
        "                             ::::: ::::::::' .ud$$$$$$$$$$$$$$$&eeu]> :",
        "                           .':::::::::::: xd$$$$R'Lued$$$$$$$$$$$$$$>.:",
        "                         ::::.::::::::::. 9$$$$Fz$$$$$$$$$$$$$$$$F'' .:",
        "                        ::::::::::::::::::'$$$$u$$$F' ''$$$$$$$$.ut  '::",
        "                        :::::::::::::::::::'$$$$$FsKxL. 9$$$$$$$edNeo :::",
        "                        :::::::::::::::::::'$$$$$FsKxL. 9$$$$$$$edNeo :::",
        "                         ':::::::::::::::::: 4$$$$$b$euud$$$$$$$$$$$$$  : %%%",
        "                    %:%: '::: :::::::::::::: $$$$$$$$$$$$%%%%%%?$$$$$>  %%%%",
        "                    %%%%%     ::::::::::::: .$$$$$$$$$$$$$$$$I$u$$$$$> %%%%",
        "                    %%%%%%%:  ::::::::::::' d$$$$$$$$$$$$$$$R???'7$$F %%%%",
        "                     % %%%%%%  ::::::::::'.$$$$$$$$$$$$$b.-m$$* d$$F %%%%'",
        "                         %%%%%.  :::::::: t$$$$$$$$$$$$$$$bu..o$$$'.%%%'",
        "                          '%%%%%%.   :::: '$$$$$$$$$$$$$$$$$$$$$F':%%",
        "                          's.'%%%%%%%%::.  $$$$$$$$o.''???$$R?F.:%%%",
        "                            '$eu  %%%%%%% '$$$$$$$$$$$$er /%%%%%%%/",
        "                              '?$$eu. %%% t$$$$$$$$$$$$$! %%%%%%%%",
        "                                                 .___",
        "                                ___ ___  __.__. _| _/__  __._.           ",
        "                               /   \\\_ \<  |  |/ __|\_ \<  | |             ",
        "                              | Y Y \/ _\\\__  / /_/| / _\\\__ |           ",
        "                              |_|_| (___ /____\____|(___ / __|           ",
        "                                   \/   \/\/      \/    \/\/    ",
        center_text(f"{RED} 欢  迎  光  临{RESET}", width),
        center_text(f"{BLUE}5525回到那一天 BBS站{RESET}", width),
        center_text(f"{YELLOW}   Welcome to #5525 LIVE TOUR{RESET}", width),
        center_text(" ", width),
        center_text("********************************", width),
        center_text(f"{GREEN}    Since 1997.3.29{RESET}", width),
        center_text(f"本站开放 {YELLOW}5520-5525{RESET} 等五个part",width),
        center_text("by YUANZI", width)
    ]
 
    for line in lines:
        print(line)
        time.sleep(0.1)  # 每行打印后暂停0.1秒
 
if __name__ == "__main__":
    main()