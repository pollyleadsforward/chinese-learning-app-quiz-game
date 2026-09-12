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

st.set_page_config(
    page_title="Chinese Learning App",
    page_icon=app_icon,
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# IMAGES
# =========================================================

def find_image(names):
    for name in names:
        if os.path.exists(name):
            return name
    return None

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

left_image = find_image(["bunny_left.jpg", "bunny_left.jpeg", "bunny_left.png"])
right_image = find_image([
    "bunny_right.jpg", "bunny_right.jpeg", "bunny_right.png",
    "bunny_right2.jpg", "bunny_right2.jpeg", "bunny_right2.png"
])

if left_image is None and right_image is not None:
    left_image = right_image
if right_image is None and left_image is not None:
    right_image = left_image

left_bunny_b64 = image_to_base64(left_image)
right_bunny_b64 = image_to_base64(right_image)

# =========================================================
# STYLE
# =========================================================

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #fffdfd;
}

.block-container {
    max-width: 560px !important;
    padding-top: 0.40rem !important;
    padding-bottom: 1.2rem !important;
    padding-left: 0.70rem !important;
    padding-right: 0.70rem !important;
}

header, footer, #MainMenu,
[data-testid="stToolbar"],
[data-testid="stStatusWidget"],
[data-testid="stDecoration"] {
    display: none !important;
    visibility: hidden !important;
}

.main-title {
    text-align: center;
    font-size: clamp(27px, 7vw, 40px);
    font-weight: 900;
    line-height: 1.12;
    margin: 0 0 3px 0;
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
    margin-bottom: 6px;
}

