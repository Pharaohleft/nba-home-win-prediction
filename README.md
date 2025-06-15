# nba-home-win-prediction

---

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
