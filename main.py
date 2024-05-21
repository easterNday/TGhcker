import json
import tkinter as tk
from tkinter import messagebox
from telegram_phone_number_checker import main as tg

def check_inputs_and_call_function():
    """
    校验输入并调用函数进行手机号验证查询。
    
    从用户界面获取Telegram手机号、API ID、API Hash和待查询手机号，
    若所有字段都填写，则登录Telegram并验证指定的手机号。
    结果以JSON格式显示在文本框中。
    """
    # 获取输入框中的值
    tg_phone = entry_tg_phone.get()
    api_id = entry_api_id.get()
    api_hash = entry_api_hash.get()
    query_phone = entry_query_phone.get()

    # 检查是否有字段未填写
    if not all([tg_phone, api_id, api_hash, query_phone]):
        messagebox.showerror("错误", "所有字段都必须填写！")
    else:
        # 使用提供的API ID、API Hash和TG手机号登录
        client = tg.login(api_id, api_hash, tg_phone)
        # 使用登录后的client和待查询手机号进行用户验证
        res = tg.validate_users(client, query_phone)
        # 将查询结果转换为格式化的JSON字符串
        result = json.dumps(res, indent=4)
        # 启用显示结果的文本框，清空内容，插入结果，然后禁用文本框
        display_result.config(state=tk.NORMAL)
        display_result.delete(1.0, tk.END)
        display_result.insert(tk.END, result)
        display_result.config(state=tk.DISABLED)


# 初始化GUI窗口
root = tk.Tk()
root.title("查询工具")

# 创建输入框和标签
# 分别为TG手机号、API ID、API哈希值和待查询手机号创建输入框和对应的标签
label_tg_phone = tk.Label(root, text="TG手机号:")
label_tg_phone.grid(row=0, column=0)
entry_tg_phone = tk.Entry(root)
entry_tg_phone.grid(row=0, column=1)

label_api_id = tk.Label(root, text="API账号:")
label_api_id.grid(row=1, column=0)
entry_api_id = tk.Entry(root)
entry_api_id.grid(row=1, column=1)

label_api_hash = tk.Label(root, text="API哈希值:")
label_api_hash.grid(row=2, column=0)
entry_api_hash = tk.Entry(root)
entry_api_hash.grid(row=2, column=1)

label_query_phone = tk.Label(root, text="待查询手机号:")
label_query_phone.grid(row=3, column=0)
entry_query_phone = tk.Entry(root)
entry_query_phone.grid(row=3, column=1)

# 确认查询按钮
button_confirm = tk.Button(root, text="确认", command=check_inputs_and_call_function)
button_confirm.grid(row=4, column=1)

# 创建用于显示结果的文本框，并初始化为禁用状态
display_result = tk.Text(root, height=10, width=40, state=tk.DISABLED)
display_result.grid(row=5, column=0, columnspan=2)

# 运行GUI事件循环
root.mainloop()