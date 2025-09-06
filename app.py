
import streamlit as st
import time

# --- Case Studies Data ---
CASE_STUDIES = {
    "Sacituzumab-DM1": {
        "antigen_sequence": "MARGPGLAPPPLRLPLLLLVLAAVTGHTAAQDNCTCPTNKMTVCSPDGPGGRCQCRALGSGMAVDCSTLTSKCLLLKARMSAPKNARTLVRPSEHALVDNDGLYDPDCDPEGRFKARQCNQTSVCWCVNSVGVRRTDKGDLSLRCDELVRTHHILIDLRHRPTAGAFNHSDLDAELRRLFRERYRLHPKFVAAVHYEQPTIQIELRQNTSQKAAGDVDIGDAAYYFERDIKGESLFQGRGGLDLRVRGEPLQVERTLIYYLDEIPPKFSMKRLTAGLIAVIVVVVVALVAGMAVLVITNRRKSGKYKKVEIKELGELRKEPSL",
        "antibody_heavy_chain": "QVQLQQSGSELKKPGASVKVSCKASGYTFTNYGMNWVKQAPGQGLKWMGWINTYTGEPTYTDDFKGRFAFSLDTSVSTAYLQISSLKADDTAVYFCARGG FGSSYWYFDVWGQGSLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKRVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK",
        "antibody_light_chain": "DIQLTQSPSSLSASVGDRVSITCKASQDVSIAVWYQQKPGKAPKLLIYSASYRYTGVDRFSGSGSGTDFTLTISSLQPEDFAVYYCQQHYITPLTFGAGTKVEIKRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC",
        "linker_smiles": "O=C(C1CCC(CN2C(C=CC2=O)=O)CC1)ON3C(CCC3=O)=O",
        "payload_smiles": "C[C@@H]1[C@@H]2C[C@]([C@@H](/C=C/C=C(/CC3=CC(=C(C(=C3)OC)Cl)N(C(=O)C[C@@H]([C@]4([C@H]1O4)C)OC(=O)[C@H](C)N(C)C(=O)CCS)C)\\C)OC)(NC(=O)O2)O",
        "dar": 6.2,
        "predicted_score": 0.9991,
        "predicted_activity": "ACTIVE (Good Candidate)",
        "confidence": 99.9,
    },
    "Trastuzumab-Gemcitabine": {
        "antigen_sequence": "MELAALCRWGLLLALLPPGAASTQVCTGTDMKLRLPASPETHLDMLRHLYQGCQVVQGNLELTYLPTNASLSFLQDIQEVQGYVLIAHNQVRQVPLQRLRIVRGTQLFEDNYALAVLDNGDPLNNTTPVTGASPGGLRELQLRSLTEILKGGVLIQRNPQLCYQDTILWKDIFHKNNQLALTLIDTNRSRLCHPCSPMCKGSRCWGESSEDCQSLTRTVCAGGCARCKGPLPTDCCHEQCAAGCTGPKHSDCLACLHFNHSGICELHCPALVTYNTDTFESMPNPEGRYTFGASCVTACPYNYLSTDVGSCTLVCPLHNQEVTAEDGTQRCEKCSKPCARVCYGLGMEHLREVRAVTSANIQEFAGCKKIFGSLAFLPESFDGDPASNTAPLQPEQLQVFETLEEITGYLYISAWPDSLPDLSVFQNLQVIRGRILHNGAYSLTLQGLGISWLGLRSLRELGSGLALIHHNTHLCFVHTVPWDQLFRNPHQALLHTANRPEDECVGEGLACHQLCARGHCWGPGPTQCVNCSQFLRGQECVEECRVLQGLPREYVNARHCLPCHPECQPQNGSVTCFGPEADQCVACAHYKDPPFCVARCPSGVKPDLSYMPIWKFPDEEGACQPCPINCTHSCVDLDDKGCPAEQRASPLTSIISAVVGILLVVVLGVVFGILIKRRQQKIRKYTMRRLLQETELVEPLTPSGAMPNQAQMRILKETELRKVKVLGSGAFGTVYKGIWIPDGENVKIPVAIKVLRENTSPKANKEILDEAYVMAGVGSPYVSRLLGICLTSTVQLVTQLMPYGCLLDHVRENRGRLGSQDLLNWCMQIAKGMSYLEDVRLVHRDLAARNVLVKSPNHVKITDFGLARLLDIDETEYHADGGKVPIKWMALESILHRIYTHQSDVWSYGVTVWELMTFGAEPYAGLRLAEVPDLLEKGERLAQPQICTIDVYMVMVKCWMIDENIRPTFKNLANKPDFLPCASPNKPREEQRFEKETTLWPEYAGGPADVLDRFYKTLRAEKEGLGSLGSFQSLPMLGVLGIYSKVQGNLQALRGRLETYLPTNASLSFLQDIQEVQGYVLIAHNQVRQVPLQRLRIVRGTQLFEDNYALAVLDNGDPLNNTTPVTGASPGGLRELQLRSLTEILKGGVLIQRNPQLCYQDTILWKDIFHKNNQLALTLIDTNRSRLCHPCSPMCKGSRCWGESSEDCQSLTRTVCAGGCARCKGPLPTDCCHEQCAAGCTGPKHSDCLACLHFNHSGICELHCPALVTYNTDTFESMPNPEGRYTFGASCVTACPYNYLSTDVGSCTLVCPLHNQEVTAEDGTQRCEKCSKPCARVCYGLGMEHLREVRAVTSANIQEFAGCKKIFGSLAFLPESFDGDPASNTAPLQPEQLQVFETLEEITGYLYISAWPDLPDLSVFQNLQVIRGRILHNGAYSLTLQGLGISWLGLRSLRELGSGLALIHHNTHLCFVHTVPWDQLFRNPHQALLHTANRPEDECVGEGLACHQLCARGHCWGPGPTQCVNCSQFLRGQECVEECRVLQGLPREYVNARHCLPCHPECQPQNGSVTCFGPEADQCVACAHYKDPPFCVARCPSGVKPDLSYMPIWKFPDEEGACQPCPINCTHSCVDLDDKGCPAEQRASPLTSIISAVVGILLVVVLGVVFGILIKRRQQKIRKYTMRRLLQETELVEPLTPSGAMPNQAQMRILKETELRKVKVLGSGAFGTVYKGIWIPDGENVKIPVAIKVLRENTSPKANKEILDEAYVMAGVGSPYVSRLLGICLTSTVQLVTQLMPYGCLLDHVRENRGRLGSQDLLNWCMQIAKGMSYLEDVRLVHRDLAARNVLVKSPNHVKITDFGLARLLDIDETEYHADGGKVPIKWMALESILHRIYTHQSDVWSYGVTVWELMTFGAEPYAGLRLAEVPDLLEKGERLAQPQICTIDVYMVMVKCWMIDENIRPTFKNLANKPDFLPCASPNKPREEQRFEKETTLWpeya",
        "antibody_heavy_chain": "EVQLVESGGGLVQPGGSLRLSCAASGFNIKDTYIHWVRQAPGKGLEWVARIYPTNGYTRYADSVKGRFTISADTSKNTAYLQMNSLRAEDTAVYYCSRWGGDGFYAMDYWGQGTLVTVSSASTKGPSVFPLAPSSKSTSGGTAALGCLVKDYFPEPVTVSWNSGALTSGVHTFPAVLQSSGLYSLSSVVTVPSSSLGTQTYICNVNHKPSNTKVDKKVEPKSCDKTHTCPPCPAPELLGGPSVFLFPPKPKDTLMISRTPEVTCVVVDVSHEDPEVKFNWYVDGVEVHNAKTKPREEQYNSTYRVVSVLTVLHQDWLNGKEYKCKVSNKALPAPIEKTISKAKGQPREPQVYTLPPSREEMTKNQVSLTCLVKGFYPSDIAVEWESNGQPENNYKTTPPVLDSDGSFFLYSKLTVDKSRWQQGNVFSCSVMHEALHNHYTQKSLSLSPGK",
        "antibody_light_chain": "DIQMTQSPSSLSASVGDRVTITCRASQDVNTAVAWYQQKPGKAPKLLIYSASFLYSGVPSRFSGSRSGTDFTLTISSLQPEDFATYYCQQHYTTPPTFGQGTKVEIKRTVAAPSVFIFPPSDEQLKSGTASVVCLLNNFYPREAKVQWKVDNALQSGNSQESVTEQDSKDSTYSLSSTLTLSKADYEKHKVYACEVTHQGLSSPVTKSFNRGEC",
        "linker_smiles": "C=N-N",
        "payload_smiles": "C1=CN(C(=O)N=C1N)[C@H]2C([C@@H]([C@H](O2)CO)O)(F)F",
        "dar": 6.0,
        "predicted_score": 0.0093,
        "predicted_activity": "INACTIVE (Poor Candidate)",
        "confidence": 0.9,
    }
}

