```plaintext
 ██▀███   ▒█████   ▒█████   ███▄ ▄███▓ ▄▄▄▄   ▓█████ ▓█████  ██▀███  
▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓█   ▀ ▓██ ▒ ██▒
▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒███   ▒███   ▓██ ░▄█ ▒
▒██▀▀█▄  ▒██   ██░▒██   ██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒▓█  ▄ ▒██▀▀█▄  
░██▓ ▒██▒░ ████▓▒░░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░▒████▒░▒████▒░██▓ ▒██▒
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ░ ░  ░ ░ ░  ░  ░▒ ░ ▒░
  ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░    ░    ░    ░      ░     ░░   ░ 
   ░         ░ ░      ░ ░         ░    ░         ░  ░   ░  ░   ░     
                                            ░                        
```

# RoomBeerFrontend
Dont open Frontend inside!      

# Update src
git pull origin main

# System service installation
cd scripts
sudo ./install.sh

## Restart frontend
sudo systemctl restart roombeer-frontend.service

## Restart backend
sudo systemctl restart roombeer-frontend.service

## Restart stream
sudo systemctl restart roombeer-stream.service

# Installation and deployment
# Setup Python Virtual Environment
### Inside of ./Roombeer/
```plaintext
python -m venv venv_backend
pip install "fastapi[standard]"
```
## Run Frontend
### Inside of ./room-beer-vue
```plaintext
npm run serve
```
## Run Backend
```plaintext
fastapi dev main.py
```