import streamlit as st
import requests
import os

st.set_page_config(page_title="PrivateVault • Dashboard", page_icon="🔐", 
layout="wide")

st.title("🔐 PrivateVault Dashboard")
st.caption("Your AI Ops Vault: Encrypt Everything, Optimize Everything.")

# Health panel
st.subheader("Service Health")
backend_url = os.environ.get("BACKEND_URL", "").strip()
col1, col2 = st.columns(2)

with col1:
    if backend_url:
        st.write("Backend URL:", f"`{backend_url}`")
        try:
            r = requests.get(backend_url, timeout=5)
            st.success(f"Backend OK ({r.status_code})")
            st.code(r.text.strip()[:300], language="text")
        except Exception as e:
            st.error("Backend not reachable")
            st.exception(e)
    else:
        st.info("Set `BACKEND_URL` env var to check your Flask endpoint 
health.")

# Simple “encrypt” demo (client-side for now)
st.subheader("Quick Encrypt Demo")
text = st.text_area("Enter text to encrypt", "PrivateVault Ultimate")
if st.button("Encrypt"):
    encrypted = text[::-1]  # demo logic
    st.success("Encrypted:")
    st.code(encrypted, language="text")

# Actions panel
with col2:
    st.subheader("Actions")
    st.write("• Set `BACKEND_URL` to your Flask URL (optional).")
    st.write("• Replace demo encrypt with your API call later.")
    st.write("• Add file upload, auth, and charts as you grow.")

st.divider()
st.caption("© 2025 PrivateVault • Render + Streamlit demo")

