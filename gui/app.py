import streamlit as st
import os
import json
from core.orchestrator import SwarmOrchestrator

st.set_page_config(page_title="Aegis Swarm Evolution Workbench", layout="wide")

st.title("⚡ Aegis Swarm Evolution Workbench")

# --- Configuration Section ---
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("WhatsApp API Key", type="password")
    webhook = st.text_input("Webhook URL")
    if st.button("Save Configuration"):
        with open("config.json", "w") as f:
            json.dump({"api_key": api_key, "webhook": webhook}, f)
        st.success("Config updated.")

# --- Workflow Section ---
st.subheader("Evolution Control")
target_project = st.text_input("Target Directory to Evolve:")
if st.button("Deploy Aegis Swarm"):
    if target_project and os.path.exists(target_project):
        st.info("Orchestrating autonomous evolution...")
        orchestrator = SwarmOrchestrator(target_project)
        report = orchestrator.run()
        st.success(f"Evolution Result: {report}")
    else:
        st.error("Invalid path.")
