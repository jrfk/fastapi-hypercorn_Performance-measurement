# 概要
ASGI web サーバーであるHypercornを使って、FastAPIを使って
* HTTP/1.1、HTTP/2のストリームの性能を測定する
* HTTP/2 のストリームを体感する

for PyCon mini Hiroshima  
[Pycon mini Hiroshima](https://hiroshima.pycon.jp/2020/speaker/JunyaFff)  

Python 3.8.1 を利用

# オレオレな鍵を作る

```
brew install mkcert
mkcert -install
mkcert example.com  localhost 127.0.0.1 ::1
```

ファイルができているのをご確認ください。
* example.com+3-key.pem
* example.com+3.pem

それぞれrenameしてください。

 * example.com+3-key.pem  → key.pem
 * example.com+3.pem → cert.pem


# Usage 

```
pip install hypercorn fastapi
```

HTTP2での動作させる場合  
```
hypercorn --config=h2_config.py httptest.asgi:asyncio_app
```

HTTP/1.1で動作させる場合
```
hypercorn --config=h11_config.py httptest.asgi:asyncio_app
```

# ストリーム
* ブラウザでそれぞれにアクセス
* デバッガを開き、ボタンを押下

# 性能測定
```
yum -y install epel-release
yum -y install nghttp2
```

## 性能を測定する  
* HTTP/2の場合
```
h2load -c 100 -n 10000 -m 5 https://127.0.0.1:5500/query
```

* HTTP/1.1の場合
```
h2load -p http/1.1 -c 100 -n 10000  https://127.0.0.1:5000/query
```


