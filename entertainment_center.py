#Enmanuel Hernandez
#Movie trailer project.
#

import media
import fresh_tomatoes


#Creates an object for each movie tittle with four attributes by using the Movie class from the media.py

the_300 = media.Movie(
	"300",
	"King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
	"https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
	"https://www.youtube.com/watch?v=ZJ6yq-oVKPc"
	)

the_avengers = media.Movie(
	"The Avengers",
	"A group of superheroes forms a group to protect the earth from alien destruction",
	"https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
	"https://www.youtube.com/watch?v=hIR8Ar-Z4hw"
)

iron_man = media.Movie(
	"Iron Man",
	"Tony Stark, who has inherited the defense contractor Stark Industries from his father, gets kidnapped by war terrorist.",
	"https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
	"https://www.youtube.com/watch?v=8hYlB38asDY"
)

skyfall = media.Movie(
	"SkyFall",
	"MI6 agents James Bond and Eve Moneypenny pursue mercenary Patrice, who has stolen a hard drive containing details of undercover agents",
	"https://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg",
	"https://www.youtube.com/watch?v=6kw1UVovByw"
)

the_dark_night = media.Movie(
	"The Dark Night Rises",
	"Eight years after the death of District Attorney Harvey Dent, Batman has disappeared and organized crime has been eradicated in Gotham City thanks to the Dent Act.",
	"https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
	"https://www.youtube.com/watch?v=GokKUqLcvD8"
)

logan = media.Movie(
	"Logan",
	"In 2029, no mutants have been born in 25 years. Logan's healing ability has slowed and his body has aged; he spends his days drinking and working as a limo driver in El Paso, Texas.",
	"https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
	"https://www.youtube.com/watch?v=Div0iP65aZo"
)

the_pursuit = media.Movie(
	"The Pursuit of Happyness",
	"In 1981, San Francisco salesman Chris Gardner fight through many adversities untill he becomes a successful broker",
	"https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
	"https://www.youtube.com/watch?v=89Kq8SDyvfg"
	)
stand_and_deliver = media.Movie(
	"Stand and Deliver",
	"Escalante (Olmos) becomes a math teacher at James A. Garfield High School in East Los Angeles.Escalante seeks to change the school culture to help the students excel in academics",
	"https://upload.wikimedia.org/wikipedia/en/1/1f/Stand_and_deliver.jpg",
	"https://www.youtube.com/watch?v=qtQQC23eseU"
	)

#Creates an list that holds the name of each movie object
movies = [the_300, the_avengers, iron_man, skyfall, the_dark_night, logan, the_pursuit, stand_and_deliver]

#Calls a fuction from fresh_tomatoes code to create a html page from the list of objects (movies).
fresh_tomatoes.open_movies_page(movies)


