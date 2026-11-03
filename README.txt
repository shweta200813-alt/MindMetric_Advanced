MINDMETRIC ADVANCED - UPGRADED AI APPLICATIONS LAB PROJECT
============================================================

Keep your working old MindMetric_Project folder as a backup.
Extract this ZIP into a NEW folder named MindMetric_Advanced.

NEW FEATURES
- Improved multi-page responsive website and navigation
- 12-question educational self-reflection assessment
- Result dashboard with interactive category chart
- Mood tracker with seven-day chart; entries saved only in browser local storage
- Scripted wellness information assistant (not a therapist or generative AI)
- Actual Decision Tree ML demonstration using synthetic classroom data
- ML train/test split, accuracy and confusion matrix

RUN ON WINDOWS
1. Extract the ZIP into a new folder.
2. Open MindMetric_Advanced.
3. Click File Explorer address bar, type cmd, press Enter.
4. Install dependencies:
   python -m pip install -r requirements.txt
5. Start website:
   python app.py
6. Open Chrome: http://127.0.0.1:5000

Keep Command Prompt open while using the website. Press Ctrl+C to stop.

PYTHON VERSION NOTE
If pip says no compatible distribution exists for numpy or scikit-learn,
install Python 3.12 (64-bit), then repeat the installation in a new terminal.

FILES
app.py             Flask routes and server
scoring.py         Questionnaire and transparent scoring rules
ml_demo.py         Decision Tree ML demonstration
requirements.txt   Python dependencies
templates/         HTML pages
static/style.css   Website styling

LIMITATIONS AND PRIVACY
- The custom questionnaire is NOT clinically validated.
- The response index is descriptive, not a diagnosis or medical risk probability.
- The ML demo uses synthetic data and artificial labels; accuracy has no clinical meaning.
- The Wellness Guide uses fixed response rules, not generative AI.
- Mood entries are stored in browser localStorage, not sent to Flask. Anyone using the same
  browser profile may be able to view them. Delete entries from the mood tracker.
- No user account or server-side database is used.
- For immediate danger in India, call 112. Tele-MANAS: 14416.
