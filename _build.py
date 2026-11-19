# おそうじチェックの公開用ページを作る（試作の中身を iPhone のホーム画面用に包む）
import io, sys
from PIL import Image
src, art = sys.argv[1], sys.argv[2]
body = io.open(src, encoding="utf-8").read()
body = body.replace('<title>SAMURAI おそうじチェック</title>', '').replace('<meta name="claude:viewport-fit-sides" content="cover">', '')
head = '''<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>おそうじ</title>
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="おそうじ">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#f3f4f6">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" href="icon-192.png">
<link rel="manifest" href="manifest.json">
<style>html,body{margin:0;padding:0}body{min-height:100vh;padding-top:env(safe-area-inset-top)}#demo{display:none}</style>
</head><body>
'''
tail = '''
<script>/* 見本ボタンは ?demo を付けたときだけ出す */if(location.search.indexOf("demo")>=0){var b=document.getElementById("demo");if(b)b.style.display="inline-block"}</script>
</body></html>'''
io.open("index.html", "w", encoding="utf-8").write(head + body + tail)
im = Image.open(art).convert("RGB")
w, h = im.size
sq = im.crop((0, 60, w, 60 + w))
for s in (180, 192, 512):
    sq.resize((s, s), Image.LANCZOS).save(f"icon-{s}.png")
io.open("manifest.json", "w", encoding="utf-8").write('{"name":"SAMURAI おそうじチェック","short_name":"おそうじ","start_url":"./","scope":"./","display":"standalone","background_color":"#f3f4f6","theme_color":"#f3f4f6","icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"}]}')
print("ok")
