def setbubble(Primary,Secondary,Volumn,Change,Price):
    Change_color = ['#FD7171' if '-' in str(Change) else '#24FF00'][0]
    bubble_data = {
      "type": "bubble",
      "size": "kilo",
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
                    "text": "HOT PRICE",
                    "size": "xs",
                    "color": "#ffffff",
                    "align": "center",
                    "gravity": "center",
                    "wrap": True
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
                "width": "100px",
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
                    "text": "{} VS {}".format(Primary,Secondary),
                    "color": "#ffffff",
                    "weight": "bold"
                  },
                  {
                    "type": "text",
                    "text": "PRICE : {} THB".format(Price),
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
                        "text": "Volumn : {}".format(Volumn)
                      },
                      {
                        "type": "text",
                        "text": "Change : {}".format(Change),
                        "color": "{}".format(Change_color) ##สีเขียว#24FF00 + สีแดง#FF8484 -
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
                  "label": "ตรวจสอบกราฟ",
                  "uri": "https://bx.in.th"
                },
                "style": "secondary",
                "margin": "lg"
              }
            ]
          }
        ],
        "paddingAll": "20px",
        "backgroundColor": "#464F69"
      }
    }
    return bubble_data



def setCarousel(data):
    carousel_data = {
    "type": "carousel",
    "contents": []
    }

    flexdata = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": ''
    }

    # loop 
    # for i in getbtc....
    # carousel_data['contents'].append(setbubble(i['prim_name'],......))
    # flexdata[0]['contents'] = carousel_data


    for i in data:
        bubble_data = setbubble(
            Primary = i['prim_name'],
            Secondary = i['sec_name'],
            Volumn = i['volume'],
            Change = i['change'],
            Price= i['last_price']
        )
        carousel_data['contents'].append(bubble_data)
    
    flexdata["contents"] = carousel_data

    return flexdata