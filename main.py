import json
import tkinter as tk
from tkinter import messagebox
from telegram_phone_number_checker import main as tg


def check_inputs_and_call_function():
    tg_phone = entry_tg_phone.get()
    api_id = entry_api_id.get()
    api_hash = entry_api_hash.get()
    query_phone = entry_query_phone.get()

    if not all([tg_phone, api_id, api_hash, query_phone]):
        messagebox.showerror("错误", "所有字段都必须填写！")
    else:
        # 假设函数AAA已定义并处理参数
        client = tg.login(api_id, api_hash, tg_phone)
        res = tg.validate_users(client, query_phone)
        result = json.dumps(res, indent=4)
        display_result.config(state=tk.NORMAL)
        display_result.delete(1.0, tk.END)
        display_result.insert(tk.END, result)
        display_result.config(state=tk.DISABLED)


# 初始化Tkinter窗口
root = tk.Tk()
root.title("查询工具")

# 创建输入框
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

# 确认按钮
button_confirm = tk.Button(root, text="确认", command=check_inputs_and_call_function)
button_confirm.grid(row=4, column=1)

# 显示框
display_result = tk.Text(root, height=10, width=40, state=tk.DISABLED)
display_result.grid(row=5, column=0, columnspan=2)

# 启动Tkinter事件循环
root.mainloop()
