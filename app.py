# แทนที่เฉพาะ CSS ของ CATEGORY SELECTOR เดิมทั้งหมดด้วยส่วนนี้
# วางภายใน <style> ก่อน </style>

.bottom-category-title {
    color: #707583 !important;
    font-size: 12px !important;
    font-weight: 800 !important;
    text-align: center !important;
    margin: 12px 0 6px 0 !important;
}

.st-key-category_selector [data-testid="stHorizontalBlock"] {
    gap: 5px !important;
    align-items: center !important;
}

.st-key-category_selector [data-testid="column"],
.st-key-category_selector div[data-testid="stButton"] {
    min-width: 0 !important;
    padding: 0 !important;
}

/* ปุ่มทุกปุ่ม */
.st-key-category_selector div[data-testid="stButton"] > button,
.st-key-category_selector div[data-testid="stButton"] > button:hover,
.st-key-category_selector div[data-testid="stButton"] > button:focus,
.st-key-category_selector div[data-testid="stButton"] > button:active {
    width: 100% !important;
    min-width: 0 !important;
    min-height: 34px !important;
    height: 34px !important;
    padding: 0 7px !important;
    border-radius: 999px !important;
    border: 1px solid #dedfe5 !important;
    box-shadow: none !important;
    outline: none !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 5px !important;
}

/* ปุ่มที่ยังไม่ได้เลือก */
.st-key-category_selector button[kind="secondary"],
.st-key-category_selector [data-testid="stBaseButton-secondary"] {
    background: #ffffff !important;
    background-color: #ffffff !important;
    color: #555b69 !important;
    -webkit-text-fill-color: #555b69 !important;
}

/* ปุ่มที่เลือก */
.st-key-category_selector button[kind="primary"],
.st-key-category_selector [data-testid="stBaseButton-primary"] {
    background: linear-gradient(
        135deg,
        #f8d8e8 0%,
        #e8ddff 35%,
        #dcecff 58%,
        #dff4e7 100%
    ) !important;
    background-color: #f3e8f7 !important;
    border-color: #decce8 !important;
    color: #555b69 !important;
    -webkit-text-fill-color: #555b69 !important;
}

/* สำคัญ: กำหนดเฉพาะ p ซึ่งเป็นข้อความ ห้ามกำหนด span เพราะจะกระทบ icon ภายใน Streamlit */
.st-key-category_selector div[data-testid="stButton"] > button p {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    margin: 0 !important;
    padding: 0 !important;
    color: #555b69 !important;
    -webkit-text-fill-color: #555b69 !important;
    font-size: 11px !important;
    font-weight: 800 !important;
    line-height: 1.05 !important;
    letter-spacing: -0.12px !important;
    white-space: nowrap !important;
    overflow: visible !important;
    text-overflow: clip !important;
}

.st-key-category_selector button[kind="primary"] p,
.st-key-category_selector [data-testid="stBaseButton-primary"] p {
    font-weight: 900 !important;
}

/* วงกลมสีขาวของปุ่มที่ยังไม่ได้เลือก */
.st-key-category_selector button[kind="secondary"]::before,
.st-key-category_selector [data-testid="stBaseButton-secondary"]::before {
    content: "" !important;
    display: block !important;
    width: 10px !important;
    height: 10px !important;
    min-width: 10px !important;
    flex: 0 0 10px !important;
    border-radius: 50% !important;
    background: #ffffff !important;
    border: 1.4px solid #d5d8df !important;
    box-sizing: border-box !important;
}

/* วงกลมแดงอ่อนของปุ่มที่เลือก */
.st-key-category_selector button[kind="primary"]::before,
.st-key-category_selector [data-testid="stBaseButton-primary"]::before {
    content: "" !important;
    display: block !important;
    width: 11px !important;
    height: 11px !important;
    min-width: 11px !important;
    flex: 0 0 11px !important;
    border-radius: 50% !important;
    background: #ffd9df !important;
    border: 3px solid #ff6f83 !important;
    box-sizing: border-box !important;
}

@media (max-width: 520px) {
    .st-key-category_selector [data-testid="stHorizontalBlock"] {
        gap: 5px !important;
    }

    .st-key-category_selector div[data-testid="stButton"] > button {
        min-height: 34px !important;
        height: 34px !important;
        padding: 0 6px !important;
    }

    .st-key-category_selector div[data-testid="stButton"] > button p {
        font-size: 10.5px !important;
    }
}


# แทนที่ CATEGORY SELECTOR ส่วน Python เดิมทั้งหมดด้วยส่วนนี้
# ส่วนนี้ต้องอยู่นอก st.markdown("""<style> ... </style>""")

st.markdown(
    '<div class="bottom-category-title">เลือกหมวดคำศัพท์</div>',
    unsafe_allow_html=True
)

CATEGORY_ITEMS = [
    (1, "CBS"),
    (2, "System & API"),
    (3, "Incident & Ops"),
    (4, "AI / LLM"),
    (5, "Testing / UAT"),
]

current_item = next(
    item for item in CATEGORY_ITEMS
    if item[0] == st.session_state.selected_set
)

other_items = [
    item for item in CATEGORY_ITEMS
    if item[0] != st.session_state.selected_set
]

# หมวดที่เลือกอยู่ลำดับ 3 เสมอ
display_items = other_items[:2] + [current_item] + other_items[2:]


def render_category_button(set_id, label, row_name):
    is_selected = set_id == st.session_state.selected_set

    if st.button(
        label,
        key=f"category_{row_name}_{set_id}_{st.session_state.selected_set}",
        type="primary" if is_selected else "secondary",
        use_container_width=True,
    ):
        if not is_selected:
            st.session_state.selected_set = set_id
            st.rerun()


with st.container(key="category_selector"):
    # แถวแรก 3 ปุ่ม โดยปุ่มที่เลือกอยู่ลำดับ 3
    top_row = st.columns(3, gap="small")

    for index, (set_id, label) in enumerate(display_items[:3]):
        with top_row[index]:
            render_category_button(set_id, label, "top")

    # แถวที่สอง 2 ปุ่ม วางกึ่งกลาง
    bottom_row = st.columns([0.5, 1, 1, 0.5], gap="small")

    for index, (set_id, label) in enumerate(display_items[3:]):
        with bottom_row[index + 1]:
            render_category_button(set_id, label, "bottom")
