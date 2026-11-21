import re, sys, markdown
src, out = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf-8').read()
# Drop the agent-facing part (Del 2) — the PDF is for the human.
t = re.sub(r'\n# Del 2:.*?(?=\n# Del 3:)', '\n', t, flags=re.S)
t = re.sub(r'(?m)^   (?=\S)', '    ', t)  # python-markdown wants 4-space nesting
t = t.replace('🚨', '⚠').replace('🆘', '☎')
body = markdown.markdown(t, extensions=['tables', 'fenced_code', 'sane_lists'])
css = """
@page { size: A4; margin: 18mm 17mm 18mm 17mm; }
body { font-family: 'DejaVu Sans', 'Liberation Sans', sans-serif; font-size: 10.5pt; line-height: 1.5; color: #1d2430; }
h1 { font-size: 20pt; color: #0b4f6c; border-bottom: 3px solid #0b4f6c; padding-bottom: 4px; margin-top: 0; }
h1 + p { font-size: 11.5pt; }
h2 { font-size: 13.5pt; color: #0b4f6c; margin-top: 20px; break-after: avoid; }
h3 { font-size: 11.5pt; margin-top: 14px; break-after: avoid; }
h1:not(:first-of-type) { break-before: page; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 9pt; background: #eef2f6; padding: 1px 4px; border-radius: 3px; }
pre { background: #eef2f6; border-left: 4px solid #0b4f6c; padding: 8px 10px; border-radius: 4px; white-space: pre-wrap; word-break: break-word; break-inside: avoid; }
p code, li code, td code { white-space: nowrap; }
pre code { background: none; padding: 0; white-space: pre-wrap; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; break-inside: avoid; }
th, td { border: 1px solid #c9d3dd; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #dde7ef; }
blockquote { margin: 10px 0; padding: 8px 12px; background: #fff6e0; border-left: 4px solid #e0a100; border-radius: 4px; break-inside: avoid; }
blockquote p { margin: 4px 0; }
li { margin: 3px 0; }
a { color: #0b6e99; text-decoration: none; }
hr { display: none; }
p:has(> strong:only-child) { break-after: avoid; }
"""
html = f'<!doctype html><html lang="da"><head><meta charset="utf-8"><title>Din egen AI-hjælper til Home Assistant</title><style>{css}</style></head><body>{body}</body></html>'
open(out, 'w', encoding='utf-8').write(html)
