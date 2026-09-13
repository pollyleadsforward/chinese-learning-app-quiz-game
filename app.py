import html
import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Product Management Prep",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# =========================================================
# QUESTION BANK — 36 QUESTIONS, FIXED ORDER, NO RANDOM
# =========================================================
QUESTIONS = [
    {
        "id": 1,
        "category": "Product Strategy & Management",
        "question": "ถ้าให้คุณวาง Strategy สำหรับ Personal Loan คุณจะเริ่มจากอะไร?",
        "answer": "ฉันจะเริ่มจาก 5 เรื่องค่ะ: Target Customer, Customer Need, Risk, Value Proposition และ Economics แล้วจึงออกแบบ product, pricing, channel และ process ให้สอดคล้องกัน ไม่เริ่มจากคำถามว่า ‘เราจะขายอะไร’ แต่เริ่มจาก ‘ลูกค้ากลุ่มไหนมี unmet need ที่เราสามารถให้บริการได้อย่าง profitable และ sustainable’",
    },
    {
        "id": 2,
        "category": "Product Strategy & Management",
        "question": "คุณจะรู้ได้อย่างไรว่าลูกค้าต้องการอะไร?",
        "answer": "ดูทั้ง customer data และ customer voice ค่ะ เช่น application funnel, drop-off, approval/rejection reason, complaints, usage behavior รวมถึง qualitative research แล้วเอาข้อมูลมาหา pain point ก่อนพัฒนา product",
    },
    {
        "id": 3,
        "category": "Product Strategy & Management",
        "question": "ถ้ามีหลาย Customer Segment จะเลือกกลุ่มไหนก่อน?",
        "answer": "ฉันจะดู 4 มิติ ได้แก่ Market attractiveness, Customer need, Risk profile และ Bank capability กลุ่มที่มี need ชัด มี market size เพียงพอ risk สามารถบริหารได้ และธนาคารมี data/capability รองรับ จะเป็นกลุ่มที่ควร prioritize ก่อน",
    },
    {
        "id": 4,
        "category": "Product Strategy & Management",
        "question": "Personal Loan ที่ดีควรแข่งขันด้วยอะไร นอกจากดอกเบี้ย?",
        "answer": "แข่งขันได้หลายเรื่องค่ะ เช่น approval speed, ease of application, transparency, flexible repayment, relevant credit limit และ customer experience ถ้าแข่งขันด้วยราคาอย่างเดียวจะเข้าสู่ price war ได้ง่าย",
    },
    {
        "id": 5,
        "category": "Product Strategy & Management",
        "question": "คุณจะออกแบบ Pricing อย่างไร?",
        "answer": "ฉันมองเป็น risk-based pricing ค่ะ ต้อง balance customer affordability, expected loss, cost, acquisition expense และ target return ลูกค้าที่มีข้อมูลและความเสี่ยงต่างกันไม่จำเป็นต้องได้ราคาเดียวกัน",
    },
    {
        "id": 6,
        "category": "Product Strategy & Management",
        "question": "ถ้าจะทำสินเชื่อให้ Self-employed คุณจะออกแบบอย่างไร?",
        "answer": "ฉันจะไม่มอง Self-employed เป็นกลุ่มเดียว แต่แบ่งตาม quality of evidence เช่น มีทะเบียนหรือข้อมูลธุรกิจชัด มี transaction data เช่น QR/EDC หรือมีเพียง financial behavior จากบัญชี จากนั้นกำหนด eligibility, limit และ pricing ตามระดับความเชื่อมั่นของข้อมูล",
    },
    {
        "id": 7,
        "category": "Product Strategy & Management",
        "question": "Product Strategy กับ Credit Policy ต่างกันอย่างไร?",
        "answer": "Product Strategy ตอบว่าจะให้ใคร อะไร ด้วย value proposition แบบไหน และทำไมถึงน่าสนใจเชิงธุรกิจ ส่วน Credit Policy กำหนดว่า risk แบบไหนที่ธนาคารยอมรับ และเงื่อนไขอนุมัติเป็นอย่างไร สองเรื่องต้องออกแบบร่วมกัน",
    },
    {
        "id": 8,
        "category": "Product Strategy & Management",
        "question": "คุณตั้ง KPI ของ Personal Loan อย่างไร?",
        "answer": "ฉันจะไม่ดูแค่ยอดขาย แต่ดูครบทั้ง Growth + Customer + Risk + Economics + Operations เช่น application, approval, booking/disbursement, conversion, revenue, risk-adjusted return, delinquency/NPL, complaint และ SLA",
    },
    {
        "id": 9,
        "category": "Product Strategy & Management",
        "question": "ถ้ายอด Loan Booking โตมาก คุณถือว่าประสบความสำเร็จหรือยัง?",
        "answer": "ยังค่ะ Growth อย่างเดียวไม่พอ ต้องดู portfolio quality และ profitability ด้วย ถ้า booking โตแต่ NPL, complaint หรือ acquisition cost โตเร็วกว่า แปลว่า growth นั้นอาจไม่ sustainable",
    },
    {
        "id": 10,
        "category": "Product Strategy & Management",
        "question": "Continuous Improvement ทำอย่างไร?",
        "answer": "ฉันจะสร้าง feedback loop จาก production data → identify pain point → hypothesis → improvement → test → measure และทำต่อเนื่อง ไม่รอให้มี major project ถึงจะปรับ product",
    },
    {
        "id": 11,
        "category": "Production Quality",
        "question": "‘Ensuring quality in production’ ใน JD คุณตีความว่าอะไร?",
        "answer": "ไม่ใช่แค่ระบบไม่ล่มค่ะ แต่หมายถึงลูกค้าต้องได้รับผลลัพธ์ที่ถูกต้องตั้งแต่ application → decision → documentation → disbursement → servicing รวมถึง data accuracy, SLA, compliance และ customer communication",
    },
    {
        "id": 12,
        "category": "Production Quality",
        "question": "หลัง Go-live คุณดูอะไรเป็นอันดับแรก?",
        "answer": "ฉันจะดู critical funnel เช่น application success, approval result, disbursement success, error rate, exception, customer complaint และ reconciliation เทียบกับ baseline และ expected result",
    },
    {
        "id": 13,
        "category": "Production Quality",
        "question": "ถ้ามี Incident หลัง Go-live คุณจะทำอย่างไร?",
        "answer": "อันดับแรกคือ protect customer และ contain impact จากนั้นระบุ scope, workaround, owner และ SLA แล้วค่อยทำ root cause และ permanent fix หลังเหตุการณ์ต้องมี preventive action เพื่อไม่ให้เกิดซ้ำ",
    },
    {
        "id": 14,
        "category": "Production Quality",
        "question": "คุณแยก Major Incident กับ Minor Issue อย่างไร?",
        "answer": "ดูจาก customer impact, financial impact, regulatory risk, number of customers และ business continuity ไม่ใช่ดูจากความยากของ technical issue อย่างเดียว",
    },
    {
        "id": 15,
        "category": "Production Quality",
        "question": "ถ้า System Issue กระทบลูกค้าแค่ 1 คน ยังต้อง investigate ไหม?",
        "answer": "ต้องค่ะ เพราะต้องตอบให้ได้ว่าเป็น isolated case หรือ systemic logic issue ถ้าเป็น logic issue แม้วันนี้เจอคนเดียวก็อาจกระทบลูกค้ารายอื่นในอนาคต",
    },
    {
        "id": 16,
        "category": "Production Quality",
        "question": "Product Owner ต้องรู้ Technical แค่ไหน?",
        "answer": "ไม่จำเป็นต้องเขียนระบบเอง แต่ต้องเข้าใจ end-to-end flow, data, integration, business rule และ failure point มากพอที่จะตั้งคำถามกับ Technology และประเมิน customer/business impact ได้",
    },
    {
        "id": 17,
        "category": "Customer Behavior & Regulation",
        "question": "คุณจะติดตามการเปลี่ยนแปลงของ Customer Behavior อย่างไร?",
        "answer": "ดูทั้ง application behavior, channel usage, transaction pattern, repayment behavior, complaints และ research แล้วดูว่าการเปลี่ยนแปลงนั้นมีผลต่อ product proposition หรือ risk อย่างไร",
    },
    {
        "id": 18,
        "category": "Customer Behavior & Regulation",
        "question": "ถ้าพฤติกรรมลูกค้าเปลี่ยน คุณจะรู้ได้อย่างไรว่าต้องแก้ Product?",
        "answer": "ต้องดูว่า change นั้นเป็น temporary noise หรือ structural change ถ้าเกิดต่อเนื่องและกระทบ conversion, profitability, risk หรือ customer satisfaction จึงควรพิจารณา product redesign",
    },
    {
        "id": 19,
        "category": "Customer Behavior & Regulation",
        "question": "ถ้ามีกฎใหม่ออกมา คุณจัดการอย่างไร?",
        "answer": "ฉันจะทำ impact assessment ก่อนว่า policy, process, system, communication และ existing customer มีอะไรได้รับผลกระทบ จากนั้นทำงานกับ Compliance, Legal, Risk, Operations และ IT เพื่อแปลง regulation เป็น business requirement และ implementation plan",
    },
    {
        "id": 20,
        "category": "Customer Behavior & Regulation",
        "question": "Product กับ Compliance ควรทำงานกันแบบไหน?",
        "answer": "Compliance ไม่ควรเข้ามาเฉพาะตอนท้ายค่ะ ฉันชอบ involve ตั้งแต่ช่วง design เพื่อให้ requirement ถูกตั้งแต่ต้น ลด rework และทำให้ทีมเข้าใจด้วยว่า regulation ต้องการควบคุม risk อะไร",
    },
    {
        "id": 21,
        "category": "Customer Behavior & Regulation",
        "question": "ถ้า Business อยาก Launch แต่ Compliance ยังมี Concern คุณจะทำอย่างไร?",
        "answer": "ฉันจะไม่มองว่าเป็น Business vs Compliance แต่จะ clarify specific risk และ requirement ก่อน แล้วดูว่ามี mitigation หรือ scope adjustment ที่ทำให้ launch ได้อย่าง compliant หรือไม่ ถ้ายังมี material risk ก็ไม่ควรฝืน Go",
    },
    {
        "id": 22,
        "category": "Customer Behavior & Regulation",
        "question": "ถ้ากฎทำให้ Conversion ลดลง คุณจะทำอย่างไร?",
        "answer": "Compliance requirement เป็น constraint ที่ต้องรักษา แต่เรายัง optimize customer journey, wording, data collection และ process ได้ เป้าหมายคือรักษากฎโดยลด unnecessary friction",
    },
    {
        "id": 23,
        "category": "Customer Behavior & Regulation",
        "question": "คุณจะป้องกัน Product Requirement ผิดจาก Regulation ได้อย่างไร?",
        "answer": "ต้องมี traceability ตั้งแต่ regulation → policy interpretation → requirement → test case → production control เพื่อให้ทุกทีมรู้ว่าแต่ละ requirement มาจากอะไร",
    },
    {
        "id": 24,
        "category": "Market & Competitor",
        "question": "เวลา Analyze Competitor คุณดูอะไร?",
        "answer": "ไม่ดูแค่ interest rate ค่ะ ฉันจะดู target segment, eligibility, credit limit, pricing, tenor, application journey, approval speed, channel, campaign และ value proposition",
    },
    {
        "id": 25,
        "category": "Market & Competitor",
        "question": "ถ้าคู่แข่งลดดอกเบี้ยแรง คุณจะลดตามไหม?",
        "answer": "ไม่จำเป็นค่ะ ต้องรู้ก่อนว่าเขากำลัง target ลูกค้ากลุ่มไหน และ economics ของเรารองรับหรือไม่ บางครั้งการตอบด้วย better experience, targeted pricing หรือ differentiated segment มีเหตุผลกว่าการลดราคาทั้ง portfolio",
    },
    {
        "id": 26,
        "category": "Market & Competitor",
        "question": "คุณหา Opportunity จาก Market Trend อย่างไร?",
        "answer": "มองหาจุดที่มี customer need เพิ่มขึ้น แต่ existing solution ยังตอบไม่ดี แล้วประเมินร่วมกับ bank capability, data advantage และ risk appetite",
    },
    {
        "id": 27,
        "category": "Market & Competitor",
        "question": "แล้วหา Risk จาก Market Trend อย่างไร?",
        "answer": "ดูทั้ง credit deterioration, aggressive competition, customer indebtedness, fraud pattern, regulatory direction และ cost of acquisition เพราะบาง market growth อาจดู attractive แต่มี risk ซ่อนอยู่",
    },
    {
        "id": 28,
        "category": "Market & Competitor",
        "question": "Competitor ทำ Feature ใหม่ เราควรทำตามไหม?",
        "answer": "ไม่ควร copy โดยอัตโนมัติ ต้องถามว่า customer problem คืออะไร และ feature นั้นสร้าง value จริงหรือไม่ ถ้าเหมาะกับลูกค้าและ strategy ของเรา จึงค่อยนำมาปรับใช้",
    },
    {
        "id": 29,
        "category": "Product Testing & PMF",
        "question": "PMF ใน Personal Loan คืออะไร?",
        "answer": "สำหรับ Lending ฉันมองว่า PMF ไม่ใช่แค่มีคนสมัครเยอะ แต่คือ ลูกค้าเห็น value, ใช้ product จริง และ portfolio สร้าง economics ที่ดีภายใต้ acceptable risk ต้องมีทั้ง customer fit และ business fit",
    },
    {
        "id": 30,
        "category": "Product Testing & PMF",
        "question": "จะวัด PMF ด้วยอะไร?",
        "answer": "เช่น application demand, conversion, approval-to-booking, utilization/drawdown, repeat behavior, complaints, customer satisfaction, acquisition cost, portfolio quality และ profitability",
    },
    {
        "id": 31,
        "category": "Product Testing & PMF",
        "question": "ก่อน Launch Product ใหม่ คุณจะ Test อย่างไร?",
        "answer": "เริ่มจาก hypothesis และ success criteria แล้วทำ pilot กับ segment จำกัด กำหนด guardrail ด้าน risk, operations และ customer impact ก่อนขยาย scale",
    },
    {
        "id": 32,
        "category": "Product Testing & PMF",
        "question": "Product Test ต่างจาก UAT อย่างไร?",
        "answer": "UAT ตอบว่าระบบทำงานตาม requirement หรือไม่ แต่ Product Test ตอบว่า product นี้ตอบโจทย์ลูกค้าและธุรกิจหรือไม่ ระบบอาจผ่าน UAT แต่ product ยังไม่ผ่าน PMF ก็ได้",
    },
    {
        "id": 33,
        "category": "Product Testing & PMF",
        "question": "ถ้า Pilot Conversion สูงมาก แต่ NPL เริ่มสูง คุณจะ Scale ไหม?",
        "answer": "ยังไม่ scale ค่ะ ต้องเข้าใจก่อนว่า growth มาจาก segment ไหน และ risk สูงเพราะอะไร อาจต้องปรับ eligibility, limit, pricing หรือ underwriting ก่อน",
    },
    {
        "id": 34,
        "category": "Product Testing & PMF",
        "question": "คุณกำหนด Go / No-Go อย่างไร?",
        "answer": "ดู critical defects, customer impact, regulatory issue, operational readiness, workaround และ remaining risk ถ้ามี issue แต่มี workaround และ controlled risk อาจ Go ได้ แต่ material customer/regulatory risk ต้องแก้ก่อน",
    },
    {
        "id": 35,
        "category": "Head-Level Questions",
        "question": "ถ้า Growth Target กับ Risk Target ขัดกัน คุณจะเลือกอะไร?",
        "answer": "หน้าที่ของ Product ไม่ใช่เลือก Growth หรือ Risk แต่คือหา risk-adjusted growth ค่ะ Growth ที่ทำลาย portfolio quality ไม่ sustainable ขณะเดียวกัน risk control ที่ conservative เกินไปก็ทำให้เสีย opportunity ดังนั้นต้องปรับ segment, pricing, limit หรือ criteria ให้ balance",
    },
    {
        "id": 36,
        "category": "Head-Level Questions",
        "question": "ถ้าคุณได้ตำแหน่งนี้ 90 วันแรกจะทำอะไร?",
        "answer": "30 วันแรก: Understand portfolio, customers, performance, risk, team และ stakeholders\n60 วัน: Identify key gaps/opportunities และ prioritize\n90 วัน: Align roadmap และเริ่ม initiative ที่มี clear impact พร้อม KPI",
    },
]

