---
components:
    - rx.Html
---

```python exec
import reflex as rx
from pcweb.templates.docpage import docdemo_from
from pcweb.pages.docs import styling
```

# HTML 

The HTML component can be used to render raw HTML code. 

Before you reach for this component, consider using Reflex's raw HTML element support instead.

```python demo
rx.vstack(
    rx.html("<h1>Hello World</h1>"),
    rx.html("<h2>Hello World</h2>"),
    rx.html("<h3>Hello World</h3>"),
    rx.html("<h4>Hello World</h4>"),
    rx.html("<h5>Hello World</h5>"),
    rx.html("<h6>Hello World</h6>"),
)
```

```python eval
rx.alert(
    rx.alert_icon(),
    rx.box(
        rx.alert_title("Missing Styles?"),
        rx.alert_description(
            rx.markdown(
                "Reflex uses Chakra-UI and Tailwind for styling, both of "
                "which reset default styles for headings. If you are "
                "using the html component and want pretty default "
                "styles, consider setting `class_name='prose'` "
                ", adding `@tailwindcss/typography` package to "
                "`frontend_packages` and enabling it via `tailwind` "
                "config in `rxconfig.py`. See the "
                "[Tailwind docs]({styling.overview.path}) for an example of adding this plugin."
            ),
        )
    )
)
```

In this example, we render an image.

```python demo
rx.html("<img src='https://reflex.dev/reflex_banner.png' />")
```