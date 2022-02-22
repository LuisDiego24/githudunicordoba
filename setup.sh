
mkdir -p ~/.streamlit/
echo "
[theme]
base='light'
primaryColor='#ff0000'
secondaryBackgroundColor='#838383'
textColor='#000000'
font='serif'
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
" > ~/.streamlit/config.toml
