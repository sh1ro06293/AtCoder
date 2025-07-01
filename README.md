## My profile (https://atcoder.jp/users/merrysh1ro)
たまにコンテスト解いてます

## Docker起動コマンド
以下のコマンドを使用してコンテナを起動してください:
```
docker build -t python-devcontainer .devcontainer && docker run -it --rm -v $(pwd):/workspace python-devcontainer
```

## コンテナ停止方法
コンテナを停止するには、以下の手順を実行してください:
1. VSCodeのターミナルで`Ctrl+C`を押してプロセスを終了します。
2. コンテナ内で`exit`コマンドを使用して終了します。
3. 必要に応じてホスト側で`docker ps`でコンテナの状態を確認し、`docker stop [コンテナID]`を使用して停止します。
