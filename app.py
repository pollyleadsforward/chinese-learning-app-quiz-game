import streamlit as st
import random
import html

# =========================================================
# APP ICON
# =========================================================

try:
    from PIL import Image
    app_icon = Image.open("app_icon.png")
except Exception:
    app_icon = "🇨🇳"

st.set_page_config(
    page_title="Chinese Learning App",
    page_icon=app_icon,
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>
/* =======================================================
   FINAL APPROVED MOBILE UI — Samsung S23 Ultra reference
   ======================================================= */

html {
    color-scheme: light !important;
}

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: #fffdfd !important;
}

.block-container {
    max-width: 800px !important;
    padding-top: 0.65rem !important;
    padding-bottom: 0.85rem !important;
    padding-left: 1.05rem !important;
    padding-right: 1.05rem !important;
}

/* Hide Streamlit's internal page chrome */
header, footer, #MainMenu,
[data-testid="stToolbar"],
[data-testid="stStatusWidget"],
[data-testid="stDecoration"],
[data-testid="stAppDeployButton"],
.stDeployButton {
    display: none !important;
    visibility: hidden !important;
}

/* =======================================================
   HEADER
   ======================================================= */

.main-title {
    text-align: center;
    font-size: clamp(36px, 5.2vw, 50px);
    font-weight: 900;
    line-height: 1.02;
    margin: 0 0 4px 0;
    white-space: nowrap;
    letter-spacing: -0.45px;

    background: linear-gradient(
        90deg,
        #efa6d5,
        #d2b3fa,
        #acc4ff,
        #8fddff,
        #90e8d3,
        #beeaa9,
        #efd79b,
        #f3b7b8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Rainbow byline, deliberately smaller than line 3 */
.by-line {
    text-align: center;
    font-size: 12px;
    font-weight: 800;
    line-height: 1.15;
    margin: 0 0 11px 0;

    background: linear-gradient(
        90deg,
        #d7b0f7,
        #9ec9ff,
        #8ddfd7,
        #b9e89e,
        #f2c8a2,
        #eea6c8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.active-category {
    text-align: center;
    color: #727784;
    font-size: 15.5px;
    font-weight: 800;
    line-height: 1.2;
    margin: 0 0 13px 0;
}

/* =======================================================
   SCORE
   ======================================================= */

.score-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 10px;
    width: 100%;
    margin: 0 0 30px 0;
}

.score-card {
    min-width: 0;
    min-height: 72px;
    padding: 8px 5px;
    box-sizing: border-box;
    border-radius: 18px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    box-shadow: 0 2px 8px rgba(50,45,65,0.03);
}

.score-purple {
    background: #edddfb;
    border: 1.4px solid #d7b3f6;
}

.score-pink {
    background: #ffdee9;
    border: 1.4px solid #f4b4cc;
}

.score-green {
    background: #ddf4e4;
    border: 1.4px solid #9cddae;
}

.score-label {
    color: #727784;
    font-size: 11px;
    font-weight: 800;
    white-space: nowrap;
    margin-bottom: 4px;
}

.score-number {
    color: #565b67;
    font-size: 27px;
    line-height: 1;
    font-weight: 900;
}

/* =======================================================
   QUESTION
   ======================================================= */

.question-shell {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 0 9px 0;
}

.question-center {
    width: 100%;
    min-width: 0;
    text-align: center;
}

.question-label,
.review-label {
    text-align: center;
    color: #727784;
    font-size: 17px;
    font-weight: 800;
    line-height: 1.2;
    margin: 0 0 15px 0;
}

.review-label {
    color: #8c7b91;
}

/* =======================================================
   CHINESE WORD — approximately +20% vs previous approved mockup
   ======================================================= */

.chinese-short,
.chinese-medium,
.chinese-long {
    font-weight: 900;
    line-height: 1.00;
    text-align: center;
    display: inline-block;
    white-space: nowrap;
    max-width: 100%;
    margin: 0;

    background: linear-gradient(
        90deg,
        #efa6d5,
        #d2b3fa,
        #acc4ff,
        #8fddff,
        #90e8d3,
        #beeaa9,
        #efd79b,
        #f3b7b8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.chinese-short {
    font-size: clamp(72px, 11vw, 102px);
}

.chinese-medium {
    font-size: clamp(49px, 8vw, 70px);
}

.chinese-long {
    font-size: clamp(34px, 5.6vw, 50px);
}

/* =======================================================
   ANSWER BUTTONS
   ======================================================= */

.st-key-answer_area div[data-testid="stVerticalBlock"] {
    gap: 0.42rem !important;
}

.st-key-answer_area div[data-testid="stButton"] > button,
.st-key-answer_area div[data-testid="stButton"] > button:hover,
.st-key-answer_area div[data-testid="stButton"] > button:focus,
.st-key-answer_area div[data-testid="stButton"] > button:active {
    width: 100% !important;
    min-height: 49px !important;
    padding: 0.48rem 0.72rem !important;

    border-radius: 15px !important;
    background: #ffffff !important;
    background-color: #ffffff !important;
    color: #4d5260 !important;

    border: 1px solid #dedfe5 !important;
    box-shadow: none !important;
    outline: none !important;
}

.st-key-answer_area div[data-testid="stButton"] > button p,
.st-key-answer_area div[data-testid="stButton"] > button span {
    color: #4d5260 !important;
    -webkit-text-fill-color: #4d5260 !important;
    font-size: 16px !important;
    font-weight: 500 !important;
}

/* =======================================================
   CATEGORY SELECTOR — EXACT REFERENCE STYLE
   ======================================================= */

.bottom-category-title {
    text-align: center;
    color: #727784;
    font-size: 12px;
    font-weight: 800;
    margin: 15px 0 6px 0;
}

.st-key-category_selector {
    width: 100% !important;
    max-width: 100% !important;
    overflow: visible !important;
}

.st-key-category_selector [data-testid="stHorizontalBlock"] {
    display: grid !important;

    /* proportions matched to reference image */
    grid-template-columns:
        minmax(0, 1.25fr)
        minmax(0, 1.32fr)
        minmax(0, 0.72fr)
        minmax(0, 0.87fr)
        minmax(0, 1.22fr) !important;

    gap: 7px !important;

    width: 100% !important;
    max-width: 100% !important;

    align-items: center !important;
    justify-content: stretch !important;
}

.st-key-category_selector [data-testid="column"] {
    width: 100% !important;
    min-width: 0 !important;
    max-width: 100% !important;

    flex: none !important;

    padding: 0 !important;
    margin: 0 !important;
}

.st-key-category_selector div[data-testid="stButton"] {
    width: 100% !important;
    min-width: 0 !important;
    max-width: 100% !important;
    margin: 0 !important;
}

.st-key-category_selector div[data-testid="stButton"] > button,
.st-key-category_selector div[data-testid="stButton"] > button:hover,
.st-key-category_selector div[data-testid="stButton"] > button:focus,
.st-key-category_selector div[data-testid="stButton"] > button:active {
    width: 100% !important;
    min-width: 0 !important;
    max-width: 100% !important;

    min-height: 40px !important;
    height: 40px !important;

    padding: 0 8px !important;

    border-radius: 999px !important;
    border: 1px solid #dfe1e7 !important;

    background: #ffffff !important;
    background-color: #ffffff !important;

    color: #555b69 !important;

    box-shadow: none !important;
    outline: none !important;

    display: flex !important;
    align-items: center !important;
    justify-content: center !important;

    gap: 7px !important;

    white-space: nowrap !important;
    overflow: visible !important;
}

/* ONE circle only */
.st-key-category_selector div[data-testid="stButton"] > button::before {
    content: "";
    display: inline-block;

    width: 18px;
    height: 18px;
    min-width: 18px;
    flex: 0 0 18px;

    border-radius: 50%;
    box-sizing: border-box;

    background: #ffffff !important;
    border: 1.5px solid #d4d7df !important;
}

/* Selected pill */
.st-key-category_selector button[kind="primary"],
.st-key-category_selector [data-testid="stBaseButton-primary"] {
    background: linear-gradient(
        135deg,
        #f8d8e8 0%,
        #e6ddff 55%,
        #e3f3e9 100%
    ) !important;

    border-color: #dfc7e8 !important;
}

/* Selected circle */
.st-key-category_selector button[kind="primary"]::before,
.st-key-category_selector [data-testid="stBaseButton-primary"]::before {
    background: #ffffff !important;
    border: 5px solid #ff6576 !important;
}

.st-key-category_selector div[data-testid="stButton"] > button p,
.st-key-category_selector div[data-testid="stButton"] > button span {
    color: #555b69 !important;
    -webkit-text-fill-color: #555b69 !important;

    opacity: 1 !important;

    font-size: 12px !important;
    font-weight: 800 !important;
    line-height: 1 !important;

    white-space: nowrap !important;
    word-break: keep-all !important;
    overflow: visible !important;
    text-overflow: clip !important;

    min-width: 0 !important;
}

/* selected text stays dark gray */
.st-key-category_selector button[kind="primary"] p,
.st-key-category_selector button[kind="primary"] span,
.st-key-category_selector [data-testid="stBaseButton-primary"] p,
.st-key-category_selector [data-testid="stBaseButton-primary"] span {
    color: #555b69 !important;
    -webkit-text-fill-color: #555b69 !important;
    font-weight: 900 !important;
}

/* =======================================================
   RESET + QUOTE
   ======================================================= */

.st-key-bottom_actions {
    margin-top: 11px !important;
}

.st-key-bottom_actions [data-testid="stHorizontalBlock"] {
    align-items: center !important;
    gap: 1.15rem !important;
}

.st-key-bottom_actions div[data-testid="stButton"] > button,
.st-key-bottom_actions div[data-testid="stButton"] > button:hover,
.st-key-bottom_actions div[data-testid="stButton"] > button:focus,
.st-key-bottom_actions div[data-testid="stButton"] > button:active {
    width: 40px !important;
    min-width: 40px !important;
    max-width: 40px !important;

    min-height: 37px !important;
    height: 37px !important;

    padding: 0 !important;

    border-radius: 10px !important;

    background: #ffffff !important;
    background-color: #ffffff !important;

    color: #727784 !important;

    border: 1px solid #dedfe5 !important;
    box-shadow: none !important;
    outline: none !important;
}

.st-key-bottom_actions div[data-testid="stButton"] > button p,
.st-key-bottom_actions div[data-testid="stButton"] > button span {
    color: #727784 !important;
    -webkit-text-fill-color: #727784 !important;
    font-size: 17px !important;
    font-weight: 500 !important;
}

.st-key-bottom_actions button,
.st-key-bottom_actions button[kind="secondary"],
.st-key-bottom_actions [data-testid="stBaseButton-secondary"] {
    background: #ffffff !important;
    background-color: #ffffff !important;
    color: #727784 !important;
    border-color: #dedfe5 !important;
    box-shadow: none !important;
}

/* approximately +20% vs previous approved mockup */
.quote-text {
    padding: 0;
    margin: 0;

    text-align: center;
    font-size: clamp(23px, 4.2vw, 32px);
    font-weight: 850;
    font-style: italic;
    line-height: 1.32;
    white-space: normal;

    background: linear-gradient(
        90deg,
        #efa6d5,
        #d2b3fa,
        #acc4ff,
        #8fddff,
        #90e8d3,
        #beeaa9,
        #efd79b,
        #f3b7b8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* =======================================================
   MOBILE — tuned to Samsung S23 Ultra proportions
   ======================================================= */

@media (max-width: 520px) {

    .block-container {
        max-width: 100% !important;

        padding-top: 0.38rem !important;
        padding-bottom: 0.50rem !important;

        padding-left: 0.62rem !important;
        padding-right: 0.62rem !important;
    }

    /* +20% from previous mockup, but still single line */
    .main-title {
        font-size: clamp(32.46px, 9.557vw, 37.87px) !important;
        line-height: 1.01 !important;
        margin-bottom: 4px !important;

        white-space: nowrap !important;
        letter-spacing: -0.75px !important;
    }

    .by-line {
        font-size: 12px !important;
        margin-bottom: 10px !important;
    }

    .active-category {
        font-size: 15px !important;
        margin-bottom: 12px !important;
    }

    /* score */
    .score-grid {
        gap: 7px !important;
        margin-bottom: 28px !important;
    }

    .score-card {
        min-height: 61px !important;
        padding: 6px 3px !important;
        border-radius: 16px !important;
    }

    .score-label {
        font-size: 9.6px !important;
        margin-bottom: 3px !important;
    }

    .score-number {
        font-size: 23px !important;
    }

    /* question */
    .question-shell {
        margin: 0 0 8px 0 !important;
    }

    .question-label,
    .review-label {
        font-size: 15.5px !important;
        margin-bottom: 14px !important;
    }

    /* Chinese +20% */
    .chinese-short {
        font-size: clamp(68px, 20vw, 84px) !important;
    }

    .chinese-medium {
        font-size: clamp(46px, 13.4vw, 59px) !important;
    }

    .chinese-long {
        font-size: clamp(31px, 8.5vw, 42px) !important;
    }

    /* answers */
    .st-key-answer_area div[data-testid="stVerticalBlock"] {
        gap: 0.36rem !important;
    }

    .st-key-answer_area div[data-testid="stButton"] > button,
    .st-key-answer_area div[data-testid="stButton"] > button:hover,
    .st-key-answer_area div[data-testid="stButton"] > button:focus,
    .st-key-answer_area div[data-testid="stButton"] > button:active {
        min-height: 45px !important;
        padding: 0.41rem 0.58rem !important;
        border-radius: 14px !important;

        background: #ffffff !important;
        background-color: #ffffff !important;

        color: #4d5260 !important;

        border: 1px solid #dedfe5 !important;
        box-shadow: none !important;
    }

    .st-key-answer_area div[data-testid="stButton"] > button p,
    .st-key-answer_area div[data-testid="stButton"] > button span {
        font-size: 14.5px !important;
    }

    /* Category selector — EXACT REFERENCE on S23 Ultra */
    .bottom-category-title {
        font-size: 11.5px !important;
        margin-top: 12px !important;
        margin-bottom: 5px !important;
    }

    .st-key-category_selector {
        width: 100% !important;
        max-width: 100% !important;
        overflow: visible !important;
    }

    .st-key-category_selector [data-testid="stHorizontalBlock"] {
        display: grid !important;

        grid-template-columns:
            minmax(0, 1.25fr)
            minmax(0, 1.32fr)
            minmax(0, 0.72fr)
            minmax(0, 0.87fr)
            minmax(0, 1.22fr) !important;

        gap: 4px !important;

        width: 100% !important;
        max-width: 100% !important;

        align-items: center !important;
        justify-content: stretch !important;
    }

    .st-key-category_selector [data-testid="column"] {
        width: 100% !important;
        min-width: 0 !important;
        max-width: 100% !important;

        padding: 0 !important;
        margin: 0 !important;
    }

    .st-key-category_selector div[data-testid="stButton"] {
        width: 100% !important;
        min-width: 0 !important;
        max-width: 100% !important;
    }

    .st-key-category_selector div[data-testid="stButton"] > button,
    .st-key-category_selector div[data-testid="stButton"] > button:hover,
    .st-key-category_selector div[data-testid="stButton"] > button:focus,
    .st-key-category_selector div[data-testid="stButton"] > button:active {
        width: 100% !important;
        min-width: 0 !important;
        max-width: 100% !important;

        min-height: 36px !important;
        height: 36px !important;

        padding: 0 3px !important;

        border-radius: 999px !important;
        border: 1px solid #dfe1e7 !important;

        background: #ffffff !important;
        background-color: #ffffff !important;

        color: #555b69 !important;

        gap: 3px !important;

        white-space: nowrap !important;
        overflow: visible !important;
    }

    .st-key-category_selector div[data-testid="stButton"] > button::before {
        width: 14px !important;
        height: 14px !important;
        min-width: 14px !important;
        flex: 0 0 14px !important;

        background: #ffffff !important;
        border: 1.4px solid #d4d7df !important;
    }

    .st-key-category_selector button[kind="primary"]::before,
    .st-key-category_selector [data-testid="stBaseButton-primary"]::before {
        background: #ffffff !important;
        border: 4px solid #ff6576 !important;
    }

    .st-key-category_selector div[data-testid="stButton"] > button p,
    .st-key-category_selector div[data-testid="stButton"] > button span {
        color: #555b69 !important;
        -webkit-text-fill-color: #555b69 !important;

        opacity: 1 !important;

        font-size: 9.6px !important;
        font-weight: 800 !important;
        line-height: 1 !important;

        white-space: nowrap !important;
        word-break: keep-all !important;
        overflow: visible !important;
        text-overflow: clip !important;
    }

    .st-key-category_selector button[kind="primary"] p,
    .st-key-category_selector button[kind="primary"] span,
    .st-key-category_selector [data-testid="stBaseButton-primary"] p,
    .st-key-category_selector [data-testid="stBaseButton-primary"] span {
        color: #555b69 !important;
        -webkit-text-fill-color: #555b69 !important;
        font-weight: 900 !important;
    }

    /* reset + quote immediately below categories */
    .st-key-bottom_actions {
        margin-top: 10px !important;
    }

    .st-key-bottom_actions [data-testid="stHorizontalBlock"] {
        gap: 0.95rem !important;
    }

    .st-key-bottom_actions div[data-testid="stButton"] > button,
    .st-key-bottom_actions div[data-testid="stButton"] > button:hover,
    .st-key-bottom_actions div[data-testid="stButton"] > button:focus,
    .st-key-bottom_actions div[data-testid="stButton"] > button:active {
        width: 36px !important;
        min-width: 36px !important;
        max-width: 36px !important;

        min-height: 34px !important;
        height: 34px !important;

        background: #ffffff !important;
        background-color: #ffffff !important;

        color: #727784 !important;

        border: 1px solid #dedfe5 !important;
    }

    /* Quote +20%, wrapping into 2–3 lines is allowed */
    .quote-text {
        font-size: clamp(23px, 7.8vw, 31px) !important;
        line-height: 1.32 !important;
        text-align: center !important;
        white-space: normal !important;
    }
}

/* FINAL reset protection against Android/PWA dark theme */
.st-key-bottom_actions button,
.st-key-bottom_actions button:hover,
.st-key-bottom_actions button:focus,
.st-key-bottom_actions button:active,
.st-key-bottom_actions button[kind="secondary"],
.st-key-bottom_actions [data-testid="stBaseButton-secondary"] {
    background: #ffffff !important;
    background-color: #ffffff !important;
    color: #727784 !important;
    -webkit-text-fill-color: #727784 !important;
    border-color: #dedfe5 !important;
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# VOCABULARY
# =========================================================

VOCAB_SET_1 = [
    ('系统', 'System'),
    ('做系统', 'Build System'),
    ('开发', 'Development'),
    ('开发人员', 'Developer'),
    ('需求', 'Requirement'),
    ('请求', 'Request'),
    ('调用接口', 'Call API'),
    ('参数', 'Parameter'),
    ('响应', 'Response'),
    ('测试', 'Testing'),
    ('测试系统', 'Test System'),
    ('系统测试', 'System Testing'),
    ('测试用例', 'Test Case'),
    ('验收测试', 'UAT / Acceptance Testing'),
    ('签字确认', 'Sign-off'),
    ('确认', 'Confirm'),
    ('流程', 'Process'),
    ('人工流程', 'Manual Process'),
    ('人工审核', 'Manual Review'),
    ('自动', 'Automatic'),
    ('自动化流程', 'Automation Process'),
    ('上线', 'Go Live'),
    ('系统事故', 'System Incident'),
    ('解决问题', 'Fix / Solve Problem'),
    ('异常', 'Exception'),
    ('错误', 'Error'),
    ('日志', 'Log'),
    ('数据', 'Data'),
    ('数据库', 'Database'),
    ('数据源', 'Data Source'),
    ('字段', 'Field'),
    ('为空', 'Empty / Blank'),
    ('空值', 'Null / Empty Value'),
    ('数据验证', 'Data Validation'),
    ('数据缺失', 'Missing Data'),
    ('数据错误', 'Incorrect / Wrong Data'),
    ('数据流', 'Data Flow'),
    ('业务部门', 'Business Division'),
    ('项目', 'Project'),
    ('范围', 'Scope'),
    ('需要', 'Need / A Must'),
    ('先', 'Before / First'),
    ('产品', 'Product'),
    ('目标', 'Goal'),
    ('前端', 'Frontend'),
    ('后端', 'Backend'),
    ('显示', 'Display'),
    ('不正确', 'Incorrect'),
    ('返回', 'Return'),
    ('发生', 'Occur'),
    ('层', 'Layer'),
    ('用户', 'User'),
    ('点击', 'Click'),
    ('按钮', 'Button'),
    ('传递', 'Pass / ส่งค่า'),
    ('哪些', 'Which / อะไรบ้าง'),
    ('使用', 'Use'),
    ('令牌', 'Token'),
    ('错误码', 'Error Code'),
    ('时', 'When / ตอนที่'),
    ('解释', 'Explain'),
    ('架构', 'Architecture'),
    ('传到', 'Flow To / A → B'),
    ('连接', 'Connect'),
    ('步骤', 'Step'),
    ('同步', 'Synchronous'),
    ('异步', 'Asynchronous'),
    ('不可用', 'Unavailable'),
    ('备用', 'Backup / Fallback'),
    ('方案', 'Solution'),
    ('备用方案', 'Contingency Plan'),
    ('环境', 'Environment'),
    ('版本', 'Version'),
    ('流水线', 'Pipeline'),
    ('失败', 'Fail'),
    ('成功', 'Success'),
    ('回滚', 'Rollback'),
    ('出现', 'Appear / Occur'),
    ('进行', 'Proceed / ดำเนินการ'),
    ('发布', 'Release'),
    ('金丝雀', 'Canary'),
    ('提供', 'Provide'),
    ('根本', 'Root'),
    ('原因', 'Cause'),
    ('根本原因', 'Root Cause'),
    ('影响', 'Impact'),
    ('明确', 'Clear / ชัดเจน'),
    ('增加', 'Increase'),
    ('复盘', 'Postmortem'),
    ('主要', 'Main'),
    ('衡量', 'Measure'),
    ('而', 'But / แต่'),
    ('不仅仅', 'Not Only / ไม่เพียงแค่'),
    ('产出', 'Output'),
    ('风险', 'Risk'),
    ('最大', 'Biggest / Maximum'),
    ('假设', 'Assumption'),
    ('怎么', 'How'),
    ('验证', 'Validate'),
    ('标准', 'Standard')
]


VOCAB_SET_2 = [
    ('这个', 'this'),
    ('需求', 'Requirement'),
    ('是', 'be, is'),
    ('什么', 'what'),
    ('业务', 'Business'),
    ('部门', 'department'),
    ('想', 'want, think'),
    ('解决', 'Resolve'),
    ('问题', 'Issue'),
    ('项目', 'Project'),
    ('的', 'possessive particle'),
    ('范围', 'Scope'),
    ('我们', 'we'),
    ('需要', 'need'),
    ('先', 'first, beforehand'),
    ('确认', 'Confirm'),
    ('产品', 'Product'),
    ('目标', 'Goal'),
    ('前端', 'Frontend'),
    ('还是', 'or'),
    ('后端', 'Backend'),
    ('显示', 'display'),
    ('数据', 'Data'),
    ('不', 'not'),
    ('正确', 'correct'),
    ('返回', 'Return'),
    ('了', 'completed-change particle'),
    ('发生', 'Occur'),
    ('在', 'at, in'),
    ('哪', 'which'),
    ('一', 'one'),
    ('层', 'layer'),
    ('用户', 'User'),
    ('点击', 'click'),
    ('按钮', 'button'),
    ('后', 'after'),
    ('没有', 'not have'),
    ('响应', 'Response'),
    ('怎么', 'how'),
    ('调用', 'call, invoke'),
    ('请求', 'Request'),
    ('传', 'pass, transmit'),
    ('哪些', 'which ones'),
    ('参数', 'Parameter'),
    ('使用', 'use'),
    ('令牌', 'Token'),
    ('错误', 'Error'),
    ('时', 'when'),
    ('系统', 'System'),
    ('码', 'code'),
    ('来自', 'come from'),
    ('哪个', 'which'),
    ('数据库', 'Database'),
    ('主要', 'main, primary'),
    ('数据源', 'Data Source'),
    ('请', 'please'),
    ('检查', 'check, inspect'),
    ('里', 'inside'),
    ('字段', 'Field'),
    ('可以', 'can'),
    ('为', 'be, become'),
    ('空', 'empty, null'),
    ('吗', 'question particle'),
    ('两', 'two'),
    ('个', 'general measure word'),
    ('一致', 'consistent'),
    ('给', 'give, for'),
    ('我', 'I'),
    ('解释', 'explain'),
    ('一下', 'a bit'),
    ('架构', 'Architecture'),
    ('从', 'from'),
    ('到', 'to'),
    ('连接', 'Connect'),
    ('步骤', 'step'),
    ('同步', 'Synchronous'),
    ('异步', 'Asynchronous'),
    ('如果', 'if'),
    ('可用', 'available'),
    ('有', 'have'),
    ('备用', 'backup, standby'),
    ('方案', 'plan, solution'),
    ('现在', 'now'),
    ('环境', 'Environment'),
    ('版本', 'Version'),
    ('时候', 'time, when'),
    ('上线', 'Go-live'),
    ('流水线', 'Pipeline'),
    ('失败', 'fail'),
    ('出现', 'appear, occur'),
    ('回滚', 'Rollback'),
    ('进行', 'carry out, proceed'),
    ('金丝雀', 'canary'),
    ('发布', 'Release'),
    ('提供', 'provide'),
    ('日志', 'Log'),
    ('根本', 'fundamental, root'),
    ('原因', 'reason, cause'),
    ('影响', 'Impact'),
    ('多少', 'how much, how many')
]


VOCAB_SET_3 = [
    ('客户', 'customer'),
    ('时间', 'time'),
    ('明显', 'obvious, significant'),
    ('增加', 'increase'),
    ('事故', 'Incident'),
    ('做', 'do'),
    ('复盘', 'Postmortem'),
    ('衡量', 'measure'),
    ('结果', 'Outcome'),
    ('而', 'while, but'),
    ('仅仅', 'merely, only'),
    ('产出', 'output'),
    ('风险', 'Risk'),
    ('最', 'most'),
    ('大', 'big'),
    ('假设', 'Assumption'),
    ('谁', 'who'),
    ('验证', 'Validate'),
    ('还', 'still, also'),
    ('够', 'enough'),
    ('明确', 'Clarify'),
    ('非', 'non-'),
    ('功能性', 'functional'),
    ('必须', 'must'),
    ('超过', 'exceed'),
    ('秒', 'second'),
    ('这', 'this'),
    ('种', 'kind, type'),
    ('异常', 'Exception'),
    ('情况', 'situation'),
    ('下', 'under, below'),
    ('应该', 'should'),
    ('处理', 'Handle'),
    ('验收', 'Acceptance'),
    ('标准', 'standard'),
    ('必填', 'Mandatory'),
    ('可选', 'Optional'),
    ('变更', 'Change'),
    ('向后', 'backward'),
    ('兼容', 'Compatible'),
    ('补充', 'supplement, add'),
    ('场景', 'Scenario'),
    ('任务', 'task'),
    ('完成', 'Complete'),
    ('测试', 'Testing'),
    ('发现', 'discover, find'),
    ('缺陷', 'Defect'),
    ('会', 'will, can'),
    ('回归', 'Regression'),
    ('性能', 'Performance'),
    ('怎么样', 'how is it'),
    ('个人', 'personal'),
    ('信息', 'information'),
    ('依赖', 'Dependency'),
    ('开发', 'Development'),
    ('大概', 'approximately'),
    ('多', 'many, much'),
    ('长', 'long'),
    ('缩小', 'reduce, shrink'),
    ('技术', 'technology, technical'),
    ('债', 'debt'),
    ('接受', 'accept'),
    ('这些', 'these'),
    ('包含', 'contain, include'),
    ('权限', 'Permission'),
    ('访问', 'access'),
    ('是否', 'whether'),
    ('已经', 'already'),
    ('加密', 'Encryption'),
    ('记录', 'record'),
    ('审计', 'Audit'),
    ('服务', 'Service'),
    ('账号', 'account'),
    ('部署', 'Deployment'),
    ('计划', 'plan'),
    ('迁移', 'Migration'),
    ('核对', 'Reconciliation'),
    ('要', 'need to, will'),
    ('监控', 'Monitoring'),
    ('指标', 'Metric'),
    ('今晚', 'tonight'),
    ('生产', 'production'),
    ('机器', 'machine'),
    ('学习', 'learn, learning'),
    ('语言', 'language'),
    ('模型', 'Model'),
    ('应用', 'application'),
    ('所有', 'all'),
    ('都', 'all'),
    ('人工', 'manual, human'),
    ('智能', 'intelligence'),
    ('只是', 'only, merely'),
    ('部分', 'part'),
    ('输出', 'Output'),
    ('存在', 'exist'),
    ('确定性', 'certainty'),
    ('定义', 'define'),
    ('容忍度', 'tolerance'),
    ('训练', 'Training'),
    ('推理', 'Inference')
]


VOCAB_SET_4 = [
    ('目前', 'Currently'),
    ('延迟', 'Delay'),
    ('支持', 'support'),
    ('每', 'every'),
    ('温度', 'temperature'),
    ('设置', 'set, configure'),
    ('上下文', 'Context'),
    ('太', 'too'),
    ('用', 'use'),
    ('格式', 'Format'),
    ('防止', 'prevent'),
    ('提示词', 'Prompt'),
    ('注入', 'Injection'),
    ('嵌入', 'Embedding'),
    ('切分', 'split, chunk'),
    ('文档', 'document'),
    ('元数据', 'Metadata'),
    ('过滤', 'Filter'),
    ('条件', 'condition'),
    ('检索', 'Retrieval'),
    ('相关', 'relevant, related'),
    ('混合', 'hybrid, mixed'),
    ('文件', 'Document'),
    ('知识库', 'Knowledge Base'),
    ('和', 'and'),
    ('答案', 'answer'),
    ('引用', 'Citation'),
    ('来源', 'source'),
    ('索引', 'Index'),
    ('最后', 'last, final'),
    ('更新', 'update'),
    ('微调', 'Fine-tuning'),
    ('对', 'toward, to'),
    ('基准', 'benchmark, baseline'),
    ('成本', 'Cost'),
    ('更', 'more'),
    ('高', 'high'),
    ('经常', 'often'),
    ('变化', 'change'),
    ('所以', 'therefore'),
    ('适合', 'suitable'),
    ('评估', 'Evaluation'),
    ('供应商', 'Vendor / Supplier'),
    ('锁定', 'Lock-in'),
    ('回答', 'answer'),
    ('准确', 'accurate'),
    ('质量', 'Quality'),
    ('依据', 'Evidence'),
    ('幻觉', 'Hallucination'),
    ('率', 'rate'),
    ('低于', 'below'),
    ('百分之', 'percent'),
    ('二', 'two'),
    ('不足', 'insufficient'),
    ('拒绝', 'Refuse'),
    ('能', 'can'),
    ('带来', 'bring'),
    ('价值', 'Value'),
    ('审核', 'review, audit'),
    ('辅助', 'Assist'),
    ('模式', 'mode'),
    ('开始', 'Start'),
    ('采用', 'adopt'),
    ('护栏', 'Guardrail'),
    ('端到', 'end-to-'),
    ('端', 'end'),
    ('工具', 'Tool'),
    ('通过', 'pass, through'),
    ('敏感', 'Sensitive'),
    ('发送', 'send'),
    ('外部', 'external'),
    ('高峰期', 'peak period'),
    ('并发', 'Concurrent'),
    ('降低', 'reduce'),
    ('使用量', 'usage'),
    ('缓存', 'Cache'),
    ('新鲜度', 'freshness'),
    ('次', 'occurrence, time'),
    ('实验', 'Experiment'),
    ('新', 'new'),
    ('影子', 'shadow'),
    ('平台', 'Platform'),
    ('人员', 'personnel'),
    ('提高', 'improve, increase'),
    ('自助', 'self-service'),
    ('能力', 'capability'),
    ('才', 'only then'),
    ('模板', 'Template'),
    ('团队', 'team'),
    ('独立', 'independent'),
    ('配额', 'Quota'),
    ('北极星', 'North Star'),
    ('试点', 'Pilot'),
    ('将', 'will'),
    ('一百', 'one hundred'),
    ('名', 'measure word for people'),
    ('显著', 'Significant'),
    ('负面', 'negative'),
    ('反馈', 'Feedback'),
    ('等级', 'level, grade')
]


VOCAB_SET_5 = [
    ('暂时', 'temporarily'),
    ('关闭', 'close, disable'),
    ('功能', 'Function'),
    ('有关', 'related'),
    ('负责人', 'Responsible person'),
    ('整改', 'corrective rectification'),
    ('措施', 'measure, action'),
    ('今天', 'today'),
    ('决定', 'Decision'),
    ('三', 'three'),
    ('件', 'measure word'),
    ('事', 'matter, thing'),
    ('说明', 'explain'),
    ('当前', 'current'),
    ('行为', 'behavior'),
    ('预期', 'Expected'),
    ('重现', 'Reproduce'),
    ('替代', 'replace, alternative'),
    ('提前', 'ahead of time'),
    ('多久', 'how long'),
    ('交付', 'Delivery'),
    ('负责', 'be responsible'),
    ('行动', 'action'),
    ('项', 'item'),
    ('日期', 'date'),
    ('明天', 'tomorrow'),
    ('再', 'again'),
    ('跟进', 'Follow up'),
    ('选择', 'choose'),
    ('因为', 'because'),
    ('核心', 'core'),
    ('前', 'before, front'),
    ('安全', 'Security'),
    ('审查', 'review'),
    ('接口', 'Interface'),
    ('错误码', 'Error code'),
    ('查询', 'Query'),
    ('一致性', 'Consistency'),
    ('根本原因', 'Root Cause'),
    ('非功能性需求', 'NFR'),
    ('测试数据', 'Test Data'),
    ('技术债', 'Technical debt'),
    ('敏感数据', 'Sensitive data'),
    ('人工智能', 'Artificial'),
    ('机器学习', 'Machine Learning'),
    ('不确定性', 'Uncertainty'),
    ('吞吐量', 'Throughput'),
    ('温度参数', 'Temperature'),
    ('向量', 'Vector'),
    ('检索增强生成', 'RAG'),
    ('基准测试', 'Benchmark'),
    ('准确率', 'Accuracy'),
    ('人工审核', 'Human-in-the-loop'),
    ('采用率', 'Adoption'),
    ('端到端', 'End-to-end'),
    ('高峰', 'Peak'),
    ('模型版本', 'Model Version'),
    ('影子测试', 'Shadow test'),
    ('生命周期', 'Lifecycle'),
    ('开发人员', 'Developer'),
    ('自助服务', 'Self-service'),
    ('整改措施', 'Corrective action'),
    ('替代方案', 'Alternative'),
    ('核心指标', 'Core metric'),
    ('安全审查', 'Security review'),
    ('数据表', 'Table'),
    ('队列', 'Queue'),
    ('网络', 'Network'),
    ('告警', 'Alert'),
    ('可用性', 'Availability'),
    ('可扩展性', 'Scalability'),
    ('业务需求', 'Business Requirement'),
    ('需求变更', 'Requirement Change'),
    ('优先级', 'Priority'),
    ('业务流程', 'Business Process'),
    ('业务逻辑', 'Business Logic'),
    ('使用场景', 'Use Case'),
    ('验收标准', 'Acceptance Criteria'),
    ('代码', 'Code'),
    ('逻辑', 'Logic'),
    ('修改', 'Modify'),
    ('系统架构', 'System Architecture'),
    ('微服务', 'Microservice'),
    ('组件', 'Component'),
    ('配置', 'Configuration'),
    ('调用接口', 'Call'),
    ('传参数', 'Pass Parameter'),
    ('集成', 'Integration'),
    ('传输数据', 'Data Transmission'),
    ('超时', 'Timeout'),
    ('网关', 'API Gateway'),
    ('端点', 'Endpoint'),
    ('身份验证', 'Authentication'),
    ('授权', 'Authorization'),
    ('源数据', 'Source Data'),
    ('映射', 'Mapping'),
    ('数据不一致', 'Data Mismatch'),
    ('数据一致性', 'Data'),
    ('数据迁移', 'Data Migration'),
    ('数据验证', 'Data Validation'),
    ('测试用例', 'Test Case'),
    ('集成测试', 'Integration Test'),
    ('验收测试', 'UAT'),
    ('回归测试', 'Regression Test'),
    ('性能测试', 'Performance Test'),
    ('通过测试', 'Pass Testing'),
    ('测试未通过', 'Fail Testing'),
    ('开发环境', 'Development Environment'),
    ('测试环境', 'Test Environment'),
    ('生产环境', 'Production Environment'),
    ('下线', 'Take Offline'),
    ('部署计划', 'Deployment Plan'),
    ('发布窗口', 'Release'),
    ('错误日志', 'Error Log'),
    ('恢复', 'Recover'),
    ('临时解决方案', 'Workaround'),
    ('预防措施', 'Preventive Action'),
    ('已完成', 'Completed'),
    ('进行中', 'In Progress'),
    ('尚未开始', 'Not Started'),
    ('等待', 'Waiting'),
    ('阻塞', 'Blocked'),
    ('延期', 'Postpone'),
    ('预计', 'Estimate'),
    ('进度', 'Progress'),
    ('截止日期', 'Deadline'),
    ('访问权限', 'Access Permission'),
    ('个人数据', 'Personal Data'),
    ('云服务', 'Cloud'),
    ('服务器', 'Server'),
    ('持续集成和持续交付', 'CI/CD'),
    ('代码仓库', 'Git Repository'),
    ('扩展', 'Scale'),
    ('大语言模型', 'LLM'),
    ('向量嵌入', 'Embedding'),
    ('向量数据库', 'Vector Database'),
    ('模型监控', 'Model Monitoring'),
    ('隐私', 'Privacy'),
    ('单次请求成本', 'Cost per Request')
]


VOCAB_SETS = {
    1: VOCAB_SET_1,
    2: VOCAB_SET_2,
    3: VOCAB_SET_3,
    4: VOCAB_SET_4,
    5: VOCAB_SET_5,
}

SET_LABELS = {
    1: "CBS · Core Banking System",
    2: "System & API",
    3: "Incident & Operations",
    4: "AI / LLM / Platform",
    5: "Testing / UAT / Deployment",
}



# =========================================================
# PER-SET PROGRESS
# =========================================================

def blank_progress():
    return {
        "correct": 0,
        "attempts": 0,

        # Main deck: every word appears once.
        "phase": "main",
        "main_order": [],
        "main_pos": 0,

        # Words answered incorrectly during the main deck.
        "wrong_ids": [],

        # Quick review queue:
        # wrong -> after 5 questions -> after another 10 questions.
        "scheduled_reviews": [],

        # Two final review rounds after the whole set is complete.
        "final_order": [],
        "final_pos": 0,
        "final_round_wrong": [],

        # Current question.
        "question_id": None,
        "question_kind": None,
        "options": [],

        # End popups.
        "reminder_ack": False,
        "congrats_shown": False,
    }


QUOTES = [
    "Knowledge stays with you forever.",
    "Every small thing you study adds to your inner strength.",
    "No one can steal your skills or what is in your mind.",
    "Every expert was once a beginner.",
    "Keep learning, keep growing.",
]

if "quote_of_the_day" not in st.session_state:
    st.session_state.quote_of_the_day = random.choice(QUOTES)

if "selected_set" not in st.session_state:
    st.session_state.selected_set = 1

if "progress_by_set" not in st.session_state:
    st.session_state.progress_by_set = {
        i: blank_progress() for i in range(1, 6)
    }


def get_progress():
    return st.session_state.progress_by_set[st.session_state.selected_set]


def make_options(vocab, question_id):
    correct_answer = vocab[question_id][1]

    wrong_pool = list({
        meaning
        for _, meaning in vocab
        if meaning != correct_answer
    })

    wrong_answers = random.sample(wrong_pool, 2)
    options = [correct_answer, *wrong_answers]
    random.shuffle(options)
    return options


def initialize_main_round(progress, vocab):
    if not progress["main_order"]:
        progress["main_order"] = list(range(len(vocab)))
        random.shuffle(progress["main_order"])


def set_question(progress, vocab, question_id, kind):
    progress["question_id"] = question_id
    progress["question_kind"] = kind
    progress["options"] = make_options(vocab, question_id)


def schedule_review(progress, question_id, after_questions, kind):
    progress["scheduled_reviews"].append({
        "qid": question_id,
        "due_at": progress["attempts"] + after_questions,
        "kind": kind,
    })


def pop_due_review(progress):
    if not progress["scheduled_reviews"]:
        return None

    progress["scheduled_reviews"].sort(key=lambda item: item["due_at"])

    if progress["scheduled_reviews"][0]["due_at"] <= progress["attempts"]:
        return progress["scheduled_reviews"].pop(0)

    return None


def start_final_review(progress, round_number):
    progress["phase"] = f"final{round_number}"
    progress["final_order"] = list(progress["wrong_ids"])
    random.shuffle(progress["final_order"])
    progress["final_pos"] = 0

    if round_number == 2:
        progress["final_round_wrong"] = []


def finish_session(progress):
    progress["phase"] = "done"
    progress["question_id"] = None
    progress["question_kind"] = None
    progress["options"] = []


def new_question(progress, vocab):
    initialize_main_round(progress, vocab)

    # MAIN ROUND
    if progress["phase"] == "main":
        # Once every new word has appeared, go to the final review rounds.
        if progress["main_pos"] >= len(progress["main_order"]):
            progress["scheduled_reviews"] = []

            if progress["wrong_ids"]:
                start_final_review(progress, 1)
            else:
                finish_session(progress)
                return
        else:
            due_review = pop_due_review(progress)

            if due_review is not None:
                set_question(
                    progress,
                    vocab,
                    due_review["qid"],
                    due_review["kind"]
                )
                return

            question_id = progress["main_order"][progress["main_pos"]]
            set_question(progress, vocab, question_id, "main")
            return

    # FINAL REVIEW 1
    if progress["phase"] == "final1":
        if progress["final_pos"] < len(progress["final_order"]):
            question_id = progress["final_order"][progress["final_pos"]]
            set_question(progress, vocab, question_id, "final1")
            return

        start_final_review(progress, 2)

    # FINAL REVIEW 2
    if progress["phase"] == "final2":
        if progress["final_pos"] < len(progress["final_order"]):
            question_id = progress["final_order"][progress["final_pos"]]
            set_question(progress, vocab, question_id, "final2")
            return

        finish_session(progress)


def advance_after_answer(progress, vocab, is_correct):
    question_id = progress["question_id"]
    kind = progress["question_kind"]

    progress["attempts"] += 1

    if is_correct:
        progress["correct"] += 1

    # Fresh word from the main deck.
    if kind == "main":
        if not is_correct:
            if question_id not in progress["wrong_ids"]:
                progress["wrong_ids"].append(question_id)

            # First quick review after 5 other questions.
            schedule_review(
                progress,
                question_id,
                after_questions=5,
                kind="quick5"
            )

        progress["main_pos"] += 1

    # First quick review: schedule one more review after another 10 questions.
    elif kind == "quick5":
        schedule_review(
            progress,
            question_id,
            after_questions=10,
            kind="quick10"
        )

    # Second quick review: no more quick loops.
    elif kind == "quick10":
        pass

    # Final review after the whole set.
    elif kind == "final1":
        progress["final_pos"] += 1

    elif kind == "final2":
        if not is_correct and question_id not in progress["final_round_wrong"]:
            progress["final_round_wrong"].append(question_id)

        progress["final_pos"] += 1

    progress["question_id"] = None
    progress["question_kind"] = None
    progress["options"] = []

    new_question(progress, vocab)


def chinese_html(word):
    safe_word = html.escape(word)
    length = len(word)

    # 1–4 Chinese characters: always one line.
    if length <= 4:
        return f'<div class="chinese-short">{safe_word}</div>'

    # 5–6 characters: still one line, smaller.
    if length <= 6:
        return f'<div class="chinese-medium">{safe_word}</div>'

    # Longer words: one line with smaller text.
    return f'<div class="chinese-long">{safe_word}</div>'


def render_question_area(label_html, chinese_word_html):
    st.markdown(
        f"""
        <div class="question-shell">
            <div class="question-center">
                {label_html}
                {chinese_word_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_reminder_dialog(vocab, progress):
    if hasattr(st, "dialog"):
        @st.dialog("🌷 ไม่เป็นไรนะ")
        def reminder_dialog():
            st.write("ทบทวนคำเหล่านี้อีกรอบนะ เดี๋ยวก็จำได้ค่ะ 💪")

            for qid in progress["final_round_wrong"]:
                chinese_word, meaning = vocab[qid]
                st.markdown(f"**{chinese_word}** — {meaning}")

            if st.button(
                "ไปต่อ",
                use_container_width=True,
                key=f"reminder_continue_{st.session_state.selected_set}"
            ):
                progress["reminder_ack"] = True
                st.rerun()

        reminder_dialog()
    else:
        st.warning("🌷 ไม่เป็นไรนะ ทบทวนคำเหล่านี้อีกรอบ เดี๋ยวก็จำได้ค่ะ")
        for qid in progress["final_round_wrong"]:
            chinese_word, meaning = vocab[qid]
            st.markdown(f"- **{chinese_word}** — {meaning}")

        if st.button(
            "ไปต่อ",
            use_container_width=True,
            key=f"reminder_continue_fallback_{st.session_state.selected_set}"
        ):
            progress["reminder_ack"] = True
            st.rerun()


def show_congratulations_dialog(progress):
    if hasattr(st, "dialog"):
        @st.dialog("🎉 Congratulations!")
        def congratulations_dialog():
            st.markdown("### You did a great job 👍")
            st.markdown("**Keep going!**")

        progress["congrats_shown"] = True
        congratulations_dialog()
    else:
        progress["congrats_shown"] = True
        st.success("🎉 Congratulations! You did a great job 👍 Keep going!")


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

selected_set = st.session_state.selected_set
vocab = VOCAB_SETS[selected_set]
progress = get_progress()

if progress["question_id"] is None and progress["phase"] != "done":
    new_question(progress, vocab)


# =========================================================
# SCORE / PROGRESS
# =========================================================

if progress["attempts"] > 0:
    percentage = round((progress["correct"] / progress["attempts"]) * 100)
else:
    percentage = 0

main_done = min(progress["main_pos"], len(vocab))

st.markdown(
    f'<div class="active-category">📚 {SET_LABELS[selected_set]}</div>',
    unsafe_allow_html=True
)

score_html = (
    f'<div class="score-grid">'
    f'<div class="score-card score-purple">'
    f'<div class="score-label">✅ Correct</div>'
    f'<div class="score-number">{progress["correct"]}</div>'
    f'</div>'

    f'<div class="score-card score-pink">'
    f'<div class="score-label">📝 Answered</div>'
    f'<div class="score-number">{progress["attempts"]}</div>'
    f'</div>'

    f'<div class="score-card score-green">'
    f'<div class="score-label">🎯 Score</div>'
    f'<div class="score-number">{percentage}%</div>'
    f'</div>'
    f'</div>'
)

st.markdown(score_html, unsafe_allow_html=True)


# =========================================================
# QUESTION
# =========================================================

if progress["phase"] != "done":
    question_id = progress["question_id"]
    kind = progress["question_kind"]

    chinese_word = vocab[question_id][0]
    correct_answer = vocab[question_id][1]

    if kind == "main":
        label_html = '<div class="question-label">คำนี้แปลว่าอะไร?</div>'
    else:
        label_html = '<div class="review-label">🌷 ทบทวนอีกครั้ง</div>'

    render_question_area(
        label_html=label_html,
        chinese_word_html=chinese_html(chinese_word)
    )

    with st.container(key="answer_area"):
        for i, option in enumerate(progress["options"]):
            if st.button(
                option,
                use_container_width=True,
                key=(
                    f"answer_{selected_set}_{question_id}_{kind}_"
                    f"{progress['attempts']}_{i}"
                )
            ):
                is_correct = option == correct_answer

                if not is_correct:
                    st.error(
                        f"❌ คำตอบที่ถูกคือ\n\n"
                        f"### {chinese_word} = {correct_answer}"
                    )

                    import time
                    time.sleep(1.35)

                advance_after_answer(progress, vocab, is_correct)
                st.rerun()


# =========================================================
# END OF SESSION
# =========================================================

else:
    st.success("✅ จบการทบทวนคำศัพท์ชุดนี้แล้ว")

    if progress["final_round_wrong"] and not progress["reminder_ack"]:
        show_reminder_dialog(vocab, progress)

    elif not progress["congrats_shown"]:
        show_congratulations_dialog(progress)


# =========================================================
# CATEGORY SELECTOR + BOTTOM ACTIONS
# =========================================================

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

# Keep the currently selected category in position 3.
current_item = next(
    item for item in CATEGORY_ITEMS
    if item[0] == st.session_state.selected_set
)

other_items = [
    item for item in CATEGORY_ITEMS
    if item[0] != st.session_state.selected_set
]

display_items = (
    other_items[:2]
    + [current_item]
    + other_items[2:]
)

# IMPORTANT:
# Use buttons, NOT st.radio.
# This permanently removes the Android native black radio controls.
# Each pill gets exactly ONE circle from CSS ::before.
with st.container(key="category_selector"):

    category_columns = st.columns(
        [1, 1, 1, 1, 1],
        gap="small"
    )

    for index, (set_id, label) in enumerate(display_items):

        is_selected = (
            set_id == st.session_state.selected_set
        )

        with category_columns[index]:

            if st.button(
                label,
                key=(
                    f"category_"
                    f"{set_id}_"
                    f"{st.session_state.selected_set}"
                ),
                type="primary" if is_selected else "secondary"
            ):

                if not is_selected:
                    st.session_state.selected_set = set_id
                    st.rerun()


# Quote first, reset button last.
# Reset DOES NOT change the quote.
with st.container(key="bottom_actions"):

    safe_quote = html.escape(
        st.session_state.quote_of_the_day
    )

    st.markdown(
        f'<div class="quote-text">“{safe_quote}”</div>',
        unsafe_allow_html=True
    )

    reset_col, reset_spacer = st.columns(
        [0.65, 5.35],
        gap="large",
        vertical_alignment="center"
    )

    with reset_col:

        if st.button(
            "↻",
            key=f"reset_set_{selected_set}",
            help="เริ่มหมวดนี้ใหม่"
        ):

            st.session_state.progress_by_set[
                selected_set
            ] = blank_progress()

            st.rerun()

