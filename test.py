import webview
inHtml ="""
    <!doctype html>
    <html>
        <head></head>
        <body>
            테스트 페이지
        </body>
    </html>

"""

webview.create_window("테스트버전",height=500,width=300,html=inHtml)

webview.start()