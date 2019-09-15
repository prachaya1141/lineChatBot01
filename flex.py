def setbubble(Primary,Secondary,Volumn,Change,Price):
    bubble_data =   {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "image",
                    "url": "https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fspecials-images.forbesimg.com%2Fdam%2Fimageserve%2F1173135847%2F960x0.jpg%3Ffit%3Dscale",
                    "size": "full",
                    "aspectMode": "cover",
                    "aspectRatio": "150:196",
                    "gravity": "center",
                    "flex": 1
                },
                {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "text",
                        "text": "NEW",
                        "size": "xs",
                        "color": "#ffffff",
                        "align": "center",
                        "gravity": "center"
                    }
                    ],
                    "backgroundColor": "#EC3D44",
                    "paddingAll": "2px",
                    "paddingStart": "4px",
                    "paddingEnd": "4px",
                    "flex": 0,
                    "position": "absolute",
                    "offsetStart": "18px",
                    "offsetTop": "18px",
                    "cornerRadius": "100px",
                    "width": "48px",
                    "height": "25px"
                }
                ],
                "height": "200px"
            }
            ],
            "paddingAll": "0px"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "contents": [],
                        "size": "xl",
                        "wrap": True,
                        "text": "BTC VS THB",
                        "color": "#ffffff",
                        "weight": "bold"
                    },
                    {
                        "type": "text",
                        "text": "PRICE = 300,00 THB",
                        "color": "#ffffffcc",
                        "size": "sm"
                    }
                    ],
                    "spacing": "sm"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "contents": [],
                            "size": "sm",
                            "wrap": True,
                            "margin": "lg",
                            "color": "#ffffffde",
                            "text": "Volume=n : {}".format(Volumn)
                        },
                        {
                            "type": "text",
                            "text": "Change : {}".format(Change),
                            "color": "#FD7171",
                            # "color": "{}".format(['#FD7171' if '-' in Change else '#24FF00'][0]),
                            "size": "sm"
                        }
                        ]
                    }
                    ],
                    "paddingAll": "13px",
                    "backgroundColor": "#ffffff1A",
                    "cornerRadius": "2px",
                    "margin": "xl"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "uri",
                    "label": "ตรวจสอบ",
                    "uri": "http://linecorp.com/"
                    },
                    "position": "relative",
                    "margin": "lg",
                    "style": "secondary"
                }
                ]
            }
            ],
            "paddingAll": "20px",
            "backgroundColor": "#464F69"
        }
        }
    return bubble_data
def flex():
    flex_data = {
    "type": "carousel",
    "contents": [
    ]
    }
    