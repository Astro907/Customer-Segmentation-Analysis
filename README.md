# Customer-Segmentation-Analysis
E-Commerce Customer Segmentation Analysis

## Project Overview
Analyzed 392K transactions from a UK-based online retail company to segment 4,338 customers using RFM (Recency, Frequency, Monetary) analysis. This segmentation enables targeted marketing strategies and improves customer retention.

## Dataset
* Source: UK Online Retail Dataset
* Time Period: December 2010 - September 2011 (10 months)
* Transactions: 392,692 (after cleaning)
* Customers: 4,338 unique customers
* Revenue: $8.9M total

## Methodology

### Data Cleaning
* Removed duplicate transactions (5,268 rows)
* Excluded returns/cancellations (negative quantities)
* Removed transactions without customer IDs (25% of data - data quality issue identified)
* Removed invalid prices

### RFM Analysis
Segmented customers based on three dimensions:
* Recency: Days since last purchase
* Frequency: Number of purchases
* Monetary: Total spending

Each dimension scored 1-5, combined into customer segments.

## Key Findings

### Customer Segments
| Segment | Count | Avg Recency | Avg Frequency | Avg Monetary | Total Revenue |
|---------|-------|-------------|---------------|--------------|---------------|
| Champions | 957 | 12.8 days | 11.1 purchases | $6,052 | $5.79M |
| Loyal Customers | 778 | 73.0 days | 5.0 purchases | $1,706 | $1.33M |
| Potential Loyalists | 687 | 36.3 days | 2.1 purchases | $975 | $670K |
| Lost | 1,220 | 213.5 days | 1.2 purchases | $464 | $565K |
| At Risk | 213 | 159.0 days | 2.4 purchases | $1,497 | $319K |
| New Customers | 319 | 18.5 days | 1.2 purchases | $455 | $145K |
| Others | 164 | 53.9 days | 1.8 purchases | $419 | $68K |

## Business Recommendations

### Priority 1: Champions (957 customers, $5.79M revenue)
**Goal:** Retain and maximize value
**Strategy:**
* VIP treatment and exclusive early access to new products
* Personalized thank-you communications
* Referral program incentives
* Expected Impact: Maintain 90%+ retention rate

### Priority 2: Loyal Customers (778 customers, $1.33M revenue)
**Goal:** Upgrade to Champions status
**Strategy:**
* Targeted upselling campaigns
* Bundle offers on complementary products
* Frequency incentives (purchase more often)
* Expected Impact: 15% conversion = 117 new Champions

### Priority 3: Potential Loyalists (687 customers, $670K revenue)
**Goal:** Increase purchase frequency
**Strategy:**
* Personalized product recommendations
* Time-sensitive offers to encourage repeat purchases
* Loyalty program enrollment
* Expected Impact: Move 30% to Loyal/Champions tier

### Priority 4: At Risk (213 customers, $319K historical revenue)
**Goal:** Re-engage before they become Lost
**Strategy:**
* Focus on top 25% by monetary value (highest spenders)
* "We miss you" personalized win-back campaigns
* Special discount codes or exclusive offers
* Expected Impact: 30% recovery = ~$96K revenue boost

## Data Quality Issues Identified
* 25% of transactions lack customer identification
* Recommendation: Investigate why CustomerID isn't captured consistently (guest checkouts? POS system gaps?)
* Capturing this data would enable better customer tracking and personalization

## Tools & Technologies
* Python (pandas, numpy)
* Analysis: RFM segmentation, customer behavior analysis
* Data Cleaning: Handled duplicates, missing values, outliers

## Files
* `Ukstoredata.py` - Main analysis script
* `customer_rfm_segments.csv` - Full RFM analysis results
* `segment_summary.csv` - Summary statistics by segment

## Key Learnings
* Champions and Loyal Customers (39% of customer base) generate 80% of revenue ($7.1M)
* Customer retention is more valuable than acquisition for this business
* Recent purchasers (Champions, New Customers, Potential Loyalists) are still engaged - focus retention efforts here

## Next Steps
* A/B test marketing campaigns for each segment
* Track conversion rates and segment movement over time
* Analyze product preferences within each segment
* Implement automated email campaigns based on RFM scores

**Author:** Anshul Pande

**Date:** November 2025 

**Contact:** LinkedIn- https://www.linkedin.com/in/anshul-pande-9b33632a4/?trk=opento_sprofile_goalscard
