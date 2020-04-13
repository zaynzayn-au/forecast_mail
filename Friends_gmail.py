import pyowm
from gmail import GMail, Message

owm = pyowm.OWM('3d2e01eac301a7de4720f37117917f56')

def get_forecast():
	fcst = owm.three_hours_forecast('Sydney')
	forecast_message = '\n\n***阳间天气预测***\n\n\n'

	if fcst.will_have_rain():
		for f in fcst.when_rain():
			forecast_message += ('{} {}\n'.format(f.get_reference_time('iso'), f.get_status()))
		forecast_message += '\n 要下雨啦，请不要带伞哦'
	else:
		forecast_message += '\n 接下来五天不会下雨，请带伞出门增加负重哦'
	return forecast_message

def send_email(message):
    gmail = GMail(
        username = 'yz.huang1218@gmail.com',
        password = 'Aa941218**'
    )
    with open('friends.txt','r') as f:
        for friend in f:
            name = friend.split('s')[0].strip().title()
            email = friend.split(',')[1].strip()
            msg = Message(subject='***阳间天气预测资料***',
                          sender=gmail.username,
                          to=email,
                          text=message)
            print('Sending email to {}'.format(name))
            gmail.send(msg)

if __name__ == '__main__':
	print('正在为您收集天气资料...')
	msg = get_forecast()

	print('正在传送天气资料奥利给...')
	send_email(msg)

	print('Done')