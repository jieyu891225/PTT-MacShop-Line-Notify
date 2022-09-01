# PTT-MacShop-Notifier

###### *暑假與@jieyu891225協作的簡易小專案 —— 爬蟲+Line Notify實作。*

## 專案內容
透過Line-Notify訂閱Apple特定產品(如：Airpods)，在特定時間內將PTT Macshop板之新發布販售特定產品貼文時通知Line user。

## 使用須知
Windows版可搭配工作排程器，Linux、MacOS版需搭配Crontab定期執行達成即時通知效果，本系統搭配Heroku Scheduler達成定期傳送通知。

## 使用教學
### LINE Notify 設定教學
1. 在[LINE Notify](https://notify-bot.line.me/zh_TW/)中登入並進入 **個人頁面** 
2. 點選 **發行權杖** 並選擇要接收通知的**群組聊天室** 或選擇 **透過一對一聊天接收Line Notify通知** 獲取token後 **務必記下token** 離開後將不再顯示
3. 在程式碼裡面設定token，可以選擇一對一或加到現有群組內，即完成設定。

### Heroku 設定教學
1. 在[Heroku](https://www.heroku.com)官網建立帳號
2. 點選 **New** 後再點選 **create new app** 新增APP服務空間，並設定 **App name**與**region**後新增成功。
3. 在電腦安裝 **Git**與**Heroku CLI**套件以利後續使用

### 部署程式至Heroku 

##### 登入Heroku
```
heroku login
```
##### 建立Git資料夾
```
git init
```
##### 綁定Heroku APP服務空間
```
heroku git:remote -a APP Name
```

##### 上傳檔案指令
```
git add .
git commit -m "your message"
git push heroku master
```

#### 點選影片以跳轉到Youtube觀看Demo影片

[![IMAGE ALT TEXT](https://github.com/Emily-Weng/PTT-MacShop-Notifier/blob/main/line-notify.jpg)](https://www.youtube.com/watch?v=yw8b3av3hro "PTT-MacShop-Notifier成果展示")


#### 參考資料
* [LINE Notify 教學](https://ithelp.ithome.com.tw/articles/10282029)
* [Heroku 教學](https://ithelp.ithome.com.tw/articles/10246300?sc=rss.iron)
