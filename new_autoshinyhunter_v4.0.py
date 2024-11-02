import tkinter as tk
from tkinter import messagebox, scrolledtext, font
import json
import os
import webbrowser
import requests
import re
from bs4 import BeautifulSoup
import win32gui, win32api, win32con, win32ui
import time
import cv2
import subprocess
import pygetwindow as gw
from datetime import datetime
import uiautomator2 as u2
import base64
from PIL import Image, ImageTk
from io import BytesIO

# 檔案名稱：parameter.json，用來存儲字串的 JSON 文件，包含捕捉參數與爬蟲資料
file_name = "parameter.json"

# 檢查 parameter.json 是否存在，若存在則從 parameter.json 讀取字串並返回；若不存在則返回空字串
def load_saved_strings():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)  # 若存在則從 parameter.json 讀取字串並返回
    return {}                       # 若不存在則返回空字串

# 儲存字串字典到 parameter.json
def save_strings_to_file(strings):
    with open(file_name, "w") as file:
        json.dump(strings, file)

# 更新 IP 地址到字典
def update_ip_address(ip_address):
    # 先读取现有的字典
    stored_strings = load_saved_strings()

    # 更新字典
    stored_strings["ip"] = ip_address

    # 将更新后的字典保存到 JSON 文件
    save_strings_to_file(stored_strings)

# 以全域變數來儲存輸入的字串
stored_strings = load_saved_strings()
# 以全域變數來定義字串名稱
custom_names = ["channelid", "L_wanted", "more_check", "check_delay", "wifi_delay", "check_position", "male_and_female", "specific_pokemon", "phone_name", "DC_headers", "Pokedex100_header_Cookie_csrftoken", "Pokedex100_header_Cookie_sessionid"]
# 以全域變數來定義 labels 和 buttons
start_label_1 = None
start_label_2 = None
start_label_3 = None
start_label_4 = None
connect_phone_button = None
usb_connect_mode_button = None
wifi_connect_mode_button = None
usb_connected_button = None
wifi_connected_button = None
connect_mode = None
ip_label = None
ip_entry = None
ip_address = None
usb_disconnected_button = None
check_pokemon = None
new_coord_waiting = None
Pokedex100_url_temp = None

# 切換到首頁
def show_home_frame():
    parameter_frame.pack_forget()
    home_frame.pack(fill="both", expand=True)

# 切換到參數設定介面
def show_parameter_frame():
    global custom_names
    defult_strings = ["XXXXXXXXXXXXXXXXX", "0", "0", "2", "0", "0", "", "", "XXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXX_XX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]

    home_frame.pack_forget()
    parameter_frame.pack(fill="both", expand=True)

    # 清空之前的輸入框
    for entry in entry_boxes:
        entry.delete(0, tk.END)

    # 將已儲存的字串填入對應的輸入框
    for i, entry in enumerate(entry_boxes):
        try:
            entry.insert(0, stored_strings[custom_names[i]])  # 在輸入框中顯示已儲存的字串
        except:
            entry.insert(0, defult_strings[i])                # 在輸入框中顯示未儲存的預設字串

# 定義保存字串的功能
def save_strings():
    global stored_strings
    global custom_names

    new_strings = {custom_names[i]: entry.get().strip() for i, entry in enumerate(entry_boxes)}  # 使用字典來儲存字串

    # 過濾掉空字串
    # new_strings = {k: v for k, v in new_strings.items() if v}

    if new_strings:
        stored_strings.update(new_strings)      # 更新字典
        save_strings_to_file(stored_strings)    # 將字串字典保存到 parameter.json
        # messagebox.showinfo("儲存成功", f"已儲存 {len(new_strings)} 個字串。")
        show_home_frame()                       # 儲存後返回首頁
    else:
        messagebox.showwarning("輸入錯誤", "請輸入字串。")

def DC_crawler(): # DC爬蟲：https://youtu.be/xh28F6f-Cds
    r = requests.get(f"https://discord.com/api/v9/channels/{stored_strings['channelid']}/messages", headers={"Authorization": stored_strings["DC_headers"]})    # 選擇DC特定頻道爬蟲
    jsonn = json.loads(r.text)

    Pokedex100_url = re.findall(r"(https?://[^\s]+)", jsonn[0]["embeds"][0]["description"])[0][:-1]                                                         # 尋找Pokedex100網址
    Pokedex100_name = jsonn[0]["content"][jsonn[0]["content"].find("***") + 3:jsonn[0]["content"].find("***", jsonn[0]["content"].find("***") + 3)].strip()
    Pokedex100_CP = int(re.search(r'\*\*CP(\d+)\*\*', jsonn[0]["content"]).group(1))
    Pokedex100_L = int(re.search(r'\*\*L(\d+)\*\*', jsonn[0]["content"]).group(1))

    if re.search(r"(♂)", jsonn[0]["content"]) != None:
        Pokedex100_sex = "1"
    elif re.search(r"(♀)", jsonn[0]["content"]) != None:
        Pokedex100_sex = "0"
    else:
        Pokedex100_sex = "none"

    if "<a:shiny:622469442395439135>" in jsonn[0]["content"]:
        Pokedex100_symbol = True
    else:
        Pokedex100_symbol = False

    # print("DC_crawler test: ", Pokedex100_name, Pokedex100_CP, Pokedex100_L, Pokedex100_sex, Pokedex100_url)

    def is_catchable(Pokedex100_name, Pokedex100_L, Pokedex100_sex, Pokedex100_symbol):
        catchable = False   # 默认值
        criteria_count = 0  # 统计有值的指標数量
        catchable_count = 0 # 统计符合的指標数量

        # 检查等級
        if stored_strings["L_wanted"] != 0:
            criteria_count += 1
            if int(Pokedex100_L) >= int(stored_strings["L_wanted"]):                # 大于给定等級
                catchable_count += 1

        # 检查性別
        if stored_strings["male_and_female"] is not str():
            criteria_count += 1
            if Pokedex100_sex == stored_strings["male_and_female"]:                 # 性別相符
                catchable_count += 1

        # 检查特定種類
        if stored_strings["specific_pokemon"] is not str():
            specific_pokemon = [item.strip() for item in stored_strings["specific_pokemon"].split(",")]
            criteria_count += 1
            if Pokedex100_name in specific_pokemon:                                 # 包含在特定種類
                catchable_count += 1
        else:
            criteria_count += 1
            if Pokedex100_symbol:
                catchable_count += 1

        # print("criteria_count: ", criteria_count, "catchable_count: ", catchable_count)
        if criteria_count == 0 or criteria_count == catchable_count:
            catchable = True

        # 返回最终的可捕获状态
        return catchable

    catchable = is_catchable(Pokedex100_name, Pokedex100_L, Pokedex100_sex, Pokedex100_symbol)

    return catchable, Pokedex100_name, Pokedex100_CP, Pokedex100_L, Pokedex100_sex, Pokedex100_url

def Pokedex100_crawler(Pokedex100_url):
    Pokedex100_headers = {"Cookie": f"csrftoken={stored_strings['Pokedex100_header_Cookie_csrftoken']}; sessionid={stored_strings['Pokedex100_header_Cookie_sessionid']}"}
    resp = requests.get(Pokedex100_url, headers= Pokedex100_headers)    # 對 Pokedex100 網址爬蟲
    soup = BeautifulSoup(resp.text, "html.parser")
    coord_index = soup.find_all("input")
    coord = coord_index[0].get("value")                                 # 尋找座標
    # print(coord)
    return coord

# 获取 pokemon.json 数据
response = requests.get("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json")
pokemons = response.json()
def pokemon_json_translate(english_name):
    english_name = english_name.split()[-1]
    for pokemon in pokemons:
        if pokemon["name"]["english"].lower() == english_name.lower():
            return pokemon["name"]["chinese"]
    return None

def click_position(hwnd, x_position, y_position): # 點擊子句柄的相對座標
    """
    鼠標左鍵點擊座標
    :param hwnd:
    :param x_position:
    :param y_position:
    :return:
    """
    # 將兩個 16 位的值連接成一個 32 位的地址座標
    long_position = win32api.MAKELONG(x_position, y_position)
    win32api.SendMessage(hwnd, win32con.MOUSEEVENTF_LEFTDOWN, win32con.MOUSEEVENTF_LEFTUP, long_position)
    # 點擊左鍵
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(0.5)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)

