import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "simple_white"

##
# grid

x = np.linspace(-6, 6, 200)
y = np.linspace(-6, 6, 200)

X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)

Z = np.sin(R)

# figure

fig = go.Figure()

fig.add_trace(
    go.Surface(
        x=X,
        y=Y,
        z=Z,
    )
)

# layout

fig.update_layout(
    title=r"$z = \sin\left(\sqrt{x^2+y^2}\right)$",
    scene=dict(
        xaxis_title=r"$x$",
        yaxis_title=r"$y$",
        zaxis_title=r"$z$",
    ),
    autosize=True,
    margin=dict(l=0, r=0, b=0, t=50),
)

# export

fig.write_html(
    "plots/simple-test/sine-surface.html",
    include_plotlyjs="cdn",
    include_mathjax="cdn",
    config={"responsive": True},
)

# %%
