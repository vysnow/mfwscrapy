# MFWScrapy

## 项目idea
这是一个学习Scrapy和Django的项目，使用python3.11抓取MFW的景点数据，并在web展示。

## 下载体验
1. 拉取代码
```
% git clone git@github.com:vysnow/mfwscrapy.git
```

2. 进入项目目录并开启虚拟环境
```
% make env
```

3. 安装依赖
```
% make prepare
```

4. 迁移db
```
% make migrate
```

5. 爬取数据
```
% make crawl SQ=chenzhou
```

6. 运行展示
```
% make serve
```

## 运行效果
![screenshot.gif](https://github.com/vysnow/mfwscrapy/blob/main/screenshot.gif)

## Todos
- [ ] 开发django admin管理页面；
- [ ] 将`scrapy scrawl`如果能结合到web中就方便；
- [ ] 处理景点的详情页面的反爬处理，导致想抓取图片、门票、开放时间等详情时遇阻（error 521)，需要研究：
```
[scrapy.core.engine] DEBUG: Crawled (521) <GET https://www.mafengwo.cn/poi/8090261.html> (referer: https://www.mafengwo.cn/jd/10792/gonglve.html)
[mdd] ERROR: HttpError on https://www.mafengwo.cn/poi/8090261.html
```
- [ ] 增加登录功能
- [ ] 增加路径图规划，输入若干景点，完成行程安排（AI）

## 声明
此项目仅供学习和记录，请勿用于恶意或商业。