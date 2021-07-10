mkdir -p ~/.streamlit

echo "[serveur] 
headless = true 
port = $PORT 
enableCORS = false 
" > ~/.streamlit/config.toml