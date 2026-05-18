#!/bin/bash

mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = \"#FF4B4B\"
backgroundColor = \"#0E1117\"
secondaryBackgroundColor = \"#262730\"
textColor = \"#FAFAFA\"
font = \"sans serif\"

[server]
port = \$PORT
enableXsrfProtection = false
headless = true
" > ~/.streamlit/config.toml
