
mkdir -p ~/.streamlit/
echo "
[theme]
base='light'
primaryColor='#ff0000'
secondaryBackgroundColor='#c3c3c3'
textColor='#000000'
font='serif'
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
" > ~/.streamlit/config.toml