def window_capture(filename, hwnd=0, pos=None):
    # 获取窗口设备上下文 DC（0 表示当前活跃窗口）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的 DC 获取 mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # 创建与 mfcDC 兼容的 DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建 bitmap 准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    monitor_info = win32api.EnumDisplayMonitors(None, None)
    # 获取屏幕尺寸
    screen_width = monitor_info[0][2][2]
    screen_height = monitor_info[0][2][3]

    # 判断是否指定区域截取
    if pos is None:
        x1, y1 = 0, 0                       # 从屏幕左上角开始
        w, h = screen_width, screen_height  # 截取整个屏幕
    else:
        x1, y1 = pos[0], pos[1]
        w, h = pos[2] - pos[0], pos[3] - pos[1]

    # 创建与屏幕尺寸一致的 bitmap
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 保存截图到 saveBitmap
    saveDC.SelectObject(saveBitMap)
    # 从指定位置（0, 0）截取指定大小的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (x1, y1), win32con.SRCCOPY)
    # 保存图片到文件
    saveBitMap.SaveBitmapFile(saveDC, filename)

    # 清除图片数据，防止内存泄漏
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

def find_picture(target_gray, template):
    # 获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    # 执行模板匹配，采用的匹配方式 cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target_gray, template, cv2.TM_SQDIFF_NORMED)
    # 归一化处理
    # cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1 )
    # 寻找矩阵（一维数组当做向量，用 Mat 定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 匹配值转换为字符串
    # 对于 cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED 方法 min_val 越趋近与 0 匹配度越好，匹配位置取 min_loc
    # 对于其他方法 max_val 越趋近于 1 匹配度越好，匹配位置取 max_loc
    strmin_val = str(min_val)
    # 绘制矩形边框，将匹配区域标注出来
    # min_loc：矩形定点
    # (min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    # (0,0,225)：矩形的边框颜色；2：矩形边框宽度
    cv2.rectangle(target_gray, min_loc, (min_loc[0] + twidth, min_loc[1] + theight),(0, 0, 225),2)
    # 显示结果,并将匹配值显示在标题栏上
    # cv2.imshow("MatchResult----MatchingValue="+strmin_val,target)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    X = min_loc[0]
    Y = min_loc[1]
    return X, Y, twidth, theight, min_val

# 定義開始程式的功能
def start_program():
    global start_label_1
    global start_label_2

    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 開始運行腳本！\n")
    start_button.pack_forget()                                          # 隐藏开始按钮
    start_label_1 = tk.Label(home_frame, text="", font=large_font)
    start_label_1.pack(pady=10)
    start_label_1.config(text="腳本正在執行...")                          # 显示字串
    start_label_2 = tk.Label(home_frame, text="")
    start_label_2.pack(pady=10)
    start_label_2.config(text="如果腳本出現錯誤或意外停止，請直接重啟腳本。")   # 显示字串
    console_output.update()

    home_frame.after(2000, run_exe)  # 開始運行腳本，接續開啟 NemoADB.exe