CORE_SENTENCES = [
    "I start from customer need, but I always balance it with risk and business economics.",
    "I look at the product end to end, not only acquisition.",
    "Growth alone is not success if portfolio quality is not sustainable.",
    "I use data to identify the problem, then validate the solution before scaling.",
    "For lending, PMF must include both customer fit and risk-adjusted profitability.",
    "My role is to connect Product, Risk, Compliance, Operations and Technology toward the same business outcome.",
]

TELL_ME_CN = """目前，我负责数字贷款产品，主要关注从需求、测试、上线到上线后问题管理的端到端产品流程。\n\n我的经验主要有三个方面。第一是产品管理。我和不同团队合作，不断改善客户流程和产品体验。第二是生产环境和系统事故管理。发生问题时，我会先了解客户和业务影响，再分析原因，并推动临时方案和长期解决方案。第三是风险和合规。我会和风险、合规、法务、运营和技术团队合作，确保产品满足客户需求，也符合相关规定。\n\n我对这个职位很感兴趣，因为我希望从数字贷款进一步扩展到更全面的个人贷款产品管理，包括产品策略、客户需求、市场机会和产品市场匹配。\n\n我的优势是能够从端到端看产品，把客户、业务、风险和技术连接起来，并把生产环境中的问题转化为持续改善产品的机会。"""

