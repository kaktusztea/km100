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
{{ sentence_case(kov.név) }}: {% if kov.érték > 0 and kov.típus in [1, 51, 52, 53, 54, 55]%}+{% endif %}{{ kov.érték -}}
{%- if kov.típus == 2 -%}
.szint
{%- endif -%}
{%- if kov.text -%}
{{" "}} ({{ kov.text }})
{%- endif -%}
<br />
{%- endfor -%}
 | {%- for hattext in item.hatástext if item.hatástext -%}
{{ hattext.text }} {{ "<br />" if hattext.text }}
{%- endfor -%}
{%- for hat in item.hatások if item.hatások and True == hat.enabled  -%}
{{ sentence_case(hat.név) }}: `{% if hat.érték > 0 and hat.típus in [1, 51, 52, 53, 54, 55, 555] %}+{% endif %}{{ hat.érték }}`
{%- if hat.text -%}
{{" "}} ({{ hat.text }})
{%- endif -%}
<br />
{%- endfor -%}
{%- for khat in item.kombihatások if item.kombihatások and True == khat.enabled -%}
{{ sentence_case(khat.forrásnév) }} x {{ khat.bónuszarány }} → +{{ khat.célnév }}
{%- if khat.text -%}
{{" "}} ({{ khat.text }})
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
