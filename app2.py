
import speedtest

speed = speedtest.Speedtest()

def bytes_para_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes/MB)

velocidade_download = speed.download()
velocidade_upload = speed.upload()

print(f"Velocidade de download: {bytes_para_mb(velocidade_download)}MB")
print(f"Velocidade de upload:{bytes_para_mb(velocidade_upload)}MB")