TELL_ME_PINYIN = """Mùqián, wǒ fùzé shùzì dàikuǎn chǎnpǐn, zhǔyào guānzhù cóng xūqiú, cèshì, shàngxiàn dào shàngxiàn hòu wèntí guǎnlǐ de duāndào duān chǎnpǐn liúchéng.\n\nWǒ de jīngyàn zhǔyào yǒu sān gè fāngmiàn. Dì yī shì chǎnpǐn guǎnlǐ. Wǒ hé bùtóng tuánduì hézuò, bùduàn gǎishàn kèhù liúchéng hé chǎnpǐn tǐyàn. Dì èr shì shēngchǎn huánjìng hé xìtǒng shìgù guǎnlǐ. Fāshēng wèntí shí, wǒ huì xiān liǎojiě kèhù hé yèwù yǐngxiǎng, zài fēnxī yuányīn, bìng tuīdòng línshí fāng’àn hé chángqī jiějué fāng’àn. Dì sān shì fēngxiǎn hé héguī. Wǒ huì hé fēngxiǎn, héguī, fǎwù, yùnyíng hé jìshù tuánduì hézuò, quèbǎo chǎnpǐn mǎnzú kèhù xūqiú, yě fúhé xiāngguān guīdìng.\n\nWǒ duì zhège zhíwèi hěn gǎn xìngqù, yīnwèi wǒ xīwàng cóng shùzì dàikuǎn jìnyíbù kuòzhǎn dào gèng quánmiàn de gèrén dàikuǎn chǎnpǐn guǎnlǐ, bāokuò chǎnpǐn cèlüè, kèhù xūqiú, shìchǎng jīhuì hé chǎnpǐn shìchǎng pǐpèi.\n\nWǒ de yōushì shì nénggòu cóng duāndào duān kàn chǎnpǐn, bǎ kèhù, yèwù, fēngxiǎn hé jìshù liánjiē qǐlái, bìng bǎ shēngchǎn huánjìng zhōng de wèntí zhuǎnhuà wéi chíxù gǎishàn chǎnpǐn de jīhuì."""

