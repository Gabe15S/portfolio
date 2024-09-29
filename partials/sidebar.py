import flet as ft
from components.skills import SkillRing, SkillProgressBar

class SidebarHeader(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Badge(
                        content=ft.Image(
                            src='images/Gabe_1.jpg',
                            border_radius=ft.border_radius.all(100),
                            width=100,
                        ),                        
                        alignment=ft.alignment.bottom_right,
                        bgcolor=ft.colors.PRIMARY,
                        small_size=20,
                    ),
                    ft.Text(value='Gabriel de Souza', theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(value='Desenvolvedor Python', theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding= ft.padding.symmetric(vertical=20, horizontal=40),
            alignment=ft.alignment.center,
        )


class SidebarContent(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.expand= True

    def build(self):
        location = ft.Column(
            # Depois fazer uma função para atualizar os dados de localização atual e idade
            controls=[
                ft.Row(
                    controls=[ft.Text(value="Residência: ", theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value="Brasil", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[ft.Text(value="Cidade: ", theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value="São Paulo", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Row(
                    controls=[ft.Text(value="Idade: ", theme_style=ft.TextThemeStyle.BODY_LARGE),
                        ft.Text(value="30", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                    ],
                    alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ]
        )

        languages = ft.Row(
            controls=[
                SkillRing(title='Português Brasileiro', value=1),                
                SkillRing(title='Inglês', value=0.9),                
            ]
        )

        skills = ft.Column(
            controls=[
                SkillProgressBar(title="Python", value=.5)
            ]
        )

        technologies = ft.Column(
            controls=[
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text(value="Selenium, Pandas, Numpy, Flet. Loguru", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text(value="RPA - Robotic Process Automation / Data Scraping", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text(value="Regex - Regular Expression", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text(value="Jira Software", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text(value="Versionamento com GIT", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text(value="UI / UX", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
                ft.ListTile(
                    leading=ft.Icon(name=ft.icons.CHECK, color=ft.colors.PRIMARY),
                    title=ft.Text(value="QA - Quality Assurance", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
        )

        # cv = ft.TextButton(
        #     text="Download CV",
        #     style=ft.ButtonStyle(color=ft.colors.GREY),
        #     icon= ft.icons.DOWNLOAD,
        #     icon_color=ft.colors.GREY,
        #     url="", # Colocar aqui a url gerada no link abaixo

        #     # https://sites.google.com/site/gdocs2direct/?pli=1
        #     # ver ma aula 73, por volta de 1h06min como colocar o curriculo no drive e compartilhar ele e gerar o link para colocar na url
        # )

        return ft.Container(
            bgcolor=ft.colors.BLACK12,
            padding=ft.padding.all(20),
            content=ft.Column(
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    location,
                    ft.Divider(height=30),
                    languages,
                    ft.Divider(height=30),
                    skills,
                    ft.Divider(height=30),
                    technologies,
                    # ft.Divider(height=30),
                    # cv,
                ]
            )
        )
    


class SidebarFooter(ft.UserControl):
    def build(self):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=10),
            content=ft.Row(
                controls=[
                    ft.TextButton(
                        text="Download CV",
                        style=ft.ButtonStyle(color=ft.colors.PRIMARY),
                        icon= ft.icons.DOWNLOAD,
                        icon_color=ft.colors.PRIMARY,
                        # url="https://drive.google.com/uc?export=download&id=1tDLMsCLTVwA6WVmsBR7cZX1Sxuz0QBfR",
                        url='https://drive.google.com/file/d/1tDLMsCLTVwA6WVmsBR7cZX1Sxuz0QBfR/view?usp=drive_link,'
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/002-linkedin.png', height=15, color=ft.colors.PRIMARY),
                        url="https://www.linkedin.com/in/gabes15/"
                    ),
                    ft.IconButton(
                        content=ft.Image(src='icons/003-github.png', height=15, color=ft.colors.PRIMARY),
                        url="https://github.com/Gabe15S"
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )


class Sidebar(ft.UserControl):
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    SidebarHeader(),
                    SidebarContent(),
                    SidebarFooter(),
                ]
            ),
            bgcolor= ft.colors.BACKGROUND,
        )
    