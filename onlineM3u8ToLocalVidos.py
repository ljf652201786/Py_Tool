import os
import requests
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/72.0.3626.109 Safari/537.36",
}

def get_url_content():
    '''获取m3u8文件的内容并放入内存'''
    m3u8_target = input('输入m3u8对应URL:').strip()
    target = '/'.join(m3u8_target.split('/')[:-1])
    # print(target)
    m3u8_res = requests.get(m3u8_target,headers)
    if m3u8_res.status_code != 200:
        print('URL不能正常访问', m3u8_res.status_code)
    m3u8_content = m3u8_res.content.decode('utf8')
    return m3u8_content,target


def read_m3u8(m3u8_content):
    '''获取m3u8中的下载连接'''
    media_url_list = []
    lines_list = m3u8_content.strip().split('\r\n')
    if len(lines_list) < 3:
        lines_list = m3u8_content.strip().split('\n')
    if '#EXTM3U' not in m3u8_content:
        raise BaseException('非M3U8连接')
    for index,line in enumerate(lines_list):
        # print(index,line)
        if '#EXTINF' in line:
            media_url_list.append(lines_list[index+1])
    return media_url_list


def download_media(url_list,target,dir_path):
    '''下载媒体文件'''
    for index,url in enumerate(url_list):
        try:
            res = requests.get(url,headers)
        except requests.exceptions.MissingSchema:  #捕获不完整URL的异常
            target_url =target+'/'+url
            res = requests.get(target_url,headers)
        media_file_path = dir_path+'full_media.mp4'
        if res.status_code != 200:
            print('下载URL连接访问失败')
            break
        with open(media_file_path,'ab')as f:
            f.write(res.content)
        print('下载进度：%.1f%%' % ((index + 1) / len(url_list) * 100))
    flag = False
    if index == len(url_list) - 1:
        flag = True
    return flag


def main():
    file_name = input("输入媒体名称:")
    dir_path = mkdir(file_name)       #创建媒体名命名的文件夹
    m3u8_content,target = get_url_content()
    media_url_list = read_m3u8(m3u8_content)
    flag = download_media(media_url_list,target, dir_path) #  用于校验是否成功下载媒体文件
    if flag:
        print('媒体下载完成')
    else:
        print('媒体下载失败')
    print("*"*16)
def mkdir(path):
    path = path.strip().rstrip('\\')
    is_exists = os.path.exists(path)
    if not is_exists:      # 校验目录是否存在
        os.makedirs(path)
        print('创建媒体目录')
    else:
        print('媒体目录已经存在')
    return path+'/'
if __name__ == '__main__':
    
    while True:
        main()
