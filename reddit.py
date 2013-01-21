import web

urls = (
	"/",  "index",
	"/new",  "new",
	"/(.*)/vote", "vote",
	"/(.*)", "post"
)

app = web.application(urls, globals())
render = web.template.render('templates/')
def upperTitle(s):
	return s.upper()


db = web.database(dbn="sqlite", db="reddit.db")

class index:
	def GET(self):
		posts = db.select("posts")
		modules = {'new_post': render.new(), 'posts': render.post(posts)}
		return render.page(modules)

class vote:
	def POST(self, id):
		response = "Post with id=%s has been" %(id)
		i = web.input(action="up")
		if i.action == "up":
			db.query("UPDATE posts SET votes=votes+1 WHERE id=$id", {"id": id})
			print response, "Up Voted!!!"
			return "1"
		elif i.action == "down":
			db.query("UPDATE posts SET votes=votes-1 WHERE id=$id", {"id": id})
			print response, "Down Voted!!!"
			return "-1"
		else:
			print response, " called with an Undefined Action!!!"
			return "0"

class post:
	def GET(self, id):
		return "Hello %s" % id

class new:
	def GET(self):
		return render.page(render.new())

	def POST(self):
		i = web.input()
		db.insert("posts", title=i.title, url=i.url)
		raise web.seeother("/")

if __name__ == "__main__":
	app.run()
