import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from shapely.geometry import MultiPoint
import shapely
import colorsys

# run with streamlit run streamlit_data_science_app.py

# use Iris - all-numbers.csv file given in directory for testing CSV upload (or generate random data)

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Variable Analyser", layout="wide", initial_sidebar_state="expanded"
)

# --- SESSION STATE SETUP ---
if "manual_points" not in st.session_state:
    st.session_state["manual_points"] = []
if "cached_csv_data" not in st.session_state:
    st.session_state["cached_csv_data"] = None

# --- CSS STYLING (LIGHT MODE ONLY) ---
st.markdown(
    """
    <style>
    /* Main Background - Light Gradient */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        color: #2e4053;
    }
    
    /* Typography */
    h1, h2, h3, h4, .stMarkdown, p, label {
        color: #2e4053 !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Stats Box Styling */
    .stats-box {
        background: rgba(255, 255, 255, 0.85);
        border: 1px solid rgba(0, 0, 0, 0.1);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s;
    }
    .stats-box:hover {
        transform: scale(1.02);
    }
    
    /* Large Stats Text */
    .stats-label {
        font-size: 1.0rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #5d6d7e;
        margin-bottom: 5px;
    }
    .stats-value {
        font-size: 1.5rem; 
        font-weight: 700;
        color: #1a5276;
    }

    /* Maximize Chart Area */
    .stPlotlyChart {
        width: 100%;
    }
    
    /* Sidebar styling tweaks */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- HELPER FUNCTIONS ---


def get_vibgyor_color(ratio):
    """
    Maps ratio 0.0 (Red) to 1.0 (Violet) across the hue spectrum.
    Red=0deg, Violet approx 270-280deg.
    """
    # In HSV, Hue is 0-1. We want 0 (Red) to ~0.78 (Violet/Purple)
    hue = ratio * 0.78
    # Convert HSV to RGB
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Full Saturation, Full Value
    # Convert RGB (0-1) to CSS string 'rgb(r,g,b)'
    return f"rgba({int(rgb[0]*255)}, {int(rgb[1]*255)}, {int(rgb[2]*255)}, 0.3)"


def get_vibgyor_line_color(ratio):
    """Same as above but opaque for the line border"""
    hue = ratio * 0.78
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return f"rgb({int(rgb[0]*255)}, {int(rgb[1]*255)}, {int(rgb[2]*255)})"


def convert_strings_to_numeric(df):
    for col in df.columns:
        if df[col].dtype == "object":
            temp = df[col]
            df[col] = pd.to_numeric(df[col], errors="coerce")
            if df[col].isna().sum() > 0:
                df[col] = temp
    return df


def process_csv_upload(uploaded_file):
    if uploaded_file is None:
        return None, False
    try:
        df = pd.read_csv(uploaded_file)
        if df is None or len(df) == 0:
            return None, False
        df = df.dropna()
        df = convert_strings_to_numeric(df)
        df = df.select_dtypes(include=[np.number])
        for col in df.columns:
            df[col] = np.round(df[col], 2)
        if len(df.columns) < 1:
            return None, False
        return df, True
    except:
        return None, False


# --- DIALOGS (MODALS) ---


@st.dialog("➕ Add New Point")
def open_add_point_dialog():
    st.write("Enter coordinates to add.")
    c1, c2 = st.columns(2)
    with c1:
        px = st.number_input("X Coord", value=0.0, step=1.0, key="ax")
    with c2:
        py = st.number_input("Y Coord", value=0.0, step=1.0, key="ay")
    if st.button("Add Point", type="primary", width="stretch"):
        st.session_state["manual_points"].append({"x": px, "y": py})
        st.rerun()


@st.dialog("➖ Remove Point")
def open_remove_point_dialog():
    st.write("Enter coordinates to remove.")
    c1, c2 = st.columns(2)
    with c1:
        rx = st.number_input("X Coord", value=0.0, step=1.0, key="rx")
    with c2:
        ry = st.number_input("Y Coord", value=0.0, step=1.0, key="ry")
    if st.button("Remove Point", type="primary", width="stretch"):
        orig_len = len(st.session_state["manual_points"])
        st.session_state["manual_points"] = [
            p
            for p in st.session_state["manual_points"]
            if not (p["x"] == rx and p["y"] == ry)
        ]
        if len(st.session_state["manual_points"]) < orig_len:
            st.rerun()
        else:
            st.error("Point not found.")


@st.dialog("🎲 Add Random Points")
def open_random_dialog():
    st.write("Generate random data (0-100).")
    n = st.slider("Count", 1, 100, 50)
    if st.button(f"Generate {n}", type="primary", width="stretch"):
        rx, ry = np.random.uniform(0, 100, n), np.random.uniform(0, 100, n)
        rx, ry = np.round(rx, 2), np.round(ry, 2)
        for x, y in zip(rx, ry):
            st.session_state["manual_points"].append({"x": x, "y": y})
        st.rerun()


# --- MAIN DISPLAY LOGIC ---


def display_analyzer(x_label="X", y_label="Y"):
    # 1. Prepare Data
    df_man = pd.DataFrame(st.session_state["manual_points"])

    df_csv = pd.DataFrame()
    csv_exists = False
    if st.session_state["cached_csv_data"] is not None:
        raw = st.session_state["cached_csv_data"]["df"]
        if x_label in raw.columns and y_label in raw.columns:
            df_csv = pd.DataFrame(
                {"x": raw[x_label], "y": raw[y_label], "source": "CSV"}
            )
            csv_exists = True

    combined = pd.DataFrame()
    if not df_man.empty:
        df_man["source"] = "Manual"
        combined = pd.concat([combined, df_man])
    if csv_exists and not df_csv.empty:
        combined = pd.concat([combined, df_csv])

    if combined.empty:
        st.info("Waiting for data... Upload a CSV or use the Sidebar.")
        return

    # 2. Sidebar Controls
    st.sidebar.markdown("---")
    st.sidebar.header("🎨 Visuals")
    show_hull = st.sidebar.selectbox("Hull Overlay", ["No", "Yes"])
    show_reg = st.sidebar.selectbox("Linear Regression", ["No", "Yes"])

    # 3. Build Plot
    fig = go.Figure()

    # Trace: CSV (Blue Dots)
    if csv_exists:
        fig.add_trace(
            go.Scatter(
                x=df_csv["x"],
                y=df_csv["y"],
                mode="markers",
                marker=dict(size=9, color="#3498db", opacity=0.8),  # Blue
                name="CSV Data",
            )
        )

    # Trace: Manual (Green Crosses)
    if not df_man.empty:
        fig.add_trace(
            go.Scatter(
                x=df_man["x"],
                y=df_man["y"],
                mode="markers",
                marker=dict(
                    size=11, color="#27ae60", symbol="x-thin", line=dict(width=2)
                ),  # Green Cross
                name="Manual Points",
            )
        )

    all_x, all_y = combined["x"], combined["y"]

    # Trace: Hull (VIBGYOR)
    if show_hull == "Yes" and len(combined) >= 3:
        ratio = st.sidebar.slider(
            "Concavity (Red=Concave, Violet=Convex)", 0.0, 1.0, 0.5
        )
        try:
            pts = np.column_stack((all_x, all_y))
            poly = shapely.concave_hull(MultiPoint(pts), ratio=ratio)
            if poly.geom_type == "Polygon":
                xh, yh = map(list, poly.exterior.xy)
                fill_col = get_vibgyor_color(ratio)
                line_col = get_vibgyor_line_color(ratio)
                fig.add_trace(
                    go.Scatter(
                        x=xh,
                        y=yh,
                        fill="toself",
                        fillcolor=fill_col,
                        line=dict(color=line_col, width=2),
                        name="Hull",
                    )
                )
        except:
            pass

    # Trace: Regression (Pink Dotted)
    if show_reg == "Yes" and len(combined) > 1:
        m, b = np.polyfit(all_x, all_y, 1)
        xr = np.linspace(all_x.min(), all_x.max(), 100)
        fig.add_trace(
            go.Scatter(
                x=xr,
                y=m * xr + b,
                mode="lines",
                line=dict(color="#FF1493", dash="dot", width=3),  # Deep Pink
                name="Regression",
            )
        )

    # Layout: Minimal whitespace, max height
    fig.update_layout(
        template="plotly_white",
        margin=dict(l=10, r=10, t=10, b=10),
        height=750,  # Large fixed height
        xaxis_title=x_label,
        yaxis_title=y_label,
        hovermode="closest",
        legend=dict(orientation="h", yanchor="bottom", y=1.01, xanchor="right", x=1),
    )

    # 4. Render Grid (Graph + Stats)
    c_graph, c_stats = st.columns([5, 1])  # 5:1 Ratio for max graph space

    with c_graph:
        st.plotly_chart(fig, width="stretch")

    with c_stats:
        st.markdown("### 📊 Stats")
        desc = combined[["x", "y"]].describe()
        for s in ["count", "mean", "std", "min", "max"]:
            vx, vy = desc.loc[s, "x"], desc.loc[s, "y"]
            st.markdown(
                f"""
            <div class="stats-box">
                <div class="stats-label">{s}</div>
                <div class="stats-value">X: {vx:.2f}</div>
                <div class="stats-value">Y: {vy:.2f}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )


