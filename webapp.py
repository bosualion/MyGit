from flet import *
def main(page:Page):
    category_card = Column()
    category = ['Start','Stop','Off']
    for i, cate in enumerate (category):
        category_card.controls.append(
            Container (
                border_radius=35,
                bgcolor='red',
                height=100,
                width=200,
                padding=15,
                content= Column(
                    controls=[
                        Text(cate),
                        Container(
                            width=180,
                            height=20,
                            bgcolor="white",
                            border_radius=35,
                            padding=padding.only(right=i*30),
                            content= Container(
                                bgcolor="green",

                            )
                        )

                    ]
                )

            )
        )
    first_page_content = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(
                                icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATION_IMPORTANT_OUTLINED)
                            ]
                        ),
                    ]
                ),
                Container(
                    height=20
                ),
                Text(
                    value="Hello"
                ),
                Text(
                    value="My name is ESP32 CAM"
                ),
                Container(
                    padding = padding.only(
                        top=10,bottom=20
                    ),
                    content=category_card
                )
            ]
        )
    )
    page1 = Container()
    page2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor='blue',
                border_radius=35,
                padding=padding.only(
                    top=50,
                    left=20,
                    right=20,
                    bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_content
                    ]
                )
            )
       ]
    )
    container = Container(
        width=400,
        height=850,
        bgcolor='blue',
        border_radius=35,
        content=Stack(
            controls=[
                page1,
                page2
            ]
        )
    )
    page.add(container)
app(target=main)