# 開啟 NemoADB.exe
def run_exe():
    console_output.insert(tk.END, " \n")

    # 自動或手動開啟 NemoADB.exe
    # 自動開啟 NemoADB.exe
    try:
        # win32api.ShellExecute(0, "open", ".\\NemoADB\\NemoADB.exe", "", "", 1)  # 启动 NemoADB.exe

        # 進入 NenoADB 資料夾，存取得到依賴的 dll 文件，NemoADB.exe 才能正常運行
        os.chdir(os.path.abspath(".\\NemoADB"))
        # 啟動 NemoADB.exe
        subprocess.Popen(".\\NemoADB.exe", shell=True, startupinfo=subprocess.STARTUPINFO())
        time.sleep(1)                       # 等待 NemoADB.exe 啟動
        os.chdir(os.path.abspath(".."))     # 回到預設資料夾

        # 获取 NemoADB.exe 窗口并最小化
        windows = gw.getWindowsWithTitle("NemoADB for GPS Joystick")
        if windows:
            console_output.insert(tk.END, "- 已自動開啟 NemoADB.exe，並將其最小化。\n")
            console_output.update()
            windows[0].minimize()           # 最小化窗口

    # 手動開啟 NemoADB.exe
    except Exception as e:
        console_output.insert(tk.END, "- 開啟 NemoADB.exe 失敗，請手動開啟。\n")
        console_output.update()

        def check_window_open():
            while True:
                time.sleep(1)                   # 每秒检查一次

                # 获取 NemoADB.exe 窗口并最小化
                windows = gw.getWindowsWithTitle("NemoADB for GPS Joystick")
                if windows:
                    console_output.insert(tk.END, "- 已手動開啟 NemoADB.exe，並將其最小化。\n")
                    console_output.update()
                    windows[0].minimize()       # 最小化窗口

                    break                       # 退出循环

        # 创建一个线程检查 NemoADB.exe 是否已手動開啟
        check_window_open()

    # 已開啟 NemoADB.exe，接續手機確認開啟
    phone_ready()

# 手機確認開啟
def phone_ready():
    global start_label_1
    global start_label_2
    global connect_phone_button

    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 請將手機啟用AtxAgent，\n  開啟GPS Joystick傳送至任意位置並隱藏，\n  開啟Pokemon Go並確認遊戲視角與記事本設定相同。\n")
    console_output.insert(tk.END, "- 確認完成後，直接點擊下方 手機已就緒！\n")
    console_output.update()

    # 隐藏原本的标签
    start_label_1.pack_forget()
    start_label_2.pack_forget()

    # 显示手機確認開啟按钮，接續連結手機
    connect_phone_button = tk.Button(home_frame, text="手機已就緒！", command=phone_connect)
    connect_phone_button.pack(pady=10)

# 連結手機
def phone_connect():
    global connect_phone_button
    global usb_connect_mode_button
    global wifi_connect_mode_button

    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 手機已就緒！\n")
    console_output.update()

    # 隐藏手機確認開啟按钮
    connect_phone_button.pack_forget()
    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 請點擊下方選擇手機連接模式，\n  USB連接：  請點擊 * USB-連接模式（建議）、\n  Wifi連接： 請點擊 * Wifi-連接模式。\n")
    console_output.update()

    # 顯示 USB 連接模式按鈕，接續 USB 連接模式
    usb_connect_mode_button = tk.Button(home_frame, text="* USB-連接模式", command=usb_connect)
    usb_connect_mode_button.pack(pady=10)

    # 顯示 Wifi 連接模式按鈕，接續 Wifi 連接模式
    wifi_connect_mode_button = tk.Button(home_frame, text="* Wifi-連接模式", command=wifi_connect)
    wifi_connect_mode_button.pack(pady=10)

# USB 連接模式
def usb_connect():
    global usb_connect_mode_button
    global wifi_connect_mode_button
    global usb_connected_button
    global connect_mode

    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "* USB-連接模式\n")
    connect_mode = 0
    console_output.update()

    usb_connect_mode_button.pack_forget()
    wifi_connect_mode_button.pack_forget()
    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 請將手機以USB接上電腦，允許USB偵錯。\n")
    console_output.insert(tk.END, "- 確認完成後，直接點擊下方 手機已連接！\n")
    console_output.update()

    # 顯示 USB 已連接按鈕，接續 USB 已連接
    usb_connected_button = tk.Button(home_frame, text="手機已連接！", command=usb_connected)
    usb_connected_button.pack(pady=10)

# Wifi 連接模式
def wifi_connect():
    global usb_connect_mode_button
    global wifi_connect_mode_button
    global wifi_connected_button
    global connect_mode
    global stored_strings
    global ip_label
    global ip_entry
    global ip_address

    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "* Wifi-連接模式\n")
    connect_mode = 1
    console_output.update()

    usb_connect_mode_button.pack_forget()
    wifi_connect_mode_button.pack_forget()
    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 請將手機連上Wifi並以USB接上電腦，允許USB偵錯，\n  並在下方輸入手機的IP位置。\n")
    console_output.insert(tk.END, "- 確認完成後，直接點擊下方 手機已連接！。\n")
    console_output.update()

    # 检查 "ip" 键是否存在于 stored_strings 中
    if "ip" in stored_strings:
        ip_address = stored_strings["ip"]
    else:
        ip_address = ""                     # 如果不存在，可以设置一个默认值

    # 创建 IP 输入框
    ip_label = tk.Label(home_frame, text="請輸入手機IP位置（需切換至英文輸入法）：")
    ip_label.pack(pady=5)
    ip_entry = tk.Entry(home_frame, width=20)
    ip_entry.pack(pady=5)
    ip_entry.insert(0, ip_address)    # 如果有保存的 IP，填入输入框

    # 顯示 Wifi 已連接按鈕，接續 ip 已輸入
    wifi_connected_button = tk.Button(home_frame, text="手機已連接！", command=ip_connected)
    wifi_connected_button.pack(pady=10)