# --- Functions to load case studies ---
def load_case(case_name):
    case_data = CASE_STUDIES[case_name]
    st.session_state.antigen_sequence = case_data["antigen_sequence"]
    st.session_state.antibody_heavy_chain = case_data["antibody_heavy_chain"]
    st.session_state.antibody_light_chain = case_data["antibody_light_chain"]
    st.session_state.linker_smiles = case_data["linker_smiles"]
    st.session_state.payload_smiles = case_data["payload_smiles"]
    st.session_state.dar = case_data["dar"]

# --- Streamlit App ---
st.set_page_config(page_title="DeepCure Prototype", layout="wide")

st.title("DeepCure: ADC Activity Prediction Prototype")

# --- ADC Explanation Section ---
with st.expander("Click here to learn what an Antibody-Drug Conjugate (ADC) is!"):
    st.markdown("### How ADCs Work: A Targeted Cancer Therapy")
    st.image("https://i.makeagif.com/media/5-17-2018/R9nDmq.gif", caption="Mechanism of Action for an Antibody-Drug Conjugate (ADC)")
    st.markdown("""
    An Antibody-Drug Conjugate (ADC) is a smart drug that delivers a powerful toxin directly to cancer cells while sparing healthy ones.

    1.  **🎯 Targeting:** An antibody (the 'A' in ADC) is engineered to seek out and bind to specific proteins (antigens) on the surface of cancer cells.
    2.  **🔗 Linking:** A stable linker (the 'C' for 'Conjugate') connects the antibody to a potent chemotherapy drug, or 'payload'.
    3.  **💣 Delivery & Release:** Once the antibody docks onto a cancer cell, the cell absorbs the ADC. Inside, the linker is broken down, releasing the payload.
    4.  **💥 Cell Destruction:** The released payload kills the cancer cell from within. This targeted approach minimizes the side effects associated with traditional chemotherapy.
    """)

