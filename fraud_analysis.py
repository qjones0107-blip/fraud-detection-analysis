import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fraud_data.csv")

# 1. Fraud vs Non-Fraud Count
fraud_counts = df["is_fraud"].value_counts().sort_index()
fraud_counts.index = ["Not Fraud", "Fraud"]

plt.figure()
fraud_counts.plot(kind="bar")
plt.title("Fraud vs Non-Fraud Transactions")
plt.xlabel("Transaction Type")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("fraud_vs_nonfraud.png")
plt.close()

# 2. Fraud by Location
fraud_by_location = df[df["is_fraud"] == 1]["location"].value_counts()

plt.figure()
fraud_by_location.plot(kind="bar")
plt.title("Fraud by Location")
plt.xlabel("Location")
plt.ylabel("Number of Fraud Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("fraud_by_location.png")
plt.close()

# 3. Fraud by Device
fraud_by_device = df[df["is_fraud"] == 1]["device"].value_counts()

plt.figure()
fraud_by_device.plot(kind="bar")
plt.title("Fraud by Device")
plt.xlabel("Device")
plt.ylabel("Number of Fraud Cases")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("fraud_by_device.png")
plt.close()

# 4. Average Transaction Amount by Fraud Status
avg_amount = df.groupby("is_fraud")["amount"].mean()
avg_amount.index = ["Not Fraud", "Fraud"]

plt.figure()
avg_amount.plot(kind="bar")
plt.title("Average Transaction Amount by Fraud Status")
plt.xlabel("Transaction Type")
plt.ylabel("Average Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("amount_by_fraud_status.png")
plt.close()

print("Fraud analysis files created.")
