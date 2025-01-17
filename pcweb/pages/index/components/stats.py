import reflex as rx

from pcweb.components.webpage.pill import pill

github_url = "https://github.com/reflex-dev/reflex"
features_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen"
contribution_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22"
bugs_url = "https://github.com/reflex-dev/reflex/issues?q=is%3Aopen+is%3Aissue"


def user_count_item(count, platform) -> rx.Component:
    return rx.flex(
        rx.text(f"{count}+", color="var(--c-slate-11)", font_size="32px"),
        rx.text(platform, color="var(--c-slate-9)"),
        direction="column",
        align="center",
    )


def user_count_comp() -> rx.Component:
    return rx.center(
        rx.tablet_and_desktop(user_count_item(110, "Contributors")),
        rx.mobile_only(user_count_item(110, "Contributors")),
        rx.divider(size="4", orientation="vertical"),
        rx.tablet_and_desktop(user_count_item(5000, "Project created per month")),
        rx.mobile_only(user_count_item(5000, "Project")),
        rx.divider(size="4", orientation="vertical"),
        rx.tablet_and_desktop(user_count_item(3700, "Discord Members")),
        rx.mobile_only(user_count_item(3700, "On Discord")),
        spacing="5",
        padding="1em",
    )


def open_source_badge() -> rx.Component:
    return rx.button(
        rx.flex(
            rx.text(
                "Open Source",
                color="transparent",
                font_size="14px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.28px",
                background="linear-gradient(95deg, #B1A9FB 25.71%, #867BF1 83.81%);",
                background_clip="text",
                _webkit_background_clip="text",
            ),
            height="31px",
            padding="0px 10px",
            justify="center",
            align="center",
            gap="10px",
            border_radius="15px",
            border="1px solid #4435D4",
            background="linear-gradient(180deg, rgba(97, 81, 243, 0.20) 0%, rgba(86, 70, 237, 0.20) 100%);",
            box_shadow="0px 0px 4px -1px rgba(27, 21, 90, 0.40), 0px 3px 6px -3px rgba(34, 25, 121, 0.60);",
        ),
        background="transparent",
        on_click=rx.redirect(
            github_url,
            external=True,
        ),
        _hover={
            "cursor": "pointer",
        },
    )


def github_button() -> rx.Component:
    return rx.button(
        rx.flex(
            rx.image(src="/companies/light/github.svg", height="20px", width="20px"),
            rx.center(
                "Github",
                color="var(--c-slate-11)",
                font_size="14px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.28px",
            ),
            rx.center(
                "15.7k",
                color="var(--c-violet-10)",
                font_size="12px",
                font_style="normal",
                font_weight="400",
                line_height="normal",
                letter_spacing="-0.24px",
            ),
            spacing="2",
        ),
        position="relative",
        top="32px",
        right="-140px",
        z_index="999",
        padding="var(--Space-4, 16px);",
        align="center",
        width="151px",
        height="42px",
        border_radius="70px",
        border="1px solid var(--c-slate-5)",
        class_name="bg-slate-2 shadow-small",
        on_click=rx.redirect(
            github_url,
            external=True,
        ),
        _hover={
            "cursor": "pointer",
        },
    )


def invite_message() -> rx.Component:
    return rx.box(
        rx.text(
            "Contribute to our open-source community.",
            color="var(--c-slate-11)",
            font_size="38px",
            weight="bold",
            align="center",
            line_height="1",
        ),
        width="30em",
    )


def request_buttons() -> rx.Component:
    return rx.hstack(
        rx.button(
            "Bugs",
            weight="Medium",
            height="24px",
            width="138px",
            color_scheme="blue",
            variant="surface",
            on_click=rx.redirect(
                bugs_url,
                external=True,
            ),
            _hover={
                "cursor": "pointer",
            },
        ),
        rx.button(
            "Good First Issues",
            weight="Medium",
            height="24px",
            color_scheme="green",
            variant="surface",
            on_click=rx.redirect(
                contribution_url,
                external=True,
            ),
            _hover={
                "cursor": "pointer",
            },
        ),
    )


def invite_card_comp() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.text(
                "Contribute to Reflex!",
                color="var(--c-slate-11)",
                weight="medium",
            ),
            request_buttons(),
            rx.text(
                "Start contributing today, checkout our Github for Details",
                color="var(--c-slate-10)",
                weight="medium",
            ),
            justify="start",
            direction="column",
            spacing="2",
        ),
        border_radius="10px",
        padding="1em",
        width="30em",
        border="1px solid var(--c-slate-5);",
        # background="linear-gradient(218deg, #1D1B23 -35.66%, #131217 100.84%);",
        class_name="bg-slate-2 shadow-large",
    )


def stats() -> rx.Component:
    return rx.vstack(
        # open_source_badge(),
        pill(text="Open Source"),
        invite_message(),
        github_button(),
        invite_card_comp(),
        user_count_comp(),
        padding="2em",
        style={
            "@media screen and (max-width: 1024px)": {
                "transform": "scale(0.9)",
            },
            "@media screen and (max-width: 837px)": {
                "transform": "scale(0.85)",
            },
            "@media screen and (max-width: 768px)": {
                "transform": "scale(0.8)",
            },
            "@media screen and (max-width: 627px)": {
                "transform": "scale(0.75)",
            },
            "@media screen and (max-width: 480px)": {
                "transform": "scale(0.65)",
            },
        },
    )
