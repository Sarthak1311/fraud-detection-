import streamlit as st
import joblib

# Load model
model = joblib.load("/Users/sarthaktyagi/Desktop/projects /fraudDetection/notebook/bestRF.joblib")

def main():
    st.set_page_config(page_title="Fraud Detector", page_icon="🕵️‍♂️", layout="centered")

    st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🕵️‍♂️ Fraud Detection System</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: grey;'>Enter transaction details to evaluate fraud risk</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Input fields in columns
    col1, col2 = st.columns(2)
    
    with col1:
        step = st.number_input("📅 Step (time of transaction)", min_value=0)
        amount = st.number_input("💰 Amount to transfer", min_value=0.0)
        oldBalSender = st.number_input("🏦 Sender's old balance", min_value=0.0)
        oldBalrec = st.number_input("🏦 Receiver's old balance", min_value=0.0)

    with col2:
        newBalSender = st.number_input("🏦 Sender's new balance", min_value=0.0)
        newBalrec = st.number_input("🏦 Receiver's new balance", min_value=0.0)
        modeofpayment = st.selectbox("💳 Mode of Payment", ["cash Out", "debit", "payment", "transfer", "other"])

    # Compute derived features
    balanceErrorSender = (newBalSender + amount) - oldBalSender
    balanceErrorReciver = oldBalrec + amount - newBalrec

    # One-hot encode payment mode
    cash_out = modeofpayment == "cash Out"
    debit = modeofpayment == "debit"
    payment = modeofpayment == "payment"
    transfer = modeofpayment == "transfer"

    # Final input to model
    point = [step, amount, oldBalSender, newBalSender,
             oldBalrec, newBalrec, cash_out, debit,
             payment, transfer, balanceErrorSender, balanceErrorReciver]

    st.markdown("---")
    if st.button("🔍 Predict Transaction Legitimacy"):
        result = model.predict([point])
        if result[0] == 1:
            st.markdown("<h3 style='color: red;'>⚠️ Fraudulent Transaction Detected!</h3>", unsafe_allow_html=True)
            st.error("This transaction is likely fraudulent. Please investigate further.")
        else:
            st.markdown("<h3 style='color: green;'>✅ Legitimate Transaction</h3>", unsafe_allow_html=True)
            st.success("This transaction appears to be legitimate.")

    st.markdown("---")
    st.markdown("<footer style='text-align: center; color: gray;'>Made with ❤️ by Sarthak Tyagi</footer>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
