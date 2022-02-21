
mkdir -p ~/.streamlit/
echo "
[theme]
primaryColor='#c12b4f'
backgroundColor='#c9d3f9'
secondaryBackgroundColor='#ffffff'
textColor='#000000'
font="serif"
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
" > ~/.streamlit/config.toml
