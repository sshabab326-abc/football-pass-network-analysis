[README_pass_network (2).md](https://github.com/user-attachments/files/27127702/README_pass_network.2.md)[Uploading README_pass_ne# ⚽ Player Pass Network Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Status-Completed-green) ![Domain](https://img.shields.io/badge/Domain-Football%20Analytics-black)

## 📌 Overview
This project analyses passing connections between players in a football match. By mapping who passes to whom and how often, we can identify key playmakers, understand ball circulation patterns and reveal tactical structures used by a team.

## 🎯 Objectives
- Identify the most influential players in ball distribution
- Visualise passing connections between all players on the pitch
- Understand team shape and positional tendencies through passing data

## 🛠️ Tools & Libraries
| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| VS Code | Development environment |
| Matplotlib | Visualisation and plotting |
| Pandas | Data handling and processing |
| NetworkX | Building and drawing pass networks |

## 📊 What the Visualisation Shows
- Each **node** represents a player positioned on the pitch
- Each **line (edge)** represents passes between two players
- **Thicker lines** = more passes between those players
- **Larger nodes** = players with more total passes (key distributors)

## 🖼️ Output
> Pass network map plotted on a football pitch showing team's passing structure during a match.

## 📁 Project Structure
```
football-pass-network-analysis/
│
├── data/
│   └── pass_data.csv          # Match passing data
├── pass_network.py            # Main analysis script
├── output/
│   └── pass_network_plot.png  # Output visualisation
└── README.md
```

## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/shabab-analyst/football-pass-network-analysis

# Install dependencies
pip install matplotlib pandas networkx

# Run the script
python pass_network.py
```

## 💡 Key Insights
- Identified the top 3 players responsible for majority of ball circulation
- Revealed the team's preferred build-up pattern from defence to attack
- Highlighted isolated players who received fewer passes

## 👤 Author
**Shabab** — Aspiring Sports Analyst | Kerala, India
- LinkedIn: linkedin.com/in/shabab-sports-analyst
- Email: shabab326@gmail.com
twork (2).md…]()