# USB 已連接
def usb_connected():
    global usb_connected_button

    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 手機已連接！\n")
    console_output.update()

    usb_connected_button.pack_forget()
    start_label_1.pack(pady=10)
    start_label_2.pack(pady=10)
    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 即將投影手機，\n  若手機需要允許USB偵錯，請在允許USB偵錯後重啟腳本。\n  若投影失敗請檢查問題後重啟腳本。\n")
    console_output.insert(tk.END, " \n")
    console_output.update()
    console_output.see(tk.END)
    console_output.insert(tk.END, "- 請稍等，此時視窗可能暫時沒有回應，屬正常現象。\n")
    console_output.insert(tk.END, " \n")
    console_output.update()
    console_output.see(tk.END)

    subprocess.Popen("cd .\\scrcpy-win64-v2.7 && adb disconnect", shell=True, stdout=subprocess.PIPE)
    time.sleep(0.5)
    subprocess.Popen("cd .\\scrcpy-win64-v2.7 && scrcpy -t -b2M -m1080", shell=True, stdout=subprocess.PIPE)

    # 手機 adb 連線完成，接續 uiautomator2 連接手機
    u2_connect()

# ip 已輸入
def ip_connected():
    global wifi_connected_button
    global ip_label
    global ip_entry
    global ip_address
    global usb_disconnected_button

    ip_address = ip_entry.get()
    if ip_address:
        console_output.insert(tk.END, f" \n- 已輸入手機IP地址: {ip_address}。\n")
        console_output.update()

        # 隐藏 IP 输入框和确认按钮
        ip_label.pack_forget()
        ip_entry.pack_forget()
        wifi_connected_button.pack_forget()

        update_ip_address(ip_address)

        console_output.insert(tk.END, " \n")
        console_output.insert(tk.END, "- 手機已連接！\n")
        console_output.update()

        subprocess.Popen("cd .\\scrcpy-win64-v2.7 && adb disconnect", shell=True, stdout=subprocess.PIPE)
        time.sleep(0.5)
        subprocess.Popen("cd .\\scrcpy-win64-v2.7 && adb tcpip 5555", shell=True, stdout=subprocess.PIPE)
        time.sleep(0.5)

        console_output.insert(tk.END, " \n")
        console_output.insert(tk.END, "- 請將手機與電腦的USB連接拔除。\n")
        console_output.insert(tk.END, "- 確認完成後，直接點擊下方 手機已拔除！\n")
        console_output.update()

        # 顯示 USB 已拔除按鈕，接續 USB 已拔除
        usb_disconnected_button = tk.Button(home_frame, text="手機已拔除！", command=usb_disconnected)
        usb_disconnected_button.pack(pady=10)

# USB 已拔除
def usb_disconnected():
    global ip_address
    global usb_disconnected_button

    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 手機已拔除！\n")
    console_output.update()

    usb_disconnected_button.pack_forget()
    start_label_1.pack(pady=10)
    start_label_2.pack(pady=10)
    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "- 即將投影手機，\n  若手機需要允許USB偵錯，請在允許USB偵錯後重啟腳本。\n  若投影失敗請檢查問題後重啟腳本。\n")
    console_output.insert(tk.END, " \n")
    console_output.update()
    console_output.see(tk.END)
    console_output.insert(tk.END, "- 請稍等，此時視窗可能暫時沒有回應，屬正常現象。\n")
    console_output.insert(tk.END, " \n")
    console_output.update()
    console_output.see(tk.END)

    subprocess.Popen("cd .\\scrcpy-win64-v2.7 && adb connect " + ip_address + ":5555 && scrcpy -t -b2M -m1080", shell=True, stdout=subprocess.PIPE)
    time.sleep(1)
    NemoADB_hwnd = win32gui.FindWindow(None, u"NemoADB for GPS Joystick")           # 獲得 NemoADB 的句柄
    NemoADB_hwnd_wifi = win32gui.FindWindowEx(NemoADB_hwnd, 0, "Button", "WiFi")    # 獲得 NemoADB Wifi 的句柄
    click_position(NemoADB_hwnd_wifi,25, 25)

    # 手機 adb 連線完成，接續 uiautomator2 連接手機
    u2_connect()

