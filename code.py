import web
import chemweight

urls = (
	'/', 'index',
	'/calculate/(.*)', 'calculate'
)
app = web.application(urls, globals())

class index:
	def GET(self):
		return open('static/index.html').read()

class calculate:
	def GET(self, chem):
		return chemweight.calculate_weight(chem)

if __name__ == "__main__":
	app.run()
