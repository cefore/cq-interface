# Interface 2月号「特設: ラズパイで試す！次世代ネットワーク・アーキテクチャICNの研究」 をご覧の皆様へ

## はじめに
本 readme をご覧いただき、誠にありがとうございます。ここでは、雑誌には書ききれていない注意事項・補足等をまとめました。是非、実験をされる前にご一読ください。

## 動作環境
- 本書で紹介した Cefore ソフトウェアの安定動作は、cefore-0.10.0f (2023年12月25日時点の最新版) を対象としています。
- 今後公開されていく新しいバージョン、例えば、cefore-0.10.1 での実行方法については、近日公開させて頂く予定です。
<!-- では、OpenSSL などのライブラリ周りの改修が入っておりますので、追加手順が必要になります。このバージョンのソースコードで実行される方は後述の "cefore-0.10.1 での動作" をご覧ください。 -->

## 各プログラムの説明
- 本書で紹介する実験にて利用するサンプルプログラム（スクリプト）を以下の通り公開しています。適宜ご活用ください。
```console
├── README.md
└── script
    ├── chapter1
    │   ├── 88-cefore.conf
    │   ├── dhcpcd.conf
    │   ├── dnsmasq.conf
    │   ├── enable-wifi-ap.bash
    │   ├── hostapd.conf
    │   └── wpa_supplicant.conf
    ├── chapter4
    │   ├── livcam.bash
    │   └── playback.bash
    └── chapter5
            ├── cefpyco
        │   ├── list_1.py
        │   ├── list_2.py
        │   ├── list_3.py
        │   ├── list_4_a.py
        │   └── list_4_b.py
        └── fan-sensor
            ├── actuate_fan.py
            ├── actuate_sensor.py
            ├── polling_fan.py
            └── polling_sensor.py
```
- `chapter1/*` 第2部1章で環境構築に利用するファイル・スクリプトです。
- `chapter4/*` 第2部4章でラズパイで作るライブ配信カメラに利用するスクリプトです。
- `chapter5/*` 第2部5章で Cefpyco を用いたアプリ開発（基本操作、センサー・ファンアプリ）に利用するファイルです。

<!-- ## cefore-0.10.1 のインストール
先述の通り、cefore-0.10.1 は OpenSSL 3.x を前提としているため OpenSSL 1.x 対応の cefore-0.10.0f とは OpenSSL のインストール方法が異なります。以下の手順で OpenSSL をインストールした後、Cefore のインストール時に当該ライブラリをご指定ください。
### ラズパイの OpenSSL 3.x 設定
-  -->

## ラズパイのカメラモジュール取り付け
- 本書で紹介した ラズパイ Model 4B, カメラモジュール ver. 3 の組み合わせでは、機器にモジュールを接続するだけで libcamera-vid のコマンドが利用できましたが、端末と利用するカメラモジュールのバージョンによっては、動作確認においてカメラモジュールが上手く認識されない場合があるとの報告を受けています。
- カメラモジュール ver. 2 の場合は以下のサイトに従うことで動作可能でした。うまく認識しない場合はお試し下さい。
  - https://www.hobbyhappyblog.jp/raspberrypi-bullseye-camera-connect

## 正誤表
- 初版では以下に示す誤植がありました。お手数ですが、読み替えてご覧いただけますと幸いです。
### pp. 112 右上、「● 手順2：カメラ・モジュールを取り付ける」
誤）`$ livcamera-vid`  
正）`$ libcamera-vid`   

### pp. 112 左上、「● 手順 3:Cefore のインストール」
誤）source code (cefore-0.10.1.zip)  
正）source code (cefore-0.10.0f.zip)  

### pp. 121 右中、「▶(3)ファイルのアップロード」
誤） `$ cefputfile ccnx:/hello/file. -f ./file.txt -r 10 -t 3600 -e 3600`  
正）`$ cefputfile ccnx:/hello/file -f ./file.txt -r 10 -t 3600 -e 3600`  
（通信に利用する名前は "ccnx:/hello/file" ですので、ピリオド「.」を除いてください）


## おわりに
最後までご覧いただき、ありがとうございます。まだまだ不十分な readme ですので、適宜、皆様からのフィードバックに基づいてアップデートしていけたらと考えております。ご質問等は、以下のメールアドレスまでご連絡下さい。
- na5-info@nict.go.jp