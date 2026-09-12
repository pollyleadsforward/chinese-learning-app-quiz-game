import streamlit as st
import random
import time
import os
import html
import base64

# =========================================================
# APP ICON
# =========================================================

try:
    from PIL import Image
    app_icon = Image.open("app_icon.png")
except Exception:
    app_icon = "🐰"

# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="Chinese Learning App",
    page_icon=app_icon,
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# FIND IMAGE
# =========================================================

def find_image(names):
    for name in names:
        if os.path.exists(name):
            return name
    return None


left_image = find_image([
    "bunny_left.jpg",
    "bunny_left.jpeg",
    "bunny_left.png"
])

right_image = find_image([
    "bunny_right.jpg",
    "bunny_right.jpeg",
    "bunny_right.png",
    "bunny_right2.jpg",
    "bunny_right2.jpeg",
    "bunny_right2.png"
])

# ถ้ามีแค่รูปเดียว ให้ใช้รูปเดิมทั้งซ้ายและขวา
if left_image is None and right_image is not None:
    left_image = right_image

if right_image is None and left_image is not None:
    right_image = left_image

# =========================================================
# IMAGE -> BASE64
# =========================================================

def image_to_base64(path):
    if not path or not os.path.exists(path):
        return None

    ext = os.path.splitext(path)[1].lower()
    mime_map = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }
    mime_type = mime_map.get(ext, "image/png")

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


left_bunny_b64 = image_to_base64(left_image)
right_bunny_b64 = image_to_base64(right_image)

# =========================================================
# CSS
# =========================================================