# uiautomator2 連接手機
def u2_connect():
    global connect_mode
    global check_pokemon
    global new_coord_waiting
    check_pokemon = 0
    new_coord_waiting = 0

    start_time = datetime.now()
    console_output.insert(tk.END, f"~ 開始時間：{start_time}\n")
    console_output.see(tk.END)      # 自动滚动到最下方

    time.sleep(5)

    phone_hwnd = win32gui.FindWindow(None, stored_strings["phone_name"])    # 獲得手機的句柄
    NemoADB_hwnd = win32gui.FindWindow(None, u"NemoADB for GPS Joystick")   # 獲得 NemoADB 的句柄

    if (connect_mode == 0):
        d = u2.connect()            # uiautomator2 連接手機（手機要先安裝 ATXagent）
        # d.info
        wifi_delay = 0
    elif (connect_mode == 1):
        d = u2.connect(ip_address)
        # d.info
        wifi_delay = int(stored_strings["wifi_delay"])

    def get_device_resolution():
        try:
            result = subprocess.Popen("cd .\\scrcpy-win64-v2.7 && adb shell wm size", shell=True, stdout=subprocess.PIPE)
            result = result.communicate()
            resolution = result[0].decode("utf-8").strip().split(": ")[1]
            width, height = resolution.split("x")
            width = int(width)      # 转换为整数
            height = int(height)    # 转换为整数
        except:
            width = None
            height = None

        return width, height

    # screen_w = d.info["displayWidth"]
    # screen_h = d.info["displayHeight"]
    screen_w, screen_h = get_device_resolution()
    # print("screen_w: ", screen_w, "screen_h: ", screen_h)

    console_output.insert(tk.END, " \n")
    console_output.insert(tk.END, "~ 腳本正在執行。\n")
    console_output.insert(tk.END, "~ 若發現手機畫面無法自動點擊，\n  請開啟AtxAgent並手動點擊\"启动 UIAUTOMATOR\"，\n  再返回遊戲即可。\n")
    console_output.insert(tk.END, " \n")

    # 加載模板
    Shiny_Symbol_template = cv2.imread("templates\\Shiny_Symbol.jpg", 0)
    Weather_warning_template = cv2.imread("templates\\Weather_warning.jpg", 0)
    Youre_going_too_fast_template = cv2.imread("templates\\Youre_going_too_fast.jpg", 0)
    Home_Page_template = cv2.imread("templates\\Home_Page.jpg", 0)

    Pokedex100_url_temp = "0"

    NemoADB_hwnd_Edit = win32gui.FindWindowEx(NemoADB_hwnd, 0, "Edit", "")                  # 獲得 NemoADB 輸入框的句柄
    NemoADB_hwnd_START = win32gui.FindWindowEx(NemoADB_hwnd, 0, "Button", "   START   ")    # 獲得 NemoADB 傳送定位的句柄

    # 迴圈的非阻塞實現
    def main_loop():
        global check_pokemon, new_coord_waiting, Pokedex100_url_temp

        catchable, Pokedex100_name, Pokedex100_CP, Pokedex100_L, Pokedex100_sex, Pokedex100_url = DC_crawler()

        if catchable:
            if (Pokedex100_url != Pokedex100_url_temp):
                coord = Pokedex100_crawler(Pokedex100_url) # 取得座標
                Pokedex100_url_temp = Pokedex100_url

                console_output.insert(tk.END, f"~ Tp to：{coord}\n")
                Pokedex100_name_translate = pokemon_json_translate(Pokedex100_name)
                if Pokedex100_sex == "1":
                    print_sex = ", ♂"
                elif Pokedex100_sex == "0":
                    print_sex = ", ♀"
                else:
                    print_sex = ""
                if Pokedex100_name_translate is not None:
                    console_output.insert(tk.END, f"~ Name：{Pokedex100_name} ({Pokedex100_name_translate}), CP：{Pokedex100_CP}, L：{Pokedex100_L}{print_sex}\n")
                else:
                    console_output.insert(tk.END, f"~ Name：{Pokedex100_name}, CP：{Pokedex100_CP}, L：{Pokedex100_L}{print_sex}\n")
                console_output.see(tk.END)

                win32gui.SendMessage(NemoADB_hwnd_Edit, win32con.WM_SETTEXT, None, coord)  # 在 NemoADB 輸入框貼上 coord

                def click_START():
                    click_position(NemoADB_hwnd_START, 25, 25)  # 點擊傳送定位
                    click_position(NemoADB_hwnd_START, 25, 25)
                    home_frame.after(20000 + wifi_delay, find_alert_screenshot)

                home_frame.after(500, click_START)

                def find_alert_screenshot():
                    global check_pokemon, new_coord_waiting, start_label_1, start_label_2, start_label_3, start_label_4

                    window_capture(".\\screenshot\\alert_screenshot", phone_hwnd, pos=None)
                    target = cv2.imread(".\\screenshot\\alert_screenshot")
                    target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

                    _, _, _, _, min_val = find_picture(target_gray, Youre_going_too_fast_template)
                    # time.sleep(0.5)
                    if (abs(min_val) < abs(0.02)):
                        console_output.insert(tk.END,"~ You're going too fast alert !\n")
                        console_output.update()
                        console_output.see(tk.END)
                        d.click(screen_w / 2, screen_h * 0.65)
                        time.sleep(0.5 + wifi_delay)

                    _, _, _, _, min_val = find_picture(target_gray, Weather_warning_template)
                    # time.sleep(0.5)
                    if (abs(min_val) < abs(0.02)):
                        console_output.insert(tk.END,"~ Weather warning alert !\n")
                        console_output.update()
                        console_output.see(tk.END)
                        d.click(screen_w / 2, screen_h * 0.65)
                        time.sleep(0.5 + wifi_delay)

                    time.sleep(0.5)

                    def click_in_directions(center_x, center_y, offset, wifi_delay):
                        # 中心
                        d.click(center_x, center_y)
                        time.sleep(0.5 + wifi_delay)
                        # 上
                        d.click(center_x, center_y - offset)
                        # 下
                        d.click(center_x, center_y + offset)
                        # 左
                        d.click(center_x - offset, center_y)
                        # 右
                        d.click(center_x + offset, center_y)
                        time.sleep(0.5 + wifi_delay)
                        # 左上
                        d.click(center_x - offset, center_y - offset)
                        # 右上
                        d.click(center_x + offset, center_y - offset)
                        # 左下
                        d.click(center_x - offset, center_y + offset)
                        # 右下
                        d.click(center_x + offset, center_y + offset)
                        time.sleep(0.5 + wifi_delay)

                    if (int(stored_strings["check_position"]) == 0):
                        click_in_directions(screen_w / 2, screen_h * 0.75, 110, wifi_delay)

                    elif (int(stored_strings["check_position"]) == 1):
                        click_in_directions(screen_w / 2, screen_h * 0.62, 60, wifi_delay)

                    time.sleep(4 + wifi_delay)
                    check_pokemon = check_pokemon + 1
                    console_output.insert(tk.END, f"~ Checked：{check_pokemon}\n")
                    console_output.update()
                    console_output.see(tk.END)

                    window_capture(".\\screenshot\\catch_screenshot", phone_hwnd, pos=None)
                    target = cv2.imread(".\\screenshot\\catch_screenshot")
                    target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

                    _, _, _, _, min_val = find_picture(target_gray, Shiny_Symbol_template)
                    if (abs(min_val) < abs(0.03)):
                        console_output.insert(tk.END, " \n")
                        console_output.insert(tk.END, "~ !!! Shiny !!!\n")
                        console_output.insert(tk.END, " \n")
                        console_output.update()
                        console_output.see(tk.END)
                        end_time = datetime.now()
                        console_output.insert(tk.END, f"~ 結束時間：{end_time}\n")
                        console_output.insert(tk.END, " \n")
                        console_output.insert(tk.END, "~ Please STOP the code !\n")
                        console_output.update()
                        console_output.see(tk.END)
                        # 隐藏原本的标签
                        start_label_1.pack_forget()
                        start_label_2.pack_forget()
                        start_label_3 = tk.Label(home_frame, text="", font=large_font)
                        start_label_3.pack(pady=10)
                        start_label_3.config(text="色違出現！")
                        start_label_4 = tk.Label(home_frame, text="")
                        start_label_4.pack(pady=10)
                        start_label_4.config(text="請檢查是否點擊到正確的寶可夢！")  # 显示字串
                        return
                    else:
                        console_output.insert(tk.END, "~ Not Shiny or Clicked Error !\n")
                        console_output.update()
                        console_output.see(tk.END)

                    for t in range(0, int(stored_strings["more_check"])):
                        time.sleep(int(stored_strings["check_delay"]) + wifi_delay)
                        window_capture(".\\\\screenshot\\more_check_screenshot_" + str(t), phone_hwnd, pos=None)
                        target = cv2.imread(".\\screenshot\\more_check_screenshot_" + str(t))
                        target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

                        _, _, _, _, min_val = find_picture(target_gray, Shiny_Symbol_template)
                        if (abs(min_val) < abs(0.03)):
                            console_output.insert(tk.END, " \n")
                            console_output.insert(tk.END, "~ !!! Shiny !!!\n")
                            console_output.insert(tk.END, " \n")
                            end_time = datetime.now()
                            console_output.insert(tk.END, f"~ 結束時間：{end_time}\n")
                            console_output.insert(tk.END, " \n")
                            console_output.insert(tk.END, "~ Please STOP the code !\n")
                            console_output.update()
                            console_output.see(tk.END)
                            # 隐藏原本的标签
                            start_label_1.pack_forget()
                            start_label_2.pack_forget()
                            start_label_3 = tk.Label(home_frame, text="", font=large_font)
                            start_label_3.pack(pady=10)
                            start_label_3.config(text="色違出現！")
                            start_label_4 = tk.Label(home_frame, text="")
                            start_label_4.pack(pady=10)
                            start_label_4.config(text="請檢查是否點擊到正確的寶可夢！")  # 显示字串
                            return
                        else:
                            console_output.insert(tk.END, "~ Not Shiny or Clicked Error !\n")
                            console_output.update()
                            console_output.see(tk.END)

                    home_page_flag = 1
                    while (home_page_flag):
                        window_capture(".\\screenshot\\temp_screenshot", phone_hwnd, pos=None)
                        target = cv2.imread(".\\screenshot\\temp_screenshot")
                        target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

                        _, _, _, _, min_val = find_picture(target_gray, Home_Page_template)
                        if (abs(min_val) > abs(0.02)):
                            d.press("back")
                            time.sleep(1)
                        else:
                            home_page_flag = 0

                    console_output.insert(tk.END, " \n")
                    console_output.see(tk.END)
                    # d.click(screen_w * 0.09, screen_h * 0.11)
                    time.sleep(wifi_delay)
                    new_coord_waiting = 0

                    # 使用 after 繼續下一次迴圈
                    home_frame.after(500, main_loop)

            else:
                wait_for_new_coord()
                # 使用 after 繼續下一次迴圈
                home_frame.after(500, main_loop)
        else:
            wait_for_new_coord()
            # 使用 after 繼續下一次迴圈
            home_frame.after(500, main_loop)

    def wait_for_new_coord():
        global new_coord_waiting

        new_coord_waiting += 1
        if (new_coord_waiting == 1):
            console_output.insert(tk.END, "~ No new coord, waiting")
            console_output.update()
            console_output.see(tk.END)
            time.sleep(0.5)
            console_output.insert(tk.END, " .")
            console_output.update()
            console_output.see(tk.END)
            time.sleep(0.5)
            console_output.insert(tk.END, " .")
            console_output.update()
            console_output.see(tk.END)
            time.sleep(0.5)
            console_output.insert(tk.END, " .\n")
            console_output.update()
            console_output.see(tk.END)
            console_output.insert(tk.END, " \n")
            console_output.update()
            console_output.see(tk.END)
        else:
            time.sleep(0.5)

    # 使用 after 繼續下一次迴圈
    home_frame.after(500, main_loop)

