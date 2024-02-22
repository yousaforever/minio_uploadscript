import tkinter as tk
from tkinter import filedialog
from minio import Minio
from minio.error import S3Error

# 域名
domain = "https://"

# 桶名
bucket_name = "lfs"

# 连接到Minio服务
minioClient = Minio(
    "", # 域名/IP
    access_key="",
    secret_key="",
    secure=True # 是否启用TLS加密
)

# 上传文件到存储桶
def upload_file_to_minio(bucket_name, file_path, object_name):
    try:
        minioClient.fput_object(bucket_name, object_name, file_path)
        print(f"Successfully uploaded {object_name} to {bucket_name}")
    except S3Error as e:
        print(f"Error uploading {object_name}: {e}")

# 获取文件链接
def get_file_url(bucket_name, object_name):
    return f"{domain}/{bucket_name}/{object_name}" #

# 创建GUI窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 打开文件选择对话框
file_path = filedialog.askopenfilename()

if file_path:
    # 获取文件名
    file_name = file_path.split("/")[-1]

    # 上传文件并获取链接
    object_name = file_name

    upload_file_to_minio(bucket_name, file_path, object_name)
    file_url = get_file_url(bucket_name, object_name)
    print(f"File URL: {file_url}")
