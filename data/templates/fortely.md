{% macro sentence_case(text) %}
    {{- text[0]|upper}}{{text[1:] -}}
{% endmacro %}
#### 🟣 {{ sentence_case(név) }} ({{maxfok}})

{{leírás}}

| |  Követelmény | Hatás  |
| :----------- | :----------- | :----------- |
{% for item in fokok -%}
|
{%- if item.fok > 0 -%}
{{ item.fok }}.fok |
{%- else -%}
Alapeset |
{%- endif %}
{{- item.követelménytext -}} {{ "<br />" if item.követelménytext }}
{%- for kov in item.követelmények if item.követelmények and True == kov.enabled -%}
{{ sentence_case(kov.név) }}: {{ kov.érték }}
{%- if kov.text -%}
{{" "}} ({{ kov.text }})
{%- endif -%}
<br />
{%- endfor -%}
 | {%- for hattext in item.hatástext if item.hatástext -%}
{{ hattext.text }}<br />
{%- endfor -%}
{%- for hat in item.hatások if item.hatások and True == hat.enabled  -%}
{{ sentence_case(hat.név) }}: {{ hat.érték }}
{%- if hat.text -%}
{{" "}} ({{ hat.text }})
{%- endif -%}
<br />
{%- endfor -%}
 |
{% endfor %}
<br />

**Megjegyzések**

{% for megjegyzés in megjegyzések -%}
- {{ megjegyzés.text }}
{% endfor %}
<br />

---