TELL_ME_EN = """Currently, I work in Digital Lending, where I look after the end-to-end product journey, from requirements and testing through production and post-launch issue management.\n\nMy experience is mainly in three areas. First, product management, working across functions to develop and continuously improve the customer journey. Second, production and incident management, where I focus on understanding customer and business impact, identifying root causes, and driving both workarounds and long-term solutions. Third, risk and compliance, where I work closely with Risk, Compliance, Legal, Operations, and Technology to ensure that the product serves customer needs while operating within the right controls and regulations.\n\nWhat interests me about this role is the opportunity to expand from Digital Lending into a broader Personal Loan Product Management scope, including product strategy, customer needs, portfolio performance, market opportunities, and product-market fit.\n\nI believe my key strength is my ability to look at a product end to end, connect customer, business, risk, and technology perspectives, and turn production issues into opportunities for continuous product improvement."""

TELL_ME_TH = """ปัจจุบันดิฉันดูแลงานด้าน Digital Lending โดยดูแล end-to-end product journey ตั้งแต่การพัฒนา requirement การทดสอบ ไปจนถึง production และการดูแลปัญหาหลังจากระบบขึ้นใช้งานค่ะ\n\nประสบการณ์หลักของดิฉันอยู่ใน 3 ด้านค่ะ หนึ่ง คือ Product Management การทำงานร่วมกับหลายทีมเพื่อพัฒนาและปรับปรุง customer journey สอง คือ Production & Incident Management โดยเฉพาะการวิเคราะห์ผลกระทบ หา root cause และวางทั้ง workaround และ long-term solution และสาม คือ Risk & Compliance ซึ่งต้องทำงานร่วมกับ Risk, Compliance, Legal, Operations และ Technology เพื่อให้ product ตอบโจทย์ลูกค้าและอยู่ภายใต้ข้อกำหนดที่เหมาะสม\n\nสิ่งที่ดิฉันสนใจสำหรับตำแหน่งนี้ คือโอกาสที่จะขยายจากการดูแล Digital Lending ไปสู่การดูแล Personal Loan Product ในภาพที่กว้างขึ้น ทั้งด้าน strategy, customer needs, portfolio performance, market opportunity และ product-market fit\n\nดิฉันคิดว่าจุดแข็งของตัวเองคือการมองปัญหาแบบ end to end เชื่อม customer, business, risk และ technology เข้าด้วยกัน และเปลี่ยนปัญหาที่เกิดขึ้นใน production ให้กลายเป็นโอกาสในการพัฒนา product ให้ดีขึ้นค่ะ"""

