from tkinter import Tk, filedialog
from minio import Minio
from minio.error import S3Error
from urllib3 import PoolManager
import urllib3

# 域名
domain = "" 

# 桶名
bucket_name = ""

# 禁用不安全请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 创建一个不验证SSL证书的HTTP客户端
http_client = PoolManager(cert_reqs='CERT_NONE', assert_hostname=False)

# 初始化Minio客户端时使用上面创建的HTTP客户端
minioClient = Minio(
    "",
    access_key="",
    secret_key="",
    secure=True,
    http_client=http_client
)

# 弹出窗口选择文件
def choose_file():
    root = Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename()  # 弹出文件选择窗口
    root.destroy()  # 关闭主窗口
    return file_path

# 上传文件到存储桶
def upload_file_to_minio(bucket_name, file_path, object_name):
    try:
        minioClient.fput_object(bucket_name, object_name, file_path)
        print(f"Successfully uploaded {object_name} to {bucket_name}")
    except S3Error as e:
        print(f"Error uploading {object_name}: {e}")

# 获取文件链接
def get_file_url(bucket_name, object_name):
    return f"{domain}/{bucket_name}/{object_name}"

# 上传文件并获取链接
file_path = choose_file()  # 选择文件
object_name = file_path.split("/")[-1]  # 使用文件名作为对象名称

if file_path:
    upload_file_to_minio(bucket_name, file_path, object_name)
    file_url = get_file_url(bucket_name, object_name)
    print(f"File URL: {file_url}")
