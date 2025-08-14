""" import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000 # in Mbs
    upload_speed = st.upload() / 1_000_000 # in Mbs

    if download_speed < 20 or upload_speed < 20:
        print("Speak 2")
    else:
        print("Speak Edge")

# Calling the funstion to check internet speed
check_internet_speed() """