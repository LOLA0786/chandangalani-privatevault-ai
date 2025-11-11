import streamlit as st
import requests
import os

st.set_page_config(page_title="PrivateVault Control Center", page_icon="🔐", layout="wide")

# --- Header ---
st.markdown("<h1 style='text-align:center;'>🔐 PrivateVault • Unified Control Center</h1>", unsafe_allow_html=True)
st.caption("Test-run & monitor all 3 products: CloudShift • TechDebtZero • Vault-X")

# --- Sidebar Navigation ---
page = st.sidebar.radio("🧭 Select Product", ["🏦 CloudShift FinOps", "🧩 TechDebtZero Analyzer", "🔒 Vault-X Privacy Core"])

# --- Utility ---
BACKEND_URL = os.environ.get("BACKEND_URL", "https://api.getprivatevault.com")

def check_backend():
    try:
        r = requests.get(BACKEND_URL, timeout=5)
        st.success(f"Backend OK ({r.status_code})")
    except Exception as e:
        st.error("Backend unreachable")
        st.exception(e)

# --- Product 1: CloudShift FinOps ---
if "CloudShift" in page:
    st.header("🏦 CloudShift • AI FinOps Autopilot")
    st.write("Simulate cloud cost optimization & savings estimator.")
    if st.button("Run FinOps Simulation"):
        st.json({"Top Savings": "Migrate Azure CosmosDB → Supabase", "Impact / mo": "$12 000", "Confidence": "95 %"})
    st.divider()
    check_backend()

# --- Product 2: TechDebtZero ---
elif "TechDebtZero" in page:
    st.header("🧩 TechDebtZero • Code Quality Analyzer")
    repo = st.text_input("GitHub Repo URL", "https://github.com/example/repo")
    if st.button("Analyze Codebase"):
        st.json({
            "Maintainability Index": 82.5,
            "Complexity Score": 7.3,
            "Pylint Rating": 8.4,
            "Todo Count": 5
        })
    st.divider()
    check_backend()

# --- Product 3: Vault-X Privacy Core ---
else:
    st.header("🔒 Vault-X • Privacy & Encryption Core")
    text = st.text_area("Enter data to encrypt", "Sensitive text here …")
    if st.button("Encrypt Data (Test)"):
        encrypted = text[::-1]
        st.success("Encrypted:")
        st.code(encrypted)
    st.divider()
    check_backend()

# --- Footer ---
st.markdown("---")
st.caption("© 2025 PrivateVault Labs • Render Demo Dashboard • For internal testing only (no real data stored)")





