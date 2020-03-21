import sys
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from load_data import DATA
import matplotlib.pyplot as plt

sys.path.insert(1, "fashion-mnist")

from utils.helper import get_sprite_image

# use decision tree to find top features in credit data
clf = DecisionTreeClassifier(random_state=0)
clf.fit(DATA["credit"][0], DATA["credit"][1])
fi = pd.DataFrame(data=clf.feature_importances_, index=DATA["credit"][0].columns)
fi.plot(
    kind="bar",
    legend=False,
    title="Feature importance from decision tree on credit data",
)
plt.tight_layout()
plt.savefig("output/feature_importance_credit.png")
plt.close()
TOP_FEATURES = (-clf.feature_importances_).argsort()


def examine_credit_cluster(X, labels, title, xylabel, fname):
    plt.scatter(x=X[:, 0], y=X[:, 1], c=labels, alpha=0.5, cmap="coolwarm")
    plt.title(title)
    plt.xlabel(xylabel[0])
    plt.ylabel(xylabel[1])
    plt.savefig(fname)
    plt.close()


def plot_fashion_cluster(X, labels, fname):
    sample = []
    for i in np.unique(labels):
        X_i = X[labels == i, :]
        sample.append(X_i[:10, :])
    plt.imsave(fname, get_sprite_image(sample), cmap="gray")
    plt.close()