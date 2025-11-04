# Customer-Segmentation-Analysis

# E-Commerce Customer Segmentation Analysis

## Project Overview
Analyzed 392K transactions from a UK-based online retail company to segment 4,338 customers using RFM (Recency, Frequency, Monetary) analysis. This segmentation enables targeted marketing strategies and improves customer retention.

## Dataset
- **Source:** UK Online Retail Dataset
- **Time Period:** December 2010 - September 2011 (10 months)
- **Transactions:** 392,692 (after cleaning)
- **Customers:** 4,338 unique customers
- **Revenue:** $8.9M total

## Methodology

### Data Cleaning
- Removed duplicate transactions (5,268 rows)
- Excluded returns/cancellations (negative quantities)
- Removed transactions without customer IDs (25% of data - data quality issue identified)
- Removed invalid prices

### RFM Analysis
Segmented customers based on three dimensions:
- **Recency:** Days since last purchase
- **Frequency:** Number of purchases
- **Monetary:** Total spending

Each dimension scored 1-5, combined into customer segments.

## Key Findings

### Customer Segments

| Segment | Count | Avg Recency | Avg Frequency | Avg Monetary | Total Revenue |
|---------|-------|-------------|---------------|--------------|---------------|
| Champions | 957 | 12.8 days | 11.1 purchases | $605 | $5.9M |
| Potential Loyalists | 687 | 96.4 days | 2.1 purchases | $974 | $6.7M |
| Loyal Customers | 778 | 73.0 days | 5.0 purchases | $1,706 | $1.3M |
| At Risk | 213 | 159.0 days | 2.4 purchases | $1,497 | $318K |
| New Customers | 319 | 18.5 days | 1.2 purchases | $455 | $145K |
| Lost | 1,220 | 213.5 days | 1.2 purchases | $464 | $565K |
| Others | 164 | 53.9 days | 1.8 purchases | $419 | $68K |

## Business Recommendations

### Priority 1: Potential Loyalists (687 customers, $6.7M revenue)
**Goal:** Convert to Champions  
**Strategy:** 
- Personalized product recommendations based on purchase history
- Category-specific email campaigns
- Loyalty program invitation
- **Expected Impact:** 20% conversion = 137 new Champions

### Priority 2: New Customers (319 customers)
**Goal:** Encourage second purchase  
**Strategy:**
- Welcome email series
- Post-purchase follow-up
- "Complete your collection" recommendations
- **Target Metric:** 35% second purchase rate within 60 days

### Priority 3: At Risk (213 customers, $318K historical revenue)
**Goal:** Re-engage high-value customers  
**Strategy:**
- Focus on top 25% by monetary value
- "We miss you" campaign
- Personalized win-back offers
- **Expected Impact:** 30% recovery = ~$95K revenue

## Data Quality Issues Identified
- 25% of transactions lack customer identification
- **Recommendation:** Investigate why CustomerID isn't captured consistently (guest checkouts? POS system gaps?)
- Capturing this data would enable better customer tracking and personalization

## Tools & Technologies
- **Python** (pandas, numpy)
- **Analysis:** RFM segmentation, customer behavior analysis
- **Data Cleaning:** Handled duplicates, missing values, outliers

## Files
- `Ukstoredata.py` - Main analysis script
- `customer_rfm_segments.csv` - Full RFM analysis results
- `segment_summary.csv` - Summary statistics by segment

## Key Learnings
- Potential Loyalists represent the largest revenue opportunity ($6.7M)
- 22% of customers are Champions/Loyal, generating 82% of revenue
- Customer retention is more valuable than acquisition for this business

## Next Steps
- A/B test marketing campaigns for each segment
- Track conversion rates over time
- Analyze product preferences within each segment
- Build predictive model for customer lifetime value

---

**Author:** [Anshul Pande]  
**Date:** November 2025
**Contact:** [aapande18044@gmail.com]
