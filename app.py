import streamlit as st
import random
import time
import html

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Chinese Learning App",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================================================
# SETTINGS
# =========================================================

FIRST_PASS_QUESTIONS = 100
REVIEW_QUESTIONS = 50
BASE_SESSION_QUESTIONS = FIRST_PASS_QUESTIONS + REVIEW_QUESTIONS
WRONG_REVIEW_1_AFTER = 5
WRONG_REVIEW_2_AFTER = 10
WRONG_FEEDBACK_SECONDS = 1.35

# =========================================================
# STYLE
# =========================================================

st.markdown(
    """
<style>
:root {
    --text: #3f4657;
    --muted: #777d8d;
    --border: #e3e5ee;
}

[data-testid="stAppViewContainer"] {
    background: #fffefe;
}

.block-container {
    max-width: 620px !important;
    padding-top: 0.35rem !important;
    padding-bottom: 1.1rem !important;
    padding-left: 0.72rem !important;
    padding-right: 0.72rem !important;
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
    font-size: clamp(30px, 8vw, 46px);
    font-weight: 900;
    line-height: 1.06;
    margin: 0 0 2px 0;
    background: linear-gradient(
        90deg,
        #d799f7,
        #9eb9ff,
        #7ed9ed,
        #83e3bd,
        #b9e887,
        #ffd178,
        #f5a4bd
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.by-line {
    text-align: center;
    color: #606675;
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 12px;
}

.active-category {
    text-align: center;
    color: #5f6573;
    font-size: 15px;
    font-weight: 800;
    margin: 0 0 12px 0;
}

.score-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 9px;
    width: 100%;
    margin-bottom: 16px;
}

.score-card {
    min-width: 0;
    min-height: 82px;
    padding: 10px 4px 9px 4px;
    box-sizing: border-box;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 0 4px 13px rgba(45, 45, 70, 0.035);
}

.score-purple {
    background: linear-gradient(135deg, #f1e2ff, #eadfff);
    border: 1.5px solid #d8b5f8;
}

.score-pink {
    background: linear-gradient(135deg, #ffe6ed, #ffdde8);
    border: 1.5px solid #f6b9cf;
}

.score-green {
    background: linear-gradient(135deg, #e6f8eb, #dff5e7);
    border: 1.5px solid #a6dfb5;
}

.score-label {
    color: #565c69;
    font-size: 12px;
    font-weight: 800;
    white-space: nowrap;
    margin-bottom: 5px;
}

.score-number {
    color: #292f3f;
    font-size: 31px;
    line-height: 1;
    font-weight: 900;
}

.question-shell {
    width: 100%;
    text-align: center;
    margin: 3px 0 13px 0;
}

.question-label {
    color: #6d7382;
    font-size: 20px;
    font-weight: 800;
    margin: 0 0 6px 0;
}

.review-label {
    color: #855da8;
    font-size: 14px;
    font-weight: 900;
    margin: 0 0 5px 0;
}

.chinese-short,
.chinese-four,
.chinese-long {
    font-weight: 900;
    line-height: 1.02;
    text-align: center;
    display: inline-block;
    background: linear-gradient(
        90deg,
        #d98ae9,
        #8fa8ff,
        #62c8f3,
        #72dfa9,
        #b8e469,
        #ffd15f,
        #ef8caf
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 3px 7px rgba(130, 120, 180, 0.08));
}

.chinese-short {
    font-size: clamp(82px, 23vw, 124px);
}

.chinese-four {
    font-size: clamp(64px, 18vw, 94px);
}

.chinese-long {
    font-size: clamp(38px, 10vw, 58px);
    white-space: nowrap;
    max-width: 100%;
}

/* Answer buttons */
div[data-testid="stButton"] > button {
    width: 100% !important;
    min-height: 50px !important;
    border-radius: 18px !important;
    border: 1.35px solid #e1e3eb !important;
    background: linear-gradient(90deg, #ffffff, #fffdfd) !important;
    margin-bottom: 5px !important;
    box-shadow: 0 2px 7px rgba(45, 40, 60, 0.025) !important;
}

div[data-testid="stButton"] > button:hover {
    border-color: #d5cce2 !important;
    background: #fffafd !important;
}

div[data-testid="stButton"] > button p {
    color: #3f4657 !important;
    font-size: 17px !important;
    font-weight: 850 !important;
    line-height: 1.16 !important;
}

.small-note {
    text-align: center;
    color: #9297a5;
    font-size: 12px;
    margin-top: 7px;
    margin-bottom: 6px;
}

.finish-box {
    text-align: center;
    padding: 18px 14px;
    margin: 8px 0 14px 0;
    border-radius: 20px;
    border: 1px solid #e6dfef;
    background: linear-gradient(135deg, #fff1f7, #f4efff, #eef8f3);
    color: #525868;
    font-weight: 800;
}

.bottom-divider {
    height: 1px;
    background: #ececf2;
    margin: 13px 0 10px 0;
}

.bottom-category-title {
    text-align: center;
    color: #666c79;
    font-size: 15px;
    font-weight: 900;
    margin: 0 0 7px 0;
}

/* Category pills */
div[data-testid="stRadio"] > div {
    justify-content: center !important;
    gap: 0.38rem !important;
    flex-wrap: wrap !important;
}

div[data-testid="stRadio"] label {
    background: linear-gradient(135deg, #f9e4ef, #e7e3ff, #e3f5eb);
    border-radius: 999px;
    padding: 6px 10px !important;
    border: 1px solid rgba(170, 160, 185, 0.18);
}

div[data-testid="stRadio"] label p {
    color: #515766 !important;
    font-size: 12px !important;
    font-weight: 900 !important;
}

/* Keep radio controls visually compact */
div[data-testid="stRadio"] [data-testid="stMarkdownContainer"] {
    margin: 0 !important;
}

@media (max-width: 480px) {
    .block-container {
        padding-top: 0.28rem !important;
        padding-left: 0.55rem !important;
        padding-right: 0.55rem !important;
    }

    .main-title {
        font-size: clamp(28px, 8vw, 36px);
    }

    .by-line {
        font-size: 13px;
        margin-bottom: 10px;
    }

    .active-category {
        font-size: 13px;
        margin-bottom: 10px;
    }

    .score-grid {
        gap: 7px;
        margin-bottom: 13px;
    }

    .score-card {
        min-height: 72px;
        border-radius: 17px;
        padding: 8px 2px;
    }

    .score-label {
        font-size: 10px;
    }

    .score-number {
        font-size: 25px;
    }

    .question-label {
        font-size: 18px;
    }

    .review-label {
        font-size: 12px;
    }

    .chinese-short {
        font-size: clamp(76px, 24vw, 108px);
    }

    .chinese-four {
        font-size: clamp(58px, 18vw, 82px);
    }

    .chinese-long {
        font-size: clamp(33px, 9.5vw, 48px);
    }

    div[data-testid="stButton"] > button {
        min-height: 47px !important;
        border-radius: 16px !important;
        margin-bottom: 4px !important;
    }

    div[data-testid="stButton"] > button p {
        font-size: 16px !important;
    }

    .bottom-category-title {
        font-size: 14px;
    }

    div[data-testid="stRadio"] label {
        padding: 5px 8px !important;
    }

    div[data-testid="stRadio"] label p {
        font-size: 11px !important;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

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
    ('标准', 'Standard'),
]

VOCAB_SET_2 = [
    ('这个', 'this'), ('需求', 'Requirement'), ('是', 'be, is'), ('什么', 'what'),
    ('业务', 'Business'), ('部门', 'department'), ('想', 'want, think'), ('解决', 'Resolve'),
    ('问题', 'Issue'), ('项目', 'Project'), ('的', 'possessive particle'), ('范围', 'Scope'),
    ('我们', 'we'), ('需要', 'need'), ('先', 'first, beforehand'), ('确认', 'Confirm'),
    ('产品', 'Product'), ('目标', 'Goal'), ('前端', 'Frontend'), ('还是', 'or'),
    ('后端', 'Backend'), ('显示', 'display'), ('数据', 'Data'), ('不', 'not'),
    ('正确', 'correct'), ('返回', 'Return'), ('了', 'completed-change particle'), ('发生', 'Occur'),
    ('在', 'at, in'), ('哪', 'which'), ('一', 'one'), ('层', 'layer'),
    ('用户', 'User'), ('点击', 'click'), ('按钮', 'button'), ('后', 'after'),
    ('没有', 'not have'), ('响应', 'Response'), ('怎么', 'how'), ('调用', 'call, invoke'),
    ('请求', 'Request'), ('传', 'pass, transmit'), ('哪些', 'which ones'), ('参数', 'Parameter'),
    ('使用', 'use'), ('令牌', 'Token'), ('错误', 'Error'), ('时', 'when'),
    ('系统', 'System'), ('码', 'code'), ('来自', 'come from'), ('哪个', 'which'),
    ('数据库', 'Database'), ('主要', 'main, primary'), ('数据源', 'Data Source'), ('请', 'please'),
    ('检查', 'check, inspect'), ('里', 'inside'), ('字段', 'Field'), ('可以', 'can'),
    ('为', 'be, become'), ('空', 'empty, null'), ('吗', 'question particle'), ('两', 'two'),
    ('个', 'general measure word'), ('一致', 'consistent'), ('给', 'give, for'), ('我', 'I'),
    ('解释', 'explain'), ('一下', 'a bit'), ('架构', 'Architecture'), ('从', 'from'),
    ('到', 'to'), ('连接', 'Connect'), ('步骤', 'step'), ('同步', 'Synchronous'),
    ('异步', 'Asynchronous'), ('如果', 'if'), ('可用', 'available'), ('有', 'have'),
    ('备用', 'backup, standby'), ('方案', 'plan, solution'), ('现在', 'now'), ('环境', 'Environment'),
    ('版本', 'Version'), ('时候', 'time, when'), ('上线', 'Go-live'), ('流水线', 'Pipeline'),
    ('失败', 'fail'), ('出现', 'appear, occur'), ('回滚', 'Rollback'), ('进行', 'carry out, proceed'),
    ('金丝雀', 'canary'), ('发布', 'Release'), ('提供', 'provide'), ('日志', 'Log'),
    ('根本', 'fundamental, root'), ('原因', 'reason, cause'), ('影响', 'Impact'), ('多少', 'how much, how many'),
]

VOCAB_SET_3 = [
    ('客户', 'customer'), ('时间', 'time'), ('明显', 'obvious, significant'), ('增加', 'increase'),
    ('事故', 'Incident'), ('做', 'do'), ('复盘', 'Postmortem'), ('衡量', 'measure'),
    ('结果', 'Outcome'), ('而', 'while, but'), ('仅仅', 'merely, only'), ('产出', 'output'),
    ('风险', 'Risk'), ('最', 'most'), ('大', 'big'), ('假设', 'Assumption'),
    ('谁', 'who'), ('验证', 'Validate'), ('还', 'still, also'), ('够', 'enough'),
    ('明确', 'Clarify'), ('非', 'non-'), ('功能性', 'functional'), ('必须', 'must'),
    ('超过', 'exceed'), ('秒', 'second'), ('这', 'this'), ('种', 'kind, type'),
    ('异常', 'Exception'), ('情况', 'situation'), ('下', 'under, below'), ('应该', 'should'),
    ('处理', 'Handle'), ('验收', 'Acceptance'), ('标准', 'standard'), ('必填', 'Mandatory'),
    ('可选', 'Optional'), ('变更', 'Change'), ('向后', 'backward'), ('兼容', 'Compatible'),
    ('补充', 'supplement, add'), ('场景', 'Scenario'), ('任务', 'task'), ('完成', 'Complete'),
    ('测试', 'Testing'), ('发现', 'discover, find'), ('缺陷', 'Defect'), ('会', 'will, can'),
    ('回归', 'Regression'), ('性能', 'Performance'), ('怎么样', 'how is it'), ('个人', 'personal'),
    ('信息', 'information'), ('依赖', 'Dependency'), ('开发', 'Development'), ('大概', 'approximately'),
    ('多', 'many, much'), ('长', 'long'), ('缩小', 'reduce, shrink'), ('技术', 'technology, technical'),
    ('债', 'debt'), ('接受', 'accept'), ('这些', 'these'), ('包含', 'contain, include'),
    ('权限', 'Permission'), ('访问', 'access'), ('是否', 'whether'), ('已经', 'already'),
    ('加密', 'Encryption'), ('记录', 'record'), ('审计', 'Audit'), ('服务', 'Service'),
    ('账号', 'account'), ('部署', 'Deployment'), ('计划', 'plan'), ('迁移', 'Migration'),
    ('核对', 'Reconciliation'), ('要', 'need to, will'), ('监控', 'Monitoring'), ('指标', 'Metric'),
    ('今晚', 'tonight'), ('生产', 'production'), ('机器', 'machine'), ('学习', 'learn, learning'),
    ('语言', 'language'), ('模型', 'Model'), ('应用', 'application'), ('所有', 'all'),
    ('都', 'all'), ('人工', 'manual, human'), ('智能', 'intelligence'), ('只是', 'only, merely'),
    ('部分', 'part'), ('输出', 'Output'), ('存在', 'exist'), ('确定性', 'certainty'),
    ('定义', 'define'), ('容忍度', 'tolerance'), ('训练', 'Training'), ('推理', 'Inference'),
]

VOCAB_SET_4 = [
    ('目前', 'Currently'), ('延迟', 'Delay'), ('支持', 'support'), ('每', 'every'),
    ('温度', 'temperature'), ('设置', 'set, configure'), ('上下文', 'Context'), ('太', 'too'),
    ('用', 'use'), ('格式', 'Format'), ('防止', 'prevent'), ('提示词', 'Prompt'),
    ('注入', 'Injection'), ('嵌入', 'Embedding'), ('切分', 'split, chunk'), ('文档', 'document'),
    ('元数据', 'Metadata'), ('过滤', 'Filter'), ('条件', 'condition'), ('检索', 'Retrieval'),
    ('相关', 'relevant, related'), ('混合', 'hybrid, mixed'), ('文件', 'Document'), ('知识库', 'Knowledge Base'),
    ('和', 'and'), ('答案', 'answer'), ('引用', 'Citation'), ('来源', 'source'),
    ('索引', 'Index'), ('最后', 'last, final'), ('更新', 'update'), ('微调', 'Fine-tuning'),
    ('对', 'toward, to'), ('基准', 'benchmark, baseline'), ('成本', 'Cost'), ('更', 'more'),
    ('高', 'high'), ('经常', 'often'), ('变化', 'change'), ('所以', 'therefore'),
    ('适合', 'suitable'), ('评估', 'Evaluation'), ('供应商', 'Vendor / Supplier'), ('锁定', 'Lock-in'),
    ('回答', 'answer'), ('准确', 'accurate'), ('质量', 'Quality'), ('依据', 'Evidence'),
    ('幻觉', 'Hallucination'), ('率', 'rate'), ('低于', 'below'), ('百分之', 'percent'),
    ('二', 'two'), ('不足', 'insufficient'), ('拒绝', 'Refuse'), ('能', 'can'),
    ('带来', 'bring'), ('价值', 'Value'), ('审核', 'review, audit'), ('辅助', 'Assist'),
    ('模式', 'mode'), ('开始', 'Start'), ('采用', 'adopt'), ('护栏', 'Guardrail'),
    ('端到', 'end-to-'), ('端', 'end'), ('工具', 'Tool'), ('通过', 'pass, through'),
    ('敏感', 'Sensitive'), ('发送', 'send'), ('外部', 'external'), ('高峰期', 'peak period'),
    ('并发', 'Concurrent'), ('降低', 'reduce'), ('使用量', 'usage'), ('缓存', 'Cache'),
    ('新鲜度', 'freshness'), ('次', 'occurrence, time'), ('实验', 'Experiment'), ('新', 'new'),
    ('影子', 'shadow'), ('平台', 'Platform'), ('人员', 'personnel'), ('提高', 'improve, increase'),
    ('自助', 'self-service'), ('能力', 'capability'), ('才', 'only then'), ('模板', 'Template'),
    ('团队', 'team'), ('独立', 'independent'), ('配额', 'Quota'), ('北极星', 'North Star'),
    ('试点', 'Pilot'), ('将', 'will'), ('一百', 'one hundred'), ('名', 'measure word for people'),
    ('显著', 'Significant'), ('负面', 'negative'), ('反馈', 'Feedback'), ('等级', 'level, grade'),
]

VOCAB_SET_5 = [
    ('暂时', 'temporarily'), ('关闭', 'close, disable'), ('功能', 'Function'), ('有关', 'related'),
    ('负责人', 'Responsible person'), ('整改', 'corrective rectification'), ('措施', 'measure, action'), ('今天', 'today'),
    ('决定', 'Decision'), ('三', 'three'), ('件', 'measure word'), ('事', 'matter, thing'),
    ('说明', 'explain'), ('当前', 'current'), ('行为', 'behavior'), ('预期', 'Expected'),
    ('重现', 'Reproduce'), ('替代', 'replace, alternative'), ('提前', 'ahead of time'), ('多久', 'how long'),
    ('交付', 'Delivery'), ('负责', 'be responsible'), ('行动', 'action'), ('项', 'item'),
    ('日期', 'date'), ('明天', 'tomorrow'), ('再', 'again'), ('跟进', 'Follow up'),
    ('选择', 'choose'), ('因为', 'because'), ('核心', 'core'), ('前', 'before, front'),
    ('安全', 'Security'), ('审查', 'review'), ('接口', 'Interface'), ('错误码', 'Error code'),
    ('查询', 'Query'), ('一致性', 'Consistency'), ('根本原因', 'Root Cause'), ('非功能性需求', 'NFR'),
    ('测试数据', 'Test Data'), ('技术债', 'Technical debt'), ('敏感数据', 'Sensitive data'), ('人工智能', 'Artificial'),
    ('机器学习', 'Machine Learning'), ('不确定性', 'Uncertainty'), ('吞吐量', 'Throughput'), ('温度参数', 'Temperature'),
    ('向量', 'Vector'), ('检索增强生成', 'RAG'), ('基准测试', 'Benchmark'), ('准确率', 'Accuracy'),
    ('人工审核', 'Human-in-the-loop'), ('采用率', 'Adoption'), ('端到端', 'End-to-end'), ('高峰', 'Peak'),
    ('模型版本', 'Model Version'), ('影子测试', 'Shadow test'), ('生命周期', 'Lifecycle'), ('开发人员', 'Developer'),
    ('自助服务', 'Self-service'), ('整改措施', 'Corrective action'), ('替代方案', 'Alternative'), ('核心指标', 'Core metric'),
    ('安全审查', 'Security review'), ('数据表', 'Table'), ('队列', 'Queue'), ('网络', 'Network'),
    ('告警', 'Alert'), ('可用性', 'Availability'), ('可扩展性', 'Scalability'), ('业务需求', 'Business Requirement'),
    ('需求变更', 'Requirement Change'), ('优先级', 'Priority'), ('业务流程', 'Business Process'), ('业务逻辑', 'Business Logic'),
    ('使用场景', 'Use Case'), ('验收标准', 'Acceptance Criteria'), ('代码', 'Code'), ('逻辑', 'Logic'),
    ('修改', 'Modify'), ('系统架构', 'System Architecture'), ('微服务', 'Microservice'), ('组件', 'Component'),
    ('配置', 'Configuration'), ('调用接口', 'Call'), ('传参数', 'Pass Parameter'), ('集成', 'Integration'),
    ('传输数据', 'Data Transmission'), ('超时', 'Timeout'), ('网关', 'API Gateway'), ('端点', 'Endpoint'),
    ('身份验证', 'Authentication'), ('授权', 'Authorization'), ('源数据', 'Source Data'), ('映射', 'Mapping'),
    ('数据不一致', 'Data Mismatch'), ('数据一致性', 'Data'), ('数据迁移', 'Data Migration'), ('数据验证', 'Data Validation'),
    ('测试用例', 'Test Case'), ('集成测试', 'Integration Test'), ('验收测试', 'UAT'), ('回归测试', 'Regression Test'),
    ('性能测试', 'Performance Test'), ('通过测试', 'Pass Testing'), ('测试未通过', 'Fail Testing'), ('开发环境', 'Development Environment'),
    ('测试环境', 'Test Environment'), ('生产环境', 'Production Environment'), ('下线', 'Take Offline'), ('部署计划', 'Deployment Plan'),
    ('发布窗口', 'Release'), ('错误日志', 'Error Log'), ('恢复', 'Recover'), ('临时解决方案', 'Workaround'),
    ('预防措施', 'Preventive Action'), ('已完成', 'Completed'), ('进行中', 'In Progress'), ('尚未开始', 'Not Started'),
    ('等待', 'Waiting'), ('阻塞', 'Blocked'), ('延期', 'Postpone'), ('预计', 'Estimate'),
    ('进度', 'Progress'), ('截止日期', 'Deadline'), ('访问权限', 'Access Permission'), ('个人数据', 'Personal Data'),
    ('云服务', 'Cloud'), ('服务器', 'Server'), ('持续集成和持续交付', 'CI/CD'), ('代码仓库', 'Git Repository'),
    ('扩展', 'Scale'), ('大语言模型', 'LLM'), ('向量嵌入', 'Embedding'), ('向量数据库', 'Vector Database'),
    ('模型监控', 'Model Monitoring'), ('隐私', 'Privacy'), ('单次请求成本', 'Cost per Request'),
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

CATEGORY_TO_SET = {
    "System & API": 2,
    "CBS": 1,
    "Incident & Ops": 3,
    "AI / LLM": 4,
    "Testing / UAT": 5,
}

CATEGORY_OPTIONS = [
    "System & API",
    "CBS",
    "Incident & Ops",
    "AI / LLM",
    "Testing / UAT",
]

SET_TO_CATEGORY = {value: key for key, value in CATEGORY_TO_SET.items()}

# =========================================================
# QUIZ STATE
# =========================================================

def build_first_pass(vocab):
    ids = list(range(len(vocab)))
    random.shuffle(ids)

    # User's agreed structure is 100 non-repeating base questions first.
    # If a set contains fewer than 100 entries, use every entry once.
    return ids[: min(FIRST_PASS_QUESTIONS, len(ids))]


def blank_progress(vocab):
    return {
        "score": 0,
        "total": 0,                 # includes extra wrong-answer reviews
        "base_count": 0,            # 150-question base session only
        "first_pass_order": build_first_pass(vocab),
        "first_pass_index": 0,
        "question_id": None,
        "question_stage": 0,        # 0=base, 1=review 1, 2=review 2
        "options": [],
        "retry_queue": [],
        "wrong_ever": [],
        "last_question_id": None,
        "finished": False,
    }


def ensure_state():
    if "selected_set" not in st.session_state:
        st.session_state.selected_set = 1

    if "progress_by_set" not in st.session_state:
        st.session_state.progress_by_set = {
            set_id: blank_progress(vocab)
            for set_id, vocab in VOCAB_SETS.items()
        }


ensure_state()


def get_progress():
    return st.session_state.progress_by_set[st.session_state.selected_set]


def schedule_retry(progress, vocab_id, stage, due_at):
    for item in progress["retry_queue"]:
        if item["vocab_id"] == vocab_id and item["stage"] == stage:
            return

    progress["retry_queue"].append({
        "vocab_id": vocab_id,
        "stage": stage,
        "due_at": due_at,
    })


def choose_final_review_word(progress, vocab):
    # Final 50 base questions prioritize words missed earlier.
    if progress["wrong_ever"]:
        pool = list(dict.fromkeys(progress["wrong_ever"]))
    else:
        pool = list(range(len(vocab)))

    if progress["last_question_id"] in pool and len(pool) > 1:
        pool = [i for i in pool if i != progress["last_question_id"]]

    return random.choice(pool)


def choose_next_base_question(progress, vocab):
    # First pass: up to 100 unique words, no repeats.
    if progress["base_count"] < FIRST_PASS_QUESTIONS:
        if progress["first_pass_index"] < len(progress["first_pass_order"]):
            question_id = progress["first_pass_order"][progress["first_pass_index"]]
            progress["first_pass_index"] += 1
            return question_id

        # Fallback only for categories containing fewer than 100 words.
        return choose_final_review_word(progress, vocab)

    # Final 50: review/repeat, prioritizing words answered wrong.
    return choose_final_review_word(progress, vocab)


def make_options(vocab, question_id):
    correct_answer = vocab[question_id][1]
    wrong_pool = list({
        meaning for _, meaning in vocab
        if meaning != correct_answer
    })

    wrong_answers = random.sample(wrong_pool, 2)
    options = [correct_answer, *wrong_answers]
    random.shuffle(options)
    return options


def new_question(progress, vocab):
    if progress["finished"]:
        return

    current_total = progress["total"]

    due_items = [
        item for item in progress["retry_queue"]
        if item["due_at"] <= current_total
    ]

    if due_items:
        due_items.sort(key=lambda item: item["due_at"])
        retry_item = due_items[0]
        progress["retry_queue"].remove(retry_item)
        question_id = retry_item["vocab_id"]
        stage = retry_item["stage"]

    elif progress["base_count"] < BASE_SESSION_QUESTIONS:
        question_id = choose_next_base_question(progress, vocab)
        stage = 0
        progress["base_count"] += 1

    elif progress["retry_queue"]:
        # Base 150 is done. Finish any remaining scheduled reviews.
        progress["retry_queue"].sort(key=lambda item: item["due_at"])
        retry_item = progress["retry_queue"].pop(0)
        question_id = retry_item["vocab_id"]
        stage = retry_item["stage"]

    else:
        progress["question_id"] = None
        progress["question_stage"] = 0
        progress["options"] = []
        progress["finished"] = True
        return

    progress["question_id"] = question_id
    progress["question_stage"] = stage
    progress["options"] = make_options(vocab, question_id)
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
    st.markdown(
        f"""
        <div class="question-shell">
            {label_html}
            {chinese_word_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# HEADER
# =========================================================

st.markdown('<div class="main-title">Chinese Learning App</div>', unsafe_allow_html=True)
st.markdown('<div class="by-line">by pollyleadsforward</div>', unsafe_allow_html=True)

selected_set = st.session_state.selected_set
vocab = VOCAB_SETS[selected_set]
progress = get_progress()

if progress["question_id"] is None and not progress["finished"]:
    new_question(progress, vocab)

# No "100 คำ" / vocabulary count is displayed anywhere.
st.markdown(
    f'<div class="active-category">📚 {SET_LABELS[selected_set]}</div>',
    unsafe_allow_html=True,
)

# =========================================================
# SCORE
# =========================================================

percentage = round((progress["score"] / progress["total"]) * 100) if progress["total"] else 0

st.markdown(
    f"""
    <div class="score-grid">
        <div class="score-card score-purple">
            <div class="score-label">✅ Correct</div>
            <div class="score-number">{progress['score']}</div>
        </div>
        <div class="score-card score-pink">
            <div class="score-label">📝 Answered</div>
            <div class="score-number">{progress['total']}</div>
        </div>
        <div class="score-card score-green">
            <div class="score-label">🎯 Score</div>
            <div class="score-number">{percentage}%</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# QUESTION + ANSWERS
# =========================================================

if progress["finished"]:
    st.markdown(
        '<div class="finish-box">🌷 จบ session นี้แล้ว<br>ครบ 150 ข้อหลัก + คำทบทวนที่ตอบผิดแล้ว</div>',
        unsafe_allow_html=True,
    )
else:
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
        chinese_word_html=chinese_html(chinese_word),
    )

    letters = ["A", "B", "C"]

    for i, option in enumerate(progress["options"]):
        if st.button(
            f"{letters[i]}. {option}",
            use_container_width=True,
            key=f"answer_{selected_set}_{question_id}_{stage}_{progress['total']}_{i}",
        ):
            progress["total"] += 1
            is_correct = option == correct_answer

            if is_correct:
                progress["score"] += 1

                # Review 1 always gets one final review after 10 more answers.
                if stage == 1:
                    schedule_retry(
                        progress=progress,
                        vocab_id=question_id,
                        stage=2,
                        due_at=progress["total"] + WRONG_REVIEW_2_AFTER,
                    )

                new_question(progress, vocab)
                st.rerun()

            else:
                if question_id not in progress["wrong_ever"]:
                    progress["wrong_ever"].append(question_id)

                if stage == 0:
                    schedule_retry(
                        progress=progress,
                        vocab_id=question_id,
                        stage=1,
                        due_at=progress["total"] + WRONG_REVIEW_1_AFTER,
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
                        due_at=progress["total"] + WRONG_REVIEW_2_AFTER,
                    )
                    st.error(
                        f"❌ คำตอบที่ถูกคือ\n\n"
                        f"### {chinese_word} = {correct_answer}\n\n"
                        f"🌷 จะถามคำนี้ใหม่หลังคำอื่นอีก 10 คำ"
                    )

                else:
                    # Review 2 ends here. No infinite loop.
                    st.error(
                        f"❌ คำตอบที่ถูกคือ\n\n"
                        f"### {chinese_word} = {correct_answer}"
                    )

                time.sleep(WRONG_FEEDBACK_SECONDS)
                new_question(progress, vocab)
                st.rerun()

if progress["retry_queue"]:
    st.markdown(
        f'<div class="small-note">🌷 Waiting for review: {len(progress["retry_queue"])}</div>',
        unsafe_allow_html=True,
    )

# =========================================================
# CATEGORY SELECTOR — CBS IN THE MIDDLE
# =========================================================

st.markdown('<div class="bottom-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="bottom-category-title">เลือกหมวดคำศัพท์</div>', unsafe_allow_html=True)

current_category = SET_TO_CATEGORY[selected_set]
selected_label = st.radio(
    "เลือกหมวดคำศัพท์",
    options=CATEGORY_OPTIONS,
    index=CATEGORY_OPTIONS.index(current_category),
    horizontal=True,
    label_visibility="collapsed",
    key="bottom_set_radio",
)

new_set = CATEGORY_TO_SET[selected_label]
if new_set != st.session_state.selected_set:
    st.session_state.selected_set = new_set
    st.rerun()

# =========================================================
# SMALL RESET BUTTON AT THE VERY BOTTOM
# =========================================================

reset_left, reset_mid, reset_right = st.columns([1.7, 1.0, 1.7])
with reset_mid:
    if st.button("↻ Reset", key="reset_current_set", use_container_width=True):
        st.session_state.progress_by_set[selected_set] = blank_progress(vocab)
        st.rerun()
