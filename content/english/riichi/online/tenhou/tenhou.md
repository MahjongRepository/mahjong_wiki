+++
title = "Tenhou"
arcturus_wiki_id = "219"
tags = ["Tenhou.net"]
+++

## General instructions

<h3>

<font color=#444444 >■</font> 仕様

</h3>

```jptranslationrow
| Japanese = テストプレイ」のCOMはツモ切り無思考
| English = COM in Test Play only discards its draw (“TSUMOGIRI”).
```
```jptranslationrow
| Japanese = 鳴かない」モードは、「ロン」以外のポン/明槓/チーをパス
| English = “No Calls” mode auto passes all calls, except for RON
```
```jptranslationrow
| Japanese = 鳴かない」ボタンは局開始毎に自動クリア
| English = The “No Calls” button is automatically depressed at the start of a round
```
```jptranslationrow
| Japanese = ツモ切り」モードは、ツモ/ロン/暗槓/加槓/リーチ以外をパス
| English = “TSUMOGIRI” Mode does not automatically pass TSUMO, RON, ANKAN, KAKAN or RIICHI
```
```jptranslationrow
| Japanese = ツモ切り」モードでは、字幕表示(和了/流局)の最大待ち時間が半分
| English =
```
```jptranslationrow
| Japanese = ツモ切り」ボタンはマウスの応答がある場合、局開始時にクリア
| English = The “tsumogiri” (auto-discard) button is automatically depressed at the start of a round
```
```jptranslationrow
| Japanese = リーチ後はロン/ツモ/暗槓以外でツモ切り
| English = After calling riichi, everything other than ron, tsumo or ankan will auto-discard.
```
```jptranslationrow
| Japanese = 60秒間マウスの動作/キー入力が発生しなかった場合は強制で「ツモ切り」モード
| English = Inactivity for 60 seconds from mouse or keyboard inputs will force tsumogiri mode.
```
```jptranslationrow
| Japanese = 打牌後は誰も鳴かない場合でも一定の割合で数秒間停止
| English = After a tile is discarded, the game will always pause for a small, set amount of time.
```
```jptranslationrow
| Japanese = ツモ切り以外の打牌位置はランダム(ツモ牌の位置を含まない)
| English = Discarded tiles will appear to come randomly from the hand (excluding tsumogiri, or the active tile drawn).
```
```jptranslationrow
| Japanese = 山牌/王牌は開始前にランダムに並べてから消費(<a href="http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/mt.html">乱数生成機</a> / <a href="#LOG">乱数種と山生成</a>)
| English = The walls are randomly generated before the round starts. (http://www.math.sci.hiroshima-u.ac.jp/\~m-mat/MT/mt.html (Random Number Generator) / \#LOG (Random Numbers and wall generation)
```
```jptranslationrow
| Japanese = チーやポンで鳴きに赤を使うか使わないかは選択できない(有料Windows版は選択可能)
| English = It is not possible to not use red fives in a chi/pon (except when using the premium windows client)
```
```jptranslationrow
| Japanese = 途中落ちプレーヤは名前を赤色で表示
| English = Dropped players will have their name indicated in red.
```
```jptranslationrow
| Japanese = 再入場の上限は3回
| English = Maximum of 3 server reconnections allowed per game.
```
```jptranslationrow
| Japanese = チョンボなし
| English = No chombo penalties.
```
```jptranslationrow
| Japanese = 「自動和了」は接続が切れた場合には機能しない
| English = "Auto Win" does not work while disconnected
```
```jptranslationrow
| Japanese = チーの複数選択は牌を２枚クリック(有料Windows版のみ)
| English = If there are multiple chi choices, you may click two tiles to select which chi (premium windows client only)
```
```jptranslationrow
| Japanese = 手動理牌は牌をドラッグ(有料Windows版のみ)
| English = Can arrange hand by dragging (premium windows client only)
```
```jptranslationrow
| Japanese = ダブルクリックでパス/ツモ切り/OK/…(待ち時間切れ動作)
| English =
```
```jptranslationrow
| Japanese = 右クリックでパス(Windows版またはFlash版専用ブラウザのみ)
| English =
```
```jptranslationrow
| Japanese = ※ダブルクリックが行なえる場所は、「卓」などの1回目のクリックでカウンタが消えない場所
| English =
```
```jptranslationrow
| Japanese = ※ただし、ツモ/ロンが表示されている場合はダブルクリックは無効
| English =
```

## Windows settings

