import pandas as pd
state = pd.read_html("https://cleartax.in/s/gst-state-code-jurisdiction")
state= state[0]
state.columns = state.iloc[0]
state = state[1:]