# nba-home-win-prediction

---
Full Project Summary: NBA Player Clustering and Shift Analysis

Project 1: NBA Player Role Discovery Using Clustering

Objective:The goal was to analyze NBA player stats and automatically group players into meaningful role-based clusters using machine learning. Instead of pre-defined positions (like PG, SF, etc.), we wanted to uncover what type of impact players have based on their performance across several key metrics.

Steps Taken:

Data Preparation:

We loaded cleaned NBA player statistics for the 2023-24 season.

Selected key features for analysis: PTS, AST, TRB, STL, BLK, TOV, FG%, 3P%, FT%.

Standardized the features using StandardScaler to ensure fair clustering.

Dimensionality Reduction with PCA:

Used Principal Component Analysis to reduce data to 2 components for visualization.

Created columns PCA1 and PCA2, which captured most of the variation in player styles.

Clustering Players:

Applied KMeans clustering with 4 clusters.

Each player was assigned a Cluster based on their playing style, not position.

Interpreting the Clusters:

We manually reviewed top players in each cluster and gave them human-readable names:

Primary Creator: High scorers and assist-makers.

Paint Protector: Players with strong blocks and rebounds.

Defensive Menace: High steal and defensive presence.

Floor General: Balanced creators with high efficiency and low turnovers.

Team Composition Analysis:

Compared the role distribution of Miami Heat to top 10 teams by total points.

Found that Miami had a skewed composition: 15 Primary Creators, 0 Paint Protectors, 0 Defensive Menaces, 3 Floor Generals.

This imbalance highlighted a potential flaw in the roster.

Key Insight:Clustering revealed Miami had scoring-heavy players but lacked defensive anchors. Successful teams had a mix of creators and protectors.

Project 2: Shift Analysis Through Noise Injection

Objective:To test the stability of player roles — what happens when a player's stats change slightly? Would they shift to a new cluster (i.e., role)? This helped us identify borderline players who are close to shifting roles.

Steps Taken:

Original Clusters Stored:

Saved each player's cluster label from Project 1.

Noise Injection:

Added small random noise (5% variation) to each player's stats to simulate performance changes.

Re-clustering:

Ran KMeans again on the noisy data.

Compared old and new cluster assignments.

Analysis of Shifts:

Identified players whose cluster changed after noise.

Created a DataFrame showing: Player, From Cluster, To Cluster, and stat values.

Assigned descriptive labels to cluster transitions (e.g., “Playmaking Forward” to “Scoring Guard”).

Findings:

Some players like Anthony Davis and Pascal Siakam changed roles with slight shifts in defensive or shooting stats.

Created a CSV file of all such players with explanations of what changes triggered the shift.

Key Insight:Players near cluster borders are valuable for development or trade targets. Minor improvements in shooting or defense could shift their impact role completely.

Player Selection and Simulations

Based on cluster roles and shifts, we manually selected a roster for Miami:

Chose 1 Primary Creator and a mix of 2 Paint Protectors + 1 Defensive Menace.

Simulated matches against top teams like Boston using a stat-weighted scoring simulator.

Simulation Result Example:

Simulated Miami vs. Boston: Miami Win Probability = 5%

Despite low sim wins, roster looked promising on paper with real-life potential.

Overall Learnings and Use-Cases:

We created a data-driven framework to define NBA roles using real performance data.

Identified team roster imbalances using role-based metrics.

Built a what-if simulation tool to test new rosters.

Detected underrated players who could evolve into better roles with slight improvements.

Walker Kessler	Paint Protector
155	Daniel Gafford	Paint Protector
248	Peyton Watson	Paint Protector
274	Dereck Lively II	Paint Protector
242	Jakob Poeltl	Paint Protector
...	...	...
617	Ryan Arcidiacono	Defensive Menace
613	TyTy Washington Jr.	Defensive Menace
607	Kendall Brown	Defensive Menace
560	Terquavion Smith	Defensive Menace
597	Daishen Nix	Defensive Menace
147 rows × 2 columns


## 📊 Dataset

We used NBA game data from 2003–2022, including:  
- **Game-level stats:** Points, shooting %, assists, rebounds  
- **Home & away team IDs**  
- **Outcome:** Whether the home team won  

The data was sourced from publicly available datasets (e.g., Kaggle).

---

## ⚙️ Process

1️⃣ **Data Cleaning & Exploration**  
- Dropped rows with missing values (~0.3% of data).  
- Explored team performance stats and outcome distributions.

2️⃣ **Feature Engineering**  
- Selected key performance features for modeling:  
  - Home & away team points  
  - Shooting % (FG, FT, 3PT)  
  - Assists and rebounds

3️⃣ **Modeling**  
- Baseline model: **Logistic Regression**  
- Achieved high accuracy (~100%) due to strong correlation of features like points scored.

4️⃣ **Insights**  
- Home team points and shooting percentages are strongly predictive of winning.  
- Away team performance is inversely correlated to home team success.

---

## 🚀 Results

✅ Logistic Regression model achieved ~100% accuracy on the test set.  
✅ This is due to direct relationship between points and winning outcomes in the dataset.

---

## 📈 Visualizations

- Correlation matrix of features and target  
- Distribution of home/away points  
- Model performance metrics  

(See `notebooks/nba_game_prediction.ipynb` for plots and analysis!)

---

## 🌟 Key Takeaways

- **Correlation insights**: High-scoring home teams are very likely to win, while away scoring decreases home win chances.  
- **Model caveats**: This perfect accuracy reflects clear-cut data — real-world prediction on future games would be harder!

---

## 🛠️ How to Run
Clone the repo and run the notebook:

```bash
git clone https://github.com/YourUsername/nba-home-win-prediction.git
cd nba-home-win-prediction
```

### Web Shop Demo

A small Flask app is included in `webapp/` demonstrating a simple clothing
and shoe store. Install Flask and run the app:

```bash
pip install flask
python webapp/app.py
```

Visit <http://localhost:5000> in your browser to try it out.