# 定義參數設定功能
def setting():
    global custom_names

    show_parameter_frame()

    # 跳出參數教學
    # ------------------------------------------------------------
    tutorial_window = tk.Toplevel(root)     # 创建一个新的 Toplevel 窗口
    tutorial_window.title("參數教學")
    tutorial_window.geometry("1000x550")    # 设置窗口大小
    # ---------參數教學的內容---------
    title = ("這裡是參數教學，請依照此至參數設定 設定捕捉參數與爬蟲資料！")
    messages = {
        "channelid": "   channelid：想要爬蟲的DC伺服器中Pokedex100的頻道ID，\n                          在網頁版DC伺服器中Pokedex100的頻道的 F12 - Network - message?limit=50 - Request URl，\n                          或網頁版DC伺服器中Pokedex100的頻道的網址最後一段數字。",
        "L_wanted": "   L_wanted：想要捕捉的寶可夢至少等級。（限整數，預設為0）",
        "more_check": "   more_check：想要多確認寶可夢是不是色違的次數（建議取決於該寶可夢的跳躍頻率）。（限整數，預設為0）",
        "check_delay": "   check_delay：想要多確認寶可夢是否色違的間隔（建議取決於該寶可夢的上下移動頻率）。（限整數，預設為2）",
        "wifi_delay": "   wifi_delay：使用Wifi-連接模式時想要多等待的延遲時間（取決於網路速度）。（限整數，預設為0）",
        "check_position": "   check_position：遊戲視角畫面最大化時設置為0；遊戲視角畫面最小化時則設置為1（適合會飛行則不在腳邊的寶可夢，ex：飛翔皮卡丘）。（限0、1，預設為0）",
        "male_and_female": "   male_and_female：若想要捕捉特定性別的寶可夢，公的設置為1；母的設置為0；若不指定，則空白。（限0、1和空白，預設為空白）",
        "specific_pokemon": "   specific_pokemon：若在DC伺服器中Pokedex100的頻道中含有多種寶可夢但只想抓取特定幾種時；或在DC伺服器中Pokedex100的頻道中的寶可夢異常不具有色違符號時，\n                                          打上寶可夢名字（寶可夢間以半形逗號（需切換至英文輸入法）相隔，ex：Cranidos,Hisuian Voltorb,Larvitar）；若無，則空白。",
        "phone_name": "   phone_name：手機在scrcpy的視窗名。",
        "DC_headers": "   DC_headers：網頁版DC的授權碼，在網頁版DC的 F12 - Network - message?limit=50 - Headers - authorization。",
        "Pokedex100_header_Cookie_csrftoken": "   Pokedex100_header_Cookie_csrftoken：Pokedex100的Cookie，在Pokedex100座標網頁的 F12 - Network - Document - Headers - Cookie - csrftoken。",
        "Pokedex100_header_Cookie_sessionid": "   Pokedex100_header_Cookie_sessionid：Pokedex100的Cookie，在Pokedex100座標網頁的 F12 - Network - Document - Headers - Cookie - sessionid。"
    }

    tutorial_label_1 = tk.Label(tutorial_window, text=title, wraplength=1000, font=medium_font)
    tutorial_label_1.pack(pady=5)
    for name in custom_names:
        message = messages[name]                        # 获取对应的消息内容
        tutorial_label_2 = tk.Label(tutorial_window, text=message, wraplength=1000, justify="left")
        tutorial_label_2.pack(pady=5, anchor="w")       # 添加标签到窗口中
    tutorial_label_3 = tk.Label(tutorial_window, text="      如果對於參數教學仍不清楚，可以參考：", wraplength=1000)
    tutorial_label_3.pack(pady=5, anchor="w")           # 添加标签到窗口中

    def open_link(event):
        # 在这里放置您的链接
        webbrowser.open("https://github.com/peter890331/new_autoshinyhunter_gui_version")  # 例如：打开一个网页链接

    # 创建一个超链接
    link = tk.Label(tutorial_window, text="                                                 GitHub", fg="blue", cursor="hand2", font=medium_font)  # 设置文本颜色和光标样式
    link.pack(pady=10, anchor="w")
    link.bind("<Button-1>", open_link)  # 绑定点击事件，打开链接
    # -------------------------
    # ------------------------------------------------------------