st.markdown("This interface simulates the predictive power of the DeepCure AI model. "
            "Use the buttons in the sidebar to load a case study, or enter your own data.")

# --- Sidebar ---
st.sidebar.image("C:/Users/Sheetal/Downloads/DeepCure_Prototype/Logo of DeepCure.png", width=150)
st.sidebar.title("About DeepCure")
st.sidebar.info(
    "The DeepCure platform aims to accelerate the discovery of novel Antibody-Drug Conjugates (ADCs) "
    "by using a multi-modal AI to predict their efficacy against cancer targets. "
    "This prototype demonstrates the intended user workflow and predictive output of the final system."
)
st.sidebar.title("🧪 Case Studies for Demo")
st.sidebar.button("Load Active Case (Sacituzumab-DM1)", on_click=load_case, args=("Sacituzumab-DM1",))
st.sidebar.button("Load Inactive Case (Trastuzumab-Gemcitabine)", on_click=load_case, args=("Trastuzumab-Gemcitabine",))


# --- Input Section ---
st.header("🔬 ADC Component Input")

with st.form(key='adc_input_form'):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧬 Biological Components")
        with st.expander("Enter Biological Sequences", expanded=True):
            antigen_sequence = st.text_area("Antigen Sequence (e.g., TROP2, HER2)", height=100, key="antigen_sequence")
            antibody_heavy_chain = st.text_area("Antibody Heavy Chain Sequence", height=100, key="antibody_heavy_chain")
            antibody_light_chain = st.text_area("Antibody Light Chain Sequence", height=100, key="antibody_light_chain")

    with col2:
        st.subheader("⚗️ Chemical Components")
        with st.expander("Enter Chemical Information", expanded=True):
            linker_smiles = st.text_input("Linker SMILES String", key="linker_smiles")
            payload_smiles = st.text_input("Payload SMILES String (e.g., DM1_SMILES, Gemcitabine_SMILES)", key="payload_smiles")
            dar = st.number_input("Drug-Antibody Ratio (DAR)", min_value=0.0, max_value=20.0, step=0.1, key="dar")

    submit_button = st.form_submit_button(label='✨ Predict ADC Activity')

# --- Processing Logic & Output Section ---
if submit_button:
    with st.spinner('🔬 Analyzing ADC components... Please wait.'):
        time.sleep(2) # Simulate processing time

        st.header("🎯 Prediction Results")

        # Simulation Logic
        active_case = CASE_STUDIES["Sacituzumab-DM1"]
        inactive_case = CASE_STUDIES["Trastuzumab-Gemcitabine"]

        # Check against case studies
        if (st.session_state.payload_smiles == active_case["payload_smiles"] and
                st.session_state.antigen_sequence == active_case["antigen_sequence"]):
            result = active_case
            activity_color = "green"
        elif (st.session_state.payload_smiles == inactive_case["payload_smiles"] and
              st.session_state.antigen_sequence == inactive_case["antigen_sequence"]):
            result = inactive_case
            activity_color = "red"
        else:
            result = None

        if result:
            score = result["predicted_score"]
            activity = result["predicted_activity"]
            confidence = result["confidence"]

            st.metric(label="Predicted Score", value=f"{score:.4f}")
            st.markdown(f"**Predicted Activity:** <span style='font-size: 1.2em; color:{activity_color};'>{activity}</span>",
                        unsafe_allow_html=True)
            st.progress(confidence / 100)
            st.write(f"Confidence: {confidence}%")
        else:
            st.warning("Input does not match a known case study. This is a functional mock-up. "
                       "Please use the buttons in the sidebar to load a valid case study for demonstration.")
