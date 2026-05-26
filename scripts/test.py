# hello_plot.py

import numpy as np
import plotly.graph_objects as go

x = np.linspace(0, 10, 1000)
y = np.sin(x)

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="sin(x)"))

fig.update_layout(
    title="interactive sine wave",
    xaxis_title="x",
    yaxis_title="sin(x)",
)

fig.write_html("plots/simple-test/interactive-sine-wave.html", include_plotlyjs="cdn")
# %%
