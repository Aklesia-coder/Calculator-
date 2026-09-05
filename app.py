import gradio as gr


# -----------------------------
# Calculator logic
# -----------------------------
def calculate(expression):
    try:
        # Only allow safe calculator characters
        allowed = "0123456789+-*/.() %"

        if not all(c in allowed for c in expression):
            return "Error"

        # Convert percentage to decimal
        expr = expression.replace("%", "/100")

        result = eval(expr)

        # Remove .0 from whole numbers
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return f"{result:,}"

    except Exception:
        return "Error"


# -----------------------------
# Button handler
# -----------------------------
def press(expression, button):
    if button == "C":
        expression = ""

    elif button == "⌫":
        expression = expression[:-1]

    elif button == "=":
        expression = calculate(expression).replace(",", "")

    elif button == "()":
        if expression.count("(") > expression.count(")"):
            expression += ")"
        else:
            expression += "("

    else:
        mapping = {
            "×": "*",
            "÷": "/",
            "−": "-"
        }

        expression += mapping.get(button, button)

    return expression if expression else "0"


# -----------------------------
# Calculator design
# -----------------------------
custom_css = """
body,
.gradio-container {
    background-color: #000000 !important;
    max-width: 420px !important;
    margin: 0 auto !important;
}

#calc-display textarea {
    background-color: #000000 !important;
    color: #4ECDC4 !important;
    font-size: 48px !important;
    text-align: right !important;
    border: none !important;
    font-family: Arial, sans-serif;
}

#calc-grid {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 10px !important;
    padding: 10px !important;
}

.calc-btn button {
    font-size: 22px !important;
    aspect-ratio: 1 / 1 !important;
    width: 100% !important;
    min-width: 0 !important;
    border-radius: 50% !important;
    background-color: #2b2b2b !important;
    color: white !important;
}

.calc-btn-op button {
    color: #4ECDC4 !important;
}

.calc-btn-clear button {
    color: #FF6B6B !important;
}

.calc-btn-equals button {
    background-color: #1E9E8C !important;
    color: white !important;
}

@media (max-width: 600px) {
    .gradio-container {
        max-width: 100% !important;
        padding: 10px !important;
    }

    #calc-display textarea {
        font-size: 38px !important;
    }
}
"""


# -----------------------------
# Gradio application
# -----------------------------
with gr.Blocks(
    css=custom_css,
    theme=gr.themes.Base()
) as demo:

    display = gr.Textbox(
        value="0",
        elem_id="calc-display",
        show_label=False,
        interactive=False
    )

    with gr.Row(elem_id="calc-grid"):

        c_btn = gr.Button(
            "C",
            elem_classes=["calc-btn", "calc-btn-clear"]
        )

        del_btn = gr.Button(
            "⌫",
            elem_classes=["calc-btn", "calc-btn-clear"]
        )

        pct_btn = gr.Button(
            "%",
            elem_classes=["calc-btn", "calc-btn-op"]
        )

        div_btn = gr.Button(
            "÷",
            elem_classes=["calc-btn", "calc-btn-op"]
        )

        b7 = gr.Button("7", elem_classes="calc-btn")
        b8 = gr.Button("8", elem_classes="calc-btn")
        b9 = gr.Button("9", elem_classes="calc-btn")

        mul_btn = gr.Button(
            "×",
            elem_classes=["calc-btn", "calc-btn-op"]
        )

        b4 = gr.Button("4", elem_classes="calc-btn")
        b5 = gr.Button("5", elem_classes="calc-btn")
        b6 = gr.Button("6", elem_classes="calc-btn")

        sub_btn = gr.Button(
            "−",
            elem_classes=["calc-btn", "calc-btn-op"]
        )

        b1 = gr.Button("1", elem_classes="calc-btn")
        b2 = gr.Button("2", elem_classes="calc-btn")
        b3 = gr.Button("3", elem_classes="calc-btn")

        add_btn = gr.Button(
            "+",
            elem_classes=["calc-btn", "calc-btn-op"]
        )

        paren_btn = gr.Button(
            "()",
            elem_classes="calc-btn"
        )

        b0 = gr.Button(
            "0",
            elem_classes="calc-btn"
        )

        dot_btn = gr.Button(
            ".",
            elem_classes="calc-btn"
        )

        eq_btn = gr.Button(
            "=",
            elem_classes=["calc-btn", "calc-btn-equals"]
        )


    # -----------------------------
    # Connect buttons
    # -----------------------------
    buttons = [
        c_btn,
        del_btn,
        pct_btn,
        div_btn,

        b7,
        b8,
        b9,
        mul_btn,

        b4,
        b5,
        b6,
        sub_btn,

        b1,
        b2,
        b3,
        add_btn,

        paren_btn,
        b0,
        dot_btn,
        eq_btn
    ]

    for button in buttons:
        button.click(
            fn=press,
            inputs=[display, button],
            outputs=display
        )


# -----------------------------
# Start application
# -----------------------------
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
