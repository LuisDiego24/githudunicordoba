mkdir -p ~/.streamlit/
echo "
[theme]
primaryColor="#141111"
backgroundColor="#2c502a"
secondaryBackgroundColor="#434040"
textColor="#fffefe"
font='monospace'
[server]
headless = true
enableCORS=false
enableXsrfProtection=false
port = $PORT
" > ~/.streamlit/config.toml