st.markdown(
    """
<style>

/* ======================================
   PAGE
====================================== */

[data-testid="stAppViewContainer"] {
    background: #fffdfd;
}

.block-container {
    max-width: 560px !important;
    padding-top: 0.45rem !important;
    padding-bottom: 1.3rem !important;
    padding-left: 0.75rem !important;
    padding-right: 0.75rem !important;
}

header,
footer,
#MainMenu,
[data-testid="stToolbar"],
[data-testid="stStatusWidget"],
[data-testid="stDecoration"] {
    display: none !important;
    visibility: hidden !important;
}

/* ======================================
   TITLE
====================================== */

.main-title {
    text-align: center;
    font-size: clamp(27px, 7vw, 40px);
    font-weight: 900;
    line-height: 1.12;
    margin-top: 0;
    margin-bottom: 3px;

    background: linear-gradient(
        90deg,
        #f3a4c6,
        #deb5f5,
        #bfc5ff,
        #a9dbff,
        #a7ead8,
        #c9edb5,
        #ffd2a5,
        #f5b1c8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.by-line {
    text-align: center;
    color: #707583;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 7px;
}

.badge-wrap {
    text-align: center;
    margin-bottom: 11px;
}

.badge {
    display: inline-block;
    padding: 6px 13px;
    border-radius: 999px;
    background: linear-gradient(
        90deg,
        #ffdbe8,
        #eadfff,
        #dcecff,
        #ddf6e7
    );
    color: #5e6270;
    font-size: 12px;
    font-weight: 800;
}

/* ======================================
   SCORE CARDS
====================================== */

.score-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 7px;
    width: 100%;
    margin-bottom: 10px;
}

.score-card {
    min-width: 0;
    min-height: 74px;
    padding: 7px 3px;
    box-sizing: border-box;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 0 3px 9px rgba(50, 45, 65, 0.04);
}

.score-purple {
    background: #edddfb;
    border: 1.5px solid #d7b3f6;
}

.score-pink {
    background: #ffdee9;
    border: 1.5px solid #f4b4cc;
}

.score-green {
    background: #ddf4e4;
    border: 1.5px solid #9cddae;
}

.score-label {
    color: #515563;
    font-size: 10px;
    font-weight: 800;
    white-space: nowrap;
    margin-bottom: 3px;
}

.score-number {
    color: #2e303b;
    font-size: 23px;
    line-height: 1;
    font-weight: 900;
}

/* ======================================
   QUESTION SHELL
====================================== */

.question-shell {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-top: 4px;
    margin-bottom: 8px;
}

.question-bunny {
    width: 72px;
    flex: 0 0 72px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.question-bunny img {
    width: 72px;
    height: auto;
    display: block;
}

.question-bunny-fallback {
    font-size: 28px;
    line-height: 1;
}

.question-center {
    flex: 1 1 auto;
    text-align: center;
    min-width: 0;
}

.question-label {
    text-align: center;
    color: #707583;
    font-size: 16px;
    font-weight: 700;
    margin-top: 0;
    margin-bottom: 4px;
}

.review-label {
    text-align: center;
    color: #8c62b0;
    font-size: 13px;
    font-weight: 800;
    margin-top: 0;
    margin-bottom: 4px;
}

/* ======================================
   CHINESE WORD
====================================== */

.chinese-short,
.chinese-four,
.chinese-long {
    font-weight: 900;
    line-height: 1.03;
    text-align: center;
    display: inline-block;

    background: linear-gradient(
        90deg,
        #f3a4c6,
        #deb5f5,
        #bfc5ff,
        #a9dbff,
        #a7ead8,
        #c9edb5,
        #ffd2a5,
        #f5b1c8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.chinese-short {
    font-size: clamp(58px, 16vw, 82px);
}

.chinese-four {
    font-size: clamp(50px, 14vw, 70px);
}

.chinese-long {
    font-size: clamp(32px, 9vw, 52px);
    white-space: nowrap;
    max-width: 100%;
    overflow: hidden;
}

/* ======================================
   ANSWER BUTTONS
====================================== */

div[data-testid="stButton"] > button {
    width: 100% !important;
    min-height: 62px !important;
    border-radius: 17px !important;
    border: 1.4px solid #e4dfe8 !important;
    background: linear-gradient(90deg, #fffefe, #fffafd) !important;
    margin-bottom: 6px !important;
    box-shadow: 0 2px 7px rgba(45, 40, 60, 0.025) !important;
}

div[data-testid="stButton"] > button p {
    color: #4b5160 !important;
    font-size: 18px !important;
    font-weight: 800 !important;
    line-height: 1.25 !important;
}

div[data-testid="stButton"] > button:hover {
    border-color: #d7b5e8 !important;
    background: linear-gradient(
        90deg,
        #fff4fa,
        #faf5ff,
        #f3fbff
    ) !important;
}

/* ======================================
   SMALL TEXT
====================================== */

.small-note {
    text-align: center;
    color: #958d9e;
    font-size: 11px;
    margin-top: 3px;
    margin-bottom: 3px;
}

/* ======================================
   DIVIDER
====================================== */

hr {
    margin-top: 10px !important;
    margin-bottom: 10px !important;
}

/* ======================================
   MOBILE
====================================== */

@media (max-width: 480px) {

    .block-container {
        padding-top: 0.3rem !important;
        padding-left: 0.55rem !important;
        padding-right: 0.55rem !important;
    }

    .main-title {
        font-size: clamp(25px, 7.1vw, 30px);
    }

    .score-card {
        min-height: 68px;
    }

    .score-label {
        font-size: 9.5px;
    }

    .score-number {
        font-size: 21px;
    }

    .question-shell {
        gap: 8px;
        margin-top: 3px;
        margin-bottom: 6px;
    }

    .question-bunny {
        width: 62px;
        flex: 0 0 62px;
    }

    .question-bunny img {
        width: 62px;
    }

    .question-label {
        font-size: 15px;
    }

    .review-label {
        font-size: 13px;
    }

    .chinese-short {
        font-size: clamp(54px, 16.5vw, 72px);
    }

    .chinese-four {
        font-size: clamp(46px, 13vw, 60px);
    }

    .chinese-long {
        font-size: clamp(28px, 8.2vw, 40px);
    }

    div[data-testid="stButton"] > button {
        min-height: 60px !important;
        border-radius: 16px !important;
    }

    div[data-testid="stButton"] > button p {
        font-size: 17px !important;
    }
}

</style>
""",
    unsafe_allow_html=True
)