# --- APP LAYOUT ---

st.title("📈 Variable Analyser")

# Sidebar Actions
st.sidebar.header("📍 Actions")
if st.sidebar.button("➕ Add Point", width="stretch"):
    open_add_point_dialog()
if st.sidebar.button("➖ Remove Point", width="stretch"):
    open_remove_point_dialog()
if st.sidebar.button("🎲 Random Points", width="stretch"):
    open_random_dialog()
if st.sidebar.button("🗑️ Reset All", type="primary", width="stretch"):
    st.session_state["manual_points"] = []
    st.session_state["cached_csv_data"] = None
    st.rerun()

# File Upload (Updates Cache)
with st.expander("📂 CSV Upload", expanded=True):
    f = st.file_uploader("Upload", type=["csv"], label_visibility="collapsed")

if f:
    d, v = process_csv_upload(f)
    if v:
        st.session_state["cached_csv_data"] = {"df": d, "name": f.name}

# Selectors (from Cache)
xl, yl = "X", "Y"
if st.session_state["cached_csv_data"]:
    cached = st.session_state["cached_csv_data"]["df"]
    cols = cached.columns
    st.write(f"**File:** {st.session_state['cached_csv_data']['name']}")
    c1, c2 = st.columns(2)
    with c1:
        xl = st.selectbox("X Axis", cols, index=0)
    with c2:
        yl = st.selectbox("Y Axis", cols, index=1 if len(cols) > 1 else 0)

# JS for warn on refresh (maintained from your original)
try:
    with open("warn_refresh.js", "r") as f:
        js = f.read()
        st.components.v1.html(f"<script>{js}</script>", height=0)
except FileNotFoundError:
    pass  # Silent fail if file missing

# Run
display_analyzer(xl, yl)