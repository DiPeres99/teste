import speedtest

def testar_velocidade_internet():
    st = speedtest.Speedtest()
    
    print("Testando velocidade de internet:")
    velocidade_download = st.download() / 10**6
    print(f"Velocidade de internet: {velocidade_download}MB") 
    
    print("Teste velocidade de upload:")
    velocidade_upload = st.upload() / 10**6
    print(f"Velocidade de upload: {velocidade_upload}MB")
    
    print("Testando ping")
    servidor = st.get_best_server()
    ping = servidor['latency']
    print(f"Ping: {ping}MS")

testar_velocidade_internet()