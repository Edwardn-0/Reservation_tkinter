import tkinter as tk

window = tk.Tk()
window.title('Reservation')
window.geometry('250x150+100+100')

tables = []
selected_table = None

def reserve_screen(table_num):
    global setting, selected_table
    selected_table = table_num
    setting = tk.Toplevel()
    reserve_setting()

def reserve_setting():
    global name, confirm, purp
    label_name = tk.Label(setting, text='NAME: ')
    name = tk.Entry(setting)
    label_purp = tk.Label(setting, text='PURPOSE')
    purp = tk.Entry(setting)
    confirm = tk.Button(setting, text='CONFIRM', command=reserving)

    label_name.grid(row=0,column=0)
    name.grid(row=0,column=1)
    label_purp.grid(row=1,column=0)
    purp.grid(row=1,column=1)
    confirm.grid(row=2,column=1)

def already_setting(table_num):
    checked = tk.Toplevel()
    label_name = tk.Label(checked, text='NAME: ')
    set_name = table_num.cget('text')
    set_name = tk.Label(checked, text=set_name)
    label_purp = tk.Label(checked, text='PURPOSE')
    set_purp = getattr(table_num, 'purpose', 'NONE')
    set_purp = tk.Label(checked, text=set_purp)

    label_name.grid(row=0,column=0)
    set_name.grid(row=0,column=1)
    label_purp.grid(row=1,column=0)
    set_purp.grid(row=1,column=1)

def reserving():
    reserving_name = str(name.get())
    reserving_purpose = str(purp.get())
    selected_table.config(text=reserving_name, bg="#BFEFFF")
    selected_table.purpose = reserving_purpose
    setting.destroy()

for i in range(16):
    btn = tk.Button(window, text=f'table{i+1}')
    btn.config(command=lambda b=btn: reserve_screen(b))
    btn.bind('<Button-3>', lambda event, b=btn: already_setting(b))
    tables.append(btn)
    row_num = i // 4
    col_num = i % 4
    btn.grid(row=row_num, column=col_num, padx=5, pady=5)

window.mainloop()