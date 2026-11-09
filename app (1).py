"""
Umesh Pandey — Finance & Business Analytics Consultant
Live portfolio web app (Streamlit)

Run locally:   streamlit run app.py
Deploy:        see README.md for GitHub + Streamlit Community Cloud steps
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# ----------------------------------------------------------------------
# PAGE CONFIG  (edit title/icon if you want to personalise further)
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Umesh Pandey | Finance & Analytics",
    page_icon="📊",
    layout="wide",
)

# ----------------------------------------------------------------------
# EDIT-ME ZONE — fill in your real contact details once, then forget it
# ----------------------------------------------------------------------
YOUR_NAME = "Umesh Pandey"
YOUR_EMAIL = "umeshpandey.work2004@gmail.com"
YOUR_LINKEDIN = "https://www.linkedin.com/in/your-linkedin-handle"   # <-- replace
YOUR_UPWORK = "https://www.upwork.com/freelancers/your-handle"       # <-- replace once live
YOUR_CONTRA = "https://contra.com/your-handle"                       # <-- replace once live

# ----------------------------------------------------------------------
# CASE STUDY CONTENT (Deliverable 2 — also lives as a standalone doc)
# ----------------------------------------------------------------------
CASE_STUDY_GIG_ECONOMY = """
## Sizing & De-Risking India's Gig Workforce
**MBA Capstone Research · AIMETC–IKGPTU, Finance & Business Analytics**

*A Study on Gig Economy Workers: Challenges, Opportunities, and Policy Imperatives
in Punjab and NCR Region*

---

