# Purchases-Analysis-of-Manufacturing-Company
### 📊 Purchases Analysis Dashboard – Overview

![Filter Pane Demo](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWw1MHkydjgzdGJ1cXpqNHd5ZXJvbmJydG5xNnowM2FrcmUxM25yMiZlcD12MV9pbnRlcm5hbF9naWZfYnIfaWQmY3Q9Zw/UsgD5nlEadfJLg1vlp/giphy.gif)


This Power BI project, is designed to provide a comprehensive and interactive overview of an organization's procurement and expense behavior. It covers vendor-wise purchases, tax compliance (TDS & GST), state-wise trends, and related party transactions, with a user-friendly custom filter pane and intuitive visual layout.

---

###  Key Objectives
- Analyze monthly and annual purchase trends.
- Identify top vendors based on purchase volume.
- Track TDS deductions under relevant Income Tax sections (194C, 194Q, 194J).
- Map GST paid (Input GST) and compliance with the 180-day rule.
- Detect related party purchases for transparency and compliance.
- Visualize state-wise purchases based on vendor GST codes.

---

###  Target Audience
While this dashboard was primarily developed for finance teams, it is accessible to non-finance users such as:
- Procurement professionals
- Compliance officers
- Business owners and executives

Explanations and visual aids make it easy to interpret without deep tax or accounting expertise.

---

###  Key Components

#### 1. **Executive Summary Page (Suggested)**
- Total Purchase (FY)
- Total TDS Deducted
- % Related Party Purchases
- No. of Active Suppliers

#### 2. **Top Vendors Page**
- Bar/column chart of Top 5 vendors
- Total value and % share

#### 3. **Trend Analysis Page**
- Month-wise line/area chart
- Cumulative purchase curve

#### 4. **TDS Compliance Page**
- Section-wise breakup (194C-1%, 194C-2%, 194Q, 194J)
- Flags for transactions above thresholds (e.g., ₹30,000 single or ₹1 lakh aggregate)
- DAX logic used to filter threshold logic and vendor grouping

#### 5. **GST Analysis Page**
- IGST, CGST, SGST breakdown
- Supplier-wise GST impact
- RCM flagged suppliers (Reverse Charge Mechanism)

#### 6. **State-wise Mapping**
- Indian state-wise purchases based on first two digits of vendor GSTIN
- Map visual and bar chart used for comparative view

#### 7. **180-Day Compliance Page**
- Bill Date vs. Booking Date logic to flag delayed payments
- 180-day rule under GST where unpaid transactions may trigger ITC reversal

---

###  Concepts Explained for Non-Finance Users

#### • **TDS (Tax Deducted at Source):**
TDS is a tax collected by the buyer on behalf of the government while making specified payments. Different sections (194C, 194Q, 194J) apply based on type of service and vendor.

#### • **GST (Goods and Services Tax):**
GST is an indirect tax levied on goods and services. This report focuses on Input GST (tax paid on purchases). If payments are delayed >180 days, Input GST may need to be reversed.

#### • **RCM (Reverse Charge Mechanism):**
Under certain conditions, the buyer is liable to pay GST directly instead of the seller.

#### • **Related Party Transactions:**
Transactions with group companies or affiliates, often requiring separate disclosures for compliance.

#### • **Vendor State Mapping:**
The first two digits of a GSTIN represent the state code, allowing the dashboard to map purchases geographically.

---

###  Features
- Custom Filter Pane using bookmarks
- Sync slicers across pages
- Conditional formatting for overdue or non-compliant transactions
- Bookmark-based navigation

---

###  File Details
- File Name: `expense analysis.pbix`
- Format: Power BI Desktop (.pbix)
- Supporting File: PDF version for sharing and review

---

### 🔗 How to Use This Report
- Use slicers to filter by date, state, vendor, or GST category.
- Hover on visuals for tooltips.
- Click icons/buttons to toggle filter pane.
- Export summaries as needed from visuals.

---

For any questions or walkthroughs, feel free to raise an issue in this GitHub repository .