# =========================================================
# VOCABULARY — 100 WORDS
# =========================================================

vocab = [
    ("系统", "System"),
    ("做系统", "Build System"),
    ("开发", "Development"),
    ("开发人员", "Developer"),
    ("需求", "Requirement"),
    ("请求", "Request"),
    ("调用接口", "Call API"),
    ("参数", "Parameter"),
    ("响应", "Response"),
    ("测试", "Testing"),

    ("测试系统", "Test System"),
    ("系统测试", "System Testing"),
    ("测试用例", "Test Case"),
    ("验收测试", "UAT / Acceptance Testing"),
    ("签字确认", "Sign-off"),
    ("确认", "Confirm"),
    ("流程", "Process"),
    ("人工流程", "Manual Process"),
    ("人工审核", "Manual Review"),
    ("自动", "Automatic"),

    ("自动化流程", "Automation Process"),
    ("上线", "Go Live"),
    ("系统事故", "System Incident"),
    ("解决问题", "Fix / Solve Problem"),
    ("异常", "Exception"),
    ("错误", "Error"),
    ("日志", "Log"),
    ("数据", "Data"),
    ("数据库", "Database"),
    ("数据源", "Data Source"),

    ("字段", "Field"),
    ("为空", "Empty / Blank"),
    ("空值", "Null / Empty Value"),
    ("数据验证", "Data Validation"),
    ("数据缺失", "Missing Data"),
    ("数据错误", "Incorrect / Wrong Data"),
    ("数据流", "Data Flow"),
    ("业务部门", "Business Division"),
    ("项目", "Project"),
    ("范围", "Scope"),

    ("需要", "Need / A Must"),
    ("先", "Before / First"),
    ("产品", "Product"),
    ("目标", "Goal"),
    ("前端", "Frontend"),
    ("后端", "Backend"),
    ("显示", "Display"),
    ("不正确", "Incorrect"),
    ("返回", "Return"),
    ("发生", "Occur"),

    ("层", "Layer"),
    ("用户", "User"),
    ("点击", "Click"),
    ("按钮", "Button"),
    ("传递", "Pass / ส่งค่า"),
    ("哪些", "Which / อะไรบ้าง"),
    ("使用", "Use"),
    ("令牌", "Token"),
    ("错误码", "Error Code"),
    ("时", "When / ตอนที่"),

    ("解释", "Explain"),
    ("架构", "Architecture"),
    ("传到", "Flow To / A → B"),
    ("连接", "Connect"),
    ("步骤", "Step"),
    ("同步", "Synchronous"),
    ("异步", "Asynchronous"),
    ("不可用", "Unavailable"),
    ("备用", "Backup / Fallback"),
    ("方案", "Solution"),

    ("备用方案", "Contingency Plan"),
    ("环境", "Environment"),
    ("版本", "Version"),
    ("流水线", "Pipeline"),
    ("失败", "Fail"),
    ("成功", "Success"),
    ("回滚", "Rollback"),
    ("出现", "Appear / Occur"),
    ("进行", "Proceed / ดำเนินการ"),
    ("发布", "Release"),

    ("金丝雀", "Canary"),
    ("提供", "Provide"),
    ("根本", "Root"),
    ("原因", "Cause"),
    ("根本原因", "Root Cause"),
    ("影响", "Impact"),
    ("明确", "Clear / ชัดเจน"),
    ("增加", "Increase"),
    ("复盘", "Postmortem"),
    ("主要", "Main"),

    ("衡量", "Measure"),
    ("而", "But / แต่"),
    ("不仅仅", "Not Only / ไม่เพียงแค่"),
    ("产出", "Output"),
    ("风险", "Risk"),
    ("最大", "Biggest / Maximum"),
    ("假设", "Assumption"),
    ("怎么", "How"),
    ("验证", "Validate"),
    ("标准", "Standard"),
]