<b>Q) 「\_bgm0.wav invalid md5」というエラーがでて起動できなくなってしまいました…</b>(Windows版)  
<b>Q) 「ShellExecute failed」というエラーがでて起動できなくなってしまいました…</b>(Windows版)  
<b>Q) 「インターネットに接続してください」というエラーがでて起動できなくなってしまいました…</b>(Windows版)  
非インストール版の天鳳から起動できる場合があるようです。その後は設定が正常に戻り、インストール版の天鳳も起動できるようになることがあるようです。
次のファイルをダウンロードして実行してください。  
<a href="http://tenhou.net/1/tenhou-launcher130.exe"><http://tenhou.net/1/tenhou-launcher130.exe></a> (非インストール版本体)  
<a href="http://tenhou.net/1/tenhou-cleanup130.exe"><http://tenhou.net/1/tenhou-cleanup130.exe></a> (手動アンインストーラ)  
  
  
<b>Q) 頻繁にサーバから切断されます…</b>(Flash版/Windows版)  
BGM/SEをカスタマイズしていると切断されることがあるようです。
BGM/SEをすべて標準にして天鳳以外を起動しない状態で使用してみてください。  
  
WiFi(無線LAN)を使用していませんか？その場合には有線での接続を試してみてください。
WiFi(無線LAN)は通信が不安定なため応答が極端に遅くなりサーバから切断されることがあります。  
  
(参考情報)無線LANの接続品質を改善する方法として「無線LANブリッジ」を使用する方法があります。
機材の購入や使用方法などについてはお客様ご自身の判断でお願いいたします。  
  
(参考情報)ADSL回線の場合、有線の場合でも通信品質が低い場合に回線が切断されるケースがあるようです。
その場合、モデムの交換や屋内配線の交換などをすることで通信品質が安定したという報告もあります。
工事や機材変更についてはお客様ご自身の判断でお願いします。  
  
  
<b>Q) 接続できません…</b>(Flash版/Windows版)  
次の環境からは接続できません。  
\- FlashPlayer 7.0.16.0以降でTCP10080ポートの通信を禁止している環境で、TCP80ポートでゲームの通信を禁止する場合  
\- FlashPlayer 7.0.14.0以前でTCP10080ポートの通信を禁止している場合  
\- FlashPlayer 9.0.115.0以降でTCP843ポートとの通信が利用できない環境  
\- URLとサーバ名が一致しない接続環境  
\- プロバイダやウィルス対策ソフトがゲームの通信を禁止している場合  
ぷらら <a href="http://www.plala.or.jp/member/option_service/secuplus/nbb/game.html"><http://www.plala.or.jp/member/option_service/secuplus/nbb/game.html></a>  
  
  
<b>Q) Windows版が起動しても応答しなくなってしまいました…</b>(Windows版)  
一度コンピュータを再起動してみてからもう一度チャレンジしてみてください。  
それでも動作しない場合には、以下をご覧ください。  
  
  
<b>Q) Windows版でIDやロビー番号が入力できません…</b>(Windows版)  
Microsoft AppLocaleを使っている場合には、それを使用せずに半角英数で入力してください。  
  
  
<b>Q) Windows8.1/Surface3でフルスクリーンになりません…</b>(Windows版)  
コントロールパネルのディスプレイの設定で「すべてのディスプレイで同じ拡大率を使用する」「小-100%」にすると表示できるようになります。  
  
  
<a name="LOADING-FAILED" ></a>
<b>Q) 突然天鳳が起動できなくなってしまいました。</b>(Windows版)  
<b>Q) Windows版が黒い画面のLOADING...で止まってしまいます…</b>(Windows版)  
<b>Q) 牌譜ファイルがダウンロードできません…</b>(Windows版)  
天鳳のアプリケーションが、ウィルス対策ソフトやファイアーウォール機能などにより
インターネットへの通信を禁止されている場合、UPDATEが途中でまってしまうことがあります。
この場合、それらのソフトの設定で次の２つのファイルを許可(または除外の指定)を行えば利用可能になります。  
  
\[Windows XPの場合\]  
C:\\Documents and Settings\\\[アカウント名\]\\Local Settings\\Application Data\\C-EGG\\tenhou\\app\\tenhou.exe  
C:\\Documents and Settings\\\[アカウント名\]\\Local Settings\\Application Data\\C-EGG\\tenhou\\app\\logana.exe  
  
\[Windows Vista/Windows7の場合\]  
C:\\Users\\\[アカウント名\]\\AppData\\Local\\C-EGG\\tenhou\\app\\tenhou.exe  
C:\\Users\\\[アカウント名\]\\AppData\\Local\\C-EGG\\tenhou\\app\\logana.exe  
  
tenhou.exe = 製品本体 / logana.exe = 牌譜解析ツール  
  
