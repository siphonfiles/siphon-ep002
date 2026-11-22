"""Shared Upsampler look-and-feel for every Upsampler/* HF Space.

`create_and_push.py` uploads this file alongside each Space's app.py, so every
Space imports the exact same theme, CSS, header, and footer. Keep this the
single source of truth (v3 recipe): Soft indigo/purple theme, gradient primary
button, Gradio's own footer hidden, 1000px max width, minimal header/footer.
"""

import gradio as gr

UPSAMPLER_THEME = gr.themes.Soft(
    primary_hue=gr.themes.colors.indigo,
    secondary_hue=gr.themes.colors.purple,
    neutral_hue=gr.themes.colors.slate,
    font=[gr.themes.GoogleFont("Inter"), "system-ui", "sans-serif"],
).set(
    button_primary_background_fill="linear-gradient(90deg, #6366f1 0%, #a855f7 100%)",
    button_primary_background_fill_hover="linear-gradient(90deg, #4f46e5 0%, #9333ea 100%)",
    button_primary_text_color="#ffffff",
    button_primary_border_color="*primary_500",
)

# Hide Gradio's built-in footer and keep the app narrow and centered.
UPSAMPLER_CSS = """
footer { display: none !important; }
.gradio-container { max-width: 1000px !important; margin: 0 auto !important; }
#usp-header h1 { font-size: 1.7rem; font-weight: 700; margin: 0 0 .25rem; }
#usp-header p { opacity: .6; margin: 0; }
#usp-footer { opacity: .5; font-size: .85rem; margin-top: 1.25rem; }
#usp-footer a { text-decoration: none; }
"""


def header_html(title: str, subtitle: str) -> str:
    return f"""<div id="usp-header">
  <h1>{title}</h1>
  <p>{subtitle}</p>
</div>"""


_LINK_STYLE = "color:#8b7cf6;font-weight:600;text-decoration:none"


def footer_html(description: str, tool_url: str, tool_anchor: str) -> str:
    """SEO footer (v4 recipe): a short paragraph describing what the model
    does (unique per Space, keyword-bearing) plus the Upsampler attribution
    with a deep link to the matching /free-* tool on upsampler.com. No model
    credit/license line (the README frontmatter carries the license). Spaces
    target model-name queries; the site pages keep the intent queries
    ("free X no signup"), so the two never compete."""
    return f"""<div id="usp-footer">
  <p style="margin:0 0 10px">{description}</p>
  <p style="margin:0">Maintained by <a href="https://upsampler.com" target="_blank" rel="noopener" style="{_LINK_STYLE}">Upsampler</a>. Check out the <a href="{tool_url}" target="_blank" rel="noopener" style="{_LINK_STYLE}">{tool_anchor}</a>, no sign-up required.</p>
</div>"""
