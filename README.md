# access_controlled_service
##server.py 
サーバの作成。

* /api/tweetでツイート可能
* /api/lineでline通知可能
* /api/slackでbot通知可能
* /でサーバとのConnection確認可能
* 現在の人数を記憶

##raspi_sender.py
rasbperry piからサーバに現在の人数をPOSTする