### 1. The Problem
India's gig and platform workforce is one of the fastest-growing segments of the
labour market. NITI Aayog estimates it will nearly triple from roughly **7.7 million
workers in 2020-21 to about 23.5 million by FY30** — close to **4% of the total
workforce** (NITI Aayog, *India's Booming Gig and Platform Economy*, 2022).

For NBFCs, insurers and fintech lenders, this is a large and underserved customer
segment: gig workers typically lack a stable payslip, employer-backed insurance,
or a formal credit history — the exact inputs traditional underwriting depends on.

**Research question:** What are the real financial, social and occupational
challenges facing gig workers in a corridor like Punjab and the NCR — and what
would it take, commercially and in policy, to serve this segment responsibly?

### 2. Analytical Method
- Designed and fielded a primary survey across **100+ gig workers** (ride-hailing,
  delivery and platform-based freelancers) across Punjab and the NCR, covering
  income stability, access to credit/insurance, working conditions and awareness
  of government welfare schemes.
- Built a structured pipeline to clean, code and analyse both closed and
  open-ended survey responses — demographic segmentation, cross-tabulation of
  income band against financial-product access, and thematic coding of
  qualitative pain points.
- Benchmarked regional findings against national data (NITI Aayog's report) to
  separate Punjab/NCR-specific patterns from the all-India trend.
- Applied the same reconciliation discipline used in NBFC loan-book analysis —
  cross-checking survey data against secondary sources the way disbursement data
  is reconciled against a loan ledger — to keep the dataset audit-ready.
- Synthesised results into a three-part framework: **Challenges** (income
  volatility, no safety net, low financial literacy), **Opportunities** (a large,
  growing, digitally-native customer base for micro-insurance, micro-credit and
  SIP-based savings), and **Policy Imperatives** (recommendations mapped to the
  Code on Social Security, 2020 provisions for gig/platform workers).

### 3. Business Impact
- Converted the national 7.7M → 23.5M growth curve into a **regional sizing
  reference** that a lender or insurer can use to estimate the addressable
  Punjab/NCR gig-worker market.
- Identified the financial products this segment is most underserved on —
  directly actionable for an NBFC or fintech product team scoping a gig-worker
  offering. *(Swap in your own top 2–3 survey findings here — e.g. the specific
  insurance/credit gaps your 100+ respondents flagged most often.)*
- Delivered policy recommendations mapped to existing Code on Social Security
  provisions, giving an early, policy-aligned entrant a ready compliance and
  positioning angle.
- Compressed a 60+ page academic study into a decision-ready one-page brief for
  the faculty panel defense — the same compression skill this app demonstrates
  for client-facing work.

*Full dissertation available on request.*
"""

CASE_STUDY_NBFC = """
## Loan Portfolio & Funding-Source Analysis
**Finance & Accounts Internship · Midland Microfin Ltd**

### 1. The Problem
Midland Microfin's loan book is sliced across products, branches and vintage —
and, like most NBFCs, a meaningful share of on-book growth is funded off-balance
sheet through **direct assignment (DA)** and **securitisation**. Leadership needed
a reliable way to (a) reconcile disbursement, collection and portfolio-cut data
coming out of the core system, and (b) understand how the *mix* between DA and
securitisation had shifted over time, and why that mix matters for funding cost
and balance-sheet capacity.

### 2. Analytical Method
- Built **VLOOKUP/X-LOOKUP-based reconciliation reports** that matched
  disbursement, collection and portfolio-cut data across source systems and
  flagged breaks for the accounts team to chase down.
- Produced recurring **portfolio cuts** (by product, branch, vintage and
  delinquency bucket) used directly in internal MIS reporting.
- Researched and tabulated **five years of funding-source history**, comparing
  how much growth was funded through direct assignment versus securitisation,
  and what that implied for cost of funds and capital relief.

### 3. Business Impact
- Reconciliation reports cut manual cross-checking time and gave the accounts
  team an audit trail instead of a one-off spreadsheet exercise.
- The 5-year DA-vs-securitisation trend gave management a concrete, data-backed
  view of which funding channel the NBFC had been leaning on — and a reference
  point for future funding-mix decisions.
- The same portfolio-cut logic is what powers the interactive **Business
  Dashboard** tab of this app — built fresh with synthetic data, but the same
  shape of report a lending business actually runs on.
"""

# ----------------------------------------------------------------------
# SIDEBAR / NAVIGATION
# ----------------------------------------------------------------------
with st.sidebar:
    st.title("📊 " + YOUR_NAME)
    st.caption("Finance & Business Analytics Consultant")
    page = st.radio(
        "Navigate",
        [
            "🏠 Home",
            "🚀 Startup Financial Model",
            "🏦 Business Dashboard (NBFC)",
            "📈 Investment Research",
            "📄 Case Studies",
        ],
    )
    st.markdown("---")
    st.markdown("**Let's work together**")
    st.markdown(f"📧 [{YOUR_EMAIL}](mailto:{YOUR_EMAIL})")
    st.markdown(f"🔗 [LinkedIn]({YOUR_LINKEDIN})")
    st.caption("Starter projects from ₹4,999 · Full pricing on request")

# ----------------------------------------------------------------------
# HOME
# ----------------------------------------------------------------------
if page == "🏠 Home":
    st.title(f"{YOUR_NAME} — Finance & Business Analytics Consultant")
    st.subheader(
        "MBA (Finance & Business Analytics) · AIR 43, NISM-SEBI National Financial "
        "Literacy Quiz 2025 (North Region, 400,000+ participants)"
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("MBA CGPA", "8.01 / 10")
    c2.metric("NISM-SEBI Quiz Rank", "AIR 43")
    c3.metric("This App", "100% live & interactive")

    st.markdown(
        """
Every page in the sidebar is a **real, interactive tool** — not a screenshot —
built the same way I would build one for a client. Explore each tab, or jump
straight to a case study below.
"""
    )

    st.markdown("### What I offer")
    o1, o2, o3 = st.columns(3)
    with o1:
        st.markdown("#### 🚀 Startup Financial Models")
        st.write(
            "Revenue/MRR projections, unit economics (LTV:CAC, burn, runway), "
            "investor-ready model files."
        )
    with o2:
        st.markdown("#### 🏦 Business Dashboards")
        st.write(
            "Power BI / Excel / Python dashboards for sales, loan portfolios "
            "and operations, built for weekly/monthly reporting."
        )
    with o3:
        st.markdown("#### 📈 Investment Research")
        st.write(
            "SIP & goal-planning calculators, fund/stock comparison notes, "
            "valuation summaries for retail-investor clients."
        )

    st.markdown("### Background")
    st.markdown(
        """
- **Finance & Accounts Intern, Midland Microfin Ltd** — built loan-portfolio
  cuts, VLOOKUP/X-LOOKUP reconciliation reports, and a 5-year study of
  direct-assignment vs. securitisation funding
- **MBA capstone:** gig economy workers in Punjab & NCR, 100+ survey
  respondents — see the Case Studies tab
- President, Finance Club & Marketing Club · Placement Cell Coordinator ·
  NSS Club Coordinator
- Certifications: NISM-SEBI Financial Literacy, Investment & Portfolio
  Management (Rice, Coursera), Financial Markets (Yale, Coursera), Investment
  Risk Management (Coursera)
"""
    )

# ----------------------------------------------------------------------
# STARTUP FINANCIAL MODEL
# ----------------------------------------------------------------------
elif page == "🚀 Startup Financial Model":
    st.title("🚀 Startup Financial Model — Interactive SaaS Projection")
    st.caption(
        "Adjust the assumptions in the sidebar. This is the kind of monthly "
        "projection model I build for founders prepping a pre-seed/seed raise."
    )

    with st.sidebar:
        st.markdown("### Model Assumptions")
        start_mrr = st.number_input("Starting MRR (₹)", 10_000, 5_000_000, 100_000, step=10_000)
        growth = st.slider("Monthly growth rate (%)", 0.0, 30.0, 8.0, 0.5)
        churn = st.slider("Monthly churn rate (%)", 0.0, 15.0, 3.0, 0.5)
        gross_margin = st.slider("Gross margin (%)", 10.0, 95.0, 70.0, 1.0)
        cac = st.number_input("CAC per customer (₹)", 500, 200_000, 5_000, step=500)
        arpu = st.number_input("ARPU / month (₹)", 100, 500_000, 2_000, step=100)
        opex = st.number_input("Fixed monthly OPEX (₹)", 10_000, 5_000_000, 300_000, step=10_000)
        months = st.slider("Projection horizon (months)", 12, 36, 24)

    net_growth = (growth - churn) / 100
    mrr = [float(start_mrr)]
    for _ in range(1, months):
        mrr.append(mrr[-1] * (1 + net_growth))

    df = pd.DataFrame({"Month": range(1, months + 1), "MRR": mrr})
    df["ARR"] = df["MRR"] * 12
    df["Gross Profit"] = df["MRR"] * gross_margin / 100
    new_cust = df["MRR"].diff().fillna(df["MRR"].iloc[0]) / arpu
    df["New Customers"] = new_cust.clip(lower=0).round(1)
    df["EBITDA"] = df["Gross Profit"] - opex

    ltv = (arpu * gross_margin / 100) / (churn / 100) if churn > 0 else np.nan
    ltv_cac = ltv / cac if cac > 0 and not np.isnan(ltv) else np.nan
    breakeven = df.loc[df["EBITDA"] > 0, "Month"]

    k1, k2, k3, k4 = st.columns(4)
    k1.metric(f"Month-{months} MRR", f"₹{df['MRR'].iloc[-1]:,.0f}")
    k2.metric("ARR (end of horizon)", f"₹{df['ARR'].iloc[-1]:,.0f}")
    k3.metric("LTV : CAC", f"{ltv_cac:,.1f}x" if not np.isnan(ltv_cac) else "N/A")
    k4.metric(
        "Breakeven Month",
        str(int(breakeven.min())) if not breakeven.empty else "Not within horizon",
    )

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Month"], y=df["MRR"], name="MRR", mode="lines"))
    fig.add_trace(go.Scatter(x=df["Month"], y=df["EBITDA"], name="EBITDA", mode="lines"))
    fig.update_layout(
        title="MRR & EBITDA Projection", xaxis_title="Month", yaxis_title="₹", height=420
    )
    st.plotly_chart(fig, width='stretch')

    st.markdown("#### Monthly Projection Table")
    st.dataframe(
        df.style.format(
            {
                "MRR": "₹{:,.0f}",
                "ARR": "₹{:,.0f}",
                "Gross Profit": "₹{:,.0f}",
                "New Customers": "{:,.1f}",
                "EBITDA": "₹{:,.0f}",
            }
        ),
        width='stretch',
    )

    st.download_button(
        "⬇️ Download projection as CSV",
        df.to_csv(index=False).encode("utf-8"),
        "financial_model_projection.csv",
        "text/csv",
    )

# ----------------------------------------------------------------------
# BUSINESS DASHBOARD (NBFC)
# ----------------------------------------------------------------------
elif page == "🏦 Business Dashboard (NBFC)":
    st.title("🏦 NBFC Loan Portfolio Dashboard")
    st.caption(
        "Built in the style of the loan-portfolio dashboards from my Midland "
        "Microfin internship. Data below is illustrative/synthetic, regenerated "
        "fresh for this app."
    )

    @st.cache_data
    def build_portfolio_data():
        rng = np.random.default_rng(42)
        regions = ["Punjab", "Delhi NCR", "Haryana", "Rajasthan", "UP West"]
        products = ["Microfinance", "MSME Loan", "Gold Loan", "Personal Loan"]
        rows = []
        for month in pd.date_range("2025-01-01", periods=24, freq="MS"):
            for r in regions:
                for p in products:
                    disb = int(rng.integers(500_000, 5_000_000))
                    npa = round(float(rng.uniform(0.5, 6.5)), 2)
                    rows.append([month, r, p, disb, npa])
        return pd.DataFrame(rows, columns=["Month", "Region", "Product", "Disbursement", "NPA %"])

    data = build_portfolio_data()
    regions_all = sorted(data["Region"].unique())
    products_all = sorted(data["Product"].unique())

    f1, f2 = st.columns(2)
    sel_region = f1.multiselect("Region", regions_all, default=regions_all)
    sel_product = f2.multiselect("Product", products_all, default=products_all)
    filtered = data[data["Region"].isin(sel_region) & data["Product"].isin(sel_product)]

    k1, k2, k3 = st.columns(3)
    k1.metric("Total Disbursement", f"₹{filtered['Disbursement'].sum()/1e7:,.2f} Cr")
    k2.metric("Avg NPA %", f"{filtered['NPA %'].mean():.2f}%" if len(filtered) else "N/A")
    k3.metric("Region × Product lines", f"{len(sel_region) * len(sel_product)}")

    col1, col2 = st.columns(2)
    with col1:
        trend = filtered.groupby("Month", as_index=False)["Disbursement"].sum()
        fig1 = px.line(trend, x="Month", y="Disbursement", title="Monthly Disbursement Trend")
        st.plotly_chart(fig1, width='stretch')
    with col2:
        mix = filtered.groupby("Product", as_index=False)["Disbursement"].sum()
        fig2 = px.pie(mix, names="Product", values="Disbursement", title="Portfolio Mix by Product")
        st.plotly_chart(fig2, width='stretch')

    npa_by_region = filtered.groupby("Region", as_index=False)["NPA %"].mean()
    fig3 = px.bar(npa_by_region, x="Region", y="NPA %", title="Average NPA % by Region")
    st.plotly_chart(fig3, width='stretch')

    st.markdown("#### Portfolio Cut — Region × Product (₹ Disbursement)")
    pivot = pd.pivot_table(
        filtered, index="Region", columns="Product", values="Disbursement", aggfunc="sum"
    )
    st.dataframe(pivot.style.format("₹{:,.0f}"), width='stretch')

# ----------------------------------------------------------------------
# INVESTMENT RESEARCH
# ----------------------------------------------------------------------
elif page == "📈 Investment Research":
    st.title("📈 Investment Research — SIP Goal Planner & Fund Comparison")
    st.caption(
        "A simplified version of the SIP projection and fund-comparison notes "
        "I build for retail-investor clients."
    )

    st.markdown("#### SIP Future Value Calculator")
    c1, c2, c3, c4 = st.columns(4)
    monthly_sip = c1.number_input("Monthly SIP (₹)", 500, 200_000, 5_000, step=500)
    lumpsum = c2.number_input("Initial Lumpsum (₹)", 0, 5_000_000, 25_000, step=5_000)
    annual_return = c3.slider("Expected annual return (%)", 4.0, 20.0, 12.0, 0.5)
    years = c4.slider("Investment horizon (years)", 1, 30, 10)

    r = annual_return / 1200  # monthly rate

    def future_value(months_n, monthly, lump, rate):
        fv_sip = monthly * (((1 + rate) ** months_n - 1) / rate) * (1 + rate) if rate > 0 else monthly * months_n
        fv_lump = lump * (1 + rate) ** months_n
        return fv_sip + fv_lump

    total_months = years * 12
    fv_total = future_value(total_months, monthly_sip, lumpsum, r)
    total_invested = monthly_sip * total_months + lumpsum

    k1, k2, k3 = st.columns(3)
    k1.metric("Total Invested", f"₹{total_invested:,.0f}")
    k2.metric("Projected Value", f"₹{fv_total:,.0f}")
    k3.metric("Wealth Gained", f"₹{fv_total - total_invested:,.0f}")

    years_range = list(range(1, years + 1))
    vals = [future_value(y * 12, monthly_sip, lumpsum, r) for y in years_range]
    chart_df = pd.DataFrame({"Year": years_range, "Projected Value": vals})
    fig = px.area(chart_df, x="Year", y="Projected Value", title="Wealth Growth Over Time")
    st.plotly_chart(fig, width='stretch')

    st.markdown("---")
    st.markdown("#### Quick Fund Comparison *(illustrative placeholders — swap in real data per client)*")
    comp_df = pd.DataFrame(
        {
            "Fund": ["Large Cap Fund A", "Flexi Cap Fund B", "Mid Cap Fund C", "Index Fund D"],
            "3Y CAGR %": [14.2, 17.8, 21.3, 13.1],
            "5Y CAGR %": [12.9, 15.6, 18.7, 12.0],
            "Expense Ratio %": [1.1, 1.6, 1.8, 0.2],
            "Risk": ["Moderate", "Moderately High", "High", "Moderate"],
        }
    )
    st.dataframe(comp_df, width='stretch')
    st.caption(
        "⚠️ Figures above are illustrative placeholders for demo purposes only — "
        "not live market data, and not investment advice."
    )

# ----------------------------------------------------------------------
# CASE STUDIES
# ----------------------------------------------------------------------
elif page == "📄 Case Studies":
    st.title("📄 Case Studies")
    tab1, tab2 = st.tabs(["Gig Economy Research", "NBFC Portfolio & Funding"])
    with tab1:
        st.markdown(CASE_STUDY_GIG_ECONOMY)
    with tab2:
        st.markdown(CASE_STUDY_NBFC)

# ----------------------------------------------------------------------
# FOOTER
# ----------------------------------------------------------------------
st.markdown("---")
st.caption(
    f"© {YOUR_NAME} · Built with Streamlit · "
    f"[Email](mailto:{YOUR_EMAIL}) · [LinkedIn]({YOUR_LINKEDIN})"
)
