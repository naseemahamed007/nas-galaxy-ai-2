import gradio as gr
from datetime import datetime

APP_TITLE = "🌌 Nas Galaxy AI"
APP_TAGLINE = "Your all‑in‑one AI companion for emotional support and programming help."
BRAND_COLOR = "#7C4DFF"

def emotional_support(history, user_input):
    """Lightweight, supportive response logic (replace later with LLM)."""
    if not user_input.strip():
        return history + [[None, "Please share a bit more so I can help."]]
    # Core supportive structure: acknowledge, clarify, actionable step, reassurance
    response = (
        "I hear you. Feeling stuck can be exhausting.\n\n"
        "Try this quick plan:\n"
        "1) Name one tiny task you can do in 5 minutes.\n"
        "2) Set a timer and start — even imperfect action beats rumination.\n"
        "3) After 5 minutes, choose the next simplest step.\n\n"
        "If you're comfortable, jot down 3 options and pick the easiest. "
        "You don’t have to solve everything today — just move one step. You’ve got this."
    )
    return history + [[user_input, response]]

def programming_help(history, user_input, code_snippet):
    """Structured engineering assistance (replace later with LLM)."""
    if not user_input.strip() and not code_snippet.strip():
        return history + [[None, "Share a question or paste code/error for targeted help."]]
    guidance = [
        "**Clarify:** Define expected vs actual behavior.",
        "**Reproduce:** Create a minimal example (failing test or short snippet).",
        "**Inspect:** Print/log inputs, types, boundary values.",
        "**Isolate:** Comment out parts until the issue surface narrows.",
        "**Verify:** Add a unit test to lock the fix."
    ]
    response = "Here’s a solid approach:\n" + "\n".join(f"- {g}" for g in guidance)
    if code_snippet.strip():
        response += "\n\nI’ve displayed your code below for reference."
    return history + [[user_input or "(code-focused request)", response]]

def build_interface():
    with gr.Blocks(theme=gr.themes.Soft(primary_hue="violet")) as demo:
        gr.HTML(f"""
        <div style="text-align:center;margin-bottom:20px">
            <h1 style="margin:0;color:{BRAND_COLOR}">{APP_TITLE}</h1>
            <p style="margin:6px 0 0;color:#BBB">{APP_TAGLINE}</p>
        </div>
        """)
        with gr.Tab("💙 Emotional Support"):
            chat1 = gr.Chatbot(height=420, show_copy_button=True)
            msg1 = gr.Textbox(placeholder="Share what's on your mind...", label="Your message")
            send1 = gr.Button("Get Support", variant="primary")
            clear1 = gr.Button("Clear")
            def on_send1(history, text):
                updated = emotional_support(history or [], text)
                return updated, ""
            send1.click(on_send1, inputs=[chat1, msg1], outputs=[chat1, msg1])
            clear1.click(lambda: [], None, chat1)

        with gr.Tab("💻 Programming Help"):
            chat2 = gr.Chatbot(height=420, show_copy_button=True)
            msg2 = gr.Textbox(placeholder="Describe your programming problem…", label="Question")
            code2 = gr.Code(placeholder="# Paste code or error message here", language="python", label="Optional code/error")
            send2 = gr.Button("Get Code Help", variant="primary")
            clear2 = gr.Button("Clear")
            def on_send2(history, text, code):
                updated = programming_help(history or [], text, code or "")
                return updated, "", code
            send2.click(on_send2, inputs=[chat2, msg2, code2], outputs=[chat2, msg2, code2])
            clear2.click(lambda: [], None, chat2)

        gr.Markdown(f"*Session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (local)*")
    return demo

if __name__ == "__main__":
    app = build_interface()
    app.launch()
