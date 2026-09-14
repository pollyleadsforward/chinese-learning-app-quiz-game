import html
import random
import time

import streamlit as st

try:
    from PIL import Image
    app_icon = Image.open("app_icon.png")
except Exception:
    app_icon = "🇨🇳"

st.set_page_config(
    page_title="Chinese Learning App",
    page_icon=app_icon,
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
html { color-scheme: light !important; }
html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background: #fffdfd !important;
}
.block-container {
    max-width: 800px !important;
    padding: .65rem 1.05rem .85rem !important;
}
header, footer, #MainMenu, [data-testid="stToolbar"],
[data-testid="stStatusWidget"], [data-testid="stDecoration"],
[data-testid="stAppDeployButton"], .stDeployButton {
    display: none !important;
    visibility: hidden !important;
}
.main-title {
    text-align: center;
    font-size: clamp(36px, 5.2vw, 50px);
    font-weight: 900;
    line-height: 1.02;
    margin: 0 0 4px;
    white-space: nowrap;
    letter-spacing: -.45px;
    background: linear-gradient(90deg,#efa6d5,#d2b3fa,#acc4ff,#8fddff,#90e8d3,#beeaa9,#efd79b,#f3b7b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.by-line {
    text-align: center;
    font-size: 12px;
    font-weight: 800;
    margin: 0 0 11px;
    background: linear-gradient(90deg,#d7b0f7,#9ec9ff,#8ddfd7,#b9e89e,#f2c8a2,#eea6c8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.active-category {
    text-align: center;
    color: #727784;
    font-size: 15.5px;
    font-weight: 800;
    margin: 0 0 13px;
}
.score-grid {
    display: grid;
    grid-template-columns: repeat(3,minmax(0,1fr));
    gap: 10px;
    width: 100%;
    margin: 0 0 30px;
}
.score-card {
    min-height: 72px;
    padding: 8px 5px;
    border-radius: 18px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
}
.score-purple { background:#edddfb; border:1.4px solid #d7b3f6; }
.score-pink { background:#ffdee9; border:1.4px solid #f4b4cc; }
.score-green { background:#ddf4e4; border:1.4px solid #9cddae; }
.score-label { color:#727784; font-size:11px; font-weight:800; margin-bottom:4px; }
.score-number { color:#565b67; font-size:27px; line-height:1; font-weight:900; }
.question-shell { width:100%; display:flex; justify-content:center; margin:0 0 9px; }
.question-center { width:100%; text-align:center; }
.question-label, .review-label {
    text-align:center; color:#727784; font-size:17px; font-weight:800; margin:0 0 15px;
}
.review-label { color:#8c7b91; }
.chinese-short, .chinese-medium, .chinese-long {
    font-weight:900; line-height:1; text-align:center; display:inline-block;
    white-space:nowrap; max-width:100%; margin:0;
    background:linear-gradient(90deg,#efa6d5,#d2b3fa,#acc4ff,#8fddff,#90e8d3,#beeaa9,#efd79b,#f3b7b8);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.chinese-short { font-size:clamp(72px,11vw,102px); }
.chinese-medium { font-size:clamp(49px,8vw,70px); }
.chinese-long { font-size:clamp(34px,5.6vw,50px); }
.st-key-answer_area div[data-testid="stVerticalBlock"] { gap:.42rem !important; }
.st-key-answer_area div[data-testid="stButton"] > button,
.st-key-answer_area div[data-testid="stButton"] > button:hover,
.st-key-answer_area div[data-testid="stButton"] > button:focus,
.st-key-answer_area div[data-testid="stButton"] > button:active {
    width:100% !important; min-height:49px !important; padding:.48rem .72rem !important;
    border-radius:15px !important; background:#fff !important; color:#4d5260 !important;
    border:1px solid #dedfe5 !important; box-shadow:none !important;
}
.st-key-answer_area button p, .st-key-answer_area button span {
    color:#4d5260 !important; -webkit-text-fill-color:#4d5260 !important;
    font-size:16px !important; font-weight:500 !important;
}
.bottom-category-title {
    color:#707583; font-size:12px; font-weight:800; text-align:center; margin:12px 0 6px;
}
.st-key-category_selector { width:100% !important; max-width:100% !important; }
.st-key-category_selector div[data-testid="stButton"] { width:100% !important; min-width:0 !important; }
.st-key-category_selector button[kind="secondary"],
.st-key-category_selector button[kind="secondary"]:hover,
.st-key-category_selector button[kind="secondary"]:focus,
.st-key-category_selector button[kind="secondary"]:active,
.st-key-category_selector [data-testid="stBaseButton-secondary"] {
    width:100% !important; min-width:0 !important; min-height:42px !important;
    padding:.35rem !important; background:#fff !important; color:#555b69 !important;
    -webkit-text-fill-color:#555b69 !important; border:1px solid #dedfe5 !important;
    border-radius:12px !important; box-shadow:none !important; outline:none !important;
}
.st-key-category_selector button[kind="primary"],
.st-key-category_selector button[kind="primary"]:hover,
.st-key-category_selector button[kind="primary"]:focus,
.st-key-category_selector button[kind="primary"]:active,
.st-key-category_selector [data-testid="stBaseButton-primary"] {
    width:100% !important; min-width:0 !important; min-height:42px !important;
    padding:.35rem !important;
    background:linear-gradient(135deg,#f8d8e8 0%,#e8ddff 35%,#dcecff 58%,#dff4e7 100%) !important;
    color:#555b69 !important; -webkit-text-fill-color:#555b69 !important;
    border:1px solid #decce8 !important; border-radius:12px !important;
    box-shadow:none !important; outline:none !important;
}
.st-key-category_selector button p, .st-key-category_selector button span {
    color:#555b69 !important; -webkit-text-fill-color:#555b69 !important;
    font-weight:800 !important; opacity:1 !important;
}
.st-key-category_selector button[kind="primary"] p,
.st-key-category_selector button[kind="primary"] span { font-weight:900 !important; }
.st-key-category_selector button[kind="secondary"]::before,
.st-key-category_selector [data-testid="stBaseButton-secondary"]::before {
    content:"" !important; display:block !important; width:11px !important; height:11px !important;
    min-width:11px !important; flex:0 0 11px !important; border-radius:50% !important;
    background:#fff !important; border:1.4px solid #d5d8df !important; box-sizing:border-box !important;
}
.st-key-category_selector button[kind="primary"]::before,
.st-key-category_selector [data-testid="stBaseButton-primary"]::before {
    content:"" !important; display:block !important; width:12px !important; height:12px !important;
    min-width:12px !important; flex:0 0 12px !important; border-radius:50% !important;
    background:#ffd9df !important; border:3px solid #ff6f83 !important; box-sizing:border-box !important;
}
.st-key-category_selector button[kind="secondary"],
.st-key-category_selector button[kind="primary"] {
    display:flex !important; align-items:center !important; justify-content:center !important; gap:6px !important;
}
.st-key-bottom_actions { margin-top:11px !important; }
.st-key-bottom_actions button {
    width:40px !important; min-width:40px !important; height:37px !important;
    padding:0 !important; border-radius:10px !important; background:#fff !important;
    color:#727784 !important; border:1px solid #dedfe5 !important; box-shadow:none !important;
}
.quote-text {
    text-align:center; font-size:clamp(23px,4.2vw,32px); font-weight:850;
    font-style:italic; line-height:1.32; margin:0;
    background:linear-gradient(90deg,#efa6d5,#d2b3fa,#acc4ff,#8fddff,#90e8d3,#beeaa9,#efd79b,#f3b7b8);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
@media (max-width:520px) {
    .block-container { max-width:100% !important; padding:.38rem .62rem .5rem !important; }
    .main-title { font-size:clamp(32.46px,9.557vw,37.87px) !important; }
    .score-grid { gap:7px !important; margin-bottom:28px !important; }
    .score-card { min-height:61px !important; padding:6px 3px !important; border-radius:16px !important; }
    .score-label { font-size:9.6px !important; }
    .score-number { font-size:23px !important; }
    .chinese-short { font-size:clamp(68px,20vw,84px) !important; }
    .chinese-medium { font-size:clamp(46px,13.4vw,59px) !important; }
    .chinese-long { font-size:clamp(31px,8.5vw,42px) !important; }
    .st-key-category_selector [data-testid="stHorizontalBlock"] {
        display: grid !important;
        grid-template-columns: repeat(6, minmax(0, 1fr)) !important;
        column-gap: 5px !important;
        row-gap: 5px !important;
        width: 100% !important;
        align-items: center !important;
    }

    /* First row: 3 equal buttons. Second row: 2 centered buttons. */
    .st-key-category_selector [data-testid="column"]:nth-child(1) {
        grid-column: 1 / span 2 !important;
    }
    .st-key-category_selector [data-testid="column"]:nth-child(2) {
        grid-column: 3 / span 2 !important;
    }
    .st-key-category_selector [data-testid="column"]:nth-child(3) {
        grid-column: 5 / span 2 !important;
    }
    .st-key-category_selector [data-testid="column"]:nth-child(4) {
        grid-column: 2 / span 2 !important;
    }
    .st-key-category_selector [data-testid="column"]:nth-child(5) {
        grid-column: 4 / span 2 !important;
    }
    .st-key-category_selector [data-testid="column"] { width:100% !important; min-width:0 !important; padding:0 !important; }
    .st-key-category_selector button[kind="secondary"],
    .st-key-category_selector button[kind="primary"] {
        height: 34px !important;
        min-height: 34px !important;
        padding: 0 7px !important;
        border-radius: 999px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 5px !important;
    }

    /* One white circle for every unselected category. */
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

    /* Selected category: soft red ring with a pale red center. */
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

    .st-key-category_selector button p,
    .st-key-category_selector button span {
        font-size: 10.5px !important;
        line-height: 1.05 !important;
        letter-spacing: -0.12px !important;
        white-space: nowrap !important;
    }
    .quote-text { font-size:clamp(23px,7.8vw,31px) !important; }
}
</style>
""",
    unsafe_allow_html=True,
)

# Vocabulary retained as editable category lists.
VOCAB_SETS = {
    1: [('系统','System'),('开发','Development'),('需求','Requirement'),('请求','Request'),('调用接口','Call API'),('参数','Parameter'),('响应','Response'),('测试','Testing'),('测试用例','Test Case'),('验收测试','UAT / Acceptance Testing'),('确认','Confirm'),('流程','Process'),('上线','Go Live'),('异常','Exception'),('错误','Error'),('日志','Log'),('数据','Data'),('数据库','Database'),('架构','Architecture'),('点击','Click')],
    2: [('这个','this'),('业务','Business'),('部门','department'),('解决','Resolve'),('问题','Issue'),('项目','Project'),('范围','Scope'),('我们','we'),('产品','Product'),('目标','Goal'),('前端','Frontend'),('后端','Backend'),('用户','User'),('按钮','button'),('接口','Interface'),('字段','Field'),('环境','Environment'),('版本','Version'),('发布','Release'),('回滚','Rollback')],
    3: [('客户','customer'),('时间','time'),('事故','Incident'),('复盘','Postmortem'),('结果','Outcome'),('风险','Risk'),('假设','Assumption'),('验证','Validate'),('场景','Scenario'),('任务','task'),('完成','Complete'),('缺陷','Defect'),('回归','Regression'),('性能','Performance'),('权限','Permission'),('审计','Audit'),('部署','Deployment'),('迁移','Migration'),('监控','Monitoring'),('指标','Metric')],
    4: [('延迟','Delay'),('支持','support'),('温度','temperature'),('上下文','Context'),('格式','Format'),('提示词','Prompt'),('嵌入','Embedding'),('文档','document'),('元数据','Metadata'),('检索','Retrieval'),('知识库','Knowledge Base'),('答案','answer'),('引用','Citation'),('来源','source'),('微调','Fine-tuning'),('成本','Cost'),('质量','Quality'),('幻觉','Hallucination'),('护栏','Guardrail'),('缓存','Cache')],
    5: [('暂时','temporarily'),('关闭','disable'),('功能','Function'),('负责人','Responsible person'),('整改措施','Corrective action'),('决定','Decision'),('当前','current'),('预期','Expected'),('重现','Reproduce'),('替代方案','Alternative'),('交付','Delivery'),('行动项','Action item'),('截止日期','Deadline'),('安全审查','Security review'),('错误码','Error code'),('根本原因','Root Cause'),('测试数据','Test Data'),('技术债','Technical debt'),('敏感数据','Sensitive data'),('端到端','End-to-end')],
}

SET_LABELS = {
    1: "CBS · Core Banking System",
    2: "System & API",
    3: "Incident & Operations",
    4: "AI / LLM / Platform",
    5: "Testing / UAT / Deployment",
}

CATEGORY_ITEMS = [
    (1, "CBS"),
    (2, "System & API"),
    (3, "Incident & Ops"),
    (4, "AI / LLM"),
    (5, "Testing / UAT"),
]

QUOTES = [
    "Knowledge stays with you forever.",
    "Every small thing you study adds to your inner strength.",
    "No one can steal your skills or what is in your mind.",
    "Every expert was once a beginner.",
    "Keep learning, keep growing.",
]

def blank_progress():
    return {
        "correct": 0,
        "attempts": 0,
        "order": [],
        "position": 0,
        "question_id": None,
        "options": [],
        "done": False,
    }

if "selected_set" not in st.session_state:
    st.session_state.selected_set = 1
if "quote_of_the_day" not in st.session_state:
    st.session_state.quote_of_the_day = random.choice(QUOTES)
if "progress_by_set" not in st.session_state:
    st.session_state.progress_by_set = {i: blank_progress() for i in VOCAB_SETS}

def get_progress():
    return st.session_state.progress_by_set[st.session_state.selected_set]

def make_options(vocab, qid):
    correct = vocab[qid][1]
    pool = list({meaning for _, meaning in vocab if meaning != correct})
    wrong = random.sample(pool, min(2, len(pool)))
    options = [correct, *wrong]
    random.shuffle(options)
    return options

def prepare_question(progress, vocab):
    if not progress["order"]:
        progress["order"] = list(range(len(vocab)))
        random.shuffle(progress["order"])
    if progress["position"] >= len(progress["order"]):
        progress["done"] = True
        progress["question_id"] = None
        progress["options"] = []
        return
    qid = progress["order"][progress["position"]]
    progress["question_id"] = qid
    progress["options"] = make_options(vocab, qid)

def chinese_html(word):
    safe = html.escape(word)
    css_class = "chinese-short" if len(word) <= 4 else "chinese-medium" if len(word) <= 6 else "chinese-long"
    return f'<div class="{css_class}">{safe}</div>'

selected_set = st.session_state.selected_set
vocab = VOCAB_SETS[selected_set]
progress = get_progress()
if progress["question_id"] is None and not progress["done"]:
    prepare_question(progress, vocab)

st.markdown('<div class="main-title">Chinese Learning App</div>', unsafe_allow_html=True)
st.markdown('<div class="by-line">by pollyleadsforward</div>', unsafe_allow_html=True)
st.markdown(f'<div class="active-category">📚 {SET_LABELS[selected_set]}</div>', unsafe_allow_html=True)

percentage = round(progress["correct"] / progress["attempts"] * 100) if progress["attempts"] else 0
st.markdown(
    f'''<div class="score-grid">
    <div class="score-card score-purple"><div class="score-label">✅ Correct</div><div class="score-number">{progress["correct"]}</div></div>
    <div class="score-card score-pink"><div class="score-label">📝 Answered</div><div class="score-number">{progress["attempts"]}</div></div>
    <div class="score-card score-green"><div class="score-label">🎯 Score</div><div class="score-number">{percentage}%</div></div>
    </div>''',
    unsafe_allow_html=True,
)

if not progress["done"]:
    qid = progress["question_id"]
    chinese_word, correct_answer = vocab[qid]
    st.markdown(
        f'<div class="question-shell"><div class="question-center"><div class="question-label">คำนี้แปลว่าอะไร?</div>{chinese_html(chinese_word)}</div></div>',
        unsafe_allow_html=True,
    )
    with st.container(key="answer_area"):
        for i, option in enumerate(progress["options"]):
            if st.button(option, use_container_width=True, key=f"answer_{selected_set}_{qid}_{progress['attempts']}_{i}"):
                progress["attempts"] += 1
                if option == correct_answer:
                    progress["correct"] += 1
                else:
                    st.error(f"❌ คำตอบที่ถูกคือ\n\n### {chinese_word} = {correct_answer}")
                    time.sleep(1.0)
                progress["position"] += 1
                progress["question_id"] = None
                progress["options"] = []
                prepare_question(progress, vocab)
                st.rerun()
else:
    st.success("✅ จบการทบทวนคำศัพท์ชุดนี้แล้ว")

st.markdown('<div class="bottom-category-title">เลือกหมวดคำศัพท์</div>', unsafe_allow_html=True)
current_item = next(item for item in CATEGORY_ITEMS if item[0] == st.session_state.selected_set)
other_items = [item for item in CATEGORY_ITEMS if item[0] != st.session_state.selected_set]
display_items = other_items[:2] + [current_item] + other_items[2:]

with st.container(key="category_selector"):
    cols = st.columns([1.2, 1.3, .7, .85, 1.18], gap="small")
    for index, (set_id, label) in enumerate(display_items):
        is_selected = set_id == st.session_state.selected_set
        with cols[index]:
            if st.button(
                label,
                key=f"category_{set_id}_{st.session_state.selected_set}",
                type="primary" if is_selected else "secondary",
                use_container_width=True,
            ):
                if not is_selected:
                    st.session_state.selected_set = set_id
                    st.rerun()

with st.container(key="bottom_actions"):
    safe_quote = html.escape(st.session_state.quote_of_the_day)
    st.markdown(f'<div class="quote-text">“{safe_quote}”</div>', unsafe_allow_html=True)
    reset_col, _ = st.columns([.65, 5.35], gap="large", vertical_alignment="center")
    with reset_col:
        if st.button("↻", key=f"reset_set_{selected_set}", help="เริ่มหมวดนี้ใหม่"):
            st.session_state.progress_by_set[selected_set] = blank_progress()
            st.rerun()
