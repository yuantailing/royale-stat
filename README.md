# royale-stat
皇室战争部落成员活跃度统计

## usage

```sh
$ pip install -r requirements.txt
$ cp settings.py.sample settings.py  # please edit TOKEN and CLAN
$ python update.py
```

然后浏览 [www/index.html](www/index.html)。（因为浏览器同源策略限制，请开启 `python -m SimpleHTTPServer` 或 `python -m http.server` 后在 [http://localhost:8000/](http://localhost:8000/) 浏览）

定时运行 `python crawl.py`（例如每 10 分钟运行一次）以保存捐赠数、杯数的历史统计。

## todo

 - [x] 部落总计的统计图
 - [x] 循环爬取数据，并保存
 - [x] 杯数曲线图
 - [x] 捐赠曲线图
 - [x] 统计成员活跃时间
