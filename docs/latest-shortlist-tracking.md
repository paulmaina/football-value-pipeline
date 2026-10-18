# Latest prediction tracking for shortlisted matches

The main win-rate, ROI, calibration and weekly/market/league/policy results use
one selection per fixture: the latest eligible pre-kickoff shortlist entry.
If a later prediction run changes the selected market, probability, bookmaker,
price or execution cost, the new archived entry replaces the earlier one for
that match's main grade. A newly shortlisted match is added. A match omitted
from a later shortlist retains its last eligible shortlisted prediction.

Generation time determines which forecast is latest. Later uploads of an older
forecast cannot roll back tracking. Both generation and Git capture must precede
kickoff by at least 20 minutes. Post-kickoff reruns never change the tracked
selection. Uploading the same generation under another commit does not create
an additional selection or stake. Predictions that were overwritten locally
before any eligible archive cannot be reconstructed or treated as forward evidence.

`shortlist_grades.csv` and the workbook Dashboard/Selections show the latest
selection per match. Generated/captured UTC timestamps and source commit identify
the exact forecast used. The main totals assume one hypothetical stake per match
at that forecast's recorded odds, after frozen costs. They are not actual account
returns or accumulator returns.

`shortlist_run_history.csv` retains every distinct eligible generation/fixture
for audit. The workbook **Run Tracking** tab and JSON `run_history_groups` show
per-run historical results; they are excluded from the main totals. Earlier
forecasts of the same match are correlated, not extra independent observations.
The first-prediction reference in Markdown/JSON permits comparison with the
previous reporting convention.

Normal pre-kickoff capture and review automate this for future uploads and the
existing immutable archives. The prediction command is unchanged; generate and
push/archive before kickoff as usual. A GitHub review cannot recover a local
prediction that was never uploaded. Existing full-fixture model assessments,
closing-price studies and research experiments keep their fixed first-eligible
cohorts, preventing repeated reruns from inflating experimental sample counts.
