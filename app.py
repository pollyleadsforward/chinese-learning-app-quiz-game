import streamlit as st
import random
import time
import os

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
# FIND DECORATION IMAGES
# =========================================================

def find_image(names):
    for name in names:
        if os.path.exists(name):
            return name
    return None


left_image = find_image([
    "bunny_left.png",
    "bunny_left.jpg",
    "bunny_left.jpeg"
])

right_image = find_image([
    "bunny_right.png",
    "bunny_right.jpg",
    "bunny_right.jpeg"
])

# =========================================================
# STYLE
# =========================================================

st.markdown(
    """
<style>

.block-container {
    max-width: 820px;
    padding-top: 2.8rem !important;
    padding-bottom: 2rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* =========================
   TITLE
========================= */

.main-title {
    width: 100%;
    box-sizing: border-box;
    text-align: center;

    font-size: clamp(30px, 6vw, 48px);
    font-weight: 900;
    line-height: 1.25;

    padding: 12px 8px 4px 8px;
    margin: 0;

    overflow: visible;

    background: linear-gradient(
        90deg,
        #f4a7c5,
        #e1b5f5,
        #bfc4ff,
        #a9d9ff,
        #a9ead8,
        #c9efb7,
        #ffd2a6,
        #f7b4ca
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.by-line {
    text-align: center;
    color: #697386;

    font-size: clamp(16px, 3vw, 21px);
    font-weight: 700;

    margin-top: 3px;
}

.badge-wrap {
    text-align: center;

    margin-top: 12px;
    margin-bottom: 20px;
}

.polly-badge {
    display: inline-block;

    padding: 8px 16px;
    border-radius: 999px;

    background: linear-gradient(
        90deg,
        #ffd9e8,
        #eadfff,
        #dcedff,
        #dcf7e6
    );

    color: #5d6170;

    font-size: 14px;
    font-weight: 800;
}

/* =========================
   SCORE
========================= */

.score-grid {
    width: 100%;

    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));

    gap: 12px;

    margin: 0 0 24px 0;
}

.score-card {
    min-width: 0;
    min-height: 126px;

    border-radius: 22px;

    display: flex;
    flex-direction: column;

    align-items: center;
    justify-content: center;

    padding: 10px 5px;

    box-sizing: border-box;

    box-shadow:
        0 5px 16px
        rgba(70, 60, 95, 0.06);
}

.score-purple {
    background: #ead8fb;
    border: 2px solid #d7b1fa;
}

.score-pink {
    background: #ffdbe7;
    border: 2px solid #f6b1cb;
}

.score-green {
    background: #dcf5e4;
    border: 2px solid #98dfad;
}

.score-label {
    text-align: center;

    color: #4e5260;

    font-size: clamp(13px, 2.4vw, 18px);
    font-weight: 800;

    margin-bottom: 5px;

    white-space: nowrap;
}

.score-number {
    text-align: center;

    color: #2d2f3b;

    font-size: clamp(31px, 6vw, 46px);
    font-weight: 900;

    line-height: 1.05;
}

/* =========================
   QUESTION
========================= */

.question-label {
    text-align: center;

    color: #4d5260;

    font-size: clamp(20px, 4vw, 27px);
    font-weight: 800;

    margin-top: 6px;
    margin-bottom: 8px;
}

.review-label {
    text-align: center;

    color: #9161b5;

    font-size: clamp(15px, 3vw, 19px);
    font-weight: 800;

    margin-top: 6px;
    margin-bottom: 8px;
}

.quiz-word {
    text-align: center;

    color: #292b38;

    font-size: clamp(58px, 14vw, 105px);
    font-weight: 900;

    line-height: 1.1;

    padding:
        4px
        2px
        12px
        2px;

    word-break: break-word;
}

/* =========================
   DECORATION
========================= */

.decor-fallback {
    min-height: 120px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 20px;

    background: #fffafb;

    border: 1px solid #f2dfe8;

    font-size: 48px;
}

/* =========================
   ANSWER BUTTONS
========================= */

div[data-testid="stButton"] > button {
    width: 100% !important;

    min-height: 76px !important;

    border-radius: 20px !important;

    border:
        1.5px solid
        #e1dce8 !important;

    background:
        linear-gradient(
            90deg,
            #fffefe,
            #fffafd
        ) !important;

    margin-bottom: 10px !important;

    box-shadow:
        0 3px 10px
        rgba(40, 35, 55, 0.03) !important;
}

/* ตัวหนังสือ Choice */
div[data-testid="stButton"] > button * {
    font-size:
        clamp(
            21px,
            4vw,
            27px
        ) !important;

    font-weight:
        700 !important;

    color:
        #3f4250 !important;

    line-height:
        1.35 !important;
}

div[data-testid="stButton"] > button:hover {
    border-color:
        #d9b4ea !important;

    background:
        linear-gradient(
            90deg,
            #fff4fa,
            #f8f2ff,
            #f1fbff
        ) !important;
}

/* =========================
   REVIEW STATUS
========================= */

.review-status {
    text-align: center;

    color: #8d8498;

    font-size: 15px;

    margin-top: 8px;
}

/* =========================
   FOOTER
========================= */

.footer {
    text-align: center;

    color: #a39bad;

    font-size: 14px;

    margin-top: 14px;
}

footer {
    visibility: hidden;
}

/* =========================
   MOBILE
========================= */

@media (max-width: 600px) {

    .block-container {
        padding-top:
            2rem !important;

        padding-left:
            0.65rem !important;

        padding-right:
            0.65rem !important;
    }

    .main-title {
        font-size:
            clamp(
                28px,
                8.5vw,
                36px
            );

        padding-top: 10px;
    }

    .score-grid {
        gap: 7px;

        margin-bottom: 18px;
    }

    .score-card {
        min-height: 98px;

        border-radius: 17px;

        padding: 7px 2px;
    }

    .score-label {
        font-size:
            clamp(
                10px,
                3vw,
                13px
            );
    }

    .score-number {
        font-size:
            clamp(
                26px,
                8vw,
                34px
            );
    }

    .quiz-word {
        font-size:
            clamp(
                52px,
                17vw,
                82px
            );
    }

    div[data-testid="stButton"] > button {
        min-height:
            74px !important;

        border-radius:
            18px !important;
    }

    div[data-testid="stButton"] > button * {

        font-size:
            clamp(
                20px,
                5.2vw,
                24px
            ) !important;
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

        if (
            item["vocab_id"] == vocab_id
            and
            item["stage"] == stage
        ):
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

    # -----------------------------------------
    # CHECK WHETHER A REVIEW WORD IS DUE
    # -----------------------------------------

    due_items = [

        item

        for item
        in st.session_state.retry_queue

        if item["due_at"] <= current_total
    ]

    if due_items:

        due_items.sort(
            key=lambda item:
            item["due_at"]
        )

        retry_item = due_items[0]

        question_id = retry_item["vocab_id"]

        stage = retry_item["stage"]

        st.session_state.retry_queue.remove(
            retry_item
        )

    else:

        # -------------------------------------
        # DON'T SHOW RETRY WORD EARLY
        # -------------------------------------

        blocked_ids = {

            item["vocab_id"]

            for item
            in st.session_state.retry_queue
        }

        candidates = [

            i

            for i
            in range(len(vocab))

            if i not in blocked_ids
        ]

        # Don't show same word twice in a row
        if (
            st.session_state.last_question_id
            in candidates

            and

            len(candidates) > 1
        ):

            candidates.remove(
                st.session_state.last_question_id
            )

        if not candidates:

            candidates = list(
                range(len(vocab))
            )

        question_id = random.choice(
            candidates
        )

        stage = 0

    # -----------------------------------------
    # CREATE 3 CHOICES
    # -----------------------------------------

    correct_answer = vocab[question_id][1]

    wrong_pool = list({

        meaning

        for _, meaning
        in vocab

        if meaning != correct_answer
    })

    wrong_answers = random.sample(
        wrong_pool,
        2
    )

    options = [

        correct_answer,

        wrong_answers[0],

        wrong_answers[1]
    ]

    random.shuffle(options)

    st.session_state.question_id = (
        question_id
    )

    st.session_state.question_stage = (
        stage
    )

    st.session_state.options = (
        options
    )

    st.session_state.last_question_id = (
        question_id
    )

# =========================================================
# INITIAL QUESTION
# =========================================================

if st.session_state.question_id is None:

    new_question()

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">'
    'Chinese Learning App'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="by-line">'
    'by pollyleadsforward'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="badge-wrap">'
    '<span class="polly-badge">'
    '🌸 pollyleadsforward'
    '</span>'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# SCORE
# =========================================================

if st.session_state.total > 0:

    percentage = round(

        st.session_state.score

        /

        st.session_state.total

        *

        100
    )

else:

    percentage = 0

# Keep this HTML as ONE string
# to prevent Streamlit from showing <div> as text.

score_html = (

    f'<div class="score-grid">'

    f'<div class="score-card score-purple">'
    f'<div class="score-label">'
    f'✅ Correct'
    f'</div>'
    f'<div class="score-number">'
    f'{st.session_state.score}'
    f'</div>'
    f'</div>'

    f'<div class="score-card score-pink">'
    f'<div class="score-label">'
    f'📝 Answered'
    f'</div>'
    f'<div class="score-number">'
    f'{st.session_state.total}'
    f'</div>'
    f'</div>'

    f'<div class="score-card score-green">'
    f'<div class="score-label">'
    f'🎯 Score'
    f'</div>'
    f'<div class="score-number">'
    f'{percentage}%'
    f'</div>'
    f'</div>'

    f'</div>'
)

st.markdown(
    score_html,
    unsafe_allow_html=True
)

# =========================================================
# CURRENT QUESTION
# =========================================================

question_id = (
    st.session_state.question_id
)

stage = (
    st.session_state.question_stage
)

chinese_word = (
    vocab[question_id][0]
)

correct_answer = (
    vocab[question_id][1]
)

# =========================================================
# QUESTION + RABBITS
# =========================================================

left_col, middle_col, right_col = st.columns(
    [1.1, 2.2, 1.1]
)

with left_col:

    if left_image:

        st.image(
            left_image,
            use_container_width=True
        )

    else:

        st.markdown(
            '<div class="decor-fallback">'
            '🌸🐰'
            '</div>',
            unsafe_allow_html=True
        )

with middle_col:

    if stage == 1:

        st.markdown(
            '<div class="review-label">'
            '🧠 Review 1'
            '<br>'
            'คำที่ตอบผิดกลับมาแล้ว'
            '</div>',
            unsafe_allow_html=True
        )

    elif stage == 2:

        st.markdown(
            '<div class="review-label">'
            '🌷 Review 2'
            '<br>'
            'ทบทวนอีกครั้ง'
            '</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<div class="question-label">'
            'คำนี้แปลว่าอะไร?'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        f'<div class="quiz-word">'
        f'{chinese_word}'
        f'</div>',
        unsafe_allow_html=True
    )

with right_col:

    if right_image:

        st.image(
            right_image,
            use_container_width=True
        )

    else:

        st.markdown(
            '<div class="decor-fallback">'
            '🐰🌷'
            '</div>',
            unsafe_allow_html=True
        )

st.write("")

# =========================================================
# ANSWER BUTTONS
# =========================================================

letters = [
    "A",
    "B",
    "C"
]

for i, option in enumerate(
    st.session_state.options
):

    if st.button(

        f"{letters[i]}. {option}",

        use_container_width=True,

        key=(
            f"answer_"
            f"{question_id}_"
            f"{stage}_"
            f"{i}"
        )

    ):

        # Count this attempt
        st.session_state.total += 1

        is_correct = (
            option == correct_answer
        )

        # =================================================
        # CORRECT
        # =================================================

        if is_correct:

            st.session_state.score += 1

            # If this was Review 1,
            # ask again after another 10 answers.
            if stage == 1:

                schedule_retry(

                    vocab_id=question_id,

                    stage=2,

                    due_at=(
                        st.session_state.total
                        + 10
                    )
                )

            # Correct = immediately next question
            new_question()

            st.rerun()

        # =================================================
        # WRONG
        # =================================================

        else:

            # ---------------------------------------------
            # WRONG FIRST TIME
            # Return after 5 other answers
            # ---------------------------------------------

            if stage == 0:

                schedule_retry(

                    vocab_id=question_id,

                    stage=1,

                    due_at=(
                        st.session_state.total
                        + 5
                    )
                )

                st.error(

                    f"❌ คำตอบที่ถูกคือ\n\n"

                    f"### "
                    f"{chinese_word}"
                    f" = "
                    f"{correct_answer}"

                    f"\n\n"

                    f"🌸 คำนี้จะกลับมา"
                    f"หลังจากตอบคำอื่นอีก 5 คำ"
                )

            # ---------------------------------------------
            # WRONG ON REVIEW 1
            # Return after another 10 answers
            # ---------------------------------------------

            elif stage == 1:

                schedule_retry(

                    vocab_id=question_id,

                    stage=2,

                    due_at=(
                        st.session_state.total
                        + 10
                    )
                )

                st.error(

                    f"❌ คำตอบที่ถูกคือ\n\n"

                    f"### "
                    f"{chinese_word}"
                    f" = "
                    f"{correct_answer}"

                    f"\n\n"

                    f"🌷 คำนี้จะกลับมาอีก"
                    f"หลังจากตอบคำอื่นอีก 10 คำ"
                )

            # ---------------------------------------------
            # REVIEW 2
            # ---------------------------------------------

            else:

                st.error(

                    f"❌ คำตอบที่ถูกคือ\n\n"

                    f"### "
                    f"{chinese_word}"
                    f" = "
                    f"{correct_answer}"
                )

            # Give time to read the answer
            time.sleep(2)

            new_question()

            st.rerun()

# =========================================================
# WAITING FOR REVIEW
# =========================================================

if len(
    st.session_state.retry_queue
) > 0:

    st.markdown(

        f'<div class="review-status">'

        f'🌷 Waiting for review: '

        f'{len(st.session_state.retry_queue)}'

        f'</div>',

        unsafe_allow_html=True
    )

# =========================================================
# RESET
# =========================================================

st.divider()

if st.button(
    "↻ Reset",
    use_container_width=True
):

    st.session_state.score = 0

    st.session_state.total = 0

    st.session_state.question_id = None

    st.session_state.question_stage = 0

    st.session_state.options = []

    st.session_state.retry_queue = []

    st.session_state.last_question_id = None

    new_question()

    st.rerun()

# =========================================================
# FOOTER
# =========================================================

st.markdown(

    '<div class="footer">'
    '🌸 Made with love by '
    'pollyleadsforward 🌷'
    '</div>',

    unsafe_allow_html=True
)