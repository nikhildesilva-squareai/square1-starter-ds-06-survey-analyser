"""CLI:  python -m survey.cli data/survey_responses.csv"""
import argparse
from .survey import load_responses, score_sentiment, top_themes, summarize


def main() -> None:
    ap = argparse.ArgumentParser(description="Sentiment + themes from survey comments.")
    ap.add_argument("csv", help="Path to the survey-responses CSV")
    args = ap.parse_args()

    df = load_responses(args.csv)
    df["sentiment"] = score_sentiment(df["comment"])
    print("Top themes:")
    for term, count in top_themes(df["comment"]):
        print(f"  {term:<20} {count}")
    print("\nSummary:")
    for key, value in summarize(df).items():
        print(f"  {key}: {value}")
    # TODO: save the summary (and optionally a sentiment-by-department chart).


if __name__ == "__main__":
    main()
