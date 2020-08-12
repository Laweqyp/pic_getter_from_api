import requests
import time

global req
download_sus = ">>>>>>>>>>>>>>>>>>>>"
download_not = "                    "


def request_download(path, url):
    download_time_start = time.time()

    def format_size(_b):
        try:
            _b = float(_b)
            _kb = _b / 1024
        except BaseException as _exp:
            return "-1"
        if _kb >= 1024:
            _m = _kb / 1024
            return "%.3fM/s" % _m
        else:
            return "%.3fK/s" % _kb

    connect_attempt = 0
    while connect_attempt < 10:
        try:
            req = requests.get(url, timeout=15, stream=True)
        except BaseException as exp:
            print(exp, " Try Attempt:", connect_attempt + 1)
            connect_attempt += 1
            if connect_attempt < 10:
                continue
            else:
                print("Failed to establish a connection with the giving URL.")
                return
        else:
            break

    download_attempt = 0
    while download_attempt < 10:
        try:
            last_time = time.time()
            src_size = int(req.headers['content-length'])
            chunk_size = 65536
            current_bytes = 0
            print("Size : %0.2f MB" % (src_size / (1024 * 1024)))

            f = open(path, "wb")
            for chunk in req.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    current_bytes += len(chunk)

                    now_time = time.time()
                    interval = abs(now_time - last_time + 0.005)
                    last_time = now_time
                    speed = len(chunk) / interval
                    m, s = divmod(src_size / speed, 60)
                    h, m = divmod(m, 60)
                    eta = "%d:%02d:%02d" % (h, m, s)
                    print("\r" + "Downloading : %s | %.2f%% %s , ETA:%s" % (
                        download_sus[0:int(current_bytes * 20 / src_size)] +
                        download_not[int(current_bytes * 20 / src_size):],
                        float(current_bytes / src_size * 100), format_size(speed), eta), end=' ')

                    if current_bytes >= src_size:
                        download_attempt = 10
                        print("\nDownload successfully in %.2fs" % (time.time() - download_time_start))
                        break
        except BaseException as exp:
            print(exp, " Try Attempt:", download_attempt + 1)
            time.sleep(5)
            download_attempt += 1
            if download_attempt < 10:
                continue
        finally:
            try:
                f.close()
            except BaseException as exp:
                print(exp)


# request_download("./test.png", "https://i.pixiv.cat/img-original/img/2018/11/11/09/29/01/71600764_p0.png")
# 13.32MB:https://i.pixiv.cat/img-original/img/2020/07/03/12/53/18/82720477_p0.jpg
