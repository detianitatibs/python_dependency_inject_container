# DIとDIコンテナは違う
DIを使ったことがなかったので、pythonでのDIを体験してみる。
- DI
    - Dependency Injection: 依存性注入
- DIコンテナ
    - DI機能を提供するフレームワーク

- 依存性注入
    - 依存している部分を切り離して、それぞれを疎に考えやすくする

# サンプルコード説明
Taskというオブジェクトに入っている値をコンソールに出力するサンプル
- main01.py
    - 何も考えずにTaskというクラスで完結させる  
      ちょっとした変更でもクラス単位で複製する必要があるのを煩わしく感じる
- main02.py
    - データを保持する機能とデータを出力する機能を分けてみる
      出力方式を複製して変更すると、呼び出し元も修正する必要があり、依存してる感を感じる。
- main03.py
    - 出力機能を抽象化してDIしてみる。  
      確かに、呼び出し元は変えなくても対応できるのね、とわかる。
- main04.py
    - injectorを使ってDIコンテナ機能を使ってみる。
      main03.pyより依存関係を整理して管理しやすくなったと感じる。  