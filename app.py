import streamlit as st
import datetime
import random

st.set_page_config(page_title="Sudais Express - Pakistan", layout="wide", page_icon="🚌")

# ===== BLACK & GOLD THEME =====
st.markdown("""
<style>
.stApp { background-color: #0F0F0F; }
header {visibility: hidden;}
.block-container {padding-top: 1rem;}
section[data-testid="stSidebar"] { background-color: #151515; border-right: 1px solid #2a2a2a; }
.gold-title { color: #E9C97B; font-weight: 800; font-size: 24px; }
.gold-sub { color: #B8A16A; font-size: 12px; }
.confirm-banner {
    background: #1A1A1A; border: 1.5px solid #C5A86A; border-radius: 12px;
    padding: 14px 20px; text-align: center; position: relative; margin-bottom: 18px;
}
.confirm-banner:before, .confirm-banner:after {
    content: " "; position: absolute; top: 50%; width: 18px; height: 18px;
    background: #0F0F0F; border: 1.5px solid #C5A86A; border-radius: 50%;
}
.confirm-banner:before { left: -10px; } .confirm-banner:after { right: -10px; }
.confirm-title { color: #E9C97B; font-size: 26px; font-weight: 800; }
.fleet-card { background: #1C1C1C; border: 1px solid #3A3525; border-radius: 12px; padding: 16px; }
.fleet-card-active { border: 1px solid #E9C97B; }
.fleet-number { color: #E9C97B; font-size: 36px; font-weight: 800; line-height: 1; }
.fleet-label { color: #CFC49A; font-size: 14px; }
.route-card { background: #1C1C1C; border: 1px solid #2E2A1F; border-radius: 12px; padding: 16px 18px; margin-bottom: 14px; }
.badge-gold { background: #E9C97B; color: #0F0F0F; font-weight: 800; padding: 4px 10px; border-radius: 6px; font-size: 13px; }
.price-gold { color: #E9C97B; font-weight: 800; font-size: 22px; }
.seat-badge { background: #2A2A2A; color: #E0D5B0; padding: 4px 10px; border-radius: 20px; font-size: 12px; border: 1px solid #3a3a3a; }
.progress-bg { background: #2A2A2A; height: 6px; border-radius: 10px; overflow: hidden; }
.progress-fill { background: #E9C97B; height: 100%; }
.boarding-pass-wrap { background: #0F0F0F; display: flex; justify-content: center; padding: 10px; }
.boarding-pass {
    background: #121212; border: 2px solid #C5A86A; border-radius: 18px; 
    padding: 22px 24px; width: 100%; max-width: 720px; position: relative;
}
.bp-title { color: #E9C97B; font-weight: 800; font-size: 18px; letter-spacing: 1px; }
.bp-conf { color: #C9B896; font-size: 11px; font-weight: 600; }
.bp-label { color: #B89F6B; font-size: 10px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; }
.bp-value { color: #F5EED0; font-weight: 700; font-size: 16px; }
.bp-value-big { color: #FFFFFF; font-weight: 800; font-size: 18px; }
.bp-divider { border-top: 1.5px dashed #5A4D2E; margin: 12px 0; }
.barcode { background: repeating-linear-gradient(90deg, #C5A86A 0 3px, transparent 3px 5px, #C5A86A 5px 6px, transparent 6px 9px); height: 36px; width: 100%; max-width: 320px; margin: 8px auto; }
.filter-box { background: #1A1A1A; border-radius: 12px; padding: 16px; border: 1px solid #252525; }
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Booking Form"
if "bookings" not in st.session_state:
    st.session_state.bookings = []

# ===== PAKISTAN ROUTES - Aapki Demand =====
routes_data = [
    {"id":"R101","from":"Karachi","to":"Hyderabad","time":"09:00 AM","duration":"Approx 2h 30m","fare":1200,"available":42,"total":45,"amen":"AC • WiFi • Recliner"},
    {"id":"R102","from":"Karachi","to":"Lahore","time":"07:00 PM","duration":"Approx 16h 00m","fare":5000,"available":30,"total":45,"amen":"Sleeper • Luxury • AC"},
    {"id":"R103","from":"Lahore","to":"Islamabad","time":"08:00 AM","duration":"Approx 4h 30m","fare":1800,"available":35,"total":40,"amen":"Executive • AC • WiFi"},
    {"id":"R104","from":"Islamabad","to":"Peshawar","time":"11:00 AM","duration":"Approx 2h 30m","fare":950,"available":28,"total":32,"amen":"AC • Business"},
    {"id":"R105","from":"Multan","to":"Faisalabad","time":"02:00 PM","duration":"Approx 3h 30m","fare":1200,"available":38,"total":45,"amen":"AC • Recliner • WiFi"},
    {"id":"R106","from":"Karachi","to":"Sukkur","time":"09:30 PM","duration":"Approx 8h 00m","fare":2000,"available":22,"total":36,"amen":"Executive Gold • AC"},
]

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown('<div class="gold-title">🚌 SUDAIS<br>EXPRESS</div><div class="gold-sub">Bus Booking Dashboard • Pakistan</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Navigation**")
    if st.button("• Booking Form", use_container_width=True):
        st.session_state.page = "Booking Form"
    if st.button("☑ Booking Confirmation", use_container_width=True):
        st.session_state.page = "Booking Confirmation"
    st.markdown("<br><br>")
    if st.session_state.page == "Booking Form":
        st.markdown('<div class="filter-box">', unsafe_allow_html=True)
        st.markdown("**🔻 Filters**")
        st.markdown("**Route**")
        route_opt = st.selectbox("Route", ["Karachi → Hyderabad","Karachi → Lahore","Lahore → Islamabad","Islamabad → Peshawar","Multan → Faisalabad","Karachi → Sukkur"], label_visibility="collapsed")
        st.markdown("**Departure Date**")
        dep_date = st.date_input("Date", datetime.date(2024,10,25), label_visibility="collapsed")
        st.markdown("**Price Range (Rs)**")
        price = st.slider("Price", 800, 5000, (800, 2000), label_visibility="collapsed")
        st.caption(f"Selected: Rs {price[0]} - Rs {price[1]}")
        st.markdown("**Amenities**")
        st.checkbox("AC", value=True)
        st.checkbox("WiFi", value=True)
        st.checkbox("Recliner", value=True)
        st.button("Apply Filters", use_container_width=True, type="primary")
        st.button("Reset Filters", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ===== PAGE 1: LIVE FLEET =====
if st.session_state.page == "Booking Form":
    col_head, col_time = st.columns([3,1])
    with col_head:
        st.markdown('<h2 style="color:#F5F5F5; margin:0;">Live Fleet Availability</h2><p style="color:#8a8a8a; margin:0;">Real-time overview of fleet status and route availability</p>', unsafe_allow_html=True)
    with col_time:
        st.markdown(f'<div style="border:1px solid #C5A86A; border-radius:8px; padding:6px 10px; text-align:center;"><span style="color:#C5A86A; font-size:11px;">Live • Pakistan Time<br><b style="color:white;">{datetime.datetime.now().strftime("%I:%M %p")}</b></span></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown('<div class="fleet-card fleet-card-active"><div class="fleet-label">🚌 Total Buses</div><div class="fleet-number">6</div><div style="color:#6fcf7a; font-size:11px;">↑ 0 from yesterday</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="fleet-card"><div class="fleet-label">💺 Total Seats</div><div class="fleet-number">243</div><div style="color:#8a8a8a; font-size:11px;">Across 6 active buses</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="fleet-card"><div class="fleet-label">📈 Occupancy</div><div class="fleet-number">0%</div><div style="color:#8a8a8a; font-size:11px;">No passengers currently onboard</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="display:flex; justify-content:space-between;"><h3 style="color:white; margin:0;">Active Routes (6) - Pakistan</h3><span style="color:#C5A86A;">Showing 6 of 6 routes</span></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    for r in routes_data:
        pct = int((r["available"]/r["total"])*100)
        st.markdown(f"""
        <div class="route-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div><span class="badge-gold">{r["id"]}</span> <span style="color:white; font-weight:700; margin-left:8px;">{r["from"]} → {r["to"]}</span></div>
                <div style="text-align:right;"><span class="price-gold">Rs {r["fare"]}</span><br><span style="color:#9a9a9a; font-size:11px;">per seat</span></div>
            </div>
            <div style="margin-top:8px; display:flex; gap:8px;">
                <span class="seat-badge">🕘 {r["time"]}</span>
                <span class="seat-badge">⏱ {r["duration"]}</span>
                <span class="seat-badge">{r["amen"]}</span>
            </div>
            <div style="margin-top:12px; display:flex; justify-content:space-between;">
                <span style="color:#E9C97B; font-weight:600;">Seat Availability</span>
                <span style="color:white; font-weight:700;">{r["available"]} / {r["total"]} Seats Available</span>
            </div>
            <div class="progress-bg" style="margin-top:6px;"><div class="progress-fill" style="width:{pct}%"></div></div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Book Now", key=f"book_{r['id']}", use_container_width=True, type="primary"):
            st.session_state.selected_route = r
            st.session_state.page = "Booking Confirmation"
            st.rerun()

# ===== PAGE 2: BOARDING PASS - PAKISTAN VERSION =====
else:
    if "selected_route" not in st.session_state:
        st.session_state.selected_route = routes_data[0]

    if len(st.session_state.bookings) == 0:
        st.markdown('<div class="confirm-banner"><div class="confirm-title">Book Your Ticket - Pakistan Routes</div><div style="color:#9a9a9a; font-size:13px;">Select Pakistan city route to generate boarding pass</div></div>', unsafe_allow_html=True)
        with st.form("booking_form"):
            c1,c2 = st.columns(2)
            with c1:
                name = st.text_input("Passenger Name", "Ahmed Al Sudais")
                # PAKISTAN ROUTES ONLY
                route_sel = st.selectbox("Route (Pakistan)", ["Karachi → Hyderabad","Karachi → Lahore","Lahore → Islamabad","Islamabad → Peshawar","Multan → Faisalabad","Karachi → Sukkur"])
                class_sel = st.selectbox("Class", ["Business Class","Executive Gold","Sleeper Luxury","Economy"])
            with c2:
                seat_sel = st.selectbox("Seat", ["B12","A1","A2","B10","C05"])
                date_sel = st.date_input("Travel Date", datetime.date(2024,10,25))
                gate_sel = st.selectbox("Gate", ["Gate 07","Gate 05","Gate 03","Gate 01"])
            submitted = st.form_submit_button("✅ Confirm & Generate Boarding Pass", type="primary", use_container_width=True)
            if submitted:
                sel_r = next((x for x in routes_data if f"{x['from']} → {x['to']}" == route_sel), routes_data[0])
                st.session_state.bookings.append({
                    "name": name, "route": route_sel, "class": class_sel, 
                    "seat": seat_sel, "date": date_sel, "gate": gate_sel,
                    "ticket": f"SE-{random.randint(80000000,89999999)}",
                    "booking_ref": f"SUDAIS-{random.randint(1000,9999)}PK",
                    "payment": f"PKR {sel_r['fare']}",
                    "fare": sel_r['fare']
                })
                st.rerun()
    else:
        b = st.session_state.bookings[-1]
        
        st.markdown("""
        <div class="confirm-banner">
            <div class="confirm-title">✅ Booking Confirmed!</div>
            <div style="color:#C9B896; font-size:13px;">Your Pakistan intercity ticket has been booked. Print or download boarding pass below.</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="text-align:center; margin-bottom: 12px;">
            <h1 style="color:#E9C97B; margin:0; font-size: 32px;">🎫 Boarding Pass</h1>
        </div>
        <div class="boarding-pass-wrap">
        <div class="boarding-pass">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 12px;">
                <span class="bp-title">SUDAIS EXPRESS</span>
                <span class="bp-conf">CONFIRMED • 1 PASSENGER • PAKISTAN</span>
            </div>
            <div class="bp-divider"></div>
            <div style="display:flex; gap:20px;">
                <div style="flex:1;">
                    <div class="bp-label">Passenger</div>
                    <div class="bp-value-big">{b['name']}</div>
                    <div style="margin-top:10px;" class="bp-label">Ticket No.</div>
                    <div class="bp-value">{b['ticket']}</div>
                    <div style="margin-top:10px;" class="bp-label">Class</div>
                    <div class="bp-value">{b['class']}</div>
                    <div style="margin-top:10px; display:flex; gap:6px;">
                        <span class="bp-label">✈ GATE</span> <span class="bp-value" style="margin-left:8px;">{b['gate']}</span>
                    </div>
                </div>
                <div style="flex:1;">
                    <div class="bp-label">Route - Pakistan</div>
                    <div class="bp-value-big">{b['route']}</div>
                    <div style="margin-top:10px;" class="bp-label">Date & Time</div>
                    <div class="bp-value">Fri, 25 Oct 2024 • 18:30 • PKT</div>
                    <div style="margin-top:10px;" class="bp-label">Seat</div>
                    <div class="bp-value-big">{b['seat']}</div>
                    <div style="margin-top:10px; display:flex; gap:6px;">
                        <span class="bp-label">⌛ BOARDING</span> <span class="bp-value" style="margin-left:8px;">17:50</span>
                    </div>
                </div>
            </div>
            <div style="text-align:center; margin-top:14px;">
                <div class="barcode"></div>
                <div style="color:#9A8A5A; font-size:11px; margin-top:4px;">Scan at boarding gate - Pakistan</div>
            </div>
            <div class="bp-divider"></div>
            <div style="display:flex; justify-content:space-between; background:#1A1A1A; border-radius:8px; padding:10px 14px; border:1px solid #2a2a2a;">
                <div><div class="bp-label">Payment</div><div class="bp-value" style="font-size:13px;">Paid • {b['payment']}</div></div>
                <div><div class="bp-label">Booking Ref</div><div class="bp-value" style="font-size:13px;">{b['booking_ref']}</div></div>
                <div><div class="bp-label">Status</div><div style="color:#8fcf7a; font-weight:700; font-size:13px;">✔ Confirmed</div></div>
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            st.button("🖨️ Print Ticket", use_container_width=True, type="primary")
        with c2:
            st.button("⬇️ Download Ticket", use_container_width=True)

        st.markdown('<p style="text-align:center; color:#6a6a6a; font-size:11px; margin-top:16px;">Need assistance? support@sudaisexpress.pk • 24/7 Hotline: 0800-SUDAIS (783247) • Pakistan</p>', unsafe_allow_html=True)
        
        if st.button("Book Another Ticket"):
            st.session_state.bookings = []
            st.session_state.page = "Booking Form"
            st.rerun()