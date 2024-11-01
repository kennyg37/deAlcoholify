from dash import html
import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("My Dash App", href="/"),
            dbc.Nav(
                [
                    dbc.NavLink("Link 1", href="#"),
                    dbc.NavLink("Link 2", href="#"),
                ],
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    style={"margin-bottom": "20px"},
)
