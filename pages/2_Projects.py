import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json

st.title("Research Projects")

#----Import Images----
img_lottie_animation = Image.open("images/taro.jpg")
img_contact_form = Image.open("images/mining.jpg")


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Taro: A New Asset Issuance Protocol on Bitcoin")
        st.write(
            """
            Learn all about Taro!
            This new proposal enables new types of asset issuance and spending on the Bitcoin and Lightning Networks. Want to learn about it?
            """
        )
        st.markdown("[Read Here](https://coinshares.com/research/taro-a-new-asset-issuance-protocol-on-bitcoin)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("The Bitcoin Mining Network")
        st.write(
            """
            Curious about Bitcoin's energy consumption and environmental impact?
            In this report, I'll show you the results of a model that calculates just that. We highlight the patterns and trends of Bitcoin Mining, its power draw and carbon emissions by country and region, check it out!
            """
        )
        st.markdown("[Read Here](https://coinshares.com/research/bitcoin-mining-network-2022)")
 
with st.container():
    st.write("---")
    st.write("##")
    st.subheader("More Research!")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("[Oridinals and Inscriptions Primer](https://blog.coinshares.com/ordinals-and-inscriptions-primer-849deb3a638)")
        st.write("[Bitcoin Market Cycles Explained](https://coinshares.com/research/bitcoin-market-cycles-explained)")
        st.write("[Decentralized Finance Demystified](https://coinshares.com/research/defi-demystified)")
        st.write("[An On-Chain Analysis of Long-term Bitcoin Investors](https://coinshares.com/research/long-term-bitcoin-investors-continue-to-restrict-available-supply)")
        st.write("[Lightning Network Primer](https://coinshares.com/research/lightning-explained-bitcoin-high-speed-transmission-protocol)")
        st.write("[Taproot: Bitcoin's Most Recent Major Upgrade](https://coinshares.com/research/taproot-explained-bitcoin-protocol-upgrade)")
        st.write("[A Model of Bitcoin Monetary Demand](https://coinshares.com/research/a-total-addressable-market-model-for-monetary-bitcoin-demand)")
        st.write("[The Market Impact of Bitcoin Mining Cyclicality](https://coinshares.com/research/cyclicality-in-the-bitcoin-mining-industry-can-have-a-small-but-notable-impact-on-the-bitcoin-price)")
        st.write("[The Stablecoin Gateway to Bitcoin Adoption Part One](https://medium.com/coinshares/the-stablecoin-gateway-to-bitcoin-adoption-part-one-41036f0c935a)")
    with right_column:
        st.write("[History and Hardships of Bitcoin Block Production](https://medium.com/coinshares/the-history-and-woes-of-bitcoin-block-production-207f1a54bbba)")
        st.write("[Bitcoin and BRC-20: 75 days later](https://medium.com/coinshares/bitcoin-and-brc-20-75-days-later-eb221dc4af08)")
        st.write("[Bitcoin Ownership Literature Review](https://blog.coinshares.com/2023-global-bitcoin-ownership-overview-322d6fc7e85a)")
        st.write("[The Value of Ether Part One: Foundations are Important](https://medium.com/coinshares/the-value-of-ether-part-1-foundations-are-important-ad46182e0bb1)")
        st.write("[The Value of Ether Part Two: Adoption's Impact on Future Supply](https://medium.com/coinshares/the-value-of-ether-part-2-adoptions-impact-on-ether-supply-480e8ca5ee11)")
        st.write("[The Value of Ether Part Three: The Past and Future of Block Space Demand](https://medium.com/coinshares/the-value-of-ether-part-3-the-past-and-future-of-block-space-demand-d45cc0c27c27)")
        st.write("[The Value of Ether Part Four: It's All About the Burn](https://medium.com/coinshares/the-value-of-ether-part-4-its-all-about-l1-burn-c8fe170a6ebc)")
        st.write("[The Stablecoin Gateway to Bitcoin Adoption Part One](https://medium.com/coinshares/the-stablecoin-gateway-to-bitcoin-adoption-part-two-122d396b8016)")
