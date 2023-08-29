============================
Standard Column Descriptions
============================

This file is an auto-generated version of `column_descriptions.csv`_,
which contains the descriptions of table column names regardless of
what file(s) they appear in.

.. _`column_descriptions.csv`: https://github.com/desihub/desidatamodel/blob/main/py/desidatamodel/data/column_descriptions.csv

{% for row in reader %}
{% if loop.first %}
{{ separator }}
{% endif %}
{{ format_string.format(*row) }}
{% if loop.first %}
{{ separator }}
{% endif %}
{% if loop.last %}
{{ separator }}
{% endif %}
{% endfor %}
