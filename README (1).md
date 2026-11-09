# Umesh Pandey — Finance & Business Analytics Consultant

**Live portfolio app** demonstrating three service lines: startup financial
modelling, business dashboards, and investment research — built and deployed
entirely free on GitHub + Streamlit Community Cloud.

🔗 **Live app:** _add your Streamlit URL here once deployed_
📧 **Contact:** umeshpandey.work2004@gmail.com

---

## What's inside

| Page | What it demonstrates |
|---|---|
| 🏠 Home | Bio, credentials (MBA, NISM-SEBI AIR 43), service menu |
| 🚀 Startup Financial Model | Interactive SaaS MRR/EBITDA projection with live assumption sliders — the kind of model used in a seed-stage pitch |
| 🏦 Business Dashboard (NBFC) | A loan-portfolio dashboard in the style of my Midland Microfin internship work — disbursement trend, NPA by region, portfolio-mix cuts |
| 📈 Investment Research | SIP future-value calculator and a fund-comparison table, the kind of tool used with retail-investor clients |
| 📄 Case Studies | Two write-ups: the Punjab/NCR gig-economy research study, and the NBFC loan-portfolio & funding-source analysis |

All data on the dashboard and fund-comparison pages is **synthetic/illustrative**
— clearly labelled as such — so there's nothing confidential and nothing that
needs a live data source. Swap in real client data later and it works the same
way.

---

## Run it locally (optional — 2 minutes)

```bash
pip install -r requirements.txt
streamlit run app.py
```

It opens at `http://localhost:8501`.

---

## Deploy it live — GitHub + Streamlit Community Cloud (10 minutes, ₹0)

### Part A — Put the code on GitHub

1. Go to **[github.com](https://github.com)** and log in (create a free account if you don't have one).
2. Click the **`+`** icon top-right → **New repository**.
3. Name it `finance-analytics-portfolio` (or anything you like). Leave it **Public**. Click **Create repository**.
4. On the new repo's page, click **uploading an existing file** (or **Add file → Upload files**).
5. Drag in all three files: `app.py`, `requirements.txt`, `README.md`.
6. Scroll down, click **Commit changes**.

Your code is now live on GitHub.

### Part B — Deploy to Streamlit Community Cloud

1. Go to **[share.streamlit.io](https://share.streamlit.io)**.
2. Click **Sign in** → choose **Continue with GitHub** → authorize Streamlit to access your GitHub account.
3. Click **Create app** (top-right) → **Deploy a public app from GitHub**.
4. In the form:
   - **Repository:** select the repo you just created (`your-username/finance-analytics-portfolio`)
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. (Optional) Click **Advanced settings** and set a custom app URL, e.g. `umesh-finance-portfolio`.
6. Click **Deploy**.

Streamlit will install your `requirements.txt` and launch the app — this takes
2–5 minutes the first time. You'll get a permanent link that looks like:

```
https://umesh-finance-portfolio.streamlit.app
```

**That link is what goes into your Upwork profile, LinkedIn featured section,
and every outreach message.**

### Keeping it awake

Streamlit's free tier puts an app to sleep after a few days with no visitors.
If a client's first click shows a "Zzz... this app is asleep" screen, just
click **Yes, wake it up** — it restarts in under a minute. For outreach, open
the link yourself once before you send it so it's warm.

### Updating it later

Any time you want to change something: edit the file on GitHub directly (pencil
icon on the file page → edit → **Commit changes**), or re-upload the changed
file. Streamlit Community Cloud redeploys automatically within a minute or two
of any GitHub commit — no redeploy button to click.

---

## Before you share the link — 3 things to personalise

1. Open `app.py`, find the **EDIT-ME ZONE** near the top, and replace
   `YOUR_LINKEDIN`, `YOUR_UPWORK`, `YOUR_CONTRA` with your real profile URLs.
2. In the Case Studies tab, the gig-economy write-up has one bracketed line —
   `(Swap in your own top 2–3 survey findings here…)` — replace it with your
   actual top findings from the dissertation data.
3. Add a real headshot/photo if you want (`st.image("photo.jpg")` near the top
   of the Home section) — optional, not required to go live.

---

## Tech stack

Python · Streamlit · Pandas · NumPy · Plotly — chosen deliberately to match a
2/5 comfort level with Python: every page is plain, readable, well-commented
code with no advanced patterns, so it's easy to extend as your skills grow.