# =========================================================
# SESSION STATE
# =========================================================
if "page" not in st.session_state:
    st.session_state.page = "Practice"
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False
if "answer_status" not in st.session_state:
    st.session_state.answer_status = {q["id"]: None for q in QUESTIONS}
if "attempt_count" not in st.session_state:
    st.session_state.attempt_count = 0


def navigate(page: str):
    st.session_state.page = page
    st.session_state.current_index = 0
    st.session_state.show_answer = False


def get_review_questions():
    return [q for q in QUESTIONS if st.session_state.answer_status.get(q["id"]) == "notyet"]


def get_active_questions():
    if st.session_state.page == "Review":
        return get_review_questions()
    return QUESTIONS


def get_current_question():
    active = get_active_questions()
    if not active:
        return None, active
    if st.session_state.current_index >= len(active):
        st.session_state.current_index = 0
    return active[st.session_state.current_index], active


def next_question():
    active = get_active_questions()
    if not active:
        st.session_state.current_index = 0
    else:
        st.session_state.current_index = (st.session_state.current_index + 1) % len(active)
    st.session_state.show_answer = False


def mark_answer(status: str):
    q, active_before = get_current_question()
    if q is None:
        return

    old_index = st.session_state.current_index
    st.session_state.answer_status[q["id"]] = status
    st.session_state.attempt_count += 1
    st.session_state.show_answer = False

    if st.session_state.page == "Review":
        active_after = get_review_questions()
        if active_after:
            # Keep the same index after removing a mastered question;
            # the next weak question slides into this position.
            st.session_state.current_index = old_index % len(active_after)
        else:
            st.session_state.current_index = 0
    else:
        st.session_state.current_index = (old_index + 1) % len(QUESTIONS)


def reset_progress():
    st.session_state.answer_status = {q["id"]: None for q in QUESTIONS}
    st.session_state.attempt_count = 0
    st.session_state.current_index = 0
    st.session_state.show_answer = False


def ready_count():
    return sum(1 for v in st.session_state.answer_status.values() if v == "can")


def weak_count():
    return sum(1 for v in st.session_state.answer_status.values() if v == "notyet")


def practiced_count():
    return sum(1 for v in st.session_state.answer_status.values() if v is not None)


