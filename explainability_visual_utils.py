from typing import Iterable
from IPython.display import display, HTML

def format_classname(classname):
    """Helper function to format class names as HTML."""
    return f"<td style='padding: 5px 10px;'>{classname}</td>"

def _get_color(value):
    """Return a color based on the attribution value."""
    # Example color map: Red for negative, Green for positive
    if value < 0:
        return "rgba(255, 99, 71, {0})".format(abs(value))  # Tomato red
    elif value > 0:
        return "rgba(60, 179, 113, {0})".format(value)  # Medium sea green
    return "transparent"  # No color for zero attribution


def format_special_tokens(token):
    if token.startswith("<") and token.endswith(">"):
        return "#" + token.strip("<>")
    return token

def format_word_importances(words, importances):
    """Format words with their importances as HTML elements with hover effects."""
    formatted_words = []
    for word, importance in zip(words, importances):
        word = format_special_tokens(word)
        
        
        # Display the word with a tooltip showing its importance when hovered
        if importance == 0:
            # No background color for zero attribution
            formatted_words.append(
                f"<span class='word' style='padding: 2px 4px;'>{word}</span>"
            )
        else:
            formatted_words.append(
                f"<span class='word' style='background-color: {_get_color(importance)}; color: white; padding: 2px 4px; border-radius: 4px;' data-tooltip='Importance: {importance:.2f}'>{word}</span>"
            )
    # print("Formatted words--->",formatted_words)
    return "<td>" + " ".join(formatted_words) + "</td>"

def visualize_text_v2(datarecords: Iterable, legend: bool = True) -> "HTML":
    # assert "IPython" in globals(), (
    #     "IPython must be available to visualize text. "
    #     "Please run 'pip install ipython'."
    # )
    dom = ["<table width='100%' style='border-collapse: collapse; margin-top: 20px;'>"]
    rows = [
        "<tr><th>True Label</th>"
        "<th>Predicted Label</th>"
        "<th>Word Importance</th>"
    ]
    for datarecord in datarecords:
        rows.append(
            "".join(
                [
                    "<tr>",
                    format_classname(datarecord.true_class),
                    format_classname(
                        "{0} ({1:.2f})".format(
                            datarecord.pred_class, datarecord.pred_prob
                        )
                    ),
                    format_word_importances(
                        datarecord.raw_input_ids, datarecord.word_attributions
                    ),
                    "</tr>",
                ]
            )
        )

    print("Generated rows--->",rows)

    dom.append("".join(rows))
    dom.append("</table>")

    if legend:
        dom.append(
            '<div style="border-top: 1px solid; margin-top: 20px; \
            padding-top: 10px; display: inline-block; font-size: 14px;">'
        )
        dom.append("<b>Legend: </b>")

        for value, label in zip([-1, 0, 1], ["Negative", "Neutral", "Positive"]):
            dom.append(
                '<span style="display: inline-block; width: 12px; height: 12px; \
                border: 1px solid #000; margin-right: 5px; background-color: \
                {value}"></span> {label}  '.format(
                    value=_get_color(value), label=label
                )
            )
        dom.append("</div>")

    # Add custom CSS and JavaScript for tooltips
    tooltip_css = """
    <style>
    .word {
        cursor: pointer;
        padding: 2px 4px;
        border-radius: 4px;
        position: relative;
        display: inline-block;
        text-decoration: none; /* Remove any text decoration like line-through */
    }
    .word:hover::after {
        content: attr(data-tooltip);
        position: absolute;
        top: -35px;
        left: 0;
        background: #333;
        color: #fff;
        padding: 5px 10px;
        border-radius: 4px;
        white-space: nowrap;
        z-index: 10;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        font-size: 12px;
    }
    </style>
    """

    dom.insert(0, tooltip_css)  # Insert CSS at the top

    html = HTML("".join(dom))
    display(html)

    return html