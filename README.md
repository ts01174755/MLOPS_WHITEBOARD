# 環境安裝－手動
## 安裝 pyenv, pyenv-virtualenv
- 專案路徑: [YourProjectPath]

ex: ${HOME}/mlops_whiteboard

1. 下載 pyenv, pyenv-virtualenv: 

    ```
    $ brew install pyenv pyenv-virtualenv
    ```

2. Clone 專案並指定虛擬環境: 
    ```
    $ git clone https://github.com/ts01174755/MLOPS_WHITEBOARD.git [YourProjectPath]
    ```

3. pyenv 設定
    ```
    $ echo 'export PYENV_ROOT=\"$HOME/.pyenv\"' >> ~/.zshrc
    $ echo 'export PATH=\"$PYENV_ROOT/shims:$PATH\"' >> ~/.zshrc
    $ echo 'if which pyenv-virtualenv-init > /dev/null; then eval \"$(pyenv virtualenv-init -)\"; fi' >> ~/.zshrc
    $ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    ```

## 安裝 python 3.8.16
1. 設定主環境 - python 3.8.16:
    ```
    $ pyenv install 3.8.16
    ```

2. 建立虛擬環境: 

    a. 切到專案目錄: 
    ```
    $ cd [YourProjectPath]
    ```

    b. 先建立virtualenv python=3.8.16並命名為 mlops_whiteboard_python: 
    ```
    $ pyenv virtualenv 3.8.16 mlops_whiteboard_python
    ```

    c. 把當前local路徑下的專案環境指向 mlops_whiteboard_python: 
    ```
    $ pyenv global system 
    $ pyenv local mlops_whiteboard_python
    ```

3. 設定根目錄
    
    當你的執行環境不是 system(系統預設) 時，會動態設定PYTHON目錄為當前目錄
    ```
    $ cd [YourProjectPath]
    $ chmod +x setting_python_root.sh
    $ echo 'source [YourProjectPath]/setting_python_root.sh' >> ~/.zshrc
    ```

## 認識系統
### 原則
1. 請用 automation 建立 pipline ，透過參數去控制多個 controller。
2. 請用 controller 建立業務邏輯，透過參數控制你需要的 model。
3. 請用 model 建立可參數化的實體，供 controller 控制。

> 注意：
> 1. model 要 100% 參數化
>
> 2. controller 可參數化程度因業務邏輯而異。
>
> 3. 參數化程度越高，復用性越高；

### 執行
- automation 範例
```
$ python3.8 [YourProjectPath]/automation/model_example.py
Output:
HERE IS CONTROLLER_EXAMPLE.PY TEST
model_example
```

- 建構環境(執行前請把 docker 打開)
```
$ python3.8 [YourProjectPath]/automation/build_all_environment.py
```

### 架構定義
- controller - 定義: 不可參數化的執行步驟，通常是業務邏輯的撰寫處，dataprocess, train...等較複雜的程式碼請寫在這。
- model - 定義: 可參數化的執行步驟，通常是可規範化的執行框架，例如模型，或是參數化的實體。
- env_config - 定義: 設定環境的參數，如果沒有要更改 docker 和 local 的環境參數，這裡可以不用動。
- automation - 定義: 給予多個controller參數，形成資料執行的pipline。
    ```
    .
    ├── README.md
    ├── automation      <<詳見automation解釋>>
    │   ├── build_all_environment.py
    │   └── data_pipline.py
    ├── doc
    ├── env_config.py   <<詳見env_config解釋>>
    ├── log
    ├── notebook
    ├── src
    │   ├── controller
    │   │   └── build_environment.py
    │   └── model
    │       ├── __init__.py
    │       ├── docker_cmd.py
    │       ├── mongodb.py
    │       └── postgres.py
    └── subproject
        ├── controller  <<詳見controller解釋>>
        │   └── controller_example.py
        └── model       <<詳見model解釋>>
            └── model_example.py
    ```
### 資料夾定義
- src - 定義: 共用的套件資料夾
- subproject - 定義: 特定目的的資料夾
- doc: 資料存放處
- log: 執行log存放處