# 定義作者介紹功能
def author():
    # 跳出作者介紹
    # ------------------------------------------------------------
    author_window = tk.Toplevel(root)  # 创建一个新的 Toplevel 窗口
    author_window.title("作者介紹")
    author_window.geometry("500x360")  # 设置窗口大小
    # ---------參數教學的內容---------
    title = "new_autoshinyhunter_v4.0, made by Peter Yu."
    author_label_1 = tk.Label(author_window, text=title, wraplength=500, font=medium_font)
    author_label_1.pack(pady=12)
    author_label_2 = tk.Label(author_window, text="您好，我是 Peter Yu。\n寫下這段話的日期是 2024 年 11 月 2 日，\n這時我正處於研究所三年級（超級可悲qq）。\n這是我自製的一個在 Pokémon GO 中自動點擊色違且 iv100 的寶可夢的外掛腳本。\n隨著年紀增長，我深知自己能夠投入 Pokémon GO 的時間只會越來越少，\n因此想透過這個腳本幫助自己自動點擊色違且 iv100 的寶可夢。\n玩了八年，仍然難以割捨對於這款遊戲的熱情。\n之前曾做過一個運行在 CMD 上的版本，而這是帶有 GUI 的升級版，\n使用 Python 編寫，希望您喜歡。\n")
    author_label_2.pack(pady=5)
    author_label_3 = tk.Label(author_window, text="❗ 警告：僅以此練習程式編寫，請勿在遊戲中使用外掛，否則後果自負！本人對此內容不負任何法律責任。 ❗\n"
                                                  "❗ WARNING: Practice programming only, please do not use it to cheat on the game! ❗\n"
                                                  "❗ The consequences are your own! I will not be responsible for any law liability to this content. ❗\n",
                              font=small_font)
    author_label_3.pack(pady=5)
    author_label_4 = tk.Label(author_window, text="      如果對於我的背景還感興趣，可以點擊查看更多：", wraplength=1000)
    author_label_4.pack(pady=5, anchor="w")

    def open_link(event):
        # 在这里放置您的链接
        webbrowser.open("https://github.com/peter890331")   # 例如：打开一个网页链接

    # 创建一个超链接
    link = tk.Label(author_window, text="                                                              GitHub", fg="blue", cursor="hand2", font=medium_font)                       # 设置文本颜色和光标样式
    link.pack(pady=10, anchor="w")
    link.bind("<Button-1>", open_link)                      # 绑定点击事件，打开链接
    # -------------------------
    # ------------------------------------------------------------

