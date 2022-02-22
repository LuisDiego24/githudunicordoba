
mkdir -p ~/.streamlit/
echo "
[theme]
primaryColor='#378585'
backgroundColor='#333333'
secondaryBackgroundColor='#6f6f6f'
textColor='#ffffff'
font='serif'
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
" > ~/.streamlit/config.toml
