---
title: Home
permalink: /
---

# Poster repo.

Trying out some initial manoevres.

| Post | Link |
| --- | --- |
{% assign posts = site.posts | sort: "title" %}
{% for post in posts %}
| {{ post.title | escape }} | [View post]({{ post.url | relative_url }}) |
{% endfor %}