# 建立 GUI
root = tk.Tk()
root.title("new_autoshinyhunter_v4.0")
root.geometry("500x820")                                    # 調整 GUI 大小

# 嵌入图标的方法
icon_base64 = "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"
icon_data = base64.b64decode(icon_base64)
icon_image = Image.open(BytesIO(icon_data))
icon_tk = ImageTk.PhotoImage(icon_image)
root.tk.call('wm', 'iconphoto', root._w, icon_tk)

# 定義首頁 Frame
home_frame = tk.Frame(root)
home_frame.pack(fill="both", expand=True)

# 定義輸入介面 Frame
parameter_frame = tk.Frame(root)

# 创建大字体
large_font = font.Font(size=16, weight="bold")   # 设置大号字体，粗体
# 创建中字体
medium_font = font.Font(size=12, weight="bold")  # 设置中号字体，粗体
# 创建小字体
small_font = font.Font(size=7)  # 设置小号字体

# ---------首頁內容---------
home_label_1 = tk.Label(home_frame, text="歡迎使用 new_autoshinyhunter_4.0 👍", font=large_font)
home_label_1.pack(pady=12)
home_label_2 = tk.Label(home_frame, text="感謝支持，祝您收穫滿滿！")
home_label_2.pack(pady=5)
home_label_3 = tk.Label(home_frame, text="❗ 警告：僅以此練習程式編寫，請勿在遊戲中使用外掛，否則後果自負！本人對此內容不負任何法律責任。 ❗\n"
                                         "❗ WARNING: Practice programming only, please do not use it to cheat on the game! ❗\n"
                                         "❗ The consequences are your own! I will not be responsible for any law liability to this content. ❗\n", font=small_font)
home_label_3.pack(pady=5)

# 控制台輸出框
console_output = scrolledtext.ScrolledText(home_frame, width=60, height=40, state="normal")
console_output.pack(pady=10)
console_output.insert(tk.END, "- new_autoshinyhunter_v4.0 - made by Peter Yu.\n\n")  # 在控制台輸出框中顯示信息
console_output.insert(tk.END, "- 開始運行腳本前，請先記得先至左上角參數設定，\n  設定捕捉參數與爬蟲資料（csrftoken和sessionid偶爾需更新）。\n")
console_output.insert(tk.END, "- 確認設定完成後，直接點擊下方 開始運行腳本！\n")

# 開始按鈕
start_button = tk.Button(home_frame, text="開始運行腳本！", command=start_program)
start_button.pack(pady=10)
# -------------------------

# ---------輸入介面的內容---------
entry_boxes = []
input_label_1 = tk.Label(parameter_frame, text="這裡是參數設定，請依照參數教學 設定捕捉參數與爬蟲資料！", font=medium_font)
input_label_1.pack(pady=5)

for i in range(12):                                 # 假設需要12個輸入框
    input_label_2 = tk.Label(parameter_frame, text=f"       請輸入 {custom_names[i]}：")
    input_label_2.pack(pady=3.5, anchor="nw")

    entry = tk.Entry(parameter_frame, width=50)     # 将输入框的宽度设置为 50
    entry.pack(pady=5)
    entry_boxes.append(entry)                       # 將每個輸入框加入列表

save_button = tk.Button(parameter_frame, text="儲存", command=save_strings)
save_button.pack(pady=10)
# -------------------------

# 建立選單
menu_bar = tk.Menu(root)

# 建立選單
menu_bar.add_cascade(label="參數設定", command=setting)
menu_bar.add_cascade(label="作者介紹", command=author)

# 將選單配置到主視窗
root.config(menu=menu_bar)

# 处理关闭事件
def on_closing():
    if messagebox.askokcancel("退出腳本", "確定要退出腳本嗎？"):
        root.destroy()                                  # 使用 destroy() 方法关闭窗口

root.protocol("WM_DELETE_WINDOW", on_closing)     # 处理窗口关闭事件

# 顯示首頁
show_home_frame()

# 啟動主事件迴圈
root.mainloop()