「Norton Internet Security（ノートンインターネットセキュリティ）による誤検出」対策  
SONARの警告画面で「詳細を表示」、次の画面で「オプション」をクリック、「復元」で「このリスクを今後のスキャンから除外する」の操作で、天鳳の警告を除外することができます。  
  
  
<b>Q) 画面が真っ黒のまま先へ進みません…</b>(Flash版)  
<b>Q) 「Load ○○ failed」というメッセージが出てゲームが開けなくなってしまいました…</b>(Flash版)  
<b>Q) ダウンロードが途中で止まってしまい入場できません…</b>(Flash版)  
<a href="http://www.google.co.jp/search?q=%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6+%E3%82%AD%E3%83%A3%E3%83%83%E3%82%B7%E3%83%A5+%E3%82%AF%E3%83%AA%E3%82%A2+%E6%96%B9%E6%B3%95">ブラウザのキャッシュをクリア</a>してからもう一度開いてみてください。
ノートンを使っている場合に、広告ブロック機能が有効になっているとFlash版が画面が黒いまま進まなくなってしまうことがあるようです。  
  
  
<b>Q) 「すでに他のブラウザで接続しています」と表示され接続できません…</b>(Flash版)  
接続している状態でブラウザが強制終了した場合（アドオンエラーなど）、このエラーが出続けてしまう場合があります。
ログオフするかコンピュータを再起動してから接続してください。  
  
  
<b>Q) 配牌時に回線が切れてしまいます…</b>(Flash版/Windows版)  
配牌のアニメーション＋サーバとの通信時間が20秒以上（通常は約7秒）かかる場合、強制的にサーバが回線を切断します。
その他ゲーム中に長い時間停止する場合も強制切断します。
他に動いているアプリケーションがあればそれを終了すると少し切れにくくなるかもしれません。
何も起動していないのに切れる場合はパソコンのスペックが不足している可能性が大きいです…。  
  
  
<b>Q) 接続してから一定時間で回線が切れてしまいます…</b>(Flash版/Windows版)  
10080番ポートへの接続が禁止されている際に使用する80番ポートの通信にproxyなどでタイムアウトが設定される場合やバッファする環境に起こるようです。ゲームサーバとTCPで10080番ポートの送受信ができるように設定を変更すると安定してゲームができるようになります。  
  
  
<b>Q) 対戦中に回線が頻繁に切れるのですが…</b>(Flash版/Windows版)  
無線LANは接続が切れることがあります。有線の接続でもう一度チャレンジしてみてください。  
  
  
<b>Q) Flash版で「エコノミー」が選択できません…(Flash版)</b>  
<b>Q) Flash版で入場画面にIDが記憶されません…(Flash版)</b>  
<b>Q) Flash版で個室の戦績が記録されません…(Flash版)</b>  
<b>Q) Flash版で牌譜が残りません…(Flash版)</b>  
IEの場合、インターネットオプションのプライバシー管理で「サイト」ボタンから「常に許可する」に設定すると選択できるようになります。  
  
<b>Q) 4枚目の字牌なのに止まることがあり心臓によくないのですが…</b>  
ランダムに待ち時間を入れています。  
  
  
<b>Q) ゲームが画面に入りきらないのですが…</b>(Flash版)  
F11キーを押してみましょう！  
\- IE/FireFoxの場合F11のフルスクリーン(KIOSKモード)表示でツールバー類を隠すことができます。  
\- ポップアップブロックを解除してポップアップで開くと少しゲーム画面が広くなります  
\- 解像度800x600以下ではフルスクリーンにしても表示できない部分があります。  
  
  
<b>Q) サーバから切断された場合の結果はランキングや戦績に反映されますか？</b>(Flash版/Windows版)  
はい。ツモ切りで最後までプレイした結果が反映されます。  
  
  
<b>Q) 予約が4人なのに開始しません…</b>(Flash版/Windows版)  
ランキング戦ロビーでは異なる4つの接続元IPからの予約が集まった場合にゲーム開始となります。
大学/会社などで同じNAT下から他に予約している人がいるのかもしれません。
個室ロビーでは同一IPでもゲームが開始します。  
  
  
<b>Q) 予期しない対戦が開始していてptやRateが下がっています…</b>(Flash版/Windows版)  
予約したまま、パソコンをスリープしたり、ブラウザを閉じたり(Flash版)すると
予期しない対戦が開始してしまう可能性があります。
予約をキャンセルしてしばらくしてから、パソコンやブラウザを終了するようにしてください。  
  
  
<b>Q) 意図しないツモ切り（一番右の牌を切る）が発生してしまいます…</b>(Flash版/Windows版)  
ダブルクリックでツモ切りになる仕様が原因です。以下の方法で防ぐことができます。  
  
\[Windows版の場合\]  
ログイン後にロビー画面で、メニュー⇒設定⇒その他から「対戦中に左ダブルクリックでツモ切りを行う」のチェックをはずしてください。  
  
\[Windows版/Flash版の場合\]  
OSの設定でダブルクリックの速度を遅くすると防げる可能性があります。以下Windowsの場合の設定方法です。  
<a href="https://www.google.co.jp/search?q=windows+%E3%83%80%E3%83%96%E3%83%AB%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF+%E9%80%9F%E5%BA%A6">Googleで「windows ダブルクリック 速度」を検索</a>  
  
  

## References

```reflist```

## External links
- [Source of this page [arcturus wiki]](http://arcturus.su/wiki/Tenhou)