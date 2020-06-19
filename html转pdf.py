import pdfkit

#自定义参数

options={
    'page-size':'A4',    # 默认是A4 Letter  etc
    'margin-top':'0.05in',   #顶部间隔
    'margin-right':'0.05in',   #右侧间隔
    'margin-bottom':'0.05in',   #底部间隔
    'margin-left':'0.05in',   #左侧间隔
    'encoding':"UTF-8",   #文本个数
    'dpi':'96',
    'image-dpi':'600',
    'image-quality':'94',
    'footer-font-size':'12',   #字体大小
    'no-outline':None
}
pdfkit.from_url('https://www.baidu.com/','out.pdf', options=options)
