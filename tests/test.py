import matplotlib.pyplot as plt

fig = plt.figure()
fig.text(
    0.5,
    0.3,
    r"\dfrac: $\dfrac{a}{b}$",
    horizontalalignment="center",
    verticalalignment="center",
)
plt.savefig("filename.png", format="png", bbox_inches="tight", dpi=300)
