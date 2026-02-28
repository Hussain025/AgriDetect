# Clean Sidebar CSS - Perfect Agriculture Theme

This is the clean, perfect sidebar CSS that should replace lines 1098-1802 in app.py:

```css
/* ============================================
   SIDEBAR - PERFECT CLEAN DESIGN V10.0
   ============================================ */

/* Sidebar Container - Light Clean Background */
section[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    width: 20rem !important;
    min-width: 20rem !important;
    max-width: 20rem !important;
    background: linear-gradient(180deg, 
        #f8fdf5 0%,
        #f0f9eb 50%,
        #e8f5e0 100%) !important;
    box-shadow: 4px 0 20px rgba(74, 124, 44, 0.1) !important;
    z-index: 999 !important;
    position: relative !important;
    border-right: 3px solid #4a7c2c !important;
}

/* Sidebar Content */
[data-testid="stSidebarContent"] {
    padding: 1.5rem 1.25rem !important;
}

/* Sidebar always visible */
section[data-testid="stSidebar"][aria-expanded="false"],
[data-testid="stSidebar"][aria-hidden="true"] {
    display: block !important;
    visibility: visible !important;
    width: 20rem !important;
}

/* Sidebar Text Colors - Dark Green */
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div {
    color: #2d5016 !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h4 {
    color: #1a4d2e !important;
}

/* Sidebar Logo/Title */
[data-testid="stSidebar"] h2:first-of-type {
    font-size: 1.5rem !important;
    font-weight: 800 !important;
    margin-bottom: 0.5rem !important;
    text-align: center !important;
    padding: 1rem 0 !important;
    color: #1a4d2e !important;
}

/* Sidebar Subtitle */
[data-testid="stSidebar"] h3 {
    font-size: 0.875rem !important;
    font-weight: 600 !important;
    margin: 1.5rem 0 0.75rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    text-align: center !important;
    color: #4a7c2c !important;
}

/* User Profile Card */
.user-profile {
    background: white !important;
    border: 2px solid #4a7c2c !important;
    border-radius: 16px !important;
    padding: 1.5rem 1.25rem !important;
    margin-bottom: 1.5rem !important;
    box-shadow: 0 4px 15px rgba(74, 124, 44, 0.15) !important;
    transition: all 0.3s ease !important;
    position: relative !important;
}

.user-profile::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #4a7c2c, #6ba83e, #8bc34a);
}

.user-profile:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 8px 25px rgba(74, 124, 44, 0.25) !important;
}

/* User Avatar */
.user-avatar {
    width: 70px !important;
    height: 70px !important;
    background: linear-gradient(135deg, #4a7c2c, #6ba83e) !important;
    color: white !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 2rem !important;
    font-weight: 900 !important;
    margin: 0 auto 1rem !important;
    box-shadow: 0 4px 15px rgba(74, 124, 44, 0.3) !important;
    border: 3px solid white !important;
    transition: all 0.3s ease !important;
}

.user-profile:hover .user-avatar {
    transform: scale(1.1) !important;
}

/* User Info */
.user-info {
    text-align: center !important;
}

.user-info h4 {
    font-size: 1.25rem !important;
    font-weight: 700 !important;
    margin: 0 0 0.5rem 0 !important;
    color: #1a4d2e !important;
}

.user-info p {
    font-size: 0.875rem !important;
    margin: 0 !important;
    color: #4a7c2c !important;
}

/* Sidebar Buttons */
[data-testid="stSidebar"] button {
    background: white !important;
    color: #2d5016 !important;
    border: 2px solid #e8f5e0 !important;
    border-radius: 12px !important;
    padding: 0.875rem 1.25rem !important;
    font-weight: 600 !important;
    font-size: 0.9375rem !important;
    width: 100% !important;
    margin: 0.5rem 0 !important;
    transition: all 0.3s ease !important;
    text-align: left !important;
    box-shadow: 0 2px 8px rgba(74, 124, 44, 0.08) !important;
}

[data-testid="stSidebar"] button:hover {
    background: #f0f9eb !important;
    border-color: #4a7c2c !important;
    transform: translateX(8px) !important;
    box-shadow: 0 4px 15px rgba(74, 124, 44, 0.2) !important;
    color: #1a4d2e !important;
}

/* Primary Button */
[data-testid="stSidebar"] button[kind="primary"] {
    background: linear-gradient(135deg, #4a7c2c, #6ba83e) !important;
    color: white !important;
    border: 2px solid #4a7c2c !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 15px rgba(74, 124, 44, 0.3) !important;
}

[data-testid="stSidebar"] button[kind="primary"]:hover {
    background: linear-gradient(135deg, #3d6520, #5a8c3c) !important;
    transform: translateX(8px) scale(1.02) !important;
}

/* Sidebar Dividers */
[data-testid="stSidebar"] hr {
    border: none !important;
    height: 2px !important;
    background: linear-gradient(90deg, 
        transparent 0%, 
        #4a7c2c 50%, 
        transparent 100%) !important;
    margin: 1.5rem 0 !important;
    opacity: 0.3 !important;
}

/* Sidebar Metrics */
[data-testid="stSidebar"] [data-testid="stMetric"] {
    background: white !important;
    border: 2px solid #e8f5e0 !important;
    border-radius: 12px !important;
    padding: 1.25rem !important;
    margin: 0.75rem 0 !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 2px 10px rgba(74, 124, 44, 0.08) !important;
}

[data-testid="stSidebar"] [data-testid="stMetric"]:hover {
    border-color: #4a7c2c !important;
    transform: translateY(-3px) !important;
}

[data-testid="stSidebar"] [data-testid="stMetricLabel"] {
    color: #4a7c2c !important;
    font-weight: 600 !important;
    font-size: 0.875rem !important;
    text-transform: uppercase !important;
}

[data-testid="stSidebar"] [data-testid="stMetricValue"] {
    color: #1a4d2e !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
}

/* Sidebar Alerts */
[data-testid="stSidebar"] .stAlert {
    background: white !important;
    border: 2px solid #8bc34a !important;
    border-left-width: 4px !important;
    border-radius: 12px !important;
    padding: 1rem !important;
    margin: 1rem 0 !important;
}

[data-testid="stSidebar"] .stAlert p {
    color: #2d5016 !important;
    font-size: 0.875rem !important;
}

/* Collapse Button */
[data-testid="collapsedControl"] {
    background: linear-gradient(135deg, #4a7c2c, #6ba83e) !important;
    color: white !important;
    border: 3px solid white !important;
    border-radius: 50% !important;
    width: 50px !important;
    height: 50px !important;
    box-shadow: 0 4px 15px rgba(74, 124, 44, 0.3) !important;
    transition: all 0.3s ease !important;
}

[data-testid="collapsedControl"]:hover {
    transform: scale(1.1) rotate(90deg) !important;
}

/* Force sidebar width */
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div {
    width: 20rem !important;
    min-width: 20rem !important;
    max-width: 20rem !important;
}

/* Force button styling */
[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] button,
[data-testid="stSidebar"] .stButton button,
[data-testid="stSidebar"] button[kind="secondary"] {
    background: white !important;
    color: #2d5016 !important;
    border: 2px solid #e8f5e0 !important;
}

[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] button:hover,
[data-testid="stSidebar"] .stButton button:hover {
    background: #f0f9eb !important;
    border-color: #4a7c2c !important;
}

/* Force primary button */
[data-testid="stSidebar"] button[kind="primary"],
[data-testid="stSidebar"] .stButton button[kind="primary"] {
    background: linear-gradient(135deg, #4a7c2c, #6ba83e) !important;
    color: white !important;
}
```

## Instructions:
Replace the entire sidebar section (lines 1098-1802) in app.py with this clean CSS.

## Key Features:
- Light green gradient background
- Dark green text (readable!)
- White card-based design
- Clean, simple animations
- Professional appearance
- Matches agriculture theme perfectly
