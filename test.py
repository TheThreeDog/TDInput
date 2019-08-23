import sys , os
from tdinput import td_input,td_print


# @register_func(CmdType.CMD_UP)
# def up():
#     td_print("按了↑箭头")

# @register_func(CmdType.CMD_DOWN)
# def down():
#     td_print("按了↓箭头")


if __name__ == '__main__': 
    td_print(">>> ***********************************")
    td_print(">>> **     TDInput输入模块测试程序   **")
    td_print(">>> **                               **")
    td_print(">>> **         输入exit退出          **")
    td_print(">>> ***********************************")
    try:
        while True:
            td_print(">>> ",end = '')
            cmd = td_input().strip() # 获取字符去除前后空格
            if cmd == '':    # 输入无效内容，直接跳过
                continue
            if cmd == 'exit':
                break
            # print(cmd)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        td_print(exc_type, fname, exc_tb.tb_lineno)
        #rate.sleep()

# import threading

# if __name__ == '__main__': 
#     print(">>> ***********************************")
#     print(">>> **     TDInput输入模块测试程序   **")
#     print(">>> **                               **")
#     print(">>> **         输入exit退出          **")
#     print(">>> ***********************************")

#     threading.Thread(target=td_input).start()

#     try:
#         while True:
#             print(">>> ",end = '')
#             cmd = input().strip() # 获取字符去除前后空格
#             if cmd == '':    # 输入无效内容，直接跳过
#                 continue
#             if cmd == 'exit':
#                 break
#             # print(cmd)

#     except Exception as e:
#         exc_type, exc_obj, exc_tb = sys.exc_info()
#         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#         td_print(exc_type, fname, exc_tb.tb_lineno)
#         #rate.sleep()