# =========================================================
# SESSION STATE
# =========================================================

if "score" not in st.session_state:
    st.session_state.score = 0

if "total" not in st.session_state:
    st.session_state.total = 0

if "question_id" not in st.session_state:
    st.session_state.question_id = None

if "question_stage" not in st.session_state:
    st.session_state.question_stage = 0

if "options" not in st.session_state:
    st.session_state.options = []

if "retry_queue" not in st.session_state:
    st.session_state.retry_queue = []

if "last_question_id" not in st.session_state:
    st.session_state.last_question_id = None

# =========================================================
# RETRY LOGIC
# =========================================================

def schedule_retry(vocab_id, stage, due_at):
    for item in st.session_state.retry_queue:
        if item["vocab_id"] == vocab_id and item["stage"] == stage:
            return

    st.session_state.retry_queue.append({
        "vocab_id": vocab_id,
        "stage": stage,
        "due_at": due_at
    })

# =========================================================
# CREATE NEW QUESTION
# =========================================================

def new_question():
    current_total = st.session_state.total

    due_items = [
        item
        for item in st.session_state.retry_queue
        if item["due_at"] <= current_total
    ]

    if due_items:
        due_items.sort(key=lambda item: item["due_at"])
        retry_item = due_items[0]

        question_id = retry_item["vocab_id"]
        stage = retry_item["stage"]

        st.session_state.retry_queue.remove(retry_item)

    else:
        blocked_ids = {
            item["vocab_id"]
            for item in st.session_state.retry_queue
        }

        candidates = [
            i
            for i in range(len(vocab))
            if i not in blocked_ids
        ]

        if (
            st.session_state.last_question_id in candidates
            and len(candidates) > 1
        ):
            candidates.remove(st.session_state.last_question_id)

        if not candidates:
            candidates = list(range(len(vocab)))

        question_id = random.choice(candidates)
        stage = 0

    correct_answer = vocab[question_id][1]

    wrong_pool = list({
        meaning
        for _, meaning in vocab
        if meaning != correct_answer
    })

    wrong_answers = random.sample(wrong_pool, 2)
    options = [correct_answer, wrong_answers[0], wrong_answers[1]]
    random.shuffle(options)

    st.session_state.question_id = question_id
    st.session_state.question_stage = stage
    st.session_state.options = options
    st.session_state.last_question_id = question_id

# =========================================================
# FORMAT CHINESE
# =========================================================

def chinese_html(word):
    safe_word = html.escape(word)
    length = len(word)

    if length <= 3:
        return f'<div class="chinese-short">{safe_word}</div>'

    elif length == 4:
        first_line = html.escape(word[:2])
        second_line = html.escape(word[2:])
        return f'<div class="chinese-four">{first_line}<br>{second_line}</div>'

    else:
        return f'<div class="chinese-long">{safe_word}</div>'

# =========================================================
# RENDER QUESTION AREA
# =========================================================

def render_question_area(label_html, chinese_word_html):
    if left_bunny_b64:
        left_html = f'<img src="{left_bunny_b64}" alt="left bunny">'
    else:
        left_html = '<div class="question-bunny-fallback">🐰</div>'

    if right_bunny_b64:
        right_html = f'<img src="{right_bunny_b64}" alt="right bunny">'
    else:
        right_html = '<div class="question-bunny-fallback">🐰</div>'

    question_html = f"""
    <div class="question-shell">
        <div class="question-bunny">{left_html}</div>
        <div class="question-center">
            {label_html}
            {chinese_word_html}
        </div>
        <div class="question-bunny">{right_html}</div>
    </div>
    """
    st.markdown(question_html, unsafe_allow_html=True)

# =========================================================
# INITIAL QUESTION
# =========================================================

if st.session_state.question_id is None:
    new_question()

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">Chinese Learning App</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="by-line">by pollyleadsforward</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="badge-wrap"><span class="badge">🌸 pollyleadsforward</span></div>',
    unsafe_allow_html=True
)

