
mkdir -p ~/.streamlit/
echo "
[theme]
base='light'
primaryColor='#b7e0b7'
secondaryBackgroundColor='#acdaac'
textColor='#000000'
font='serif'
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
" > ~/.streamlit/config.toml
