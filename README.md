# 環境安裝－手動
## 安裝 pyenv, pyenv-virtualenv
1. 下載 pyenv, pyenv-virtualenv: 

    ```
    $ brew install pyenv pyenv-virtualenv
    ```

2. Clone 專案並指定虛擬環境: 
    ```
    $ git clone https://github.com/ts01174755/MLOPS.git ~/Development/pyDev/mlops_whiteboard
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
    $ cd ~/Development/pyDev/mlops_whiteboard
    ```

    b. 先建立virtualenv python=3.8.16並命名為 mlops_whiteboard_python: 
    ```
    $ pyenv virtualenv 3.8.16 mlops_whiteboard_python
    ```

    c. 把當前local路徑下的專案環境指向 mlops_whiteboard_python: 
    ```
    $ pyenv local mlops_whiteboard_python
    ```

3. 設定根目錄
    ```
    $ echo 'export PYTHONPATH="${PYTHONPATH}:${HOME}/Development/pyDev/mlops_whiteboard"' >> ~/.zshrc
    ```

## 認識系統
### 執行
- 本系統為MVC架構，