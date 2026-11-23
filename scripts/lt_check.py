"""LanguageTool (en-GB) check of every spoken line and every on-screen text of ep. 002.
Usage: python scripts/lt_check.py out.md"""
import ast, json, re, sys
import language_tool_python
items = [(f"voice {x['id']}", x["text"]) for x in json.load(open("sound/ep002/ep002_lines.json"))]
for f in ["graphics/motion/ep002.py", "graphics/motion/scenes_ep002.py"]:
    tree = ast.parse(open(f).read())
    docs = {id(n.body[0].value) for n in ast.walk(tree)
            if isinstance(n, (ast.FunctionDef, ast.Module, ast.ClassDef)) and n.body
            and isinstance(n.body[0], ast.Expr) and isinstance(n.body[0].value, ast.Constant)}
    seen = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs:
            s = n.value.strip()
            if s in seen or len(s) < 3 or not re.search(r"[A-Za-z]{3}", s): continue
            if re.fullmatch(r"[a-z0-9_./\-]+", s) or s.startswith(("#", "%", "[S")): continue
            if "FLASH" in s or "fix the cut" in s: continue
            seen.add(s); items.append((f"screen {f.split('/')[-1]}:{n.lineno}", s))
tool = language_tool_python.LanguageTool("en-GB")
IGNORE = {"MORFOLOGIK_RULE_EN_GB"}   # spelling: names listed separately below
rows, spell = [], {}
for where, text in items:
    for m in tool.check(text):
        bad = text[m.offset:m.offset + getattr(m, "error_length", None) or m.errorLength]
        if getattr(m, "rule_id", None) or m.ruleId in IGNORE:
            spell.setdefault(bad, []).append(where); continue
        rows.append(f"| {where} | {getattr(m, "rule_id", None) or m.ruleId} | `{bad}` → {', '.join(m.replacements[:3]) or '—'} | {m.message} | {text} |")
out = f"# LanguageTool en-GB · {len(items)} texts\n\n## Grammar / style ({len(rows)})\n\n| where | rule | text → suggestion | message | full text |\n|---|---|---|---|---|\n"
out += "\n".join(rows) + f"\n\n## Unknown words ({len(spell)})\n\n" + "\n".join(f"- `{w}` ({len(v)}×): {', '.join(v[:4])}" for w, v in sorted(spell.items()))
open(sys.argv[1], "w").write(out + "\n"); print(out)
