"""Contract tests — fail against the starter stubs; make them pass."""
import pandas as pd
from survey import load_responses, score_sentiment, top_themes


def test_load_responses_blank_comment_is_missing(tmp_path):
    p = tmp_path / "s.csv"
    p.write_text(
        "respondent_id,submitted_at,department,rating,nps,comment\n"
        "R1,2025-01-05,Sales,5,9,Love it the team is great\n"
        "R2,2025-02-09,Support,2,3,\n"
    )
    df = load_responses(str(p))
    assert pd.api.types.is_datetime64_any_dtype(df["submitted_at"])
    # The blank comment must read as missing, not an empty string.
    assert df["comment"].isna().sum() == 1


def test_positive_scores_above_negative():
    s = pd.Series([
        "Absolutely love this, the team is fantastic and helpful",
        "Terrible experience, everything is broken and frustrating",
    ])
    scores = score_sentiment(s)
    assert scores.iloc[0] > scores.iloc[1]


def test_top_themes_finds_recurring_keyword():
    s = pd.Series([
        "the managers actually listen and communication is great",
        "great communication from the managers",
        "communication could be better",
    ])
    themes = dict(top_themes(s, n=5))
    # 'communication' appears in all three -> must surface as a top theme.
    assert "communication" in themes
