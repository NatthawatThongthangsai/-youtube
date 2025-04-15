import os
import sys
from yt_dlp import YoutubeDL

# ฟังก์ชั่นสำหรับแสดงข้อความสีสันใน PowerShell
def colored_print(message, color_code):
    os.system(f"echo \033[{color_code}m{message}\033[0m")

# ฟังก์ชั่นดาวน์โหลด
def download_video(url):
    # หาพาธโฟลเดอร์ที่ไฟล์ .py อยู่
    current_folder = os.path.dirname(os.path.abspath(__file__))

    colored_print("เริ่มดาวน์โหลดคลิป...", 34)  # สีน้ำเงิน

    if not os.path.exists(current_folder):
        colored_print("โฟลเดอร์ไม่พบ! กรุณาตรวจสอบและลองใหม่.", 31)  # สีแดง
        return

    ydl_opts = {
        'outtmpl': f'{current_folder}/%(title)s.%(ext)s',
        'format': 'mp4',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        colored_print(f"ดาวน์โหลดเสร็จสิ้น! คลิปถูกบันทึกที่ {current_folder}", 32)  # สีเขียว
    except Exception as e:
        colored_print(f"เกิดข้อผิดพลาด: {str(e)}", 31)  # สีแดง

if __name__ == "__main__":
    colored_print("=========================================", 35)  # สีม่วง
    colored_print("ยินดีต้อนรับสู่ YouTube Downloader!", 36)  # สีฟ้า
    colored_print("=========================================", 35)  # สีม่วง
    url = input("กรุณาใส่ลิงก์ YouTube ที่ต้องการดาวน์โหลด: ")
    
    if not url:
        colored_print("กรุณาใส่ลิงก์ก่อนดาวน์โหลด.", 31)  # สีแดง
    else:
        download_video(url)