# =========================================================
# SCORE
# =========================================================

if st.session_state.total > 0:
    percentage = round((st.session_state.score / st.session_state.total) * 100)
else:
    percentage = 0

score_html = (
    f'<div class="score-grid">'
    f'<div class="score-card score-purple">'
    f'<div class="score-label">✅ Correct</div>'
    f'<div class="score-number">{st.session_state.score}</div>'
    f'</div>'
    f'<div class="score-card score-pink">'
    f'<div class="score-label">📝 Answered</div>'
    f'<div class="score-number">{st.session_state.total}</div>'
    f'</div>'
    f'<div class="score-card score-green">'
    f'<div class="score-label">🎯 Score</div>'
    f'<div class="score-number">{percentage}%</div>'
    f'</div>'
    f'</div>'
)

st.markdown(score_html, unsafe_allow_html=True)

# =========================================================
# CURRENT QUESTION
# =========================================================

question_id = st.session_state.question_id
stage = st.session_state.question_stage
chinese_word = vocab[question_id][0]
correct_answer = vocab[question_id][1]

if stage == 1:
    label_html = '<div class="review-label">🧠 Review 1 • คำที่ตอบผิดกลับมาแล้ว</div>'
elif stage == 2:
    label_html = '<div class="review-label">🌷 Review 2 • ทบทวนอีกครั้ง</div>'
else:
    label_html = '<div class="question-label">คำนี้แปลว่าอะไร?</div>'

render_question_area(
    label_html=label_html,
    chinese_word_html=chinese_html(chinese_word)
)

# =========================================================
# ANSWERS
# =========================================================

letters = ["A", "B", "C"]

for i, option in enumerate(st.session_state.options):
    if st.button(
        f"{letters[i]}. {option}",
        use_container_width=True,
        key=f"answer_{question_id}_{stage}_{i}"
    ):
        st.session_state.total += 1
        is_correct = (option == correct_answer)

        if is_correct:
            st.session_state.score += 1

            if stage == 1:
                schedule_retry(
                    vocab_id=question_id,
                    stage=2,
                    due_at=st.session_state.total + 10
                )

            new_question()
            st.rerun()

        else:
            if stage == 0:
                schedule_retry(
                    vocab_id=question_id,
                    stage=1,
                    due_at=st.session_state.total + 5
                )

                st.error(
                    f"❌ คำตอบที่ถูกคือ\n\n"
                    f"### {chinese_word} = {correct_answer}\n\n"
                    f"🌸 จะถามคำนี้ใหม่หลังคำอื่นอีก 5 คำ"
                )

            elif stage == 1:
                schedule_retry(
                    vocab_id=question_id,
                    stage=2,
                    due_at=st.session_state.total + 10
                )

                st.error(
                    f"❌ คำตอบที่ถูกคือ\n\n"
                    f"### {chinese_word} = {correct_answer}\n\n"
                    f"🌷 จะถามคำนี้ใหม่หลังคำอื่นอีก 10 คำ"
                )

            else:
                st.error(
                    f"❌ คำตอบที่ถูกคือ\n\n"
                    f"### {chinese_word} = {correct_answer}"
                )

            time.sleep(1.5)
            new_question()
            st.rerun()

# =========================================================
# REVIEW STATUS
# =========================================================

if len(st.session_state.retry_queue) > 0:
    st.markdown(
        f'<div class="small-note">🌷 Waiting for review: {len(st.session_state.retry_queue)}</div>',
        unsafe_allow_html=True
    )

# =========================================================
# RESET
# =========================================================

st.divider()

if st.button("↻ Reset", use_container_width=True):
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.question_id = None
    st.session_state.question_stage = 0
    st.session_state.options = []
    st.session_state.retry_queue = []
    st.session_state.last_question_id = None
    new_question()
    st.rerun()

st.markdown(
    '<div class="small-note">🌸 Made by pollyleadsforward</div>',
    unsafe_allow_html=True
)
