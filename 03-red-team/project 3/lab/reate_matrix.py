import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/attack_success_matrix.csv")

df["Success Rate"] = (
    df["Successful Attempts"] /
    df["Total Attempts"] * 100
)

print(df.to_string(index=False))

plt.figure(figsize=(10, 6))

plt.bar(
    df["Attack Category"],
    df["Success Rate"]
)

plt.title("Project 3 - Attack Success Matrix")
plt.xlabel("Attack Category")
plt.ylabel("Success Rate (%)")
plt.xticks(rotation=25, ha="right")
plt.ylim(0, 100)

plt.tight_layout()

plt.savefig(
    "evidence/08_attack_success_matrix.png",
    dpi=200
)

plt.show()