# アプリ名
オンライン指導　予約システム

# 概要
生徒が、教師の指導可能時間から希望日時を選択し予約するシステムです。

# 作成した理由
前職において、コロナの影響で対面指導ではなく、オンラインでの指導に切り替わったため、生徒と教師のマッチングを行えるシステムが欲しいと感じたからです。

# 使用言語 フレームワーク
Python3, django, bootstrap

# 機能
1. ログイン機能
    - トップ画面を、登録された情報から 「生徒用」 「教師用」 に振り分けます。
    
生徒

![ログイン生徒](https://user-images.githubusercontent.com/63441901/91235204-02f22b00-e770-11ea-844c-7e368006fe53.gif)

教師

![ログイン教師](https://user-images.githubusercontent.com/63441901/91235203-02f22b00-e770-11ea-8d47-7c4d22db8010.gif)

1. 予約機能（生徒画面）
    - 指定日に勤務可能な講師一覧を表示し、予約可能な時間に「○」が表示されます。
    - 希望時間を選択すると、「科目・テキスト・質問内容」入力画面に遷移します。
    - 入力後、予約ボタンを押すことで予約が完了し、勤務可能日時に「○」が表示されなくなります。
    - 翌日以降も、同様の手順で予約ができます。
    
![予約機能](https://user-images.githubusercontent.com/63441901/91235197-01286780-e770-11ea-985f-cc087795a342.gif)


1. 教師スケジュール画面
    - 予約された日時に、生徒が入力した　「生徒名・テキスト・質問内容」　が表示されます。
    - ミーティングのリンクを押すと、zoomが開きます。

![教師スケジュール画面](https://user-images.githubusercontent.com/63441901/91235189-fe2d7700-e76f-11ea-85a2-a4a24c539fc0.gif)
       
       
       
       
       
       