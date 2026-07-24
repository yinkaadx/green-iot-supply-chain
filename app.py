import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Green AI Supply Chain Engine", layout="wide")

st.title("Serverless Green AI & Circular Economy Pipeline")
st.caption("IoT-Enabled Supply Chain Optimization & Dynamic Capability Modeling")

st.sidebar.header("Digital Business Configuration")
selected_network = st.sidebar.selectbox("Target IoT Supply Chain", ["Trans-Tasman E-Commerce Fleet", "African Agri-Processing Hub (Maikaza)", "Global Electronics Reverse Logistics"])
ai_efficiency = st.sidebar.slider("Green AI Energy Optimization Level", 1, 10, 8)
run_simulation = st.sidebar.button("Initialize Sustainable IoT Engine")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: IoT Ingestion -> Event-Driven Serverless Compute -> Green AI Routing")

if run_simulation:
    st.subheader(f"Active Circular Economy Monitor: {selected_network}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_efficiency = col1.empty()
    metric_circularity = col2.empty()
    metric_compute = col3.empty()
    metric_status = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(1111)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    logistics_efficiency = []
    compute_energy = []
    
    base_efficiency = 75.0 
    
    for i in range(100):
        if i < 30:
            current_eff = base_efficiency + np.random.uniform(-2.0, 2.0)
            current_energy = np.random.uniform(50.0, 60.0) - (ai_efficiency * 2.0)
            circularity_score = np.random.uniform(40.0, 50.0)
        elif i >= 30 and i < 65:
            current_eff = base_efficiency - (i - 30) * 0.8 + np.random.uniform(-5.0, 5.0)
            current_energy = np.random.uniform(80.0, 100.0) - (ai_efficiency * 4.0)
            circularity_score = np.random.uniform(50.0, 70.0)
        else:
            current_eff = base_efficiency + 15.0 + np.random.uniform(-1.0, 1.0)
            current_energy = np.random.uniform(10.0, 20.0) - (ai_efficiency * 0.5)
            circularity_score = np.random.uniform(85.0, 98.0)
            
        current_energy = max(1.0, current_energy) 
            
        logistics_efficiency.append(current_eff)
        compute_energy.append(current_energy)
        
        metric_efficiency.metric("Supply Chain Delivery Efficiency (%)", f"{current_eff:.1f}%", f"{(current_eff - base_efficiency):.1f}%")
        metric_circularity.metric("Asset Circularity Rate", f"{circularity_score:.1f}%", "Reverse Logistics")
        metric_compute.metric("AI Compute Energy Cost (Wh)", f"{current_energy:.1f} Wh", f"- Optimized")
        
        if current_eff < 60.0:
            metric_status.metric("Dynamic Capability", "ADAPTING TO SHOCK", "High Latency")
        else:
            metric_status.metric("Dynamic Capability", "OPTIMIZED ROUTING", "Stable")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=logistics_efficiency, mode='lines', name='Logistics Efficiency (%)', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=compute_energy, mode='lines', name='Serverless AI Energy Cost (Wh)', yaxis='y2', line=dict(color='green', dash='dot')))
        
        fig.update_layout(
            title="Digital Business Transformation: Supply Chain Efficiency vs Green AI Energy Consumption",
            xaxis=dict(title="High-Frequency IoT Timestamp"),
            yaxis=dict(title="Operational Efficiency (%)", range=[0, 100]),
            yaxis2=dict(title="Compute Energy (Wh)", overlaying='y', side='right', range=[0, 120]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if current_eff < 60.0:
            log_placeholder.error(f"DISRUPTION ALERT: Exogenous supply chain shock detected at {time_steps[i].strftime('%H:%M:%S')}. Green AI inference engine actively recalculating IoT logistics network graph to preserve circularity.")
        else:
            log_placeholder.success(f"Log: Telemetry tick {i} ingested via event-driven AWS Lambda. Serverless nodes terminated immediately to preserve zero-idle carbon emissions.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The serverless cloud pipeline successfully leveraged Green AI to maintain dynamic capabilities and optimize the circular economy supply chain.")
else:
    st.info("Click 'Initialize Sustainable IoT Engine' in the sidebar to simulate high-frequency digital business data ingestion.")