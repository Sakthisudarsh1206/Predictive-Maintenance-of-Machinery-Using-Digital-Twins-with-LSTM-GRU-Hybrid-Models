# Predictive-Maintenance-of-Machinery-Using-Digital-Twins-with-LSTM-GRU-Hybrid-Models
Advanced predictive maintenance for wind turbines using digital twin technology and a hybrid deep learning model. It integrates SCADA and historical fault data to create a digital twin. It combines transformer encoders, with LSTM, and GRU layers, forecasts faults while Microsoft Azure Digital Twins enable simulation, visualization, and monitoring.
# Predictive Maintenance of Wind Turbines Using Digital Twins

## Description

This project implements an advanced predictive maintenance framework for wind turbines by leveraging digital twin technology and a hybrid deep learning model. The system integrates real-time SCADA data with historical fault and operational data to create a digital twin of a wind turbine. By combining transformer encoders with LSTM and GRU layers, the model effectively captures both long-term dependencies and short-term temporal patterns to forecast potential faults. A standout feature of this project is its seamless integration with Microsoft Azure Digital Twins, which enables real-time simulation, visualization, and monitoring of turbine performance for proactive maintenance.

## Table of Contents

- [Overview](#overview)
- [Project Motivation](#project-motivation)
- [Tech Stacks & Modules](#tech-stacks--modules)
- [Architecture](#architecture)
- [Implementation Details](#implementation-details)
- [Azure Digital Twin Simulation](#azure-digital-twin-simulation)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Results & Analysis](#results--analysis)
- [Future Work](#future-work)
- [License](#license)

## Overview

This project focuses on the predictive maintenance of wind turbines using a digital twin framework. The system merges real-time SCADA data with fault logs and operational status data to build a virtual representation of a wind turbine. A hybrid model—combining transformer-based encoders with LSTM and GRU layers—is then employed to accurately predict different fault types, enhancing operational efficiency and enabling proactive maintenance strategies.

## Project Motivation

- **Enhance Operational Efficiency:**  
  Minimize downtime by predicting turbine faults before they lead to critical failures.
  
- **Optimize Maintenance Costs:**  
  Transition from reactive or scheduled maintenance to a proactive, data-driven approach.
  
- **Advance Digital Twin Applications:**  
  Leverage Azure Digital Twins for real-time simulation and visualization, providing actionable insights to support decision-making.

## Tech Stacks & Modules

### Data Acquisition and Pre-processing
- **Data Sources:**
  - **SCADA Data:** Over 60 operational parameters.
  - **Fault Data:** Details fault modes (GF, MF, FF, AF, EF) with normal conditions labeled as “NF”.
  - **Status Data:** Provides historical operational statuses.
- **Pre-processing Techniques:**
  - **Time Alignment:** Merging SCADA, fault, and status data using timestamps.
  - **Data Labeling:** Assigning “NF” for missing fault entries.
  - **Exploratory Data Analysis (EDA):** Utilizing boxplots and distribution analyses to identify trends and anomalies.
  - **Feature Engineering:** Selecting key features indicative of faults.

### Model Architecture and Training
- **Hybrid Model Components:**
  - **Transformer Encoder:**  
    - Multi-head attention for capturing long-range dependencies.
    - Positional encoding to preserve temporal order.
    - Incorporates layer normalization, dropout, and feed-forward layers.
  - **Recurrent Layers:**
    - **LSTM and GRU Layers:** Capture both short-term and long-term temporal patterns.
    - Regularization with Dropout, Batch Normalization, and L2 regularization.
- **Dense Layers:**  
  Maps processed features to fault categories using a softmax activation function.
- **Training Techniques:**
  - **Data Splitting:** Utilizing train-test split and Stratified K-Fold cross-validation.
  - **Class Imbalance Handling:** Applying SMOTE (Synthetic Minority Over-sampling Technique).
  - **Evaluation Metrics:** Measuring accuracy, precision, recall, and F1-score.

### Azure Digital Twin Integration and Simulation
- **Digital Twin Definition:**
  - Defined using the Digital Twins Definition Language (DTDL) in JSON.
  - Captures physical and operational properties of wind turbines.
- **Key Components:**
  - **Sensor Integration:** Telemetry parameters (rotor speed, temperature metrics, power outputs).
  - **Hierarchical Modeling:** Creating individual models for turbine subsystems (rotor, nacelle, blades) with defined relationships.
- **Data Simulation:**
  - **Python Script:**  
    Simulates real-time data streaming using `time.sleep()` to mimic operational behavior.
  - **REST API Integration:**  
    Maps CSV telemetry data to corresponding digital twin properties in Azure.
- **Visualization:**
  - **Azure Digital Twins Explorer:**  
    Provides live updates and custom dashboards for monitoring turbine performance and fault predictions.

## Architecture

The project architecture is divided into three layers:

1. **Input & Pre-processing Layer:**  
   - Combines and cleans multiple datasets (SCADA, fault, status) for robust input data.

2. **Modeling Layer:**  
   - **Transformer Encoder:** Extracts long-range dependencies.
   - **LSTM/GRU Layers:** Capture temporal dynamics and contextual information.
   - **Dense Classification:** Produces final fault predictions.

3. **Azure Integration Layer:**  
   - **Digital Twin Creation:** Uses DTDL to model turbine properties.
   - **Data Simulation:** Streams data into Azure for real-time digital twin simulation.
   - **Visualization:** Displays live telemetry and model outputs via Azure dashboards.

## Implementation Details

### Data Pre-processing Module
- **Merging:**  
  Combine SCADA, fault, and status data based on timestamps.
- **Cleaning:**  
  Label missing fault data as “NF” and handle missing values appropriately.
- **EDA:**  
  Use visualizations like boxplots to analyze trends and anomalies.

### Model Building Module
- **Hybrid Architecture:**
  - **Transformer Encoder:** Processes sequential data with attention mechanisms.
  - **LSTM/GRU Layers:** Further refine temporal features.
  - **Dense Layers:** Map features to fault categories.
- **Training Routines:**
  - Data is split using Stratified K-Fold.
  - SMOTE is applied to balance classes.
  - Model performance is evaluated with accuracy, precision, recall, and F1-score.

### Azure Integration Module
- **DTDL Schema:**  
  Define digital twin models with JSON:
  ```json
  {
    "@id": "dtmi:com:example:WindTurbine;1",
    "@type": "Interface",
    "displayName": "Wind Turbine",
    "contents": [
      { "@type": "Property", "name": "RotorSpeed", "schema": "double" },
      { "@type": "Property", "name": "Temperature", "schema": "double" },
      { "@type": "Property", "name": "PowerOutput", "schema": "double" },
      { "@type": "Property", "name": "PredictedFault", "schema": "string" }
    ],
    "@context": "dtmi:dtdl:context;2"
  }
