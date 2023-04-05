# YOLOv5を用いた駐輪場管理業務支援システム
Bicycle parking lot management system using YOLOv5  
## URL
ローカル：[http://localhost:3000](http://localhost:3000/login)  
ステージング：ドキュメントに記載  
本番環境：ドキュメントに記載  
## 環境構築  
※本プロジェクトは[バックエンド](https://github.com/projectd-team14/bicycle-system-backend)と[YOLOv5用サーバー](https://github.com/projectd-team14/yolov5-server)の環境構築が必要です。  
〇主要フレームワーク、ライブラリ、言語等  
・Nuxt.js(Vue.js,Node.js,TypeScript,Sass)  
・Laravel(PHP, Nginx, PHP-FPM, MySQL)  
・YOLOv5(FastAPI, YOLOv5 ※別のインスタンスに設置)  
  
1.リポジトリのclone
```
git clone https://github.com/projectd-team14/bicycle-system-frontend.git
```
2.bicycle-system-frontendディレクトリに移動
```
cd bicycle-system-frontend
```
4.Dockerイメージのビルド
```
docker compose up -d --build  
docker compose exec app sh
yarn install
```
4-2.サーバーを起動
```
yarn dev
```










