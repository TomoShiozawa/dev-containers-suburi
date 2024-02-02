## About
devcontainerを使った環境整備
https://code.visualstudio.com/docs/devcontainers/containers#_create-a-devcontainerjson-file

## How to
1. DockerとDev Containersの拡張を準備する
    - 参考：https://code.visualstudio.com/docs/devcontainers/tutorial
1. VSCodeのコマンドパレットから`Dev Containers: Reopen in Container`
    - 初回はコンテナがビルドされるのを待つ
1. よしなに開発

## その他
- poetry
  - ライブラリの管理はpoetryが良さげ
  - https://python-poetry.org/docs/
  - 必要に応じて`poetry add`してく

- test
  - テストはpytest？
  - `poetry run python -m pytest`

- lint/format
  - Ruffだけで[PEP8準拠のルール](https://docs.astral.sh/ruff/rules/#pycodestyle-e-w)とか[isort](https://docs.astral.sh/ruff/rules/#isort-i)のルール、その他たくさんやってくれる
  - 拡張にRuff入れてるから明示的に走らせる必要はないはず
  - `poetry run ruff check`
  - `poetry run ruff format`


## Tips
- vscodeの拡張まで一緒に配布できるので便利かも
- 環境のpythonのバージョンとかはDockerfileをメンテすれば良さそう
  - いちいちローカルでpyenv入れてとかはいらなくなりそう
- コンテナ上だとローカルのエイリアスが効かないので、ローカルのターミナルは別途開く
  - マウントはされているので特に困らないはず
