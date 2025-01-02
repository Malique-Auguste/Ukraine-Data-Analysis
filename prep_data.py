import pandas as pd

labelled_data = pd.read_csv("data/event_labels_latest_2024.csv")

print(f"Filtered {len(labelled_data)} events for russia committed airstrikes.")
airstrike_event_ids = labelled_data.query("t_airstrike > 0.9 and t_airalert < 0.1 and a_rus > 0.9 and a_ukr < 0.1")
airstrike_event_ids = airstrike_event_ids.filter(items=["event_id"])
print(f"Number of events: {len(airstrike_event_ids)}")

print("\nExtracted event texts from second dataset.")
unlabelled_data = pd.read_csv("data/event_info_latest_2024.csv")
airstrike_event_texts = unlabelled_data[unlabelled_data["event_id"].isin(airstrike_event_ids["event_id"])]
airstrike_event_texts = airstrike_event_texts.filter(items=["event_id_1pd", "url", "text"])
print(f"Number of events: {len(airstrike_event_texts)}")

print("\nRemoving events with duplicate event_id_1pd.")
airstrike_event_texts = airstrike_event_texts[~airstrike_event_texts.duplicated(subset = "event_id_1pd")]
print(f"Number of events: {len(airstrike_event_texts)}")

airstrike_event_texts.to_csv("data/airstrike_events.csv", index = False)