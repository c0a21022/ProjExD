# 第14回
## （jump_kokaton.py）
### ゲーム概要
- jump_kokaton.pyを実行すると，1600x900のスクリーンに砂漠が描画され、こうかとんをジャンプさせて流れてくる障害物をよけるゲーム
- スコアが画面左上に表示されている
- 障害物は大きいサボテンと小さいサボテン、一定時間経過で鳥も追加される
- 鳥が飛んでくる高さはランダム
- こうかとんが障害物と接触するとゲームオーバー
- ゲームオーバー画面で「R」キーを押すともう一度始まる
- 「Esc」キーかウィンドウ☓ボタンで画面を閉じる
### 操作方法
- スペースキーでこうかとんを真上にジャンプさせる
### グループ追加機能と作成者
- コードまとめ,一貫性,全体修正: C0119177(代表者)
- 一定時間経過後障害物(鳥)追加: C0119177
- スコアの測定(): C0B21180
- ゲームオーバー画面表示(関数game_over_screen()): C0A21022
- ゲームオーバー時スコアを表示: C0119177
- リスタート機能(関数Quit()): C0A21060
- 障害物等の画像素材作成: C0A21006
### 参考サイト
- https://goodlucknetlife.com/pygame-shooting-background/
- https://pythonmemo.com/pygame/pygame004