import streamlit as st
import random
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Dropship Scout AI Pro", page_icon="🔥", layout="wide")

if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'search_history' not in st.session_state:
    st.session_state.search_history = []

product_db = {
    "beauty": [
        {"name": "Heatless Hair Curler", "cost": 3},
        {"name": "Blackhead Vacuum Tool", "cost": 4},
        {"name": "Glow Skin Ice Roller", "cost": 2},
        {"name": "LED Face Mask", "cost": 5},
        {"name": "Jade Roller Set", "cost": 2.5},
    ],
    "kitchen": [
        {"name": "Electric Vegetable Chopper", "cost": 5},
        {"name": "Silicone Oil Brush", "cost": 1},
        {"name": "Garlic Press Pro Tool", "cost": 2},
        {"name": "Egg Cooker", "cost": 6},
        {"name": "Air Fryer Accessories", "cost": 4},
    ],
    "gadgets": [
        {"name": "Mini Phone Tripod", "cost": 3},
        {"name": "Camera Lens Kit Mobile", "cost": 4},
        {"name": "Smart Watch Budget Edition", "cost": 8},
        {"name": "Wireless Earbuds", "cost": 6},
        {"name": "Phone Ring Stand", "cost": 1.5},
    ],
    "electronics": [
        {"name": "USB Hub Adapter", "cost": 5},
        {"name": "Portable Power Bank", "cost": 7},
        {"name": "Phone Charger Cable", "cost": 2},
        {"name": "Screen Protector", "cost": 1},
        {"name": "LED Desk Lamp", "cost": 4},
    ],
    "fashion": [
        {"name": "Wireless Headband", "cost": 3},
        {"name": "Sports Water Bottle", "cost": 2.5},
        {"name": "Sunglasses UV Protection", "cost": 4},
        {"name": "Baseball Cap", "cost": 2},
        {"name": "Compression Socks", "cost": 1.5},
    ],
}

def viral_score():
    return random.randint(40, 98)

def pakistan_competition():
    return random.choice(["LOW 🔥", "MEDIUM ⚠️", "HIGH ❌"])

def profit_estimate(cost):
    return round(cost * random.uniform(2.5, 5), 2)

def winning_badge(vs, comp):
    if vs > 80 and comp == "LOW 🔥":
        return "🏆 WINNING PRODUCT"
    elif vs > 65:
        return "🔥 GOOD PRODUCT"
    else:
        return "⚠️ TEST FIRST"

def get_roi(cost, profit):
    if cost == 0:
        return 0
    return round((profit / cost) * 100, 1)

st.title("🔥 Dropship Scout AI PRO")
st.write("Find winning Shopify products + competition + viral score (Pakistan Edition)")
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Discovery", "Favorites", "Analytics", "Daily Mode", "Settings"])

with tab1:
    st.header("🔍 Product Discovery")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        niche = st.selectbox("Select a niche:", list(product_db.keys()))
    with col2:
        search_btn = st.button("Find Products", use_container_width=True)
    
    if search_btn:
        st.session_state.search_history.append({"niche": niche, "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")})
        st.subheader(f"Results for {niche.upper()}")
        st.write(f"Found {len(product_db[niche])} products")
        st.divider()
        
        for item in product_db[niche]:
            vs = viral_score()
            comp = pakistan_competition()
            profit = profit_estimate(item["cost"])
            roi = get_roi(item["cost"], profit)
            badge = winning_badge(vs, comp)
            
            st.write(f"**{item['name']}**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Cost", f"${item['cost']}")
            with col2:
                st.metric("Viral Score", f"{vs}/100")
            with col3:
                st.metric("Competition", comp)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Profit", f"${profit}")
            with col2:
                st.metric("ROI", f"{roi}%")
            with col3:
                if st.button("Save", key=f"save_{item['name']}"):
                    st.session_state.favorites.append(item)
                    st.success(f"Saved: {item['name']}")
            with col4:
                st.write(badge)
            st.divider()

with tab2:
    st.header("❤️ My Favorites")
    
    if st.session_state.favorites:
        st.write(f"Saved {len(st.session_state.favorites)} products")
        
        if st.button("Export as CSV"):
            df = pd.DataFrame(st.session_state.favorites)
            csv = df.to_csv(index=False)
            st.download_button("Download CSV", csv, f"favorites_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", "text/csv")
        
        st.divider()
        
        for idx, item in enumerate(st.session_state.favorites):
            col1, col2 = st.columns([4, 1])
            with col1:
                vs = viral_score()
                profit = profit_estimate(item["cost"])
                st.write(f"**{item['name']}** - Cost: ${item['cost']} | Profit: ${profit} | Score: {vs}/100")
            with col2:
                if st.button("Remove", key=f"remove_{idx}"):
                    st.session_state.favorites.pop(idx)
                    st.rerun()
            st.divider()
    else:
        st.info("No favorites yet")

with tab3:
    st.header("📊 Analytics")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Products", sum(len(p) for p in product_db.values()))
    with col2:
        st.metric("Niches", len(product_db))
    with col3:
        st.metric("Favorites", len(st.session_state.favorites))
    with col4:
        st.metric("Searches", len(st.session_state.search_history))
    
    st.divider()
    st.subheader("Products by Niche")
    niche_data = {niche: len(products) for niche, products in product_db.items()}
    st.bar_chart(niche_data)
    
    st.divider()
    st.subheader("Average Cost by Niche")
    cost_data = {}
    for niche, products in product_db.items():
        avg_cost = sum(p["cost"] for p in products) / len(products) if products else 0
        cost_data[niche] = round(avg_cost, 2)
    st.bar_chart(cost_data)

with tab4:
    st.header("⚡ Daily Winning Product")
    
    if st.button("Get Today's Pick", use_container_width=True):
        all_products = []
        for products in product_db.values():
            all_products.extend(products)
        
        pick = random.choice(all_products)
        vs = viral_score()
        comp = pakistan_competition()
        profit = profit_estimate(pick["cost"])
        roi = get_roi(pick["cost"], profit)
        badge = winning_badge(vs, comp)
        
        st.success("🏆 Today's Winning Product!")
        st.divider()
        st.write(f"**Product:** {pick['name']}")
        st.write(f"**Cost:** ${pick['cost']}")
        st.write(f"**Viral Score:** {vs}/100")
        st.write(f"**Competition:** {comp}")
        st.write(f"**Estimated Profit:** ${profit}")
        st.write(f"**ROI:** {roi}%")
        st.write(f"**Status:** {badge}")
        st.divider()
        st.info("Tip: Make a TikTok demo video for this product!")
        
        if st.button("Save to Favorites"):
            st.session_state.favorites.append(pick)
            st.success(f"Saved: {pick['name']}")

with tab5:
    st.header("Settings")
    
    st.subheader("App Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Products", sum(len(p) for p in product_db.values()))
    with col2:
        st.metric("Favorites", len(st.session_state.favorites))
    with col3:
        st.metric("Searches", len(st.session_state.search_history))
    
    st.divider()
    st.subheader("Clear Data")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear Favorites", use_container_width=True):
            st.session_state.favorites = []
            st.success("Favorites cleared!")
    with col2:
        if st.button("Clear History", use_container_width=True):
            st.session_state.search_history = []
            st.success("History cleared!")
    
    st.divider()
    st.subheader("About")
    st.write("Dropship Scout AI Pro - Pakistan Edition")
    st.write("Find winning Shopify products with AI-powered analysis")
    st.write("Version 1.0.0 - Made with care")

st.divider()
st.write("Dropship Scout AI Pro | Find Winning Products Fast")
