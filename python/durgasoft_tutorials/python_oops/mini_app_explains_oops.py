class Movie:
	def __init__(self,title,hero,heroine):
		self.title = title
		self.hero = hero
		self.heroine = heroine
	def info(self):
		print("Movie Name is:", self.title)
		print("Hero Name is:", self.hero)
		print("Heroine Name is:", self.heroine)

list_of_movies = []
while True:
	title = input("Enter the Movie title: ")
	hero = input("Enter the Hero Name: ")
	heroine = input("Enter the Heroine Name: ")
	m = Movie(title,hero,heroine)
	# this is same as taking t=Test from the previos examples
	list_of_movies.append(m)
	print("Movies added successfully..")
	option = input("Do you want to add more movies[yes/no] ")
	if option.lower() == 'no':
		break

print("All movies added")
print(m)
for x in list_of_movies:
	x.info()
	# this is like t.m1()
	print()