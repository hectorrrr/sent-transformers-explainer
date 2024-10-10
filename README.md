# sent-transformers-explainer
This repository contains an implementation of a method to explain sentence-transformers relevance of Inputs.


<style>\n    .word {\n        cursor: pointer;\n        padding: 2px 4px;\n        border-radius: 4px;\n        position: relative;\n        display: inline-block;\n        text-decoration: none; /* Remove any text decoration like line-through */\n    }\n    .word:hover::after {\n        content: attr(data-tooltip);\n        position: absolute;\n        top: -35px;\n        left: 0;\n        background: #333;\n        color: #fff;\n        padding: 5px 10px;\n        border-radius: 4px;\n        white-space: nowrap;\n        z-index: 10;\n        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);\n        font-size: 12px;\n    }\n    </style>\n    <table width=\'100%\' style=\'border-collapse: collapse; margin-top: 20px;\'><tr><th>True Label</th><th>Predicted Label</th><th>Word Importance</th><tr><td style=\'padding: 5px 10px;\'>1.0</td><td style=\'padding: 5px 10px;\'>1 (0.64)</td><td><span class=\'word\' style=\'padding: 2px 4px;\'>[CLS]</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.48965564127486005); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.49\'>discovering</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.7628632071477993); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.76\'>sentence</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.21684798897099714); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.22\'>meaning</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.18407592577718224); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.18\'>,</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.13665489133561112); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.14\'>one</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.16509186059987302); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.17\'>word</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.16934483485599225); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.17\'>at</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.13370410645376962); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.13\'>a</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.04820539824234946); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.05\'>time</span> <span class=\'word\' style=\'background-color: rgba(60, 179, 113, 0.05061600556547035); color: white; padding: 2px 4px; border-radius: 4px;\' data-tooltip=\'Importance: 0.05\'>.</span> <span class=\'word\' style=\'padding: 2px 4px;\'>[SEP]</span></td></tr></table><div style="border-top: 1px solid; margin-top: 20px;             padding-top: 10px; display: inline-block; font-size: 14px;"><b>Legend: </b><span style="display: inline-block; width: 12px; height: 12px;                 border: 1px solid #000; margin-right: 5px; background-color:                 rgba(255, 99, 71, 1)"></span> Negative  <span style="display: inline-block; width: 12px; height: 12px;                 border: 1px solid #000; margin-right: 5px; background-color:                 transparent"></span> Neutral  <span style="display: inline-block; width: 12px; height: 12px;                 border: 1px solid #000; margin-right: 5px; background-color:                 rgba(60, 179, 113, 1)"></span> Positive  </div>

