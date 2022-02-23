
mkdir -p ~/.streamlit/
echo "
[theme]
primaryColor='#378585'
backgroundColor='#ececec'
secondaryBackgroundColor='#9a9a9a'
textColor='#000000'
font='serif'
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
" > ~/.streamlit/config.toml