.badge-wrap {
    text-align: center;
    margin-bottom: 8px;
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

.set-title {
    text-align: center;
    color: #707583;
    font-size: 12px;
    font-weight: 700;
    margin: 1px 0 3px 0;
}

div[data-testid="stRadio"] > div {
    justify-content: center !important;
    gap: 0.25rem !important;
}

div[data-testid="stRadio"] label {
    background: linear-gradient(135deg, #f8d8e8, #e6d9ff, #dff4e7);
    border-radius: 999px;
    padding: 4px 8px !important;
}

.score-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 7px;
    width: 100%;
    margin-bottom: 8px;
}

.score-card {
    min-width: 0;
    min-height: 70px;
    padding: 7px 3px;
    box-sizing: border-box;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 0 3px 9px rgba(50,45,65,0.04);
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

.question-shell {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    margin-top: 2px;
    margin-bottom: 7px;
}

.question-bunny {
    width: 62px;
    flex: 0 0 62px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.question-bunny img {
    width: 62px;
    height: auto;
    display: block;
}

.question-bunny-fallback {
    font-size: 28px;
}

.question-center {
    flex: 1 1 auto;
    min-width: 0;
    text-align: center;
}

.question-label {
    text-align: center;
    color: #707583;
    font-size: 15px;
    font-weight: 700;
    margin: 0 0 3px 0;
}

.review-label {
    text-align: center;
    color: #8c62b0;
    font-size: 12px;
    font-weight: 800;
    margin: 0 0 3px 0;
}

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
    font-size: clamp(54px, 16vw, 78px);
}

.chinese-four {
    font-size: clamp(45px, 13vw, 62px);
}

.chinese-long {
    font-size: clamp(26px, 7.6vw, 40px);
    white-space: nowrap;
    max-width: 100%;
    overflow: hidden;
}

div[data-testid="stButton"] > button {
    width: 100% !important;
    min-height: 60px !important;
    border-radius: 16px !important;
    border: 1.4px solid #e4dfe8 !important;
    background: linear-gradient(90deg, #fffefe, #fffafd) !important;
    margin-bottom: 6px !important;
    box-shadow: 0 2px 7px rgba(45,40,60,0.025) !important;
}

div[data-testid="stButton"] > button p {
    color: #4b5160 !important;
    font-size: 17px !important;
    font-weight: 800 !important;
    line-height: 1.25 !important;
}

.small-note {
    text-align: center;
    color: #958d9e;
    font-size: 11px;
    margin-top: 3px;
    margin-bottom: 3px;
}

hr {
    margin-top: 9px !important;
    margin-bottom: 9px !important;
}

@media (max-width: 480px) {
    .block-container {
        padding-top: 0.25rem !important;
        padding-left: 0.50rem !important;
        padding-right: 0.50rem !important;
    }

    .main-title {
        font-size: clamp(24px, 7vw, 30px);
    }

    .score-card {
        min-height: 65px;
    }

    .score-label {
        font-size: 9px;
    }

    .score-number {
        font-size: 20px;
    }

    .question-bunny {
        width: 56px;
        flex: 0 0 56px;
    }

    .question-bunny img {
        width: 56px;
    }

    .question-label {
        font-size: 14px;
    }

    .chinese-short {
        font-size: clamp(48px, 15vw, 68px);
    }

    .chinese-four {
        font-size: clamp(40px, 12vw, 54px);
    }

    .chinese-long {
        font-size: clamp(24px, 7vw, 36px);
    }

    div[data-testid="stButton"] > button p {
        font-size: 16px !important;
    }
}

.active-category {
    text-align: center;
    color: #707583;
    font-size: 12px;
    font-weight: 700;
    margin: 2px 0 7px 0;
}

.bottom-category-title {
    text-align: center;
    color: #707583;
    font-size: 12px;
    font-weight: 700;
    margin-top: 7px;
    margin-bottom: 4px;
}

div[data-testid="stRadio"] > div {
    justify-content: center !important;
    gap: 0.28rem !important;
    flex-wrap: wrap !important;
}

div[data-testid="stRadio"] label {
    background: linear-gradient(135deg, #f8d8e8, #e6d9ff, #dff4e7);
    border-radius: 999px;
    padding: 5px 9px !important;
    border: 1px solid rgba(170, 160, 185, 0.18);
}

div[data-testid="stRadio"] label p {
    color: #525866 !important;
    font-size: 12px !important;
    font-weight: 800 !important;
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
    4: "AI / LLM / RAG",
    5: "Testing / UAT / Deployment",
}

# =========================================================
# PER-SET PROGRESS
# =========================================================

def blank_progress():
    return {
        "score": 0,
        "total": 0,
        "question_id": None,
        "question_stage": 0,
        "options": [],
        "retry_queue": [],
        "last_question_id": None,
    }

if "selected_set" not in st.session_state:
    st.session_state.selected_set = 1

if "progress_by_set" not in st.session_state:
    st.session_state.progress_by_set = {
        i: blank_progress() for i in range(1, 6)
    }

def get_progress():
    return st.session_state.progress_by_set[st.session_state.selected_set]

def schedule_retry(progress, vocab_id, stage, due_at):
    for item in progress["retry_queue"]:
        if item["vocab_id"] == vocab_id and item["stage"] == stage:
            return
    progress["retry_queue"].append({
        "vocab_id": vocab_id,
        "stage": stage,
        "due_at": due_at
    })

def new_question(progress, vocab):
    current_total = progress["total"]

    due_items = [
        item for item in progress["retry_queue"]
        if item["due_at"] <= current_total
    ]

    if due_items:
        due_items.sort(key=lambda item: item["due_at"])
        retry_item = due_items[0]
        question_id = retry_item["vocab_id"]
        stage = retry_item["stage"]
        progress["retry_queue"].remove(retry_item)
    else:
        blocked_ids = {
            item["vocab_id"] for item in progress["retry_queue"]
        }

        candidates = [
            i for i in range(len(vocab))
            if i not in blocked_ids
        ]

        if (
            progress["last_question_id"] in candidates
            and len(candidates) > 1
        ):
            candidates.remove(progress["last_question_id"])

        if not candidates:
            candidates = list(range(len(vocab)))

        question_id = random.choice(candidates)
        stage = 0

    correct_answer = vocab[question_id][1]

    wrong_pool = list({
        meaning for _, meaning in vocab
        if meaning != correct_answer
    })

    wrong_answers = random.sample(wrong_pool, 2)
    options = [correct_answer, wrong_answers[0], wrong_answers[1]]
    random.shuffle(options)

    progress["question_id"] = question_id
    progress["question_stage"] = stage
    progress["options"] = options
    progress["last_question_id"] = question_id

def chinese_html(word):
    safe_word = html.escape(word)
    length = len(word)

    if length <= 3:
        return f'<div class="chinese-short">{safe_word}</div>'

    if length == 4:
        first_line = html.escape(word[:2])
        second_line = html.escape(word[2:])
        return f'<div class="chinese-four">{first_line}<br>{second_line}</div>'

    return f'<div class="chinese-long">{safe_word}</div>'

def render_question_area(label_html, chinese_word_html):
    if left_bunny_b64:
        left_html = f'<img src="{left_bunny_b64}" alt="left bunny">'
    else:
        left_html = '<div class="question-bunny-fallback">🐰</div>'

    if right_bunny_b64:
        right_html = f'<img src="{right_bunny_b64}" alt="right bunny">'
    else:
        right_html = '<div class="question-bunny-fallback">🐰</div>'

    st.markdown(
        f"""
        <div class="question-shell">
            <div class="question-bunny">{left_html}</div>
            <div class="question-center">
                {label_html}
                {chinese_word_html}
            </div>
            <div class="question-bunny">{right_html}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

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

if progress["question_id"] is None:
    new_question(progress, vocab)

# =========================================================
# SCORE
# =========================================================

if progress["total"] > 0:
    percentage = round((progress["score"] / progress["total"]) * 100)
else:
    percentage = 0

st.markdown(
    f'<div class="active-category">📚 {SET_LABELS[selected_set]} · {len(vocab)} คำ</div>',
    unsafe_allow_html=True
)

score_html = (
    f'<div class="score-grid">'
    f'<div class="score-card score-purple">'
    f'<div class="score-label">✅ Correct</div>'
    f'<div class="score-number">{progress["score"]}</div>'
    f'</div>'
    f'<div class="score-card score-pink">'
    f'<div class="score-label">📝 Answered</div>'
    f'<div class="score-number">{progress["total"]}</div>'
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

question_id = progress["question_id"]
stage = progress["question_stage"]
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

for i, option in enumerate(progress["options"]):
    if st.button(
        f"{letters[i]}. {option}",
        use_container_width=True,
        key=f"answer_{selected_set}_{question_id}_{stage}_{i}"
    ):
        progress["total"] += 1
        is_correct = option == correct_answer

        if is_correct:
            progress["score"] += 1

            if stage == 1:
                schedule_retry(
                    progress=progress,
                    vocab_id=question_id,
                    stage=2,
                    due_at=progress["total"] + 10
                )

            new_question(progress, vocab)
            st.rerun()

        else:
            if stage == 0:
                schedule_retry(
                    progress=progress,
                    vocab_id=question_id,
                    stage=1,
                    due_at=progress["total"] + 5
                )

                st.error(
                    f"❌ คำตอบที่ถูกคือ\n\n"
                    f"### {chinese_word} = {correct_answer}\n\n"
                    f"🌸 จะถามคำนี้ใหม่หลังคำอื่นอีก 5 คำ"
                )

            elif stage == 1:
                schedule_retry(
                    progress=progress,
                    vocab_id=question_id,
                    stage=2,
                    due_at=progress["total"] + 10
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
            new_question(progress, vocab)
            st.rerun()

# =========================================================
# REVIEW STATUS + RESET
# =========================================================

if progress["retry_queue"]:
    st.markdown(
        f'<div class="small-note">🌷 Waiting for review: {len(progress["retry_queue"])}</div>',
        unsafe_allow_html=True
    )

st.divider()

if st.button("↻ Reset ชุดนี้", use_container_width=True):
    st.session_state.progress_by_set[selected_set] = blank_progress()
    st.rerun()

st.markdown(
    '<div class="bottom-category-title">เลือกหมวดคำศัพท์</div>',
    unsafe_allow_html=True
)

category_options = [
    "CBS",
    "System & API",
    "Incident & Ops",
    "AI / LLM",
    "Testing / UAT"
]

current_index = selected_set - 1

selected_label = st.radio(
    "เลือกหมวดคำศัพท์",
    options=category_options,
    index=current_index,
    horizontal=True,
    label_visibility="collapsed",
    key="bottom_set_radio"
)

new_set = category_options.index(selected_label) + 1

if new_set != st.session_state.selected_set:
    st.session_state.selected_set = new_set
    st.rerun()

st.markdown(
    '<div class="small-note">🌸 Made by pollyleadsforward</div>',
    unsafe_allow_html=True
)