# =========================================================
# CSS — MOBILE FIRST
# Important: styles are scoped by Streamlit container keys,
# so changing one button does NOT accidentally recolor everything.
# =========================================================
st.markdown(
    """
<style>
:root {
    --text: #47424a;
    --muted: #8d8790;
    --line: #eee8ed;
    --pink: #f8dce8;
    --peach: #f7e3cf;
    --yellow: #f7efb7;
    --mint: #dcefe1;
    --lavender: #f1e8f7;
    --answer: #f7f6fd;
}

html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans Thai", Arial, sans-serif;
}

.stApp {
    background: #ffffff !important;
}

.block-container {
    max-width: 760px;
    padding-top: 1.15rem;
    padding-left: 1.15rem;
    padding-right: 1.15rem;
    padding-bottom: 2rem;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* ---------- Header ---------- */
.pm-title {
    margin: 0;
    padding: 0;
    white-space: nowrap;
    font-size: clamp(1.72rem, 6vw, 3.05rem);
    line-height: 1.05;
    font-weight: 850;
    letter-spacing: -0.035em;
    background: linear-gradient(
        90deg,
        #cbbcff 0%,
        #a8d9ff 20%,
        #b9eadf 40%,
        #f5e8ab 60%,
        #f7d1b8 80%,
        #f4c1dd 100%
    );
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent;
}

.pm-subtitle {
    color: #817b83;
    font-size: clamp(0.95rem, 3.4vw, 1.18rem);
    line-height: 1.3;
    margin-top: 0.18rem;
    margin-bottom: 0.55rem;
    font-weight: 500;
    white-space: nowrap;
}

.soft-divider {
    height: 1px;
    background: var(--line);
    margin: 0.9rem 0 0.95rem 0;
}

/* ---------- Force navigation to stay ONE ROW on mobile ---------- */
.st-key-nav_row [data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 0.45rem !important;
    align-items: center !important;
}

.st-key-nav_row [data-testid="column"] {
    flex: 1 1 0 !important;
    width: 25% !important;
    min-width: 0 !important;
}

.st-key-nav_row [data-testid="column"] > div {
    display: flex !important;
    justify-content: center !important;
}

.st-key-nav_row button {
    width: auto !important;
    min-width: 0 !important;
    min-height: 48px !important;
    padding: 0.55rem 0.68rem !important;
    border-radius: 18px !important;
    border: 1px solid rgba(140, 125, 140, 0.10) !important;
    box-shadow: none !important;
    color: #4f4a51 !important;
    font-size: clamp(0.86rem, 3.3vw, 1rem) !important;
    font-weight: 500 !important;
}

.st-key-nav_row [data-testid="column"]:nth-child(1) button {
    background: #f8dce8 !important;
}
.st-key-nav_row [data-testid="column"]:nth-child(2) button {
    background: #f7e3cf !important;
}
.st-key-nav_row [data-testid="column"]:nth-child(3) button {
    background: #f7efb7 !important;
}
.st-key-nav_row [data-testid="column"]:nth-child(4) button {
    background: #dcefe1 !important;
}

/* ---------- Stats ---------- */
.stat-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.65rem;
    margin-top: 0.15rem;
    margin-bottom: 0.65rem;
}
.stat-card {
    background: #ffffff;
    border: 1px solid #eee8ed;
    border-radius: 22px;
    padding: 0.95rem 0.35rem 0.85rem;
    text-align: center;
    box-shadow: 0 2px 10px rgba(120, 100, 120, 0.035);
}
.stat-value {
    color: #403b44;
    font-size: clamp(1.6rem, 6vw, 2.05rem);
    line-height: 1;
    font-weight: 850;
    margin-bottom: 0.45rem;
}
.stat-label {
    color: #8e8790;
    font-size: clamp(0.78rem, 3vw, 0.95rem);
    font-weight: 500;
}

/* ---------- Progress ---------- */
[data-testid="stProgress"] {
    margin-top: 0.15rem;
}
[data-testid="stProgress"] > div > div {
    background-color: #f2edf2 !important;
    border-radius: 999px !important;
}
[data-testid="stProgress"] > div > div > div {
    background: linear-gradient(90deg, #eadff6, #f6dce9) !important;
    border-radius: 999px !important;
}
.progress-caption {
    color: #8a848c;
    font-size: clamp(0.88rem, 3.3vw, 1rem);
    line-height: 1.45;
    margin-top: 0.45rem;
    margin-bottom: 0.55rem;
    font-weight: 500;
}

/* ---------- Practice card ---------- */
.q-card {
    background: #ffffff;
    border: 1px solid #eee8ed;
    border-radius: 28px;
    padding: 1.25rem 1.35rem 1.35rem;
    box-shadow: 0 2px 10px rgba(120, 100, 120, 0.035);
    margin-top: 0.45rem;
}
.cat-pill {
    display: inline-block;
    background: #f1e8f7;
    color: #73677c;
    border-radius: 999px;
    padding: 0.48rem 0.8rem;
    font-size: clamp(0.78rem, 3vw, 0.92rem);
    line-height: 1.2;
    font-weight: 700;
    margin-bottom: 0.9rem;
}
.question-text {
    color: #3e3941;
    font-size: clamp(1.22rem, 4.8vw, 1.62rem);
    line-height: 1.46;
    font-weight: 800;
}
.instruction {
    color: #928a94;
    text-align: center;
    font-size: clamp(0.9rem, 3.4vw, 1rem);
    margin: 0.7rem 0 0.45rem;
}

/* ---------- ONLY the show-answer button ---------- */
.st-key-show_answer_button button {
    width: auto !important;
    min-height: 52px !important;
    padding: 0.62rem 0.95rem !important;
    border-radius: 18px !important;
    border: 1px solid #eaddea !important;
    background: linear-gradient(135deg, #f7e3f2 0%, #eee8fb 52%, #e6f0ff 100%) !important;
    color: #5b5360 !important;
    font-size: 1rem !important;
    font-weight: 650 !important;
    box-shadow: none !important;
}
.st-key-show_answer_button button:hover,
.st-key-show_answer_button button:focus {
    background: linear-gradient(135deg, #f7e3f2 0%, #eee8fb 52%, #e6f0ff 100%) !important;
    color: #5b5360 !important;
    border-color: #dfd1e1 !important;
}

/* ---------- Answer ---------- */
.answer-box {
    background: #f7f6fd;
    border: 1px solid #e9e5ef;
    border-radius: 26px;
    padding: 1.25rem 1.3rem;
    margin-top: 0.7rem;
    margin-bottom: 0.6rem;
}
.answer-title {
    color: #4b454f;
    font-size: 1.07rem;
    font-weight: 800;
    margin-bottom: 0.8rem;
}
.answer-text {
    color: #5d5760;
    font-size: clamp(1.02rem, 3.9vw, 1.16rem);
    line-height: 1.72;
    font-weight: 450;
    white-space: pre-wrap;
}

/* ---------- Answer status buttons: keep existing pink + peach ---------- */
.st-key-answer_actions [data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 0.55rem !important;
}
.st-key-answer_actions [data-testid="column"] {
    flex: 0 0 auto !important;
    width: auto !important;
    min-width: 0 !important;
}
.st-key-answer_actions button {
    width: auto !important;
    min-height: 52px !important;
    padding: 0.62rem 0.82rem !important;
    border-radius: 18px !important;
    border: 1px solid rgba(140, 125, 140, 0.08) !important;
    color: #5a535c !important;
    font-size: 0.98rem !important;
    font-weight: 600 !important;
    box-shadow: none !important;
}
.st-key-answer_actions [data-testid="column"]:nth-child(1) button {
    background: #f8dce8 !important;
}
.st-key-answer_actions [data-testid="column"]:nth-child(2) button {
    background: #f7e3cf !important;
}

/* ---------- Small utility buttons ---------- */
.st-key-practice_utilities button,
.st-key-home_actions button,
.st-key-core_reset button {
    width: 100% !important;
    min-height: 50px !important;
    border-radius: 18px !important;
    border: 1px solid #eee5eb !important;
    background: #fbf8fb !important;
    color: #6b646d !important;
    box-shadow: none !important;
}

/* ---------- Home/Core ---------- */
.info-card,
.core-card,
.tmy-card {
    background: #fdfbfd;
    border: 1px solid #eee7ed;
    border-radius: 26px;
    padding: 1.3rem 1.35rem;
    color: #625c64;
    line-height: 1.72;
    margin-top: 0.55rem;
}
.section-title {
    color: #6f6872;
    font-weight: 800;
    font-size: 1.08rem;
    margin-bottom: 0.8rem;
}
.core-line {
    padding: 0.68rem 0.78rem;
    background: #ffffff;
    border: 1px solid #f0eaf0;
    border-radius: 16px;
    margin-bottom: 0.55rem;
    color: #645f66;
    line-height: 1.5;
}
.lang-pill {
    display: inline-block;
    padding: 0.35rem 0.65rem;
    border-radius: 999px;
    background: #f1e8f7;
    color: #726878;
    font-weight: 800;
    margin-top: 0.55rem;
    margin-bottom: 0.5rem;
}
.tmy-text {
    white-space: pre-wrap;
    color: #5d5760;
    line-height: 1.72;
    font-size: 0.98rem;
}
.empty-card {
    background: #fdfbfd;
    border: 1px dashed #e8dfe8;
    border-radius: 24px;
    padding: 1.2rem;
    text-align: center;
    color: #817a83;
    margin-top: 0.7rem;
}

@media (max-width: 420px) {
    .block-container {
        padding-left: 0.72rem;
        padding-right: 0.72rem;
        padding-top: 0.85rem;
    }
    .st-key-nav_row [data-testid="stHorizontalBlock"] {
        gap: 0.22rem !important;
    }
    .st-key-nav_row button {
        min-height: 46px !important;
        padding: 0.48rem 0.5rem !important;
        border-radius: 16px !important;
    }
    .stat-grid {
        gap: 0.42rem;
    }
    .stat-card {
        border-radius: 19px;
        padding: 0.85rem 0.2rem 0.75rem;
    }
    .q-card {
        border-radius: 24px;
        padding: 1rem 1.05rem 1.15rem;
    }
    .answer-box {
        border-radius: 23px;
        padding: 1.05rem 1.08rem;
    }
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# HEADER + NAVIGATION
# =========================================================
st.markdown('<div class="pm-title">Product Management Prep</div>', unsafe_allow_html=True)
st.markdown('<div class="pm-subtitle">Speak first → compare → repeat weak answers</div>', unsafe_allow_html=True)

with st.container(key="nav_row"):
    c1, c2, c3, c4 = st.columns(4, gap="small")
    with c1:
        if st.button("Home", key="nav_home"):
            navigate("Home")
            st.rerun()
    with c2:
        if st.button("Practice", key="nav_practice"):
            navigate("Practice")
            st.rerun()
    with c3:
        if st.button("Review", key="nav_review"):
            navigate("Review")
            st.rerun()
    with c4:
        if st.button("Core", key="nav_core"):
            navigate("Core")
            st.rerun()

st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

# =========================================================
# STATS / PROGRESS — unchanged by audio button
# =========================================================
ready = ready_count()
weak = weak_count()
practiced = practiced_count()
attempts = st.session_state.attempt_count

st.markdown(
    f"""
<div class="stat-grid">
    <div class="stat-card">
        <div class="stat-value">{ready}/36</div>
        <div class="stat-label">พร้อมตอบ</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">{weak}</div>
        <div class="stat-label">ต้องวนซ้ำ</div>
    </div>
    <div class="stat-card">
        <div class="stat-value">{attempts}</div>
        <div class="stat-label">ครั้งที่ตอบ</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.progress(practiced / 36 if practiced else 0.0)
st.markdown(
    f'<div class="progress-caption">Progress {practiced}/36 · เป้าหมาย daily session ประมาณ 10–15 นาที</div>',
    unsafe_allow_html=True,
)

# =========================================================
# PAGES
# =========================================================
if st.session_state.page == "Home":
    st.markdown(
        """
<div class="info-card">
    <div class="section-title">วิธีใช้</div>
    1) เลือก <b>Practice</b> เพื่อฝึกตอบทีละข้อ<br>
    2) พูดคำตอบของตัวเองก่อน<br>
    3) ค่อยกด <b>ดูแนวคำตอบ</b><br>
    4) ถ้าอยากฟัง ให้กดปุ่ม <b>🔊 ฟังคำตอบ</b> เอง — ระบบจะไม่อ่านให้อัตโนมัติ<br>
    5) กด <b>ตอบได้ ✓</b> หรือ <b>ยังไม่ได้ ↻</b><br>
    6) ไปทวนข้อที่อ่อนในหน้า <b>Review</b>
</div>
""",
        unsafe_allow_html=True,
    )

    with st.container(key="home_actions"):
        if st.button("เริ่มฝึกเลย", key="home_start", use_container_width=True):
            navigate("Practice")
            st.rerun()
        if st.button("เริ่ม Review ข้ออ่อน", key="home_review", use_container_width=True):
            navigate("Review")
            st.rerun()
        if st.button("Reset Progress", key="home_reset", use_container_width=True):
            reset_progress()
            st.rerun()

elif st.session_state.page in ("Practice", "Review"):
    q, active = get_current_question()

    if q is None:
        st.markdown(
            '<div class="empty-card">ยังไม่มีข้อที่ต้องวนซ้ำค่ะ ✨<br>ตอนนี้ Review ว่างแล้ว</div>',
            unsafe_allow_html=True,
        )
    else:
        q_text = html.escape(q["question"])
        category = html.escape(q["category"])
        answer_html = html.escape(q["answer"]).replace("\n", "<br>")

        st.markdown(
            f"""
<div class="q-card">
    <div class="cat-pill">{category}</div>
    <div class="question-text">{q['id']}) {q_text}</div>
</div>
<div class="instruction">ตอบออกเสียงก่อน แล้วค่อยกดดูแนวคำตอบ</div>
""",
            unsafe_allow_html=True,
        )

        # SHOW ANSWER BUTTON — pastel only, never black
        if not st.session_state.show_answer:
            with st.container(key="show_answer_button"):
                if st.button("ดูแนวคำตอบ", key=f"show_answer_{q['id']}"):
                    st.session_state.show_answer = True
                    st.rerun()

        if st.session_state.show_answer:
            st.markdown(
                f"""
<div class="answer-box">
    <div class="answer-title">แนวคำตอบ</div>
    <div class="answer-text">{answer_html}</div>
</div>
""",
                unsafe_allow_html=True,
            )

            # =====================================================
            # MANUAL AUDIO BUTTON
            # - NO autoplay
            # - Click = speak
            # - Click again = cancel current speech + read again
            # - Completely independent from answer/progress state
            # =====================================================
            answer_json = json.dumps(q["answer"], ensure_ascii=False)
            components.html(
                f"""
<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
    html, body {{
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans Thai", Arial, sans-serif;
    }}
    #listenBtn {{
        width: 100%;
        min-height: 72px;
        border: 1px solid rgba(140,125,140,.10);
        border-radius: 24px;
        padding: 14px 18px;
        font-size: 18px;
        font-weight: 800;
        color: #554f58;
        background: linear-gradient(
            90deg,
            #f8dce8 0%,
            #eee5fb 20%,
            #dfeeff 40%,
            #def1e6 60%,
            #f7efb7 80%,
            #f7ddcd 100%
        );
        box-shadow: none;
        cursor: pointer;
        -webkit-tap-highlight-color: transparent;
        touch-action: manipulation;
    }}
    #listenBtn:active {{
        transform: scale(.99);
    }}
</style>
</head>
<body>
<button id="listenBtn" type="button">🔊 ฟังคำตอบ</button>
<script>
const text = {answer_json};
const btn = document.getElementById('listenBtn');

function chooseVoice() {{
    const voices = window.speechSynthesis.getVoices();
    return voices.find(v => v.lang && v.lang.toLowerCase().startsWith('th')) || null;
}}

function speakAnswer() {{
    if (!('speechSynthesis' in window)) return;

    // Repeated tap = restart from the beginning.
    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'th-TH';
    utterance.rate = 0.92;
    utterance.pitch = 1.0;
    utterance.volume = 1.0;

    const voice = chooseVoice();
    if (voice) utterance.voice = voice;

    window.speechSynthesis.speak(utterance);
}}

btn.addEventListener('click', speakAnswer);
</script>
</body>
</html>
""",
                height=88,
                scrolling=False,
            )

            # Existing answer buttons stay pink + peach.
            with st.container(key="answer_actions"):
                a1, a2 = st.columns([1, 1], gap="small")
                with a1:
                    if st.button("ตอบได้ ✓", key=f"can_{q['id']}"):
                        mark_answer("can")
                        st.rerun()
                with a2:
                    if st.button("ยังไม่ได้ ↻", key=f"notyet_{q['id']}"):
                        mark_answer("notyet")
                        st.rerun()

        with st.container(key="practice_utilities"):
            u1, u2 = st.columns(2, gap="small")
            with u1:
                if st.button("ข้ามข้อนี้", key=f"skip_{st.session_state.page}_{q['id']}", use_container_width=True):
                    next_question()
                    st.rerun()
            with u2:
                if st.button("Reset Progress", key=f"reset_{st.session_state.page}", use_container_width=True):
                    reset_progress()
                    st.rerun()

elif st.session_state.page == "Core":
    st.markdown(
        '<div class="core-card"><div class="section-title">6 Key Sentences to Keep in Mind</div>',
        unsafe_allow_html=True,
    )
    for i, line in enumerate(CORE_SENTENCES, start=1):
        st.markdown(
            f'<div class="core-line"><b>{i}.</b> {html.escape(line)}</div>',
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # Tell Me About Yourself order: CN → EN → TH
    st.markdown(
        f"""
<div class="tmy-card">
    <div class="section-title">Tell Me About Yourself</div>

    <div class="lang-pill">CN</div>
    <div class="tmy-text">{html.escape(TELL_ME_CN).replace(chr(10), '<br>')}</div>
    <div class="tmy-text" style="margin-top:.65rem;color:#88818a;">{html.escape(TELL_ME_PINYIN).replace(chr(10), '<br>')}</div>

    <div class="lang-pill">EN</div>
    <div class="tmy-text">{html.escape(TELL_ME_EN).replace(chr(10), '<br>')}</div>

    <div class="lang-pill">TH</div>
    <div class="tmy-text">{html.escape(TELL_ME_TH).replace(chr(10), '<br>')}</div>
</div>
""",
        unsafe_allow_html=True,
    )

    with st.container(key="core_reset"):
        if st.button("Reset Progress", key="core_reset_button", use_container_width=True):
            reset_progress()
            st.rerun()
